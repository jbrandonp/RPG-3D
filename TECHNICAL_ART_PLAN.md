# Technical Art Guidelines & Pipeline WGPU / Bevy

Ce document établit les standards, l'architecture technique et le pipeline de production artistique pour le projet de MMORPG. Son objectif est de garantir la cohérence visuelle, de respecter la direction artistique "Rétro" (ciblant une esthétique de type MMORPG des années 2000, e.g., Metin2, WoW Vanilla) tout en exploitant les performances et la portabilité offertes par **Bevy Engine** et **WGPU**.

---

## 1. Philosophie et Direction Artistique

La direction artistique repose sur l'esthétique des débuts de la 3D massivement multijoueur. Ce parti pris vise non seulement à créer une identité visuelle forte et lisible, mais également à délester drastiquement la charge GPU/CPU du client.
**Objectif technique :** Allouer le maximum de ressources matérielles à la logique réseau et au maintien de performances élevées dans les environnements surpeuplés (60 FPS+ constant sur les machines à faibles spécifications).

---

## 2. Architecture de Rendu & Shaders (WGSL)

Plutôt que d'utiliser le pipeline PBR (*Physically Based Rendering*) natif et lourd de Bevy, le rendu s'appuiera sur un pipeline personnalisé (Custom Materials) écrit en **WGSL** (*WebGPU Shading Language*).

### 2.1. Spécifications du Shader Principal (Retro Shader)
*   **Modèle d'Éclairage (Gouraud Shading / Vertex Lighting) :** L'éclairage directionnel et ambiant doit être calculé dans le *Vertex Shader* (par sommet) et interpolé sur les faces, plutôt que calculé par pixel (Phong/PBR).
*   **Texturing Non-PBR :** Les calculs de rugosité (roughness), de métallicité (metallic) ou de normales (normal maps) sont prohibés. L'ombrage et le relief (Ambient Occlusion, Cavity) doivent être peints (Baking/Hand-painted) directement dans la *Base Color Map* (Albedo).
*   **Filtrage des Textures :** Configuration stricte du *Sampler* WGPU en `FilterMode::Nearest` (Point Filtering) pour éviter l'effet de flou inhérent au filtrage bilinéaire et conserver le piqué (croustillant/pixelisé) des textures basse résolution.
*   **Fog (Brouillard) Exponentiel :** Implémentation d'un brouillard volumétrique ou de distance dans le *Fragment Shader* pour adoucir le clipping au fond de la frustum (la "draw distance" typique des anciens moteurs).
*   *Note sur le Vertex Snapping :* Contrairement au style PS1 (wobble), le style PS2/Metin2 bénéficie d'une virgule flottante stable. Le Vertex Snapping affine n'est donc **pas** requis, garantissant une meilleure lisibilité.

### 2.2. Gestion des Matériaux
*   **Matériau Unique (Unlit/Gouraud Custom) :** Un seul *Shader Def* doit gérer 95 % des assets statiques et dynamiques afin de minimiser le basculement d'état (State Changes) dans la file de rendu WGPU.

---

## 3. Création et Pipeline d'Assets

### 3.1. Outils Approuvés
*   **DCC (Digital Content Creation) 3D :** Blender (version LTS recommandée).
*   **Peinture Numérique & Textures :** Substance Painter (pour le baking vers Base Color uniquement), Krita, Photoshop ou Aseprite (pour les assets UI/Pixel Art).
*   **Intégration et Traitement WGPU :** Scripts d'automatisation via `gltf-transform` (Node.js) ou `bevy_gltf_components`.

### 3.2. Formats et Exportation
*   **Format Pivot :** Le format obligatoire est le **glTF 2.0 binaire (`.glb`)**.
*   **Compression :**
    *   Les géométries doivent être compressées via **Meshopt** ou **Draco** (si géré par le chargeur d'assets).
    *   Les textures doivent utiliser les formats supportés nativement par WGPU et compressés, préférentiellement **KTX2 / Basis Universal**, pour réduire l'empreinte en VRAM et accélérer les chargements.

### 3.3. Budgets et Polycount (Gabarits indicatifs)
*   **Personnages Joueurs :** 800 à 2 000 triangles.
*   **Monstres Communs :** 300 à 800 triangles.
*   **Boss :** 2 000 à 5 000 triangles maximum.
*   **Décor Statique (Props) :** 50 à 300 triangles.
*   **Textures :** Les personnages majeurs utilisent du 512x512. Les éléments de décor partagent des atlas de 1024x1024 ou 2048x2048.

---

## 4. Conventions de Nommage

L'organisation des assets doit permettre aux scripts d'automatisation et au `AssetServer` de Bevy de s'y retrouver sans heurts. Utilisation stricte du *snake_case*.

*   **Modèles :** `[categorie]_[nom]_[variante].glb` (ex: `npc_blacksmith_01.glb`, `wpn_sword_iron.glb`).
*   **Textures :** `[categorie]_[nom]_[type].ktx2` (ex: `env_forest_atlas_base.ktx2`).
*   **Animations :** Les animations font l'objet d'actions nommées explicitement dans Blender (ex: `Idle`, `Walk`, `Run`, `Attack_01`, `Death`) avant l'exportation unifiée dans le `.glb` du modèle.

---

## 5. Rigging et Outils d'Animation

La synchronisation avec le réseau impose une architecture d'animation déterministe. Le client gère l'interpolation visuelle, le serveur autoritaire ne calcule que les états.

### 5.1. Spécifications du Squelette (Rigging)
*   **Limite des Influences :** WGPU et glTF standard limitent à **4 os par sommet (Bone Influences)**. Le *Weight Painting* dans Blender doit être impérativement limité à ce chiffre avant l'export.
*   **Squelette Maître (Master Rig) :** Mutualisation des armatures. Toutes les entités humanoïdes (Joueurs, Gardes, Bandits) doivent partager un squelette standardisé, ce qui permet de réutiliser (Retargeting) le même fichier d'animation sur plusieurs modèles 3D différents.
*   **Hiérarchie :** Éviter les os inutiles (ex: os de doigts multiples, os faciaux) qui consomment des ressources de calcul matriciel. Préférer le rigging en "mitaine" (mitten hands) et des têtes rigides.

### 5.2. Intégration dans Bevy (Animation Graph)
*   **Graphe d'États (State Machine) :** Utilisation des capacités natives d'animation de Bevy pour transiter de manière fluide (Blending) entre les états (ex: transition de 0.2 seconde entre `Run` et `Attack`).
*   **Séparation Client/Serveur :**
    *   Le serveur valide le déclenchement d'une action à l'instant *T*.
    *   Le client interprète la prédiction locale, déclenche l'animation, et l'ajuste (ex: modification de la vitesse de lecture) en fonction des *deltas* reçus par le serveur.

---

## 6. Stratégie d'Optimisation du Rendu (Draw Calls & GPU)

L'architecture vise à maintenir le nombre de Draw Calls (appels de dessin) à un niveau extrêmement bas pour accommoder la présence simultanée de centaines de joueurs.

*   **Instancing (Rendu Instancié) :** Tous les objets répétitifs (arbres, rochers, herbe, PNJ d'une même race) doivent impérativement utiliser le pipeline de rendu par instanciation de Bevy. Des milliers d'arbres identiques ne coûteront qu'un seul Draw Call.
*   **Atlasing de Textures :** Le décor doit être regroupé sous un minimum de matériaux. Au lieu d'assigner une texture 256x256 par objet, créer des planches (Texture Atlases) de 2048x2048 regroupant toute la thématique d'une zone (ex: "Atlas_Foret", "Atlas_Donjon").
*   **Frustum Culling Dynamique :** Configuration rigoureuse des *AABB* (Axis-Aligned Bounding Boxes) pour s'assurer que le moteur d'élimination de Bevy rejette tout ce qui sort du champ de vision de la caméra.
*   **Level of Detail (LOD) & Distance Culling :** Bien que le jeu soit *Low-Poly*, implémenter un seuil de distance au-delà duquel les animations squelettiques ne sont plus mises à jour (Update Culling) et où les petits objets (herbe, débris) ne sont plus rendus.

## 7. Plan d'Action et Sprints (Horizon 6 Mois)

Ce plan d'action vise à déployer et valider l'ensemble du pipeline *Technical Art* détaillé ci-dessus sur une période de 6 mois. Il est découpé à raison d'un sprint par semaine (soit environ 24 sprints).

### Mois 1 : Fondations du Rendu et Shaders WGSL
*L'objectif est d'établir le look "Retro" via le shader WGSL personnalisé dans Bevy.*
*   **Sprint 1 :** Configuration de l'environnement WGPU/Bevy et implémentation du pipeline *Custom Material* de base (Unlit).
*   **Sprint 2 :** Écriture du *Gouraud Shading* (Vertex Lighting) dans le Vertex Shader WGSL.
*   **Sprint 3 :** Intégration du brouillard exponentiel (Distance/Volumétrique) et paramétrage du *Sampler* en `Nearest Neighbor` pour les textures.
*   **Sprint 4 :** Profiling initial et tests de validation du shader avec des primitives 3D (vérification du rendu sans PBR, ni specular).

### Mois 2 : Pipeline d'Exportation et Automatisation
*Sécuriser le chemin entre les outils de création (Blender) et l'intégration dans Bevy.*
*   **Sprint 5 :** Paramétrage standardisé dans Blender (orientations, unités, pas de Sub-D) et tests d'exportation glTF 2.0 binaire (`.glb`).
*   **Sprint 6 :** Mise en place et configuration des scripts d'automatisation (ex: `gltf-transform`) pour la compression des géométries (Meshopt/Draco) et textures (KTX2).
*   **Sprint 7 :** Déploiement et respect rigoureux des conventions de nommage (`snake_case`, catégories) via des scripts de validation pré-intégration.
*   **Sprint 8 :** Intégration de bout en bout des premiers *assets* de test statiques low-poly via le `AssetServer` de Bevy avec le pipeline automatisé.

### Mois 3 : Texturing, Atlasing et Gestion des Matériaux
*Optimiser les textures et limiter la charge VRAM.*
*   **Sprint 9 :** Définition et documentation du workflow de *Baking* (Ambient Occlusion, Cavity) fusionné dans l'Albedo.
*   **Sprint 10 :** Création du premier grand *Texture Atlas* thématique (ex: zone forêt) et ajustement des UVs d'un groupe de décors sur cet atlas.
*   **Sprint 11 :** Application à grande échelle du matériau unique (Retro Shader) sur l'ensemble de la scène de test via l'atlas.
*   **Sprint 12 :** Revue visuelle complète des environnements. Vérification de l'absence de flou bilinéaire et du maintien du polycount dans le budget défini.

### Mois 4 : Rigging et Animation Déterministe
*Gérer les entités animées avec des performances maximales et une synchronisation prévisible.*
*   **Sprint 13 :** Création et validation du Squelette Maître (Master Rig) en s'assurant de la limite stricte de 4 os par sommet.
*   **Sprint 14 :** Exportation et intégration des actions de base (Idle, Walk, Run, Attack_01) dans un fichier `.glb` unifié.
*   **Sprint 15 :** Implémentation du système natif *Animation Graph* dans Bevy pour gérer le *blending* et les transitions fluides entre états.
*   **Sprint 16 :** Interfaçage de l'animation avec la logique client : l'animation se déclenche en prédiction locale et sa vitesse de lecture s'ajuste selon les deltas du serveur.

### Mois 5 : Optimisation du Rendu (Draw Calls & GPU)
*Préparer le client à afficher des centaines d'acteurs simultanément.*
*   **Sprint 17 :** Implémentation du rendu par instanciation (*Instancing*) dans Bevy pour le dessin massif du décor (arbres, herbes, petits props).
*   **Sprint 18 :** Configuration des *AABB* et activation du *Frustum Culling Dynamique* pour rejeter les éléments hors champ.
*   **Sprint 19 :** Implémentation du *Level of Detail* (LOD) et du *Distance Culling* (arrêt des mises à jour d'animations des entités lointaines).
*   **Sprint 20 :** Analyse via GPU Profiler (ex: RenderDoc) pour confirmer la réduction drastique des Draw Calls. Ajustement du pipeline en conséquence.

### Mois 6 : Consolidation, Stress Tests et Finitions
*Valider la robustesse du pipeline sous des charges similaires à la production.*
*   **Sprint 21 :** Création d'une scène "Stress Test" simulant un rassemblement de joueurs (200+ modèles instanciés et animés) avec le Retro Shader.
*   **Sprint 22 :** Résolution des goulots d'étranglement (CPU/GPU) identifiés lors du test de charge. Ajustements de la gestion de mémoire de Bevy.
*   **Sprint 23 :** Polissage visuel final (réglages fins du brouillard, des teintes d'ombres dans le vertex shader, vérification du clipping).
*   **Sprint 24 :** Figeage de la documentation de production. Session de présentation et de validation finale avec l'équipe (ou revue solo des objectifs initiaux).
