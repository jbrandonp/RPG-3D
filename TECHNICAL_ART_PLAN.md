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
