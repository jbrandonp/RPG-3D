# Document de Conception Technique (TDD) : Système d'Animation et Effets Visuels (VFX)

## 1. Objectifs et Périmètre

Ce document de conception technique détaille l'architecture et les spécifications d'implémentation du système d'animation, des états de personnages et des effets visuels pour le projet MMORPG. Basé sur le moteur **Bevy (Rust)**, le système doit conjuguer une direction artistique tridimensionnelle rétro (génération PlayStation 2 / Metin2) avec une infrastructure réseau moderne, garantissant réactivité client et intégrité serveur (serveur autoritaire).

---

## 2. Direction Artistique et Modélisation 3D

### 2.1. Esthétique "Rétro 3D"
L'esthétique globale est contrainte par des directives techniques précises afin d'assurer de hautes performances sur un grand nombre d'entités simultanées et d'évoquer l'ère des MMO du début des années 2000.
- **Format Standardisé :** L'intégralité des assets animés doit être exportée au format **glTF 2.0** (`.glb`).
- **Squelettage (Rigging) Optimisé :** L'animation squelettique (Skeletal Animation) imposera une limite stricte sur le nombre d'os (bones) par modèle (généralement < 30 pour les PNJ mineurs, < 60 pour les joueurs) afin d'alléger le traitement CPU/GPU.
- **Interpolation et Blending :** Les transitions d'animation (blending) seront configurées sur des durées très courtes (ex: `0.1s` à `0.2s`). Cette contrainte technique volontaire produit un rendu vif et "arcade", caractéristique des cibles visuelles de référence.

---

## 3. Architecture Logicielle et Intégration Bevy

Le système d'animation s'intègre au cœur du paradigme ECS (Entity Component System) de Bevy. Le serveur gère la logique d'état en mode *headless*, tandis que le client traduit ces états en instructions visuelles.

### 3.1. Composants et Graphes d'Animation
L'architecture client s'appuiera sur les composants natifs de Bevy et sur des machines à états finis (FSM).

```rust
use bevy::prelude::*;
use serde::{Deserialize, Serialize};

/// Représente l'état canonique d'une entité (partagé Client/Serveur)
#[derive(Component, Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub enum EntityState {
    Idle,
    Locomotion(LocomotionType),
    Attacking(AttackAction),
    Casting(SpellId),
    HitRecovery,
    Dead,
}

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub enum LocomotionType { Walking, Running }

#[derive(Debug, Clone, PartialEq, Eq, Serialize, Deserialize)]
pub enum AttackAction { MeleeStrike(u8), RangedDraw }

/// Composant local au client liant l'entité à ses nœuds d'animation
#[derive(Component)]
pub struct AnimationController {
    pub graph_handle: Handle<AnimationGraph>,
    pub node_indices: std::collections::HashMap<EntityState, AnimationNodeIndex>,
    pub current_state: EntityState,
}
```

### 3.2. Système de Résolution d'Animation
Un système dédié côté client observera les mutations du composant `EntityState` et pilotera l'`AnimationPlayer` via l'`AnimationTransitions` pour effectuer le blending.

```rust
fn update_animations_system(
    mut query: Query<(
        &EntityState,
        &mut AnimationController,
        &mut AnimationPlayer,
        &mut AnimationTransitions
    ), Changed<EntityState>>,
) {
    for (new_state, mut controller, mut player, mut transitions) in query.iter_mut() {
        if controller.current_state != *new_state {
            if let Some(&node_index) = controller.node_indices.get(new_state) {
                // Transition avec un fondu de 0.15 secondes
                transitions.play(&mut player, *node_index, std::time::Duration::from_secs_f32(0.15));
            }
            controller.current_state = new_state.clone();
        }
    }
}
```

---

## 4. Topologie Réseau : Synchronisation, Prédiction et Rollback

Le postulat de base est la souveraineté du serveur (Autorité Serveur). Cependant, pour pallier la latence perçue (RTT - Round Trip Time), le client emploie des algorithmes de prédiction locale et de réconciliation.

### 4.1. Protocole de Communication (Exemple)

```rust
/// Paquet envoyé par le client au serveur
#[derive(Serialize, Deserialize)]
pub enum ClientCommand {
    ActionRequest { action: ActionType, timestamp: u64 },
    MovementInput { direction: Vec2, timestamp: u64 },
}

/// Paquet envoyé par le serveur au client
#[derive(Serialize, Deserialize)]
pub enum ServerResponse {
    ActionConfirmed { action_id: u64 },
    ActionDenied { reason: DenialReason, rollback_state: EntityState },
    StateSnapshot { entity_id: u64, state: EntityState, position: Vec3, server_tick: u64 },
}
```

### 4.2. Prédiction Locale et Rollback
Lorsqu'un joueur local initie une action (ex: frappe à l'épée) :
1. **Application Locale (Instant $T_0$) :** Le client mute immédiatement son `EntityState` à `Attacking(MeleeStrike(1))` et déclenche l'animation et les effets sonores associés. Il stocke cette intention dans un buffer circulaire d'états prédictifs.
2. **Transmission :** L'événement `ActionRequest` est expédié au serveur.
3. **Réconciliation (Instant $T_0 + RTT$) :**
   - **Succès :** Le serveur valide l'action et broadcast l'événement aux autres clients. Le client local confirme l'état prédictif.
   - **Échec (Rollback) :** Si le serveur rejette l'action (ex: ressource insuffisante, étourdissement serveur non encore reçu par le client), le client reçoit `ActionDenied`. Le système d'animation force alors une interruption abrupte de l'animation en cours pour revenir à l'état canonique dicté par le serveur (`rollback_state`), corrigeant ainsi la désynchronisation.

### 4.3. Algorithme de Compensation de Latence (Lag Compensation)
Afin d'assurer la précision des attaques malgré le délai réseau, le serveur maintient un historique de l'état du monde (Positions, Hitboxes) sur les dernières millisecondes (généralement ~500ms).

Lors de la réception d'une requête d'attaque (ex: projectile ou coup ciblé) avec le `timestamp` client $T_c$ :
1. Le serveur calcule l'écart de temps $\Delta t$ entre l'heure actuelle serveur $T_s$ et l'heure estimée de l'action du client $T_c$.
2. Le serveur "rembobine" l'état physique du monde à $T_s - \Delta t$.
3. Le serveur effectue le test de collision (Raycast ou Overlap de la Hitbox de l'arme avec les Hurtboxes des entités).
4. Le résultat est résolu et les dommages sont appliqués, puis broadcastés aux clients.
Cela garantit que si le client voyait sa cible dans son viseur, l'attaque touchera, indépendamment de la latence, évitant la frustration d'un tir "fantôme".

---

## 5. Spécifications du Catalogue des Animations

### 5.1. Matrice des États des Joueurs (PJ)
Le système d'animation gère de manière modulaire les sets d'animations en fonction de l'arme équipée.

| État (`EntityState`) | Condition de Déclenchement | Animation Associée (Clip) | Bouclage | Règles de Blending / Transition |
|----------------------|---------------------------|---------------------------|----------|--------------------------------|
| `Idle` | Absence d'input de mouvement ou d'action | Respiration lente | Oui | Transition douce depuis `Locomotion` |
| `Locomotion(Walking)`| Vitesse > 0, Input de marche | Démarche d'exploration | Oui | Basé sur la vélocité (`BlendSpace` 1D) |
| `Locomotion(Running)`| Input de course | Course soutenue | Oui | Basé sur la vélocité (`BlendSpace` 1D) |
| `Attacking(MeleeStrike)` | Input d'attaque de mêlée validé | Coup d'arme (Combo 1/2/3) | Non | Annule `Locomotion`. Priorité absolue. |
| `Casting(SpellId)` | Initiation d'un sort | Incantation (bras levés) | Oui | Ne peut être interrompu que par `HitRecovery` |
| `HitRecovery` | Dommages encaissés dépassant le seuil de posture | Tressaillement (Flinch) | Non | Interrompt `Attacking` et `Casting` |
| `Dead` | Points de vie à 0 | Effondrement physique | Non | Ne transitionne vers rien sauf `Idle` (Résurrection) |

### 5.2. Comportements des PNJ et Boss
Pour des raisons d'optimisation (LOD - Level of Detail pour l'animation), les créatures exploitent une FSM simplifiée.
- **Créatures Standard :** Limité à `Idle`, `Locomotion`, `Aggro_Shout` et `Attack_Simple`.
- **Boss :** Intégration d'événements d'animation ("Animation Notifies") synchronisés aux frames clés pour déclencher des tremblements de caméra (Camera Shake) ou spawner des AOE (Area of Effect) via le système `AnimationEvents` de Bevy.

### 5.3. Architecture des Effets Visuels (VFX)
Les effets visuels complètent l'animation pour retranscrire la lourdeur et l'impact des actions.

1. **Particules GPU-Driven :**
   Les magies et éléments environnementaux utilisent des systèmes de particules (via l'intégration de bibliothèques tierces compatibles Bevy comme `bevy_hanabi`). Les émetteurs sont attachés hiérarchiquement aux os spécifiques (ex: la main d'un mage via `BoneTarget`).
2. **Shaders Polymorphes et Décalcomanies :**
   Les AOE au sol exploitent des meshs plats avec des matériaux dotés de shaders de défilement UV (UV Scrolling) et de modification de canal Alpha temporelle, évitant l'instanciation coûteuse de géométries complexes.
3. **Imposteurs Visuels (Billboards 2D) :**
   Pour honorer l'esthétique Metin2/PS2, les impacts d'armes génèrent de brèves textures 2D orientées vers la caméra (Billboarding). Le serveur envoie l'événement `EntityHit`, le client instancie un quad éphémère (Durée de vie : ~0.15s) sur la position ciblée.

---

## 6. Séquencement du Déploiement et Intégration

L'implémentation de ces spécifications suivra un ordonnancement incrémental :

- **Phase 1 : Socle Technique (Core Animation)**
  - Intégration du composant `AnimationController` et d'un modèle glTF de référence ("Dummy").
  - Implémentation du système `update_animations_system` et test des transitions `Idle` <-> `Locomotion`.
- **Phase 2 : FSM et Infrastructure Réseau**
  - Mise en place du buffer de prédiction locale et de la logique de Rollback.
  - Test de l'interruption abrupte (annulation de l'attaque par le serveur).
- **Phase 3 : Équité Compétitive**
  - Programmation de la structure de l'historique temporel (Snapshots) sur le serveur.
  - Implémentation mathématique de l'algorithme de Lag Compensation pour la résolution des Hitboxes.
- **Phase 4 : Polissage Visuel (VFX)**
  - Attachement dynamique d'émetteurs de particules aux matrices de transformation des os.
  - Intégration du système de billboards 2D pour les retours visuels d'impact.
