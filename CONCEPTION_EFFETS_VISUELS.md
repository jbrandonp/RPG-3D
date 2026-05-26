# Conception des Effets Visuels (MMORPG Style PS2)

## 1. Introduction et Philosophie

Dans le cadre du développement de notre MMORPG sous **Bevy (Rust)**, la direction artistique s'oriente vers un rendu **rétro (style PlayStation 2 / Metin2)**. L'objectif technique derrière ce choix esthétique est d'allouer 100 % de la puissance de calcul serveur à la simulation massivement multijoueur, tout en garantissant une compatibilité maximale sur d'anciennes machines côté client.

Ce document définit l'architecture et l'implémentation des effets visuels (sorts, explosions, particules, lumières et environnements) en respectant nos deux piliers : **le client "terminal"** et **l'optimisation extrême des rendus**.

---

## 2. Architecture Réseau : Le Client "Terminal"

Dans notre architecture, le serveur est **totalement autoritaire**. Le client n'est qu'un terminal d'affichage qui interprète l'état du monde.

Pour les effets visuels (VFX), cela implique que **le serveur ne calcule jamais les particules ou la lumière**. Le processus se déroule ainsi :
1. **Intention** : Le joueur lance un sort (ex: Boule de feu).
2. **Validation Serveur** : Le serveur valide l'action et met à jour l'état de la simulation (dégâts, temps de recharge).
3. **Émission d'Événement** : Le serveur envoie au client (et aux joueurs de la zone d'intérêt) un événement réseau léger (ex: `EventSpellCast { spell_id: 1, caster_entity: 42, target_pos: (10.0, 0.0, 15.0) }`).
4. **Rendu Local** : Le client reçoit cet événement et génère les entités visuelles (particules, lumières, sons) purement localement. Ces entités visuelles n'ont aucune collision réseau et disparaissent d'elles-mêmes.

---

## 3. Contraintes Artistiques et Techniques (Style PS2)

Pour recréer l'esthétique PS2 et maintenir une exécution ultra-fluide (via WGPU) :
*   **Modèles et Textures** : Modèles 3D "Low-poly" (faible nombre de polygones), textures basse résolution (ex: 256x256), filtrage de texture point/nearest (pas de lissage bilinéaire pour un effet "pixelisé" ou "crunchy").
*   **Particules (Billboards)** : Utilisation massive de quads 2D toujours face à la caméra (billboarding) au lieu de meshes 3D complexes.
*   **Shaders** : Rendu classique (Forward rendering). Pas de PBR (Physically Based Rendering). Utilisation de shaders basiques (Gouraud shading, flat shading), de Vertex Colors, et d'Alpha Blending additif pour les effets magiques.
*   **Lumières** : Nombre de lumières dynamiques strict limité par objet (souvent entre 2 et 4). Éviter les ombres portées dynamiques douces ; privilégier des blobs noirs sous les personnages.

---

## 4. Systèmes Visuels et Exemples d'Implémentation (Rust/Bevy)

### 4.1. Événements Réseau (Le lien Serveur -> Client)

```rust
use bevy::prelude::*;

// Événement reçu depuis le serveur
#[derive(Event)]
pub struct ServerEventEffect {
    pub effect_type: EffectType,
    pub position: Vec3,
}

pub enum EffectType {
    FireballExplosion,
    HealSparkles,
}
```

### 4.2. Système de Particules (Sorts et Explosions)

Pour rester fidèle à l'ère PS2, un sort comme une explosion se traduit par un ou plusieurs plans (quads) croisés avec des textures animées ou qui grandissent très vite avec un blending additif.

```rust
// Composant pour détruire l'effet visuel après un certain temps (Fire & Forget)
#[derive(Component)]
pub struct Lifetime(Timer);

pub fn spawn_visual_effects_system(
    mut commands: Commands,
    mut events: EventReader<ServerEventEffect>,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
    asset_server: Res<AssetServer>,
) {
    for event in events.read() {
        match event.effect_type {
            EffectType::FireballExplosion => {
                // Création d'une particule type Billboard (Quad 2D)
                commands.spawn((
                    PbrBundle {
                        mesh: meshes.add(shape::Quad::new(Vec2::new(2.0, 2.0)).into()),
                        // Blending additif et texture non éclairée pour un look "VFX Rétro"
                        material: materials.add(StandardMaterial {
                            base_color_texture: Some(asset_server.load("textures/explosion.png")),
                            alpha_mode: AlphaMode::Add,
                            unlit: true,
                            ..default()
                        }),
                        transform: Transform::from_translation(event.position),
                        ..default()
                    },
                    // Le quad disparaît après 0.5 secondes
                    Lifetime(Timer::from_seconds(0.5, TimerMode::Once)),
                    // Composant personnalisé (à implémenter) pour faire toujours face à la caméra
                    Billboard,
                ));
            }
            _ => {}
        }
    }
}

pub fn lifetime_system(
    mut commands: Commands,
    time: Res<Time>,
    mut query: Query<(Entity, &mut Lifetime)>,
) {
    for (entity, mut lifetime) in query.iter_mut() {
        if lifetime.0.tick(time.delta()).just_finished() {
            commands.entity(entity).despawn_recursive();
        }
    }
}
```

### 4.3. Lumières Dynamiques (Éclairage des sorts)

Les lumières doivent être limitées. Lorsqu'une explosion se produit, on peut instancier une `PointLight` flash très brève.

```rust
pub fn spawn_explosion_light(
    mut commands: Commands,
    mut events: EventReader<ServerEventEffect>,
) {
    for event in events.read() {
        if let EffectType::FireballExplosion = event.effect_type {
            commands.spawn((
                PointLightBundle {
                    point_light: PointLight {
                        color: Color::rgb(1.0, 0.5, 0.0), // Orange feu
                        intensity: 1500.0,
                        range: 10.0,
                        shadows_enabled: false, // Pas d'ombres pour des raisons de perfs (PS2 style)
                        ..default()
                    },
                    transform: Transform::from_translation(event.position),
                    ..default()
                },
                Lifetime(Timer::from_seconds(0.3, TimerMode::Once)), // Le flash lumineux est très court
            ));
        }
    }
}
```

### 4.4. Environnements Dynamiques (Météo & Jour/Nuit)

Sur les anciens moteurs, le cycle jour/nuit se gère souvent par un simple changement de la couleur de la lumière ambiante (`AmbientLight`) et l'interpolation des couleurs du brouillard (`Fog`), plutôt que par des calculs complexes du ciel.

```rust
#[derive(Resource)]
pub struct DayNightCycle {
    pub time_of_day: f32, // De 0.0 à 24.0
    pub time_multiplier: f32,
}

pub fn day_night_system(
    time: Res<Time>,
    mut cycle: ResMut<DayNightCycle>,
    mut ambient_light: ResMut<AmbientLight>,
    mut fog_query: Query<&mut FogSettings>,
) {
    // Avancer le temps local
    cycle.time_of_day += time.delta_seconds() * cycle.time_multiplier;
    if cycle.time_of_day >= 24.0 {
        cycle.time_of_day -= 24.0;
    }

    // Calcul simple d'une intensité lumineuse (1.0 = midi, 0.1 = minuit)
    let intensity = (cycle.time_of_day / 24.0 * std::f32::consts::PI * 2.0).cos() * -0.45 + 0.55;

    // Assombrir la lumière globale et bleuter la teinte la nuit
    ambient_light.color = Color::rgb(intensity, intensity, intensity * 1.2);
    ambient_light.brightness = intensity;

    // Mise à jour de la couleur du brouillard (distance clipping PS2)
    for mut fog in fog_query.iter_mut() {
        fog.color = Color::rgb(intensity * 0.8, intensity * 0.8, intensity);
    }
}
```
