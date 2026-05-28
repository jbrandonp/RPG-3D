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

/// Dictionnaire des effets standards
pub enum StandardEffects {
    ArcaneMissileImpact = 101,
    FireblastExplosion = 102,
    HealAura = 201,
}

impl StandardEffects {
    pub fn from_u16(value: u16) -> Option<Self> {
        match value {
            101 => Some(StandardEffects::ArcaneMissileImpact),
            102 => Some(StandardEffects::FireblastExplosion),
            201 => Some(StandardEffects::HealAura),
            _ => None,
        }
    }
}
