# Structures ECS Rust/Bevy : World Design

Ce document définit les structures de données (Components, Resources) et l'architecture des systèmes pour le serveur autoritaire (Headless) et le client, conformément au cahier des charges "Elara's Black Mist".

## 1. Composants de Base (Serveur & Client)

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};
use uuid::Uuid;

// Identifiant Unique Persistant (Lien Âme-Corps)
#[derive(Component, Clone, Copy, PartialEq, Eq, Hash, Serialize, Deserialize)]
pub struct SoulLink(pub Uuid);

// Identité Réseau
#[derive(Component, Serialize, Deserialize)]
pub struct NetworkId(pub u64);

// Isolation (Monde Ouvert vs Instance Nid)
#[derive(Component, PartialEq, Eq)]
pub struct InstanceId(pub Uuid);
```

## 2. Définition des Zones et Environnement (Serveur)

```rust
#[derive(Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum DangerLevel {
    Safe,
    Low,
    Medium,
    High,
    Extreme,
}

#[derive(Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum BiomeType {
    Urban,
    Plains,
    Swamp,
    Forest,
    Abyssal,
}

#[derive(Component, Serialize, Deserialize)]
pub struct Zone {
    pub id: u32,
    pub name: String,
    pub level_range: (u8, u8),
    pub danger_level: DangerLevel,
    pub biome: BiomeType,
    // Influence dynamique du Brouillard Noir (0.0 = Sain, 1.0 = Totalement Corrompu)
    pub fog_corruption: f32,
}

#[derive(Component)]
pub struct ZoneBounds {
    pub min: Vec3,
    pub max: Vec3,
}

// Modificateur appliqué par un Trigger Volume (Ex: Eau profonde dans les marais)
#[derive(Component)]
pub struct TerrainModifier {
    pub speed_multiplier: f32, // ex: 0.6 pour ralentir
    pub applies_wet_status: bool,
}
```

## 3. Mécaniques Psychologiques et Survie (NOTES_GDD_UPDATE)

```rust
#[derive(Component, Serialize, Deserialize)]
pub struct PsychologicalState {
    pub trauma_index: f32,      // 0.0 - 100.0 (Impacte le contrôle moteur)
    pub corruption_index: f32,  // 0.0 - 100.0 (Impacte le visuel et l'hostilité IA)
}

#[derive(Clone, Copy, PartialEq, Eq, Serialize, Deserialize)]
pub enum EntityType {
    Human,
    Goblin_Genome,
    DeepOne_Genome,
}

// Composant gérant la possibilité de Rebirth (Spawn dans un nid)
#[derive(Component)]
pub struct IncubationStatus {
    pub is_active: bool,
    pub genome_seed: EntityType,
    pub cycle_timer: Timer,
}
```

## 4. Systèmes de Spawn (Serveur)

```rust
#[derive(Component)]
pub struct SpawnPoint {
    pub entity_type: EntityType,
    pub max_count: u32,
    pub respawn_timer: Timer,
    pub spawn_radius: f32,
}

// Composant anti-cheat (Le serveur utilise un Collider primitif Rapier3D)
// #[derive(Component)] // Provient de bevy_rapier3d
// pub struct Collider;
```

## 5. Architecture des Systèmes Principaux

### Serveur (WorldSimulation)
```rust
pub struct WorldSimulationPlugin;

impl Plugin for WorldSimulationPlugin {
    fn build(&self, app: &mut App) {
        app
            // Gère le chargement et déchargement logique des Chunks
            .add_systems(Update, zone_manager_system)
            // Gère l'apparition des monstres via SpawnPoint
            .add_systems(Update, spawn_system)
            // Pathfinding sur le NavMesh statique
            .add_systems(Update, navmesh_system)
            // Pression temporelle et extension de la corruption
            .add_systems(Update, fog_expansion_system)
            // Transition entre Zones, dégâts environnementaux
            .add_systems(Update, event_trigger_system)
            // Calcul de la Zone d'Intérêt (AoI) pour l'envoi réseau
            .add_systems(Update, chunk_streaming_system);
    }
}
```

### Client (WorldRender)
```rust
pub struct WorldRenderPlugin;

impl Plugin for WorldRenderPlugin {
    fn build(&self, app: &mut App) {
        app
            // Charge les assets .glb (SceneBundle) selon les instructions du serveur
            .add_systems(Update, chunk_loader_system)
            // Met à jour les positions (interpolées) selon l'état serveur
            .add_systems(Update, entity_renderer_system)
            // Modifie le rendu visuel selon la Corruption (Vertex Colors, Shaders)
            .add_systems(Update, ambient_visual_system);
    }
}
```
