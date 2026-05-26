# Architecture Serveur & Persistance – Horizon 2030

Ce document détaille la conception du serveur de jeu, des protocoles de communication, de la persistance, des sessions et de l'intégration IA pour un MMORPG massivement scalable basé sur la vision « Horizon 2030 ».

---

## 1. Vue d'Ensemble de l'Architecture

L'architecture repose sur des technologies de pointe conçues pour la distribution, la performance absolue et l'intégration native d'intelligences artificielles.

*   **Serveur de Simulation :** Rust + Bevy ECS (Mode Headless). Simulation déterministe basée sur l'Entity Component System, sans garbage collection.
*   **Protocole Réseau :** WebTransport sur QUIC. Permet le multiplexage de flux fiables (RPC, chat, transactions) et de datagrammes non fiables (mouvements fluides, synchronisation de position).
*   **Bases de Données (Polyglotte) :**
    *   *Transactionnel (NewSQL) :* CockroachDB (garanties ACID distribuées, haute résilience).
    *   *Analytique (OLAP) :* ClickHouse (télémétrie, logs de comportement).
    *   *Sémantique / IA :* Qdrant ou Milvus (base vectorielle pour la mémoire des PNJ).
*   **Orchestration :** Kubernetes + Agones pour scaler les instances de jeu selon la population.

---

## 2. Serveur de Jeu (Bevy ECS Headless)

Le serveur de jeu fait figure d'autorité absolue (Serveur Autoritaire). Le client n'est qu'un "terminal d'affichage" qui envoie ses intentions.

### Concepts Clés
*   **Tick Rate Fixe :** La simulation s'exécute à un rythme fixe (ex: 20 ou 30 ticks par seconde).
*   **Spatial Partitioning :** Les entités sont triées par zones géographiques pour limiter les requêtes et optimiser la bande passante (Interest Management).
*   **Reconciliation & Prediction :** Le serveur valide l'état $S_t$ en fonction de l'intention $I_t$.

### Pseudo-Code Rust (Structure Bevy)

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};

// Composants ECS
#[derive(Component)]
struct Player { id: u64, session_token: String }

#[derive(Component)]
struct Position { x: f32, y: f32, z: f32 }

#[derive(Component)]
struct Health(u32);

// Plugins et Boucle principale
fn main() {
    App::new()
        .add_plugins(MinimalPlugins) // Headless: pas de rendu
        .add_systems(Startup, setup_network_listener)
        .add_systems(Update, (
            process_incoming_rpc,
            simulate_movement,
            resolve_combat_events,
            broadcast_state_deltas
        ))
        .run();
}
```

---

## 3. Protocole Réseau et RPC (QUIC / WebTransport)

Le choix de **QUIC / WebTransport** est fondamental. Il évite le problème de blocage en tête de ligne (Head-of-Line Blocking) du TCP tout en offrant la fiabilité quand c'est nécessaire.

### Types de Canaux
1.  **Datagrammes (Non fiable) :** Mouvements, rotations, actions éphémères.
2.  **Streams Bidirectionnels (Fiable) :** RPC critiques (Lancer de sort, échange d'objets, connexion).

### Définition des Payloads RPC (ex: bincode / Protobuf)

Les messages réseau doivent être extrêmement compacts.

```rust
#[derive(Serialize, Deserialize)]
enum ClientIntentRPC {
    Move { x: f32, y: f32, rot: f32, timestamp: u64 },
    CastSpell { spell_id: u32, target_id: Option<u64> },
    Interact { entity_id: u64 },
}

#[derive(Serialize, Deserialize)]
enum ServerStateRPC {
    EntityUpdate { id: u64, pos: (f32, f32), action: u8 },
    CombatLog { source: u64, target: u64, damage: u32 },
    InventorySync { item_id: u32, qty: u32 },
}
```

---

## 4. Persistance des Données (CockroachDB & Vectoriel)

### A. CockroachDB (Base Transactionnelle)
Schéma pensé pour la distribution. Utilisation de UUIDv7 (triable temporellement) pour les clés primaires afin d'éviter les goulots d'étranglement lors de l'insertion.

**Schéma Conceptuel (SQL) :**
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT now()
);

CREATE TABLE characters (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    name VARCHAR(50) UNIQUE NOT NULL,
    level INT DEFAULT 1,
    zone_id INT,
    pos_x FLOAT, pos_y FLOAT, pos_z FLOAT,
    last_saved TIMESTAMP DEFAULT now()
);

CREATE TABLE inventory_items (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    character_id UUID REFERENCES characters(id),
    item_template_id INT NOT NULL,
    quantity INT DEFAULT 1,
    durability INT
);
```

### B. Qdrant (Base Vectorielle / Sémantique pour IA)
Stockage des "souvenirs" et du lore sous forme d'embeddings (vecteurs à $N$ dimensions).

*   **Format :** `Vector(1536)` (ex: OpenAI embeddings).
*   **Payload associé :** `{"player_name": "Thorin", "event": "Le joueur a sauvé le forgeron", "timestamp": "2024-05-26"}`.
*   **Utilisation :** Lorsqu'un joueur parle à un PNJ-IA, on effectue une recherche de "Similarité Cosinus" pour extraire le contexte pertinent avant de générer la réponse LLM.

---

## 5. Gestion des Sessions et Authentification

L'authentification est totalement découplée du serveur de jeu de simulation pour des raisons de sécurité.

1.  **Login Server (API REST/gRPC) :** Le client s'authentifie (Mot de passe, 2FA).
2.  **Génération de Token :** Le Login Server délivre un *JWT (JSON Web Token)* de courte durée et l'IP/Port de l'instance de jeu (Node Agones) affectée au joueur.
3.  **Handshake Jeu :** Le client se connecte au Game Server (via QUIC) et envoie son JWT dans le premier paquet.
4.  **Validation :** Le Game Server valide la signature cryptographique du JWT en local (sans bloquer via un appel DB) et ouvre la session en mémoire ECS (`PlayerSession`).

---

## 6. Transactions et Économie

L'économie dans un MMORPG est vulnérable aux failles de duplication. Nous traitons l'inventaire et les monnaies comme un **livre de comptes (Ledger)**.

*   **Garanties ACID :** CockroachDB gère les échanges entre joueurs comme une transaction de base de données (Isolation Serializable).
*   **Double Entrée :** Créer de l'or implique le transfert depuis le "compte du monde" vers le joueur. Détruire un objet le déplace vers la "poubelle".

**Flux Transactionnel Sécurisé (Rust / SQL) :**
```rust
// Côté Serveur (Thread Pool DB Asynchrone)
async fn process_trade(player1_id: Uuid, player2_id: Uuid, item_id: Uuid, price: i32) -> Result<(), TradeError> {
    // Début Transaction CockroachDB
    // 1. Verrouiller la ligne de l'or de player1
    // 2. Verrouiller l'item de player2
    // 3. UPDATE player1_gold SET amount = amount - price WHERE id = ... AND amount >= price;
    // 4. UPDATE player2_gold SET amount = amount + price WHERE id = ...;
    // 5. UPDATE inventory_items SET character_id = player1_id WHERE id = item_id;
    // 6. COMMIT
}
```
*Si la transaction échoue, l'état ECS n'est pas mis à jour en mémoire.*

---

## 7. Système d'Événements et Intégration IA (via MCP)

Le serveur de jeu expose un standard **MCP (Model Context Protocol)** pour permettre à des agents autonomes (LLMs) d'interagir dynamiquement avec le monde.

### Flux d'observation (Télémétrie)
Chaque action significative dans l'ECS (ex: `CombatEvent`, `QuestCompleteEvent`) génère un log envoyé asynchronement vers **ClickHouse**. Les agents IA lisent ces logs agrégés pour comprendre l'état macro du serveur.

### Sandboxing et Contrats MCP
Les IA agissant comme "Maîtres de Jeu" (GMs) ne peuvent pas exécuter du code arbitraire. Elles appellent des outils MCP stricts validés par le serveur Bevy.

**Exemple d'outils exposés à l'Agent LLM :**
*   `spawn_mob(zone: String, mob_type: String, intent: String)`
*   `whisper_player(player_name: String, message: String)`
*   `change_weather(zone: String, weather: WeatherState)`

**Boucle de décision Agent (Pseudo-logique) :**
1. **Contexte (RAG) :** L'agent query Qdrant : *"Que s'est-il passé au village d'Oakhaven récemment ?"*
2. **Observation :** Les joueurs farment trop de gobelins.
3. **Action (MCP) :** L'agent décide de lancer un outil : `spawn_mob("Oakhaven_Forest", "Goblin_King", "Revenge")`.
4. **Validation :** Le serveur de jeu vérifie les limites (cooldown, droits) et insère l'entité `Goblin_King` dans la simulation ECS.

---
*Ce document forme la base conceptuelle et technique pour le développement modulaire du backend du MMORPG.*
