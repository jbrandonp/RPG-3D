# Architecture et Implémentation des Effets Visuels (WGPU / Bevy)
## Spécification Technique — Direction Artistique « Rétro » (PS2 / Metin2)

---

## 1. Contexte et Philosophie d'Ingénierie

La stratégie d'ingénierie de ce projet MMORPG impose une dichotomie stricte : le backend (Rust/Bevy headless) monopolise la charge computationnelle pour gérer la simulation autoritaire, tandis que le client opère en tant que **terminal d'affichage passif**.

La direction artistique "Rétro" (esthétique PS2) n'est pas uniquement un choix stylistique, mais une décision architecturale permettant une compatibilité matérielle universelle et une maximisation de la bande passante.

L'implémentation des effets visuels (VFX) — incluant les sorts, explosions, particules et atmosphères dynamiques — doit se conformer à deux directives absolues :
1. **Isolation de l'état** : Le rendu visuel ne doit jamais interférer avec la logique de la simulation.
2. **Frugalité computationnelle** : L'utilisation de WGPU via Bevy doit minimiser les appels d'affichage (Draw Calls) en s'appuyant sur des techniques canoniques des années 2000, réimplémentées dans un moteur moderne.

---

## 2. Architecture Réseau et Séparation des Préoccupations (SoC)

Le serveur ne calcule jamais la physique des particules, ni l'éclairage dynamique. Le déclenchement des VFX repose sur un paradigme de **publication/abonnement (Pub/Sub)** via le protocole réseau.

### 2.1. Cinématique d'un Événement Visuel
1. **Exécution Autoritaire** : Une entité déclenche une compétence (ex: *Nova de Feu*). Le serveur résout les collisions, applique les dégâts et met à jour l'état.
2. **Diffusion Multiplexée** : Le serveur génère un *Delta d'Événement* et le transmet exclusivement aux clients situés dans la zone de pertinence spatiale (Spatial Partitioning).
3. **Instanciation Locale** : Le client intercepte le paquet et déclenche des routines de rendu purement esthétiques. Ces entités locales ne possèdent aucun composant de collision réseau.

---

## 3. Stratégies d'Optimisation et Contraintes Graphiques (Style PS2)

Pour garantir la fluidité sur les architectures matérielles anciennes (OpenGL ES 3.0 / DirectX 11) tout en bénéficiant de l'API WGPU, les contraintes suivantes sont impératives :

*   **Rendu 2D Planaire (Billboarding)** : Remplacement systématique des volumes 3D complexes par des polygones 2D (Quads) dynamiquement orientés vers la caméra.
*   **Atlas de Textures et Spritesheets** : Regroupement des textures d'effets pour minimiser les changements d'état du pipeline graphique (Texture Binding).
*   **Filtrage Point (Nearest-Neighbor)** : Désactivation du filtrage bilinéaire/trilinéaire pour préserver un rendu net (« pixel-perfect ») et réduire la charge sur l'unité de texture (TMU).
*   **Ombrage Simplifié** : Utilisation exclusive du *Forward Rendering*. Rejet total du PBR (Physically Based Rendering). Utilisation du *Gouraud shading* ou *Flat shading* avec mélange colorimétrique par sommet (Vertex Colors).
*   **Object Pooling (Mémoire Préallouée)** : Pour éviter la fragmentation de la mémoire et les pics de charge liés aux instanciations/destructions massives (Spawns/Despawns), un système de "pool" préalloué de particules doit être mis en place.
*   **Éclairage Limité** : Les sources lumineuses dynamiques (PointLights) sont strictement temporaires, non-projeteuses d'ombres (Unshadowed), et capées à 2-4 par scène locale.

---

## 4. Implémentation Architecturale dans Bevy (Exemples de Référence)

### 4.1. Réception et Routage des Événements Réseau

La structure de données réseau doit être hautement sérialisable et minimale.

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};

/// Structure d'événement réseau minimaliste (Deltas).
#[derive(Event, Debug, Serialize, Deserialize)]
pub struct NetEventVisualEffect {
    pub effect_id: u16,        // Identifiant dans le dictionnaire des effets
    pub origin: Vec3,          // Point de départ ou épicentre
    pub target: Option<Vec3>,  // Vecteur de direction ou cible optionnelle
    pub magnitude: f32,        // Échelle ou intensité de l'effet
}

pub enum StandardEffects {
    ArcaneMissileImpact = 101,
    FireblastExplosion = 102,
    HealAura = 201,
}
```

### 4.2. Système de Particules : Orientation Caméra (Billboarding) et Cycle de Vie

Un système robuste nécessite d'aligner mathématiquement les quads (particules) avec le plan de projection de la caméra active à chaque trame.

```rust
/// Marqueur pour les entités devant faire face à la caméra
#[derive(Component)]
pub struct BillboardConstraint;

/// Marqueur de cycle de vie (Fire & Forget)
#[derive(Component)]
pub struct VolatileLifetime {
    pub timer: Timer,
}

/// Évalue l'orientation des particules vis-à-vis de la caméra principale.
pub fn compute_billboard_orientation_system(
    camera_query: Query<&Transform, With<Camera3d>>,
    mut billboard_query: Query<&mut Transform, (With<BillboardConstraint>, Without<Camera3d>)>,
) {
    let Ok(camera_transform) = camera_query.get_single() else { return };

    // Le vecteur de vue de la caméra (opposé à la direction pour que la texture soit visible)
    let camera_forward = camera_transform.forward();
    let up_vector = Vec3::Y; // Ou camera_transform.up() selon l'effet désiré

    for mut transform in billboard_query.iter_mut() {
        // Aligner la normale du quad sur le vecteur de vue de la caméra
        transform.look_to(-camera_forward, up_vector);
    }
}

/// Supervise la destruction des effets volatils.
pub fn garbage_collect_volatile_effects_system(
    mut commands: Commands,
    time: Res<Time>,
    mut query: Query<(Entity, &mut VolatileLifetime)>,
) {
    for (entity, mut lifetime) in query.iter_mut() {
        if lifetime.timer.tick(time.delta()).just_finished() {
            // Dans un système optimisé, utiliser un Object Pool ici au lieu de despawn
            commands.entity(entity).despawn_recursive();
        }
    }
}
```

### 4.3. Instanciation des Effets (Explosions et Additive Blending)

Le rendu d'un effet magique s'appuie sur la superposition de textures éclairées sans calcul de normales (`unlit: true`), avec un mélange colorimétrique de type additif.

```rust
pub fn process_incoming_effect_events_system(
    mut commands: Commands,
    mut events: EventReader<NetEventVisualEffect>,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
    asset_server: Res<AssetServer>,
) {
    for event in events.read() {
        // Exemple pour une explosion (ID fictif 102)
        if event.effect_id == 102 {
            let base_scale = event.magnitude.max(0.1);

            // 1. Instanciation du Quad texturé (Billboard)
            commands.spawn((
                PbrBundle {
                    mesh: meshes.add(shape::Quad::new(Vec2::new(2.5 * base_scale, 2.5 * base_scale)).into()),
                    material: materials.add(StandardMaterial {
                        base_color_texture: Some(asset_server.load("textures/vfx/tex_explosion_sheet.png")),
                        alpha_mode: AlphaMode::Add, // Indispensable pour l'effet incandescent
                        unlit: true,                // Court-circuite le calcul d'éclairage
                        ..default()
                    }),
                    transform: Transform::from_translation(event.origin),
                    ..default()
                },
                BillboardConstraint,
                VolatileLifetime { timer: Timer::from_seconds(0.8, TimerMode::Once) },
            ));

            // 2. Instanciation d'un flash lumineux dynamique temporaire
            commands.spawn((
                PointLightBundle {
                    point_light: PointLight {
                        color: Color::rgb(1.0, 0.4, 0.0), // Teinte orangée
                        intensity: 2000.0 * base_scale,
                        range: 12.0 * base_scale,
                        shadows_enabled: false,           // Optimisation stricte
                        ..default()
                    },
                    transform: Transform::from_translation(event.origin + Vec3::new(0.0, 1.0, 0.0)),
                    ..default()
                },
                VolatileLifetime { timer: Timer::from_seconds(0.25, TimerMode::Once) },
            ));
        }
    }
}
```

### 4.4. Gestion des Environnements et Atmosphères Dynamiques

L'altération de l'environnement (cycle jour/nuit, météo) sur des architectures restreintes passe par la manipulation de l'éclairage global (`AmbientLight`) et la densification du brouillard volumétrique ou de distance.

```rust
#[derive(Resource)]
pub struct EnvironmentAtmosphere {
    pub diurnal_cycle_time: f32, // Heure locale du serveur normalisée (0.0 à 24.0)
    pub weather_intensity: f32,  // Ex: 0.0 = Dégagé, 1.0 = Tempête
}

/// Calcule et applique les paramètres d'environnement en fonction du cycle horaire.
pub fn process_diurnal_cycle_system(
    atmosphere: Res<EnvironmentAtmosphere>,
    mut ambient_light: ResMut<AmbientLight>,
    mut fog_query: Query<&mut FogSettings>,
) {
    // Calcul de l'intensité lumineuse basée sur une courbe trigonométrique simple
    let phase = (atmosphere.diurnal_cycle_time / 24.0) * std::f32::consts::PI * 2.0;
    // Base mathématique pour simuler le zénith (1.0) et le nadir (~0.1)
    let sun_elevation = phase.cos() * -0.45 + 0.55;

    let base_intensity = sun_elevation.clamp(0.05, 1.0);

    // Altération de la chrominance : teintes bleutées la nuit, blanches le jour
    let ambient_color = if base_intensity < 0.3 {
        Color::rgb(base_intensity, base_intensity * 1.1, base_intensity * 1.5) // Nuit
    } else {
        Color::rgb(base_intensity, base_intensity, base_intensity) // Jour
    };

    ambient_light.color = ambient_color;
    ambient_light.brightness = base_intensity * (1.0 - (atmosphere.weather_intensity * 0.5)); // Assombrissement météo

    // Mise à jour de l'atténuation du brouillard lointain (Clipping PS2)
    for mut fog in fog_query.iter_mut() {
        fog.color = ambient_color * 0.8;
        // La densité augmente avec la météo
        // fog.falloff = FogFalloff::Linear { ... } // À adapter selon la topologie
    }
}
```
