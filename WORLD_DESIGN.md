# Conception du Monde et Level Design : Projet MMO Dark Fantasy

Ce document détaille la vision, les environnements, le bestiaire et les mécaniques du monde pour notre MMORPG indépendant. Le design est pensé pour s'intégrer avec une architecture technique moderne (Moteur Bevy, ECS, serveur autoritaire), tout en conservant une direction artistique rétro (style PS2 / Metin2).

---

## 1. Vision et Ambiance (Dark Fantasy)

### Direction Artistique
- **Thème :** Un monde crépusculaire, poisseux et désespéré. La lumière est rare, le monde est en ruine suite à un cataclysme impie.
- **Rendu Visuel (Rétro PS2) :** Modèles low-poly, textures basse résolution avec filtrage `Nearest` (pixelisé), brouillard volumétrique intense pour masquer la distance d'affichage courte (et optimiser les performances). Les couleurs dominantes sont le gris cendré, le rouge sang et le vert maladif.
- **Ambiance Sonore :** Vents lugubres, tintements de cloches lointaines, bruits de pas amplifiés dans les donjons, râles étouffés des monstres.

### Intégration Technique (Bevy Engine)
- **Rendu WGPU :** Le brouillard est géré via un composant `FogSettings` global qui adapte sa densité selon la zone active.
- **Eclairage :** Éclairage minimaliste. Les joueurs portent une lumière dynamique (composant `PointLight` avec un faible rayon) pour explorer.

---

## 2. Structure de la Carte et Zones (World Map)

Le monde est construit autour de "Chunks" gérés par un système de partitionnement spatial (Grid / Octree). Le serveur ne simule que les chunks contenant des joueurs.

### Zone 1 : Le Hameau des Cendres (Hub Central)
- **Ambiance :** Un village en ruine fortifié, dernier rempart de l'humanité. Un immense feu de joie central éclaire la zone.
- **Parcours :** Architecture radiale et sécurisante. Des tentes et des marchands entourent le feu.
- **PNJ & Points d'intérêt :**
  - Forgeron Damné (Artisanat).
  - Marchand d'Âmes (Achat de consommables).
- **Note Technique :** La zone possède un composant `SafeZone`. Un système serveur écoute les événements d'attaque (`AttackEvent`) et les annule si l'entité visée a le marqueur `SafeZone`.

### Zone 2 : La Forêt des Écorchés (Zone de Progression Initial)
- **Ambiance :** Des arbres tordus sans feuilles, une brume épaisse, un sol boueux jonché de racines épineuses.
- **Parcours :** Chemins sinueux et étroits. Les hors-pistes sont remplis de "Ronces Corrompues" (zones qui infligent un debuff de ralentissement via un composant `SpeedModifier { factor: 0.5 }`).
- **Placement d'ennemis :** Des petits camps de monstres près de feux éteints. Les ennemis patrouillent le long des routes principales.

### Zone 3 : Les Marais Sanglants (Zone Intermédiaire)
- **Ambiance :** Eaux troubles rougeâtres, carcasses de créatures géantes, gaz toxiques verts.
- **Parcours :** De petites îles interconnectées par des ponts pourris ou des passages dans l'eau. Marcher dans l'eau réduit l'agilité et attire certaines créatures.
- **Note Technique :** L'eau est gérée par des "Trigger Volumes" (détection de collision via Bevy Rapier) qui ajoutent un composant `InWater` aux entités qui la traversent.

### Zone 4 : La Cathédrale d'Obsidienne (Donjon Instancié)
- **Ambiance :** Architecture gothique monumentale, vitraux brisés, pénombre percée par des bougies magiques.
- **Parcours :** Structure linéaire sous forme de "Salles d'Épreuves". Les portes (`DoorComponent { locked: true }`) ne s'ouvrent que lorsque tous les ennemis de la salle (possédant un composant `RoomId`) sont vaincus.
- **Note Technique (Instanciation) :** Côté serveur, chaque groupe qui entre crée une nouvelle collection d'entités avec un composant `InstanceId(UUID)`. Les requêtes ECS (Systems) filtrent systématiquement par `InstanceId` pour séparer les calculs entre les différents groupes de joueurs.

---

## 3. Bestiaire et Placement (IA et Combats)

Les ennemis sont gérés par des arbres de comportement (Behavior Trees) ou des machines à états finis implémentées via des composants Bevy (ex: `State<EnemyState>`).

| Ennemi | Zone | Comportement (IA) & Caractéristiques | Loots (Lâchés) |
|---|---|---|---|
| **Goule Cendrée** | Forêt | **Melee Swarm :** Fonce sur le joueur le plus proche dès qu'il entre dans l'Aggro Radius (`Sensor` collider). Attaque rapidement. | Ossements, Tissu déchiré |
| **Corbeau de Sang** | Forêt | **Hit & Run :** Perché en hauteur, attaque en piqué puis s'éloigne. Géré avec une interpolation de trajectoire. | Plumes d'Ombre |
| **Noyé en Armure** | Marais | **Tank / Embuscade :** Spawn dynamique sous l'eau quand un joueur approche. Lent, mais a des attaques de zone (AoE). | Éclats de Fer Rouillé |
| **Prêtre Déchu (Boss)** | Donjon | **Phases Multiples :** <br>Phase 1 : Attaques à distance (Projectiles avec `Velocity`). <br>Phase 2 (50% HP) : Invoque des Goules et se téléporte. | Relique Impie, Arme Épique |

### Le Système de Spawners
Les ennemis ne sont pas placés manuellement un par un. Le Level Design utilise des "Nids" (Spawners) :
- Entité avec le composant : `Spawner { enemy_type: EnemyType::Goule, cooldown: Timer, max_entities: 3, radius: 10.0 }`.
- Un système Bevy (`spawner_system`) vérifie l'état du Spawner et instancie de nouveaux monstres si les anciens ont été éliminés.

---

## 4. Objets, Équipements et Intégration ECS

Les objets existent dans le monde sous forme de "Pickups" et dans l'inventaire sous forme de données.

### Équipements
- **Lame Rouillée d'Inquisiteur (Arme de base) :**
  - Statistiques : Dégâts faibles, vitesse moyenne.
  - Effet : 10% de chance d'appliquer l'altération "Tétanos" (DoT - Damage over Time).
  - ECS : Ajoute un système asynchrone côté serveur appliquant `Health -= 2` toutes les secondes.
- **Masse d'Os Lourd :**
  - Statistiques : Dégâts lourds, très lent.
  - Effet : Ignore 30% de l'armure (Calcul géré dans le `DamageCalculationSystem`).

### Consommables
- **Fiole de Sang Purifié :**
  - Restaure instantanément une portion de la santé.
  - Technique : Envoie un événement `HealEvent { target: Entity, amount: 50 }` intercepté par le serveur.
- **Poussière d'Étoile Morte :**
  - Booste temporairement la vitesse de déplacement et d'attaque.
  - Technique : Ajoute temporairement un composant `Buff { duration: Timer::from_seconds(10.0) }` au joueur.

---

## 5. Synthèse Technique du Level Design

Pour un MMO scalable développé avec Rust/Bevy, le level design doit respecter ces contraintes :

1. **Pas de logique côté client :** Les portes, les dégâts de zone (Marais) et les comportements des monstres sont calculés uniquement sur le serveur. Le client ne gère que le rendu visuel et l'envoi d'inputs (Z, Q, S, D, Clics).
2. **Streaming du Monde :** Le Level Designer construit la carte sur un éditeur (Tiled, Blender, ou éditeur custom), puis exporte les données en format léger (ex: JSON ou binaire). Le serveur charge ces données et instancie les colliders Rapier invisibles.
3. **Data-Oriented Design :** Tout le contenu (HP des monstres, dégâts des armes) est stocké de manière contiguë en mémoire. Les équilibrages se font en modifiant des fichiers de configuration (Assets), rechargés à chaud (Hot-Reloading) par Bevy sans redémarrer le serveur.
