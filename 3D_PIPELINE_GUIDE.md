# Pipeline de Modélisation 3D et Animation : Personnages, PNJ et Créatures

## 1. Introduction et Périmètre
Ce document définit les spécifications techniques et méthodologiques relatives à la production d'assets 3D animés pour l'intégration au sein du moteur **Bevy (Rust)**.
Le flux de travail adopté combine des techniques modernes de modélisation (workflow High-to-Low Poly) tout en respectant un cahier des charges strict visant une direction artistique rétro (génération PlayStation 2 / milieu des années 2000).

## 2. Spécifications Techniques Cibles
Afin de garantir les performances et la cohérence visuelle, tous les modèles doivent respecter les contraintes suivantes :
*   **Budget Polygonal (Cibles Indicatives) :**
    *   Personnages Joueurs (PC) : 1 500 – 4 000 triangles.
    *   PNJ et Monstres Standards : 500 – 2 000 triangles.
    *   Boss ou Entités Majeures : 4 000 – 8 000 triangles.
*   **Rigging et Skinning :** Limite stricte de **4 os (bones) maximum par sommet (vertex)**.
*   **Format d'Exportation :** glTF 2.0 binaire (`.glb`).
*   **Textures et Filtrage :** Résolutions cibles basses (256x256, 512x512). Le filtrage dans le moteur sera réglé sur *Nearest Neighbor* (Point) pour conserver un rendu *pixel perfect*.

---

## 3. Méthodologie Étape par Étape

### Étape 1 : Sculpture et Modélisation Haute Résolution (High-Poly)
**Objectif :** Établir la silhouette, la volumétrie et les détails de surface (musculature, écailles, plis) qui serviront de base à la projection (Baking).
*   **Pratiques recommandées :**
    *   Initier le processus par un *Blocking* grossier des formes primaires pour valider les proportions générales avant de subdiviser.
    *   L'utilisation d'outils de sculpture numérique (ZBrush, Blender Sculpt) est préconisée.
    *   La topologie importe peu à ce stade, seule l'information visuelle et la silhouette comptent.

### Étape 2 : Retopologie et Tessellation (Low-Poly)
**Objectif :** Produire un maillage de rendu final optimisé, doté d'une topologie structurée pour garantir des déformations articulaires correctes.
*   **Pratiques recommandées :**
    *   **Géométrie :** Privilégier un maillage constitué de quadrilatères (Quads). Les triangles purs sont acceptables s'ils ne compromettent pas la déformation. Les N-gons (polygones à plus de 4 côtés) sont **strictement interdits**.
    *   **Edge Flow (Flux d'arêtes) :** Disposer des boucles d'arêtes (Edge Loops) stratégiques autour des articulations (épaules, coudes, genoux, phalanges) : prévoir au minimum 3 boucles (loops) par articulation majeure pour éviter l'écrasement des volumes lors de la flexion.
    *   **Silhouette :** Placer la géométrie là où elle impacte la silhouette ; les détails de surface internes seront gérés par les textures.

### Étape 3 : Dépliage UV (UV Unwrapping)
**Objectif :** Projeter le maillage 3D en 2D pour y appliquer les cartes de textures avec un minimum de distorsion.
*   **Pratiques recommandées :**
    *   **Placement des coutures (Seams) :** Dissimuler les coupes UV dans les zones hors du champ de vision naturel (intérieur des cuisses, aisselles, intérieur des vêtements, sous les cheveux).
    *   **Densité de Texels (Texel Density) :** Conserver une densité de pixels homogène sur l'ensemble du modèle, à l'exception du visage ou d'éléments narratifs clés qui peuvent bénéficier d'un ratio de texture supérieur.
    *   **Marge (Padding / Bleed) :** Laisser systématiquement une marge de pixels suffisante (Padding) entre les îlots UV (UV Islands) afin d'éviter le *texture bleeding* lors des mipmaps ou des compressions.

### Étape 4 : Cuisson (Baking) et Texturisation
**Objectif :** Transférer l'information géométrique du modèle High-Poly vers le modèle Low-Poly et appliquer le traitement colorimétrique final.
*   **Pratiques recommandées :**
    *   **Baking :** Cuire la Normal Map (Espace Tangent), ainsi que les cartes d'Ambient Occlusion et de Curvature depuis le modèle haute résolution.
    *   **Texturing (Approche Rétro) :** La direction artistique type PS2 se prête bien à un *baking* de l'illumination globale (AO/Cavité) directement fusionnée dans la carte de couleur (Base Color / Albedo) pour simuler l'ombrage (Hand-Painted style).
    *   **Matériaux Bevy :** S'assurer que les matériaux respectent le standard *PBR* (Physically Based Rendering) du format glTF, même si la rugosité (Roughness) est définie de manière uniforme (ex: 1.0) pour désactiver les reflets réalistes si un rendu purement *Unlit* (non-éclairé) est visé par la direction artistique.

### Étape 5 : Squelette (Rigging) et Pondération (Skinning)
**Objectif :** Construire l'armature de contrôle et la lier au maillage pour générer les mouvements.
*   **Pratiques recommandées :**
    *   **Hiérarchie et Os Racine (Root Bone) :** L'armature doit obligatoirement posséder un os maître parent unique (généralement nommé `Root`). Cet os est crucial pour l'intégration des déplacements (*Root Motion*) ou le positionnement global dans le moteur.
    *   **Limitation des Influences :** Comme mentionné, plafonner l'influence du Skinning à **4 os par vertex**. Nettoyer les poids (Normalize All Weights) pour éviter les déformations erratiques.
    *   **Conventions de Nommage :** Adopter une nomenclature standardisée (ex: `Arm_L`, `Leg_R`) pour faciliter le partage d'animations (Retargeting) entre différents modèles humanoïdes de corpulence similaire.

### Étape 6 : Animation
**Objectif :** Générer les cycles d'action et les transitions dynamiques pour les comportements *in-game*.
*   **Pratiques recommandées :**
    *   **Cycles Fermés :** Les animations cycliques (Marche, Course, Attente/Idle) doivent posséder un maillage parfait entre la première et la dernière *frame* (images de début et de fin identiques).
    *   **Fréquence d'Images :** Standardiser les animations à 30 ou 60 FPS (Frames Per Second) selon la cible.
    *   **In-Place vs Root Motion :** Livrer les animations de déplacement de type *In-Place* (le personnage mime le déplacement mais le `Root` reste fixe), sauf indication contraire des développeurs pour l'utilisation de *Root Motion*.

### Étape 7 : Standardisation et Exportation (Moteur Bevy)
**Objectif :** Compiler l'asset dans un format exploitable par le client du jeu sans erreurs de compilation ou d'affichage.
*   **Pratiques recommandées :**
    *   **Nettoyage Pré-Export :**
        *   Appliquer toutes les transformations de l'objet (Scale = 1.0, 1.0, 1.0 ; Rotation = 0.0, 0.0, 0.0). L'origine du maillage (Pivot) et de l'armature doivent se trouver en (0, 0, 0) dans l'espace Monde.
        *   Supprimer l'historique de modélisation, geler les modificateurs (sauf l'Armature) et purger les données non utilisées (Orphan Data).
    *   **Orientation :** Le système de coordonnées standard glTF est *Right-Handed, Y-Up*. S'assurer que le personnage regarde vers l'avant (généralement l'axe -Z localement, converti correctement à l'export).
    *   **Paramétrage de l'Exporteur (Ex: Blender) :**
        *   Format : `glTF 2.0 Binary (.glb)`.
        *   Inclure : *Selected Objects* (Maillage et Armature uniquement). Exclure les caméras, lampes et environnements.
        *   Animation : Cocher *Bake Animation*, *NLA Strips*, *Skinning*. Assurez-vous que l'exporteur applique automatiquement le filtrage des influences (Max Bones = 4) si l'outil le permet.
