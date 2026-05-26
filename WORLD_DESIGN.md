# System / Level Design Document (SGDD)
**Projet :** Mini-MMORPG Dark Fantasy (Architecture Bevy ECS)
**Cible Visuelle :** Rétro PS2 (Low-poly, filtrage Nearest, WGPU)

Ce document professionnel établit les standards de conception spatiale, l'équilibrage mathématique et le cahier des charges technique pour l'intégration dans le moteur Bevy.

---

## 1. Vision et Intentions de Design (Macro)

### 1.1 Direction Artistique et Thématique
Un monde crépusculaire, poisseux et en ruine. Les distances d'affichage sont volontairement courtes, masquées par un brouillard volumétrique intense (bénéfique pour l'ambiance et les performances du moteur de rendu). La palette de couleurs est dominée par des gris cendrés, des rouges sang oxydés et des verts toxiques.

### 1.2 Core Game Loop (Boucle de Gameplay)
1. **Préparation (Hub) :** Vente de butin, réparation, achat de consommables.
2. **Exploration & Chasse (Zones Ouvertes) :** Navigation vers des points d'intérêt, combat contre des créatures (farm d'XP et de matériaux).
3. **Épreuve (Donjons) :** Combat de boss instancié nécessitant un groupe.
4. **Récompense & Retour :** Acquisition de butin rare et retour au hub (TP ou marche).

### 1.3 Player Flow (Progression)
Le joueur débute dans le Hub protégé. La progression est radiale, la difficulté augmentant avec la distance par rapport au Hub central.

---

## 2. World Building et Metrics (Conception Spatiale)

### 2.1 Échelle et Métriques du Joueur
Afin de garantir des collisions précises (via Bevy Rapier) et une navigation fluide :
- **Unité de base (1u) :** 1 mètre dans le moteur.
- **Taille du joueur (Hitbox) :** Cylindre de rayon `0.5u` et hauteur `1.8u`.
- **Vitesse de déplacement (Base) :** `4.5u / seconde` (Marche/Course par défaut).
- **Vitesse en combat :** `3.0u / seconde` (Pénalité d'engagement).
- **Hauteur de saut :** Le jeu n'inclut pas de mécanique de saut complexe pour limiter les exploits topographiques (navigation via NavMesh 2.5D).

### 2.2 Architecture des Chunks (Spatial Partitioning)
La carte n'est pas chargée intégralement.
- **Taille d'un Chunk :** `64u x 64u`.
- **Distance de Rendu / Simulation :** `3x3 Chunks` centrés sur le joueur.
- **Serveur :** Ne "tick" (met à jour les entités) que dans les chunks où se trouve au moins une connexion active.

---

## 3. Topologie des Zones et Landmarks

### 3.1 Zone 1 : Le Village de Cendrecroix (Hub Central / Safe Zone)
- **Taille :** `128x128u` (4 Chunks).
- **Landmark :** Le "Grand Bûcher" (émetteur de particules et source de lumière dynamique visible de loin).
- **Flow :** Architecture circulaire fermée. Les sorties sont des goulets d'étranglement (Chokepoints) naturels (pont-levis brisé, porte défoncée).
- **Règles Systémiques :** Dégâts joueurs et ennemis désactivés.

### 3.2 Zone 2 : La Forêt de Varek (Zone de Grind Initiale)
- **Taille :** `256x256u` (16 Chunks).
- **Landmark :** L'Arbre des Pendus (au centre nord, repère d'orientation sans ouvrir de carte).
- **Flow :** Des routes sûres (`SpeedModifier x1.0`) et des bois denses remplis de "Ronces Corrompues" (`SpeedModifier x0.6`). Les joueurs sont incités à rester sur la route à bas niveau.

### 3.3 Zone 3 : Les Marais Sanglants (Zone Intermédiaire)
- **Taille :** `256x256u` (16 Chunks).
- **Landmark :** La Carcasse du Léviathan (squelette géant servant de pont naturel).
- **Flow :** Zones d'eau profonde limitant les déplacements.
- **Règles Systémiques :** Trigger volumes d'eau profonde qui appliquent un statut `Wet` (vulnérabilité aux dégâts de foudre) et une pénalité de vitesse.

### 3.4 Zone 4 : La Cathédrale d'Obsidienne (Donjon Instancié)
- **Taille :** `128x256u` (Structure en couloir).
- **Flow :** Salles verrouillées (`DoorComponent`). Obligation de purger l'Area of Interest (AoI) des ennemis ciblés.

---

## 4. Systems Design & Équilibrage (Balancing)

### 4.1 Cibles Mathématiques Globales (Combat Pacing)
L'équilibrage se base sur un **Time To Kill (TTK)** cible pour garantir un rythme "Rétro RPG" (les combats durent plusieurs secondes, la gestion des ressources est vitale).
- **TTK Joueur vs Mob Normal (Niveau équivalent) :** `6 à 8 secondes`.
- **TTK Mob vs Joueur (Niveau équivalent) :** `15 à 20 secondes` (laisse le temps de fuir ou d'utiliser une potion).
- **Global Cooldown (GCD) :** `1.5s` entre les attaques basiques.

### 4.2 Bestiaire, IA et Tables de Loot (Équilibrage Niveau 1-5)

| Entité | HP Base | Vitesse | Dégâts (DPS) | XP | Taux de Drop (Loot Table) |
|---|---|---|---|---|---|
| **Joueur (Niv 1)** | 100 | 4.5u/s | 8 | N/A | N/A |
| **Goule Cendrée** | 60 | 5.0u/s | 6 | 20 | Ossement (40%), Tissu (15%) |
| **Corbeau de Sang** | 50 | 6.5u/s | 5 | 25 | Plume (30%), Potion Mineure (5%) |
| **Noyé en Armure** | 100 | 2.5u/s | 7 | 60 | Fer Rouillé (50%), Arme Magique (2%) |
| **Prêtre (Boss N.5)**| 1200 | 3.5u/s | 25 | 500 | Relique Impie (100%), Arme Épique (10%) |

*Note de Progression XP :*
Niveau 1 -> 2 = 565 XP (28 Goules). Évolution exponentielle (`Base * (N^2.5)`).

### 4.3 Équipement et Mathématiques des Dégâts
Formule de résolution des dégâts côté serveur :
`Dégâts Subis = (Dégâts Arme * Modificateur Statistique) * (1 - (Armure / (Armure + (Niveau Attaquant * 50))))`

---

## 5. Cahier des Charges Technique (Bevy ECS Architecture)

Afin d'implémenter ce document dans notre stack Rust/Bevy (Serveur Autoritaire), voici les structures et requêtes de base requises.

### 5.1 Définition des Composants (Rust Pseudo-code)

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};

// Identité réseau et serveur
#[derive(Component)]
pub struct NetworkId(pub u64);

#[derive(Component)]
pub struct InstanceId(pub uuid::Uuid); // Pour séparer les instances (Donjon vs Open World)

// Statistiques vitales de combat
#[derive(Component, Serialize, Deserialize)]
pub struct CombatStats {
    pub hp: f32,
    pub max_hp: f32,
    pub base_damage: f32,
    pub armor: f32,
}

// Composant pour l'état de l'environnement
#[derive(Component)]
pub struct MovementModifier {
    pub multiplier: f32, // ex: 0.5 dans les Marais, 1.0 sur route
}

// Spawner de Level Design (Gère les nids d'ennemis)
#[derive(Component)]
pub struct MobSpawner {
    pub mob_type: String, // ID dans les assets
    pub spawn_radius: f32,
    pub max_alive: usize,
    pub timer: Timer,
}
```

### 5.2 Systèmes et Résolution des Dégâts

La philosophie "Server-Authoritative" implique que le client envoie des "Intentions", et le serveur exécute ce système :

```rust
// Evénement généré par les paquets réseau entrants
pub struct AttackIntentEvent {
    pub attacker_net_id: u64,
    pub target_net_id: u64,
    pub skill_id: u32,
}

// Système de résolution de combat côté serveur
pub fn combat_resolution_system(
    mut attack_events: EventReader<AttackIntentEvent>,
    mut query_stats: Query<(&NetworkId, &mut CombatStats)>,
    query_safe_zone: Query<&GlobalTransform, With<SafeZone>>,
) {
    for event in attack_events.read() {
        // Validation 1 : Vérifier la distance et le Line of Sight (LoS)
        // Validation 2 : Vérifier que ce n'est pas en Safe Zone

        let mut attacker_dmg = 0.0;

        // ... (Récupération des stats de l'attaquant) ...

        // Application des dégâts sur la cible
        if let Some((_, mut target_stats)) = query_stats.iter_mut().find(|(id, _)| id.0 == event.target_net_id) {
            let mitigated_damage = attacker_dmg * (100.0 / (100.0 + target_stats.armor));
            target_stats.hp -= mitigated_damage;

            // Si HP <= 0, générer l'événement MobDeathEvent (qui trigger le LootSystem)
        }
    }
}
```

### 5.3 Streaming du Monde et Hot-Reloading
- **Fichiers de Scène (Assets) :** Le Level Design est stocké sous forme de fichiers `.ron` (Rusty Object Notation) ou `.json`.
- **Découplage Client/Serveur :**
  - **Fichier `zone_1_server.json` :** Contient les Spawners, Colliders Rapier (Murs, NavMesh), Triggers (SafeZone).
  - **Fichier `zone_1_client.glb` (GLTF) :** Contient uniquement les maillages 3D, les textures et l'éclairage.
- **Avantage technique :** Les concepteurs peuvent ajuster les `CombatStats` dans un fichier JSON, et le composant `AssetServer` de Bevy mettra à jour l'équilibrage en temps réel sans que le serveur n'ait besoin d'être redémarré (Hot-Reloading natif de Bevy).
