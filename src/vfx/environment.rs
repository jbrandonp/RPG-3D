use bevy::prelude::*;

/// Ressource globale contrôlant l'atmosphère du client
#[derive(Resource)]
pub struct EnvironmentAtmosphere {
    pub diurnal_cycle_time: f32, // Heure locale du serveur normalisée (0.0 à 24.0)
    pub weather_intensity: f32,  // Ex: 0.0 = Dégagé, 1.0 = Tempête
}

impl Default for EnvironmentAtmosphere {
    fn default() -> Self {
        Self {
            diurnal_cycle_time: 12.0, // Commence à midi
            weather_intensity: 0.0,   // Dégagé
        }
    }
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
        // Exemple (commenté pour éviter une erreur de build si la topologie n'est pas setupée):
        // fog.falloff = FogFalloff::Linear { start: 10.0, end: 50.0 - (atmosphere.weather_intensity * 20.0) };
    }
}
