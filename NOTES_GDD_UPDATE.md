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

## 2. SYSTÈME DE CLASSES, LEVEL CAP ET SPÉCIALISATION
L'ancien système "classless" est remplacé par une arborescence de spécialisations liée aux traumatismes vécus.
- L'avatar débute en tant que `Survivor` (sans classe).
- Les classes se débloquent via les actions : l'extermination à la dague/poison débloque la classe `Exterminator_Hybrid` ; l'exposition volontaire au Brouillard Noir débloque `Corrupted_Thaumaturge`.
- **Level Cap (Niveau 100) :** Un blocage systémique dur est imposé. Au-delà du niveau 50, la courbe d'XP devient logarithmique, empêchant mathématiquement une ascension infinie pour justifier qu'un joueur vieux de 400 ans (Kazuki) soit bloqué aux alentours du niveau 80-90.

## 3. COMBAT HYBRIDE (Style Metin2)
Le système d'affrontement repose sur un modèle hybride mêlant ciblage et action (action-targeting).
- **Attaques de Base :** Les attaques physiques standard génèrent des arcs de dégâts (AoE frontales) touchant plusieurs cibles simultanément (crucial pour survivre aux essaims goblinoïdes).
- **Positionnement & Stun-Lock :** Se faire encercler par un essaim applique un "hit-stun" sévère, forçant le joueur à privilégier l'ingénierie tactique (choke points, pièges) plutôt que le face-à-face en zone ouverte.

## 4. ÉCONOMIE IA ET INFLUENCE PVP
L'économie des hubs (comme Velnor) n'est pas statique ; elle est régie par un système d'Intelligence Artificielle Macro-économique.
- **Inflation Dynamique :** Si le serveur détecte des émeutes de la faim ou des raids réussis sur les routes commerciales, le prix des vivres de base est multiplié algorithmiquement.
- **Vecteur PvP :** Les actions des "Élus" (Players) influencent directement cette économie. Le meurtre d'un autre joueur ou l'interception d'un convoi de PNJ marchands par une guilde déclenche des alertes économiques, forçant les autres survivants à adapter leurs stratégies de survie.

## 5. MORT PERMANENTE ET ARTÉFACTS RARES
La condition d'échec par défaut (`HP == 0` sans mécanisme de capture) mène à la suppression définitive du profil (Perma-Death).
- **Contournement Système :** L'utilisation d'"Artéfacts Rares" (ex: *Soul-Binding Runes*) consomme l'objet lors du coup fatal, forçant une téléportation asynchrone vers un Safe Node pré-défini.
- Ce mécanisme doit être strictement validé côté serveur pour prévenir toute désynchronisation ou triche client.

## 6. MÉCANIQUE DE REBIRTH ET ARCHITECTURE SÉPARÉE (Corps vs Âme)
Si le joueur subit un Game Over (`HP == 0`) pendant que le `Component` `IncubationStatus` est actif, la mécanique de **Transfert de Conscience (Rebirth)** s'active.
**Contrainte ECS Bevy :** Pour éviter que les données psychologiques (Trauma) et l'ID du joueur ne soient perdus lors du `commands.entity(player).despawn()`, l'architecture doit séparer strictement le Corps de l'Âme.
- Création d'un composant `SoulLink` ou d'une `Resource` serveur liant un `PlayerID` persistant.
- L'entité corporelle (Level, HP, inventaire) est détruite.
- Une nouvelle entité niveau 1 est instanciée et liée au `SoulLink` existant.
- `Goblin_Genome` : +20% Vitesse d'attaque, -30% Charisme Humain.
- `DeepOne_Genome` : Résistance magique accrue.

## 7. ARCHITECTURE DU MONDE, INSTANCES ET BOSS GÉANTS
La géographie de Velnora et l'apparition des "Nids" requièrent une scission stricte de l'environnement virtuel.
- **Monde Ouvert (Asynchrone) :** Le client gère le chunking asynchrone via des `SceneBundle`. Les définitions serveur du monde reposent sur des fichiers de sérialisation légers (JSON/RON).
- **Instances de Nids (Donjons) :** Pour gérer la prolifération Goblinoïde, chaque nid est instancié côté serveur sous la forme d'un `World` Bevy indépendant.
- **Moteur Physique Headless :** Le serveur autoritaire n'effectue aucun calcul sur des "Mesh Colliders" lourds. Toute la navigation et les collisions sont traitées via un **NavMesh statique** et des colliders mathématiques primitifs exclusifs (sphères, boîtes, capsules).
- **Multi-Part Meshes pour les Boss :** Pour contourner la limitation PS2 de "4 os par vertex", les boss géants (Kraken, Horreur) doivent impérativement être segmentés en plusieurs entités (meshes détachés) rattachées au runtime, plutôt qu'un seul gros *SkinnedMesh*.

## 8. ARCHITECTURE RÉSEAU ET NETCODE AVANCÉ (WebTransport / QUIC)
La rudesse des punitions exige une réactivité absolue (Rollback) et une architecture anti-triche infaillible. Le principe directeur est : **« Le client propose, le serveur dispose »**.
- **Mouvement et Prédiction :** Les mouvements sont streamés via des canaux **Unreliable UDP** (QUIC Datagrams). Le client effectue une prédiction locale, soumise à une stricte validation serveur.
- **Lag Compensation & Rollback :** En cas de désaccord lors d'un combat rapide (ex: esquive d'une attaque d'Ogre), le serveur utilise une technique de *rollback* pour valider ou rejeter l'impact en fonction de l'historique précis des positions, envoyant une correction au client.
- **Transactions Critiques :** Les actions irréversibles (consommation d'Artéfacts, validation de Rebirth, modifications d'inventaire) transitent exclusivement par des **Bidirectional Streams (Reliable)**.
- **Observabilité :** L'état mental (Trauma, Corruption) et les événements locaux sont poussés vers ClickHouse via des **Unidirectional Streams**.
