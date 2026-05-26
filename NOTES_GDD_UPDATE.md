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
- Ce mécanisme doit être strictement validé côté serveur pour prévenir toute désynchronisation ou triche client.

## 4. MÉCANIQUE DE REBIRTH (Renaissance Hybride)
Si le joueur subit un Game Over (`HP == 0`) pendant que le `Component` `IncubationStatus` est actif, le serveur purge le personnage principal mais crée une nouvelle Entité Niveau 1, injectant un trait spécifique.
- `Goblin_Genome` : +20% Vitesse d'attaque, -30% Charisme Humain.
- `DeepOne_Genome` : Résistance magique accrue.

## 5. ARCHITECTURE DU MONDE ET GESTION DES INSTANCES
La géographie de Velnora et l'apparition des "Nids" requièrent une scission stricte de l'environnement virtuel.
- **Monde Ouvert (Asynchrone) :** Le client gère le chunking asynchrone via des `SceneBundle`. Les définitions serveur du monde reposent sur des fichiers de sérialisation légers (JSON/RON).
- **Instances de Nids (Donjons) :** Pour gérer la prolifération Goblinoïde, chaque nid est instancié côté serveur sous la forme d'un `World` Bevy indépendant.
- **Moteur Physique Headless :** Le serveur autoritaire n'effectue aucun calcul sur des "Mesh Colliders" lourds. Toute la navigation et les collisions sont traitées via un **NavMesh statique** et des colliders mathématiques primitifs exclusifs (sphères, boîtes, capsules).

## 6. ARCHITECTURE RÉSEAU ET NETCODE AVANCÉ (WebTransport / QUIC)
La rudesse des punitions exige une réactivité absolue (Rollback) et une architecture anti-triche infaillible. Le principe directeur est : **« Le client propose, le serveur dispose »**.
- **Mouvement et Prédiction :** Les mouvements sont streamés via des canaux **Unreliable UDP** (QUIC Datagrams). Le client effectue une prédiction locale, soumise à une stricte validation serveur.
- **Lag Compensation & Rollback :** En cas de désaccord lors d'un combat rapide (ex: esquive d'une attaque d'Ogre), le serveur utilise une technique de *rollback* pour valider ou rejeter l'impact en fonction de l'historique précis des positions, envoyant une correction au client.
- **Transactions Critiques :** Les actions irréversibles (consommation d'Artéfacts, validation de Rebirth, modifications d'inventaire) transitent exclusivement par des **Bidirectional Streams (Reliable)**.
- **Observabilité :** L'état mental (Trauma, Corruption) et les événements locaux sont poussés vers ClickHouse via des **Unidirectional Streams**.
