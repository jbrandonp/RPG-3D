//! Exemple de code Bevy pour l'import et le paramétrage du rendu Rétro (Sprint 0)
//!
//! Cet exemple montre comment :
//! 1. Configurer Bevy avec un filtrage Nearest-Neighbor (pixelisé).
//! 2. Charger une scène glTF issue du pipeline (Unlit).
//! 3. Désactiver les calculs d'éclairage superflus pour coller au style PS2.

use bevy::{
    prelude::*,
    render::texture::ImageSampler,
};

fn main() {
    App::new()
        // 1. Initialisation des plugins Bevy
        .add_plugins(DefaultPlugins.set(ImagePlugin {
            // FORCER LE NEAREST-NEIGHBOR : Crucial pour le style rétro/pixelisé
            // Cela désactive le filtrage linéaire/anti-aliasing sur toutes les textures.
            default_sampler: ImageSampler::nearest_descriptor(),
        }))
        .add_systems(Startup, setup)
        .run();
}

fn setup(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    // 2. Chargement de l'Asset (issu de Blender -> glTF -> .glb)
    // Le .glb a été exporté avec l'extension KHR_materials_unlit.
    // Bevy le lira et créera un StandardMaterial avec "unlit: true".
    commands.spawn(SceneBundle {
        // Le "#Scene0" indique qu'on charge la première (et unique) scène du fichier glb
        scene: asset_server.load("models/dummy_character.glb#Scene0"),
        transform: Transform::from_xyz(0.0, 0.0, 0.0),
        ..default()
    });

    // 3. Configuration de la Caméra
    // Une caméra basique pour observer l'asset.
    commands.spawn(Camera3dBundle {
        transform: Transform::from_xyz(0.0, 5.0, 10.0).looking_at(Vec3::ZERO, Vec3::Y),
        ..default()
    });

    // NOTE IMPORTANTE SUR LA LUMIERE :
    // Dans le style "PS2 Hand-Painted", nous n'ajoutons PAS de PointLight ou DirectionalLight
    // globale pour éclairer le personnage (les ombres sont peintes).
    // Le matériau Unlit affichera la texture telle quelle (albedo brut).
}
