# Plan Artistique et Technique : Pipeline d'Assets et Rendu (Bevy / WGPU)

Ce document définit la stratégie technique et artistique pour le développement du MMORPG 3D, en s'alignant sur le style visuel rétro (PlayStation 2 / Metin2 / WoW Vanilla) et en exploitant la puissance du moteur Bevy (Rust / WGPU).

---

## 1. Shaders et Rendu (Style Rétro PS2 / Metin2)

L'objectif est d'émuler les limitations et le charme des moteurs de rendu du début des années 2000, tout en garantissant des performances exceptionnelles sur des machines anciennes comme modernes.

*   **Vertex Snapping (Jittering) :** Implémentation d'un shader personnalisé pour arrondir (snap) les positions des sommets à une grille virtuelle dans l'espace écran. Cela simule la faible précision en virgule flottante des consoles de l'époque (typiquement la PS1 et les premiers jeux PS2).
*   **Affine Texture Mapping :** Désactivation partielle ou totale de la correction de perspective pour l'échantillonnage des textures. Cela provoque cette déformation caractéristique ("warping") des textures sur les grands polygones lors des mouvements de caméra.
*   **Éclairage par Sommet (Vertex Lighting) / Gouraud Shading :** Calculer l'éclairage dans le *vertex shader* plutôt que dans le *fragment shader*. Cela donne un rendu "low-poly" authentique, légèrement imparfait, et extrêmement peu coûteux en ressources GPU.
*   **Filtrage de Texture Rétro :** Utilisation du filtrage *Nearest Neighbor* (Point) plutôt que bilinéaire/trilinéaire. Les textures basse résolution garderont un aspect "pixelisé" net et croustillant (crunchy).
*   **Brouillard (Fog) Exponentiel :** Un brouillard coloré massif basé sur la distance pour masquer le *clipping* (la distance d'affichage courte imposée jadis par les limitations matérielles).

---

## 2. Outils de Création

La suite logicielle doit être open-source, robuste, et parfaitement interfaçable avec Bevy.

*   **Modélisation et Animation 3D :** **Blender**. Le standard incontournable pour modéliser en low-poly, rigger et animer.
*   **Création de Textures :**
    *   **Krita / GIMP :** Pour peindre les textures (style "hand-painted"), appliquer les ombres directement dans la texture de base (Baking/Peinture d'ombres) afin d'éviter les calculs d'ombres dynamiques complexes.
    *   **Aseprite / LibreSprite :** Pour le pur pixel art (icônes d'inventaire, éléments d'UI, textures très basse résolution).
*   **Conception de Niveaux (Level Design) :**
    *   Blender pour la création de "tuiles" (tiles) ou de décors exportés en blocs.
    *   Éditeur de scène/terrain Bevy (via des plugins communautaires ou un outil interne minimaliste) utilisant des *heightmaps* (cartes de hauteur) pour les vastes zones extérieures.
*   **Interface Utilisateur (UI) :** Figma pour le maquettage wireframe, puis intégration avec le système d'UI natif (ou `bevy_egui` pour les outils de dev).

---

## 3. Pipeline d'Assets

Un pipeline d'importation strict est essentiel pour garder des temps de chargement rapides et un jeu léger.

*   **Format Pivot :** **glTF 2.0 (`.glb`)**. C'est le format recommandé et le mieux supporté par Bevy. Il encapsule maillages, textures, matériaux, squelettes et animations dans un seul fichier.
*   **Flux de travail (Workflow) :**
    1.  Modélisation, dépliage UV et texturage dans Blender.
    2.  Regroupement des matériaux.
    3.  Export via l'exportateur glTF de Blender.
    4.  Chargement dans le jeu via le `AssetServer` de Bevy, de manière asynchrone pour éviter les blocages.
*   **Automatisation :** Mise en place potentielle de scripts (`gltf-transform` ou scripts Python pour Blender) pour compresser les textures, purger les données orphelines et limiter le nombre d'os par sommet avant intégration dans le dossier `assets/` du jeu.

---

## 4. Rigging et Outils d'Animation

La fluidité et la simplicité sont les mots d'ordre pour l'animation.

*   **Rigging Squelettique (Skeletal Rigging) :**
    *   Armatures ultra-simples (ex: 20 à 30 os pour un humanoïde).
    *   Limitation stricte à **4 os maximum par sommet** (standard glTF) pour optimiser le calcul matriciel sur le GPU.
    *   **Partage de Squelettes :** Un modèle d'armature universel pour tous les joueurs/PNJ humanoïdes. Les différentes armures/races sont juste des maillages différents attachés au même squelette.
*   **Création d'Animations :**
    *   Animation par images clés (*Keyframe Animation*) depuis le *Action Editor* de Blender (Idle, Marche, Course, Attaque, Dégâts, Mort).
    *   Exportation de multiples animations dans un seul fichier `.glb`.
*   **Intégration Bevy :**
    *   Utilisation du graphe d'animation de Bevy pour jouer les actions.
    *   Mise en place d'un système de **blending** (transition douce entre l'animation "Marche" et "Course").
    *   *Le Serveur :* Ne calcule aucune animation. Il est "headless". Il gère uniquement la logique d'état (Joueur A attaque Joueur B).
    *   *Le Client :* Lit l'état réseau et déclenche visuellement les animations correspondantes (prédiction locale).

---

## 5. Optimisation Technique

Le choix du rendu rétro offre d'immenses opportunités d'optimisation pour soutenir un MMORPG très peuplé.

*   **Low-Poly Évident :** Personnages de 500 à 1500 triangles maximum. Monstres communs de moins de 500 triangles.
*   **Réduction des Draw Calls (Texture Atlasing) :**
    *   Pour limiter les appels au GPU, les environnements et PNJ doivent partager des matériaux.
    *   Utilisation d'Atlas de Textures (regrouper plusieurs petites textures en une seule grande image 1024x1024 ou 2048x2048) pour dessiner plusieurs objets différents en une seule passe.
*   **Culling (Élimination visuelle) :**
    *   **Frustum Culling :** (Inclus dans Bevy) Ne pas rendre ce qui est derrière la caméra.
    *   **Distance Culling :** Ne plus rendre les petits objets, particules, et arrêter l'animation des personnages très lointains pour économiser des cycles CPU/GPU.
*   **Baking des Ombres (Pas d'Ombres Dynamiques) :**
    *   Les ombres portées douces sont chères en performances.
    *   Préférer les "blob shadows" (une simple texture de cercle noir translucide sous les personnages) et des ombres peintes à la main sur les décors statiques (lightmaps bakes depuis Blender).
