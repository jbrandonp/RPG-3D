use crate::player::DummyPlayer;
use bevy::prelude::*;

pub struct CameraPlugin;

impl Plugin for CameraPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Update, camera_follow_player);
    }
}

fn camera_follow_player(
    player_query: Query<&Transform, (With<DummyPlayer>, Without<Camera3d>)>,
    mut camera_query: Query<&mut Transform, With<Camera3d>>,
) {
    if let Ok(player_transform) = player_query.get_single() {
        if let Ok(mut camera_transform) = camera_query.get_single_mut() {
            let offset = Vec3::new(0.0, 5.0, 8.0);
            let target_position = player_transform.translation + offset;
            camera_transform.translation = camera_transform.translation.lerp(target_position, 0.1);
            camera_transform.look_at(player_transform.translation, Vec3::Y);
        }
    }
}
