use bevy::prelude::*;
use bevy::render::texture::ImageSamplerDescriptor;

mod camera;
mod environment;
mod player;
mod ui;

fn main() {
    App::new()
        .add_plugins(
            DefaultPlugins
                .set(WindowPlugin {
                    primary_window: Some(Window {
                        title: "Elara's Black Mist - Terminal Client (Vertical Slice)".to_string(),
                        resolution: (1280.0, 720.0).into(),
                        ..default()
                    }),
                    ..default()
                })
                .set(ImagePlugin {
                    // Force nearest neighbor filtering globally for PS2 style
                    default_sampler: ImageSamplerDescriptor::nearest(),
                }),
        )
        .add_systems(Startup, setup_camera)
        .add_plugins(environment::EnvironmentPlugin)
        .add_plugins(ui::UiPlugin)
        .add_plugins(player::PlayerPlugin)
        .add_plugins(camera::CameraPlugin)
        .run();
}

fn setup_camera(mut commands: Commands) {
    // 3D Camera for the world, will be updated by camera_follow_player system
    commands.spawn(Camera3dBundle {
        transform: Transform::from_xyz(0.0, 5.0, 10.0).looking_at(Vec3::ZERO, Vec3::Y),
        ..default()
    });
}
