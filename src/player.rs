use bevy::prelude::*;

pub struct PlayerPlugin;

impl Plugin for PlayerPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Startup, setup_dummy_player)
            .add_systems(Update, player_movement);
    }
}

#[derive(Component)]
pub struct DummyPlayer {
    pub speed: f32,
}

fn setup_dummy_player(
    mut commands: Commands,
    mut meshes: ResMut<Assets<Mesh>>,
    mut materials: ResMut<Assets<StandardMaterial>>,
) {
    info!("Spawning Dummy Player for Vertical Slice testing...");

    commands.spawn((
        PbrBundle {
            mesh: meshes.add(Capsule3d::new(0.3, 1.1)),
            material: materials.add(StandardMaterial {
                base_color: Color::rgb(0.2, 0.6, 0.8),
                unlit: true,
                ..default()
            }),
            transform: Transform::from_xyz(0.0, 1.1 / 2.0, 0.0),
            ..default()
        },
        DummyPlayer { speed: 5.0 },
    ));

    commands.spawn(PbrBundle {
        mesh: meshes.add(Capsule3d::new(0.3, 0.8)),
        material: materials.add(StandardMaterial {
            base_color: Color::rgb(0.2, 0.8, 0.2),
            unlit: true,
            ..default()
        }),
        transform: Transform::from_xyz(3.0, 0.8 / 2.0, -3.0),
        ..default()
    });
}

fn player_movement(
    keyboard_input: Res<ButtonInput<KeyCode>>,
    time: Res<Time>,
    mut query: Query<(&mut Transform, &DummyPlayer)>,
) {
    if let Ok((mut transform, player)) = query.get_single_mut() {
        let mut direction = Vec3::ZERO;

        if keyboard_input.pressed(KeyCode::KeyW) || keyboard_input.pressed(KeyCode::ArrowUp) {
            direction.z -= 1.0;
        }
        if keyboard_input.pressed(KeyCode::KeyS) || keyboard_input.pressed(KeyCode::ArrowDown) {
            direction.z += 1.0;
        }
        if keyboard_input.pressed(KeyCode::KeyA) || keyboard_input.pressed(KeyCode::ArrowLeft) {
            direction.x -= 1.0;
        }
        if keyboard_input.pressed(KeyCode::KeyD) || keyboard_input.pressed(KeyCode::ArrowRight) {
            direction.x += 1.0;
        }

        if direction != Vec3::ZERO {
            direction = direction.normalize();
            let movement = direction * player.speed * time.delta_seconds();
            transform.translation += movement;
        }
    }
}
