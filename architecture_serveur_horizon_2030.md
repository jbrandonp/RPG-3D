# Architecture Serveur & Persistance – Horizon 2030

Ce document d'architecture technique détaille la conception du serveur de jeu, des protocoles de communication réseau, des stratégies de persistance, de la gestion des sessions, de la sécurité transactionnelle et de l'intégration d'intelligences artificielles (IA) par le biais du protocole MCP. Cette infrastructure est conçue pour un MMORPG massivement scalable et résilient, s'appuyant sur le paradigme "Horizon 2030".

---

## 1. Vue d'Ensemble de l'Architecture

Le système est conçu autour de principes de haute disponibilité, de tolérance aux pannes et de séparation stricte des préoccupations (SoC). L'architecture est orientée vers le traitement massif de données en temps réel et l'intégration native de composants autonomes.

*   **Moteur de Simulation Central :** Serveur Rust basé sur le framework Bevy en mode *Headless*. Il exécute la simulation physique et logique de manière déterministe grâce au paradigme Entity Component System (ECS), offrant des performances de pointe sans les surcoûts liés au *garbage collection*.
*   **Couche de Transport Réseau :** WebTransport au-dessus du protocole QUIC. Ce choix élimine le problème de blocage en tête de ligne (Head-of-Line Blocking) inhérent à TCP, permettant le multiplexage natif de flux fiables (RPC stricts) et non fiables (mouvements spatiaux continus).
*   **Topologie de Données Polyglotte :**
    *   *SGBD NewSQL (Transactionnel) :* CockroachDB, fournissant une cohérence forte (ACID) et une scalabilité horizontale multi-région, essentielle pour la persistance critique (comptes, inventaires, économie).
    *   *Entrepôt OLAP (Analytique) :* ClickHouse, pour l'ingestion asynchrone des métriques, de la télémétrie et des journaux d'audit à très haut débit.
    *   *Base de Données Vectorielle (Sémantique/IA) :* Qdrant ou Milvus, hébergeant les *embeddings* vectoriels pour modéliser la mémoire épisodique et contextuelle des PNJ autonomes.
*   **Orchestration Dynamique :** Flotte de serveurs gérée par Kubernetes et Agones. Le dimensionnement est élastique (*auto-scaling*), basé sur la densité de population par région géographique.

---

## 2. Serveur de Jeu (Bevy ECS Headless)

Le serveur opère en tant qu'autorité absolue de la simulation (Serveur Autoritaire). Le client est relégué au rôle de terminal de rendu visuel et de prédiction locale (« Client-Side Prediction »).

### Concepts Fondamentaux et Flux d'Exécution

*   **Tick Rate Fixe et Déterminisme :** La boucle principale s'exécute à un rythme constant (par exemple, 20 ou 30 *ticks* par seconde). Le pas de temps ($\Delta t$) est fixe, garantissant que la simulation évolue de manière prédictible et limitant la dérive liée aux fluctuations processeur.
*   **Partitionnement Spatial (Interest Management) :** Les entités sont indexées au sein d'une structure de données spatiale (ex: Quadtree ou grille de *chunks*). Le serveur calcule les "Zones d'Intérêt" de chaque client, limitant drastiquement la bande passante en n'envoyant que les mises à jour des entités pertinentes pour ce dernier.
*   **Réconciliation (Reconciliation) :** Le serveur maintient la vérité de l'état global ($S_t$). Les entrées client (intentions $I_t$) sont validées. En cas de divergence (triche, latence), le serveur impose son état de référence au client, forçant un rattrapage (« Rubberbanding » contrôlé).
*   **Compression par Delta (Delta Snapshotting) :** Plutôt que de transmettre l'état entier, le serveur génère et diffuse uniquement les deltas (champs ayant muté depuis le dernier tick confirmé par le client).

### Implémentation Conceptuelle (Rust / Bevy)

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};

// Définition des composants de l'ECS
#[derive(Component)]
struct Session { id: u64, auth_token: String, is_active: bool }

#[derive(Component)]
struct Transform3D { pub position: Vec3, pub rotation: Quat }

#[derive(Component)]
struct CombatStats { pub hp_current: u32, pub hp_max: u32 }

// Initialisation et pipeline d'Update
fn main() {
    App::new()
        // Utilisation du mode Headless pour réduire l'empreinte mémoire
        .add_plugins(MinimalPlugins)
        .add_systems(Startup, init_network_layer)
        // L'ordre d'exécution (Schedule) est strictement contrôlé
        .add_systems(Update, (
            read_network_inputs.label("input"),
            process_client_intentions.after("input").label("logic"),
            simulate_physics.after("logic").label("physics"),
            resolve_combat_systems.after("physics").label("combat"),
            serialize_and_broadcast_deltas.after("combat")
        ))
        .run();
}
```

---

## 3. Couche Réseau et Appels de Procédures Distantes (RPC)

L'implémentation de WebTransport sur QUIC est primordiale pour la fluidité de l'expérience utilisateur, en particulier dans un environnement massivement multijoueur.

### Stratégie de Multiplexage des Flux

1.  **Canal Datagramme (UDP Pur, Non garanti) :**
    *   *Usage :* Flux de positionnement, orientation, animations cycliques.
    *   *Caractéristique :* Tolérant à la perte de paquets. Les données obsolètes sont ignorées au profit des nouvelles.
2.  **Canal Stream Unidirectionnel (Garanti, Ordonné) :**
    *   *Usage :* Journaux de combat (logs d'action), messages du serveur au client.
3.  **Canal Stream Bidirectionnel (Garanti, Transactionnel) :**
    *   *Usage :* Initialisation de session, authentification, lancements de sorts critiques, transferts d'inventaire, requêtes économiques.

### Structure des Payloads (Sérialisation bincode)

La sérialisation binaire via `bincode` (ou Protobuf) est imposée pour limiter la taille des MTU réseau.

```rust
#[derive(Serialize, Deserialize, Debug)]
pub enum ClientCommand {
    /// Commande éphémère (Datagramme)
    Movement { pos: (f32, f32, f32), yaw: f32, tick: u64 },
    /// Commande critique nécessitant validation (Stream)
    CastAbility { ability_id: u32, target_entity: Option<u64> },
    /// Interaction environnementale
    InteractWithNode { node_id: u64 },
}

#[derive(Serialize, Deserialize, Debug)]
pub enum ServerResponse {
    /// Delta de l'état du monde
    StateDelta { entity_id: u64, new_pos: Option<(f32,f32,f32)>, state_flag: u8 },
    /// Notification d'événement irréversible
    CombatResolution { attacker: u64, victim: u64, effect: u32, value: i32 },
    /// Validation d'un état critique (ex: Inventaire)
    InventoryMutation { slot_id: u16, item_id: u32, amount: u32 },
}
```

---

## 4. Persistance des Données (Transactionnel & Vectoriel)

La stratégie de gestion de la donnée sépare strictement les préoccupations transactionnelles, analytiques et sémantiques.

### A. Base Transactionnelle : CockroachDB (NewSQL)

Conçue pour un déploiement cloud-native avec réplication Raft, garantissant l'intégrité ACID sans Single Point of Failure (SPOF).
L'usage systématique des `UUIDv7` garantit la triabilité temporelle, optimisant l'insertion concurrentielle dans des index B-Tree distribués. Le pooling de connexions (ex: `PgBouncer` ou gestionnaire natif) est obligatoire.

**Schémas de Base (Exemple SQL DDL) :**

```sql
-- Création optimisée avec UUIDv7 généré via application ou fonction native
CREATE TABLE users (
    id UUID PRIMARY KEY,
    account_name VARCHAR(64) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    status VARCHAR(16) DEFAULT 'ACTIVE',
    created_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

CREATE TABLE characters (
    id UUID PRIMARY KEY,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(64) UNIQUE NOT NULL,
    class_id INT NOT NULL,
    level INT DEFAULT 1,
    zone_id INT NOT NULL,
    coord_x FLOAT8, coord_y FLOAT8, coord_z FLOAT8,
    updated_at TIMESTAMPTZ DEFAULT clock_timestamp()
);

-- Indexation pour requêtes fréquentes du Login Server
CREATE INDEX idx_characters_user_id ON characters(user_id);
```

### B. Moteur Sémantique et Vectoriel : Qdrant

Cette couche permet de doter les PNJ de mémoires épisodiques (Lore, interactions passées) requêtables par similarité conceptuelle.

*   **Structure de l'Index :** Les vecteurs (par exemple, 1536 dimensions issues d'OpenAI `text-embedding-3`) sont indexés avec un algorithme HNSW (Hierarchical Navigable Small World).
*   **Payload Structuré :** Outre le vecteur, des métadonnées filtrent la recherche (`{"zone_id": 42, "player_id": "UUID", "event_type": "quest_completed"}`).
*   **Recherche de Contexte :** Lorsqu'un joueur initie un dialogue avec un PNJ IA, le serveur requête la similarité cosinus $\cos(\theta) = \frac{A \cdot B}{\|A\| \|B\|}$ pour extraire les 5 souvenirs les plus pertinents à injecter dans le prompt du LLM.

---

## 5. Gestion des Sessions et de l'Authentification

L'authentification est décorrélée de l'infrastructure de jeu par un micro-service dédié (Login Server), mitigant ainsi la surface d'attaque du serveur de simulation principal.

1.  **Phase d'Authentification :** Le client soumet ses identifiants au Login Server via HTTPS/gRPC.
2.  **Délivrance de Jeton Sécurisé :** Le Login Server vérifie les données, gère l'état (bannissement, MFA) et émet un **JWT (JSON Web Token)** signé avec une clé privée asymétrique (EdDSA/RS256). Ce token possède une durée de vie extrêmement courte (TTL < 5 min). L'orchestrateur alloue une instance de jeu au joueur.
3.  **Phase de Handshake (WebTransport) :** Le client établit la connexion QUIC avec l'instance de jeu (Game Server) assignée, en joignant son JWT.
4.  **Vérification Stateless :** Le Game Server valide mathématiquement la signature du JWT via la clé publique. Cette approche supprime le besoin de requêter la base de données lors de chaque connexion, éliminant un goulot d'étranglement majeur. Une fois validée, l'entité `PlayerSession` est intégrée à l'ECS.

---

## 6. Transactions, Économie et Idempotence

Le système économique est le point le plus sensible aux exploitations (*dupe exploits*, attaques par rejeu). Il est architecturé comme un livre de comptes immuable (Ledger).

*   **Isolation Stricte :** Le serveur de jeu utilise le niveau d'isolation `SERIALIZABLE` de CockroachDB pour toute mutation économique.
*   **Idempotence :** Chaque requête transactionnelle émise par le client comporte un UUID de corrélation (`Idempotency-Key`). Si le serveur de jeu ou la DB constate que la clé a déjà été traitée, il ignore l'action, empêchant la duplication d'objets via le double clic ou la latence réseau.
*   **Principe de la Double Entrée :** Toute création, destruction ou transfert de richesse nécessite un équilibrage à somme nulle. (ex: L'achat à un PNJ débite le joueur et crédite le compte global de la "Banque Centrale" du système).

**Workflow Asynchrone de Transfert (Pseudo-code Rust) :**

```rust
/// Traite un échange entre deux joueurs de manière asynchrone pour ne pas bloquer l'ECS
async fn execute_trade_transaction(
    db_pool: &PgPool,
    idempotency_key: Uuid,
    buyer_id: Uuid,
    seller_id: Uuid,
    item_id: Uuid,
    price: i32
) -> Result<(), TradeError> {
    let mut tx = db_pool.begin().await?;

    // 1. Vérification d'idempotence (évite le rejeu)
    if is_processed(&mut tx, idempotency_key).await? { return Ok(()); }

    // 2. Lock optimiste sur les entités (Ordre déterministe pour éviter les deadlocks)
    // 3. Validation des pré-requis (fonds suffisants, objet possédé et non lié)

    // 4. Mutations
    sqlx::query("UPDATE characters SET gold = gold - $1 WHERE id = $2 AND gold >= $1")
        .bind(price).bind(buyer_id).execute(&mut tx).await?;

    sqlx::query("UPDATE characters SET gold = gold + $1 WHERE id = $2")
        .bind(price).bind(seller_id).execute(&mut tx).await?;

    sqlx::query("UPDATE inventory_items SET owner_id = $1 WHERE id = $2")
        .bind(buyer_id).bind(item_id).execute(&mut tx).await?;

    // 5. Enregistrement de la clé d'idempotence et de l'audit log
    record_idempotency(&mut tx, idempotency_key).await?;

    // 6. Commit de la transaction ACID
    tx.commit().await?;

    Ok(())
}
```

---

## 7. Système d'Événements et Intégration IA Autonome (MCP)

Le serveur de jeu se conforme au **Model Context Protocol (MCP)**, exposant une API standardisée qui permet à des agents d'intelligence artificielle (ex: LLMs) d'analyser le monde et d'interagir avec lui de manière encadrée.

### Télémétrie et Observabilité (Pipeline ClickHouse)
Afin de ne pas impacter la base transactionnelle, tout événement d'importance généré au sein de l'ECS (décès de monstre, réussite de quête, commerce massif) produit un événement de télémétrie asynchrone injecté par *batch* dans ClickHouse. Les agents IA l'utilisent pour observer le "Macro-État" (ex: détection d'une pénurie de minerai de fer sur une région).

### Sandboxing, Audits et Contrats MCP
Les agents IA ne possèdent en aucun cas un accès root ou une capacité d'exécution de code binaire arbitraire. Leurs intentions passent par un filtre de sécurité et de logique applicative strict au sein du serveur.

**Exemple d'outils (Tools) MCP mis à disposition :**
*   `analyze_market_trend(item_category)` : Lecture seule.
*   `spawn_entity(type: "Orc_Boss", coords: {x,y,z}, profile_id: Uuid)` : Nécessite des droits de "Maître de Jeu".
*   `trigger_world_event(event_id: "Goblin_Raid", zone_id: 12)` : Action macro-scopique.

**Flux d'exécution sécurisé pour l'Agent IA :**
1.  **Réflexion (RAG) :** L'agent IA détecte via ClickHouse qu'une zone est vide de monstres. Il interroge Qdrant pour connaître l'historique narratif de la zone.
2.  **Action Planifiée :** L'agent génère une requête de l'outil MCP `trigger_world_event`.
3.  **Validation Applicative (Gatekeeper) :** Le serveur de jeu reçoit la commande MCP. Il vérifie :
    *   La signature et les droits d'accréditation du token IA.
    *   Les règles métier (ex: un *Goblin Raid* ne peut avoir lieu qu'une fois toutes les 6 heures, un délai qui est audité).
4.  **Exécution & Mutabilité :** Si validé, le composant ECS correspondant est muté, déclenchant le spawn des entités dans le cycle du moteur physique, qui sera ensuite propagé aux joueurs via des Deltas Réseau.
5.  **Audit Log :** La décision IA, le prompt associé, et la commande résultante sont consignés immuablement en base de données pour permettre la traçabilité et le débogage (Audit Trail).

---

*Ce document d'architecture garantit l'alignement entre les contraintes de performance du moteur Bevy en environnement distribué, la sécurité transactionnelle inhérente à l'économie de MMO, et les possibilités de manipulation d'univers par intelligence artificielle requises par l'initiative "Horizon 2030".*
