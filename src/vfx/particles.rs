use bevy::prelude::*;
use super::events::{NetEventVisualEffect, StandardEffects};

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

/// Instanciation des Effets (Explosions et Additive Blending)
pub fn process_incoming_effect_events_system(
    mut commands: Commands,
    mut events: EventReader<NetEventVisualEffect>,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
    asset_server: Res<AssetServer>,
) {
    for event in events.read() {
        let Some(effect) = StandardEffects::from_u16(event.effect_id) else { continue };

        match effect {
            StandardEffects::FireblastExplosion => {
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
            },
            // Gérer les autres effets ici (ArcaneMissileImpact, HealAura, etc.)
            _ => {}
        }
    }
}
