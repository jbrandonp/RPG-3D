use bevy::prelude::*;

pub struct EnvironmentPlugin;

impl Plugin for EnvironmentPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Startup, setup_environment);
    }
}

fn setup_environment(mut commands: Commands, asset_server: Res<AssetServer>) {
    info!("Loading Velnor Slums environment props...");

    let tile_handle = asset_server.load("models/prop_floor_tile.glb#Scene0");

    // Spawn a 5x5 grid of floor tiles
    for x in -2..=2 {
        for z in -2..=2 {
            commands.spawn(SceneBundle {
                scene: tile_handle.clone(),
                transform: Transform::from_xyz(x as f32 * 1.0, 0.0, z as f32 * 1.0),
                ..default()
            });
        }
    }

    let barrel_handle = asset_server.load("models/prop_barrel.glb#Scene0");
    commands.spawn(SceneBundle {
        scene: barrel_handle,
        transform: Transform::from_xyz(1.0, 0.0, 1.0),
        ..default()
    });

    let crate_handle = asset_server.load("models/prop_crate.glb#Scene0");
    commands.spawn(SceneBundle {
        scene: crate_handle,
        transform: Transform::from_xyz(-1.0, 0.0, -1.0),
        ..default()
    });

    commands.spawn(PointLightBundle {
        point_light: PointLight {
            intensity: 1500.0,
            shadows_enabled: true,
            ..default()
        },
        transform: Transform::from_xyz(4.0, 8.0, 4.0),
        ..default()
    });
}
