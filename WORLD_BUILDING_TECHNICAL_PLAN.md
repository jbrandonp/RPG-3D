# Spécifications Techniques : Modélisation et Intégration du Monde (World Building)

## 1. Objectif et Portée du Document
Ce document de conception technique (TDD) définit les standards de modélisation, le pipeline de production des assets 3D (décors, bâtiments, forêts, donjons, ruines), et l'architecture d'intégration des scènes dans le moteur **Bevy (Rust)**. Il s'inscrit dans la vision d'un MMORPG à architecture « Client Terminal » avec une direction artistique rétro (génération PlayStation 2 / Metin2).

---

## 2. Contraintes Visuelles et Standards Techniques (Style "Retro PS2")

Afin de garantir l'homogénéité visuelle et le maintien de performances optimales sur des configurations matérielles anciennes ou modestes, les assets 3D doivent respecter les directives suivantes :

### 2.1. Topologie et Polygones (Low-Poly)
- **Topologie** : Triangulation délibérée. Les modeleurs doivent utiliser des maillages non lissés (Flat Shading prédominant, Smooth Shading réservé aux géométries organiques spécifiques). L'utilisation de modificateurs de subdivision (Subdivision Surface) est formellement proscrite.
- **Budgets Polycount (par instance)** :
  - **Bâtiments majeurs / Palais** : 2 000 à 5 000 triangles.
  - **Bâtiments standards (maisons, boutiques)** : 500 à 2 000 triangles.
  - **Végétation (Arbres, Buissons)** : 50 à 300 triangles (utilisation prédominante de *billboards* et de plans croisés avec masques alpha).
  - **Props (Caisses, Barils, Ruines mineures)** : 10 à 200 triangles.
- **Détails Structurels** : Les aspérités (fissures, briques, tuiles) ne doivent pas être modélisées géométriquement. Elles doivent être intégralement gérées via le texturing (Albedo/Diffuse).

### 2.2. Textures et Shading
- **Résolution** : Les textures individuelles doivent être limitées à des résolutions allant de `64x64` à `256x256` pixels.
- **Filtrage (Texture Filtering)** : Le moteur WGPU/Bevy doit être configuré pour utiliser un échantillonnage par point (`Nearest Neighbor` / `Point Filtering`) afin de désactiver l'interpolation bilinéaire ou trilinéaire, produisant ainsi un rendu net et "pixélisé".
- **Pipeline Matériau** :
  - Utilisation exclusive de matériaux *Unlit* (sans calcul d'éclairage dynamique complexe) ou de modèles de shading de Lambert basiques.
  - **Interdiction du PBR** (Physically Based Rendering). L'utilisation de *Normal Maps*, *Metallic Maps* ou *Roughness Maps* est interdite.
  - **Éclairage statique (Baking)** : L'occlusion ambiante (AO) et les ombres portées statiques doivent être "bakées" directement dans la texture diffuse (`Albedo`) ou gérées via les couleurs de sommets (`Vertex Colors`).
- **Optimisation (Draw Calls)** : Les textures d'un même biome (ex: Forêt Sombre) doivent être regroupées au sein de *Texture Atlases* (ex: atlas de `512x512` ou `1024x1024` pixels) pour réduire drastiquement les appels de rendu (*draw calls*).

---

## 3. Pipeline de Production des Assets 3D

Ce pipeline normalise la création de tous les éléments environnementaux avant leur intégration dans Bevy.

### 3.1. Phase 1 : Blockout (Gabarit 3D)
- Création de primitives géométriques (boîtes, cylindres) pour définir les volumes et les échelles.
- Importation immédiate dans le moteur Bevy pour validation des lignes de vue, de l'échelle par rapport à l'avatar du joueur, et des contraintes de navigation.

### 3.2. Phase 2 : Modélisation et Dépliage UV
- Remplacement des primitives par les modèles finaux respectant les budgets alloués.
- Dépliage UV (*UV Unwrapping*) optimisé. Les UVs doivent être disposés de manière à maximiser l'utilisation de l'espace dans les *Texture Atlases* partagés. Le chevauchement d'UVs (UV overlapping) est encouragé pour les éléments symétriques ou répétitifs.

### 3.3. Phase 3 : Texturing et Baking
- Peinture des textures (Hand-painted texturing) directement sur le modèle ou via des logiciels spécialisés.
- *Baking* de l'éclairage ambiant dans le canal des *Vertex Colors* ou directement fusionné avec la texture `Diffuse`.

### 3.4. Phase 4 : Exportation et Standardisation
- **Format cible** : L'intégralité des modèles doit être exportée au format `glTF 2.0` (fichiers `.glb` préférés pour l'encapsulation des textures).
- **Points de pivot (Origin)** : L'origine du mesh doit être placée à sa base logique (ex: au niveau du sol pour un bâtiment, à la racine pour un arbre) afin de faciliter le placement procédural ou manuel sur la carte.
- **Convention de nommage** : `[Biome]_[Type]_[Nom]_[Variante].glb` (ex: `Forest_Tree_Pine_A.glb`, `City_Building_Blacksmith_A.glb`).

---

## 4. Architecture et Intégration des Scènes dans Bevy ECS

L'architecture du monde repose sur une stricte séparation entre le **Serveur Autoritaire** (logique, physique, événements) et le **Client** (rendu visuel, inputs).

### 4.1. Chargement Spatial (Chunking)
- Le monde continu est divisé en sections (Chunks) gérées via un système de grille spatiale.
- **Client-side** : Chargement asynchrone des modèles `.glb` via le `AssetServer` et instanciation avec des composants `SceneBundle`.
- **Server-side** : Le serveur "Headless" ne charge aucun asset graphique. Il parse des fichiers de définition de scène structurés (JSON, RON) contenant uniquement les identifiants d'entités, leurs positions (Transform), rotations et échelles.

### 4.2. Physique et Navigation (Serveur Autoritaire)
- **NavMesh (Navigation Mesh)** : La topographie navigable (sol, escaliers) est compilée sous forme de NavMesh statique. Il est utilisé **uniquement** par le serveur pour le *Pathfinding* des PNJ/Monstres.
- **Colliders Primitifs (Validation Anti-Cheat)** : Aucun *Mesh Collider* complexe n'est utilisé. L'environnement physique (murs, obstacles) est représenté côté serveur par des géométries primitives strictes (Box, Sphere, Capsule, Cylinder) gérées par un moteur physique intégré (ex: Rapier3D). **C'est ce moteur physique qui sert à valider (Anti-Cheat) les déplacements soumis par les clients.**
  - *Exemple ECS* : Un bâtiment visuel côté client correspond côté serveur à une entité dotée d'un `Transform` et d'un `Collider::cuboid(hx, hy, hz)`.

### 4.3. Gestion des Entités par Biome

- **Forêts et Végétation Vaste** :
  - *Client* : Utilisation massive de l'*Instanced Rendering* pour dessiner des milliers d'arbres avec un seul appel de rendu.
  - *Serveur* : Les arbres purement décoratifs n'existent pas sur le serveur. Seuls les arbres récoltables (ex: Bûcheronnage) possèdent des entités serveur avec des composants `ResourceNode` et `Health`.
- **Bâtiments et Ruines** :
  - *Client* : Modèles statiques.
  - *Serveur* : Modélisés via leurs `Colliders` de fondation. Les portes interactives ou les mécanismes (leviers) disposent d'entités distinctes synchronisées sur le réseau (composant `Interactable { state: Open | Closed }`).
- **Donjons (Instances)** :
  - Contrairement au monde ouvert (géré en chunks contigus), les donjons sont isolés.
  - Le serveur instancie dynamiquement un nouvel environnement logique (ex: un nouveau `World` Bevy ou une arène encapsulée) lors de l'entrée d'un groupe, empêchant toute interaction avec l'extérieur.

### 4.4. Volumes et Événements Spatiaux (Triggers)

La logique de peuplement et d'interaction s'articule autour de volumes invisibles gérés par le serveur :

**A. Volumes d'Apparition (Spawn Zones)**
- Volumes (Cylindres ou AABB) dédiés à la génération d'entités.
- Composants ECS serveur :
  - `SpawnZone`: Identifie le volume.
  - `SpawnerConfig`: Définit le type d'entité (ex: "Rodeur_SousBois"), le délai de réapparition (Cooldown), et la limite de population locale (MaxCap).
- *Workflow* : Un `System` serveur vérifie la population de la zone à intervalles réguliers et génère de nouvelles entités si nécessaire, en calculant une position aléatoire valide sur le NavMesh local.

**B. Zones de Déclenchement (Triggers / Teleporters)**
- Utilisés pour les transitions de carte (entrée de donjon, changement de région) ou le déclenchement de scripts (quêtes, pièges).
- Composants ECS serveur :
  - `TriggerVolume`: Le volume physique de détection.
  - `OnEnterEvent` / `OnLeaveEvent`: Les actions à exécuter.
- *Workflow* : Lorsque le collider d'un joueur intersecte un `TriggerVolume` configuré comme "Entrée de Donjon", le serveur émet un `PlayerTransitionEvent`, désinscrit le joueur du Chunk actuel, l'inscrit dans l'Instance du donjon, et envoie un paquet RPC au client pour lancer le chargement des assets correspondants.

## 5. Plan d'Action Stratégique et Planification des Sprints

**Capacité de l'équipe :** 100 collaborateurs (Ingénieurs Backend Rust, Développeurs Moteur/Client WGPU, Architectes Réseau, Technical Artists).
**Durée d'un Sprint :** 6 mois.

L'objectif de cette planification est de déployer de manière optimale cette force de frappe conséquente, en respectant la stricte dépendance technique des fondations avant d'engager la production massive d'assets graphiques.

### 5.1. Structuration de l'équipe (100 personnes) pour le Sprint 1
Pour gérer efficacement une équipe de 100 personnes sur un socle technique pur, l'équipe est divisée en plusieurs pôles (Squads/Tribes) :
- **Pôle ECS & Simulation Serveur (25 personnes) :** Implémentation du Headless Server Bevy, gestion de l'état (CombatStats, PlayerId), implémentation de Rapier3D pour la validation côté serveur.
- **Pôle Réseau & Infrastructure (20 personnes) :** Implémentation de WebTransport/QUIC, gestion du chunking spatial asynchrone, delta state serialization, et orchestration Kubernetes/Agones.
- **Pôle Architecture Client (20 personnes) :** Intégration du rendu WGPU, AssetServer, Interpolation, prédiction locale, et interface UI Data-driven.
- **Pôle Level Design Technique & Outils (20 personnes) :** Création du système de chargement des fichiers de scènes JSON/RON, génération statique du NavMesh, pipeline de hot-reloading.
- **Pôle Assurance Qualité (QA) & DevOps (15 personnes) :** Tests d'intégration, CI/CD, métriques Prometheus/Grafana, automatisation de la validation anti-cheat.

### 5.2. Découpage en Sprints

#### Sprint 1 (Mois 1 à 6) : Fondations Techniques et Architecture "Headless"
*Focus exclusif sur la technique : Aucune production d'assets graphiques finaux. L'objectif est d'obtenir un monde navigable en primitives 3D (Cubes, Sphères) synchronisé massivement en réseau.*

**Livrables du Sprint 1 :**
- **Architecture Serveur :** Serveur autoritaire fonctionnel tournant sous Bevy Headless. Moteur de collision primitif (Rapier3D) validant le déplacement de centaines d'entités simultanément.
- **Streaming & Chunking :** Le système de grille spatiale charge et décharge correctement les zones d'intérêt (AOI - Area of Interest) des joueurs.
- **Parsing d'Environnement :** Le serveur charge un "monde" via un fichier JSON/RON définissant les `SpawnZone`, `TriggerVolume`, et l'emplacement des obstacles.
- **Client Terminal :** Le client se connecte au serveur et instancie des `SceneBundle` de primitives (blockout) basés sur les paquets reçus. Mouvement fluide grâce à la prédiction locale.
- **Système de Navigation :** Pathfinding PNJ fonctionnel côté serveur utilisant le NavMesh pré-compilé.

#### Sprint 2 (Mois 7 à 12) : Pipeline WGPU, Outils d'Édition et Pré-Production Visuelle
*Transition vers le rendu visuel et déploiement des outils de création d'environnement.*

**Livrables du Sprint 2 :**
- **Pipeline Rendu "Rétro" :** Implémentation des shaders WGSL custom (Nearest Neighbor, Vertex Lighting, Fog).
- **Outils World Building :** Éditeur interne ou pipeline d'export Blender vers JSON/RON parfaitement fonctionnel, permettant le placement d'instances 3D par les level designers.
- **Instances de Donjon :** Isolement réseau et logique permettant la création de "Worlds" Bevy temporaires pour les instances fermées.
- **Système d'Événements Spatiaux :** Fonctionnement complet des Trigger Volumes (téléportation, activation de scripts/spawns).
- **Intégration Assets Test :** Intégration d'un biome complet (arbres instanciés, architecture blockout avancée) respectant les limites de Polycount (max 5k polys par bâtiment majeur).

#### Sprint 3 (Mois 13 à 18) : Production de Masse et Intégration IA
*Avec un socle technique et des outils robustes, l'équipe intègre la direction artistique finale et les agents IA.*

**Livrables du Sprint 3 :**
- Remplacement global des blockouts par des assets 3D texturés (glTF 2.0).
- Finalisation des Atlas de textures et optimisation massive des Draw Calls.
- Intégration des endpoints MCP (Model Context Protocol) permettant à l'IA de modifier l'état des Spawners ou de lire les Triggers.
