# NOTES DE MISE À JOUR : GAME DESIGN DOCUMENT (GDD)

Suite à la bascule narrative vers l'univers de **"Elara's Black Mist"**, le fichier `GAME_DESIGN_DOCUMENT.md` actuel doit être revu en profondeur. Voici les directives techniques, conceptuelles et architecturales à intégrer :

## 1. NOUVELLES STATISTIQUES JOUEUR (Variables d'État ECS)
Le profil de personnage d'Elara n'est plus classique. La survie psychologique et physique se quantifie via de nouvelles jauges.

**Implémentation Bevy (Rust) :**
```rust
#[derive(Component)]
pub struct PsychologicalState {
    pub trauma_index: f32, // (0.0 - 100.0)
    pub corruption_index: f32, // (0.0 - 100.0)
}

#[derive(Component)]
pub struct IncubationStatus {
    pub is_active: bool,
    pub genome_seed: EntityType, // Détermine le trait hérité en cas de Rebirth
    pub cycle_timer: Timer,
}
```
- **Trauma :** À partir de 75, désactivation temporaire du contrôle moteur (Fuite impossible) ou buff non ciblé de type `Cold_Rage`.
- **Corruption :** Modifie le rendu du modèle 3D du joueur (vertex colors) et les tables d'hostilité des PNJ.

## 2. SYSTÈME DE CLASSES ET SPÉCIALISATION
L'ancien système "classless" est remplacé par une arborescence de spécialisations liée aux traumatismes vécus.
- L'avatar débute en tant que `Survivor` (sans classe).
- Les classes se débloquent via les actions : l'extermination à la dague/poison débloque la classe `Exterminator_Hybrid` ; l'exposition volontaire au Brouillard Noir débloque `Corrupted_Thaumaturge`.

## 3. MORT PERMANENTE ET ARTÉFACTS RARES
La condition d'échec par défaut (`HP == 0` sans mécanisme de capture) mène à la suppression définitive du profil (Perma-Death).
- **Contournement Système :** L'utilisation d'"Artéfacts Rares" (ex: *Soul-Binding Runes*) consomme l'objet lors du coup fatal, forçant une téléportation asynchrone vers un Safe Node pré-défini.
- Ce mécanisme doit être validé côté serveur pour prévenir la triche client.

## 4. MÉCANIQUE DE REBIRTH (Renaissance Hybride)
Si le joueur subit un Game Over (`HP == 0`) pendant que le `Component` `IncubationStatus` est actif, le serveur purge le personnage principal mais crée une nouvelle Entité Niveau 1, injectant un trait spécifique.
- `Goblin_Genome` : +20% Vitesse d'attaque, -30% Charisme Humain.
- `DeepOne_Genome` : Résistance magique accrue.

## 5. ARCHITECTURE RÉSEAU (WebTransport / QUIC)
La rudesse des punitions exige une réactivité sans faille et une architecture anti-triche stricte ("Le client propose, le serveur dispose").
- Les mouvements et le positionnement sont streamés via des canaux **Unreliable UDP** (QUIC Datagrams) avec de la prédiction côté client.
- Les actions irréversibles (consommation d'un Artéfact Rare, validation d'un état de Capture ou de Mort, loot d'objets vitaux) sont traitées via des **Bidirectional Streams (Reliable)**.
- Les mises à jour de l'état mental (Trauma, Corruption) peuvent être synchronisées en arrière-plan via des **Unidirectional Streams**.

## 6. DYNAMIQUES DE MONDE ET RENDU (Le Brouillard Noir)
- Le serveur orchestre une horloge globale. Lorsqu'une zone est consumée par le Brouillard, le serveur notifie les clients de modifier l'état visuel du Chunk correspondant.
- **Rendu Visuel Client :** Le jeu impose l'utilisation de shaders basiques (`KHR_materials_unlit`) sans éclairage dynamique, limitant les modèles à 5,000 polygones avec un filtrage *Nearest-Neighbor*. Les ombres sont intégrées directement dans les textures (Baking), soulignant la rigidité cruelle de l'environnement PS2.
