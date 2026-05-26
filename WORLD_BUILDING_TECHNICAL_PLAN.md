# Plan Technique : Modélisation et Mise en Place du Monde

Ce document définit les standards techniques et le pipeline de création pour la modélisation des décors et l'intégration des scènes dans le moteur **Bevy (Rust)** pour un projet de MMORPG avec une direction artistique de type **PS2 / Metin2**.

---

## 1. Direction Artistique & Contraintes Techniques (Style PS2 / Metin2)

Pour respecter la volonté d'avoir un client "Terminal" ultra-léger et un rendu rétro, les contraintes suivantes doivent être appliquées à toutes les créations 3D :

### Modélisation (Low-Poly)
- **Topologie** : Triangulation manuelle encouragée pour un look "crunchy". Pas de subdivision (Sub-D).
- **Budget par modèle** :
  - **Bâtiments simples** : 500 - 2000 triangles.
  - **Grands bâtiments / Palais** : 2000 - 5000 triangles.
  - **Arbres / Flore** : 50 - 300 triangles (utilisation massive de plans/billboards avec canal alpha).
  - **Props (ruines, caisses, etc.)** : 10 - 200 triangles.
- **Détails** : Les détails (tuiles, fissures, briques) doivent être gérés par la texture, pas par la géométrie.

### Textures et Matériaux
- **Basse Résolution** : Textures de 64x64, 128x128 à 256x256 max. Rendu "Pixelated" (Filtrage de texture paramétré sur *Nearest/Point* et non *Bilinear/Trilinear* dans WGPU).
- **Matériaux** : Matériaux Unlit ou très basiques (Diffuse uniquement, avec éventuellement du Vertex Color pour simuler un éclairage ambiant "Bake" statique). Pas de PBR (Physically Based Rendering), pas de Normal Maps ni de Metallic/Roughness.
- **Atlas de Textures** : Regrouper au maximum les textures d'un même biome sur un seul Atlas (ex: 512x512) pour limiter les *draw calls*.

---

## 2. Pipeline Générique de Création

Ce pipeline s'applique à tous les types d'environnements (Forêts, Bâtiments, Donjons, Ruines).

### Étape A : Blockout (Maquette 3D)
- Création des volumes grossiers dans Blender.
- Export et test dans Bevy pour valider l'échelle (comparée au collider du joueur) et les lignes de vue.

### Étape B : Modélisation et UV Mapping
- Affinage des formes en respectant le budget "PS2".
- Dépliage UV optimisé pour l'utilisation d'Atlas de textures communs.

### Étape C : Texturing et Baking
- Peinture des textures (diffuse).
- *Baking* optionnel d'une Ambient Occlusion basique directement dans la texture diffuse ou via les *Vertex Colors* pour ajouter de la profondeur sans coût de rendu en temps réel.

### Étape D : Intégration et Export
- Configuration des origines (Pivot) au bas des objets (ex: au niveau des racines de l'arbre, fondation du bâtiment) pour un placement facile sur le terrain.
- Export au format **GLTF/GLB**.

---

## 3. Mise en place Technique des Scènes (Architecture Bevy ECS)

La mise en place du monde se fait en séparant strictement la logique client (Rendu WGPU) de la logique serveur (Simulation Headless).

### 3.1. Architecture des Scènes et Chargement (Client & Serveur)

- **Map Chunks** : Le monde ne charge pas en un seul bloc. Il est divisé en Chunks.
- Utilisation de `SceneBundle` de Bevy côté client pour spawner les GLTF.
- Côté serveur (Headless), les données de map sont chargées depuis des fichiers de configuration (JSON, RON, ou base de données) contenant les positions, rotations, et bounding boxes des entités.

### 3.2. Collisions et Physique (Serveur Autoritaire)

- **NavMesh (Navigation Mesh)** : Le serveur utilise un NavMesh statique par zone/chunk pour valider les déplacements des joueurs et l'IA des mobs.
- **Colliders Primitifs** : Pour l'environnement, ne jamais utiliser de mesh-colliders complexes. Remplacer les bâtiments et murs par des primitives simples (Cylindres, Boîtes) invisibles côté serveur.
- Composant typique : `Collider { shape: ColliderShape::Box(x, y, z) }` couplé à une entité statique.

### 3.3. Zones Spécifiques et Volumes Interactifs

**Zones de Spawn (Monstres, Ressources, Joueurs)**
- Implémentées comme des volumes invisibles (composant `SpawnZone`).
- **Composants ECS** :
  - `Position`
  - `Volume` (Rayon pour sphère ou Extents pour box)
  - `SpawnerConfig` (Type d'entité, Fréquence de respawn, Capacité max)
- Le serveur vérifie périodiquement avec un `System` quels Spawners ont besoin de régénérer des entités.

**Zones d'Événement (Triggers / Teleporters / Entrées de Donjon)**
- Reposent sur la détection d'intersection (AABB ou Radius).
- **Composants ECS** :
  - `TriggerArea`
  - `OnEnterEvent(Action)` / `OnLeaveEvent(Action)`
- Exemple : Un joueur entre dans l'AABB "Entrée Donjon" $\rightarrow$ Le système détecte la collision $\rightarrow$ Envoie un événement `PlayerChangeZoneEvent` $\rightarrow$ Le serveur déplace l'entité et notifie le client pour charger la nouvelle scène.

### 3.4. Gestion des Biomes (Forêts, Ruines, Donjons, Bâtiments)

- **Forêts** : Les arbres sont instanciés (Instanced Rendering) côté client pour minimiser les *draw calls*. Côté serveur, chaque arbre coupable possède un `Health` et un composant `ResourceNode`. Les arbres de décor sont ignorés par le serveur sauf pour le collider.
- **Bâtiments / Villes** : Entités regroupées. Les portes ont un composant `Interactable` géré par le serveur (Etat Ouvert/Fermé synchronisé).
- **Ruines et Décors Statiques** : Mappés uniquement comme obstacles dans le NavMesh serveur. Côté client, pure cosmétique.
- **Donjons** : Instances privées. Lorsqu'un groupe entre, le serveur clone l'architecture de base du donjon dans un "World" ou une isolation logique temporaire avec son propre gestionnaire d'événements.

### 3.5. Pipeline ECS de Chargement d'une Scène (Exemple de flux technique)

1. `Client` envoie `RequestZoneLoad(ZoneID)` au `Serveur`.
2. `Serveur` valide la position, renvoie `ZoneDataSync` (état des portes, mobs présents, joueurs dans la zone).
3. `Client` (Bevy) lance un System asynchrone qui charge le GLTF de la zone.
4. `Client` instancie les modèles (Arbres, Ruines, Terrain).
5. `Client` applique le shader "PS2 Point Filtering" aux textures.
6. `Serveur` maintient la simulation physique (NavMesh/Colliders) et notifie le client des `Transform` (positions) dynamiques via le flux réseau (Deltas).
