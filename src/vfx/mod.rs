pub mod events;
pub mod particles;
pub mod environment;

use bevy::prelude::*;
use events::NetEventVisualEffect;
use particles::{
    compute_billboard_orientation_system,
    garbage_collect_volatile_effects_system,
    process_incoming_effect_events_system,
};
use environment::{EnvironmentAtmosphere, process_diurnal_cycle_system};

/// Plugin principal gérant tous les Effets Visuels (VFX)
pub struct VfxPlugin;

impl Plugin for VfxPlugin {
    fn build(&self, app: &mut App) {
        app
            // Événements
            .add_event::<NetEventVisualEffect>()
            // Ressources
            .init_resource::<EnvironmentAtmosphere>()
            // Systèmes
            .add_systems(Update, (
                compute_billboard_orientation_system,
                garbage_collect_volatile_effects_system,
                process_incoming_effect_events_system,
                process_diurnal_cycle_system,
            ));
    }
}
