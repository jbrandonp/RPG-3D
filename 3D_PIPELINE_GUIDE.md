# Pipeline de Création 3D : Personnages, PNJ et Créatures (Style Rétro / Moteur Bevy)

Ce guide décrit de manière générique les étapes de création d'assets 3D animés pour le projet de jeu, en combinant un flux de travail moderne (High-to-Low) tout en ciblant une esthétique rétro (PlayStation 2) et en respectant les contraintes du moteur Bevy (Rust).

## Étape 1 : Sculpture (Modélisation High-Poly)
**Objectif :** Créer les détails primaires et secondaires, la silhouette et les volumes globaux.
*   **Processus :**
    *   Commencer par une forme de base (Base Mesh).
    *   Utiliser des outils de sculpture numérique (ex: ZBrush, mode Sculpt de Blender) pour définir la musculature, les plis des vêtements, les écailles, la fourrure, etc.
    *   Ne pas se soucier du nombre de polygones lors de cette étape. L'objectif est uniquement la qualité visuelle.

## Étape 2 : Retopologie et Tessellation (Modélisation Low-Poly)
**Objectif :** Créer un maillage propre et optimisé (Low-Poly), adapté au moteur de jeu et à l'animation, tout en visant l'esthétique "rétro".
*   **Processus :**
    *   Dessiner manuellement une nouvelle topologie (maillage) par-dessus le modèle sculpté.
    *   Assurer un flux d'arêtes (Edge Flow) correct autour des zones de déformation (épaules, coudes, genoux, mâchoire) pour que le modèle se plie correctement lors de l'animation.
*   **Cibles "Style PS2" (à titre indicatif) :**
    *   Personnages Joueurs : ~1 500 à 4 000 Triangles.
    *   PNJ et Créatures moyennes : ~500 à 2 000 Triangles.

## Étape 3 : Dépliage UV (UV Unwrapping)
**Objectif :** Mettre le modèle 3D à plat pour y peindre et projeter des textures 2D.
*   **Processus :**
    *   Définir des "Coutures" (Seams) dans les zones les moins visibles du modèle (intérieur des cuisses, sous les bras, derrière la tête ou cachées par des vêtements).
    *   Déplier et organiser les "îlots" d'UV (UV Islands) dans un carré (espace UV).
    *   Optimiser l'espace : allouer plus de place (densité de pixels) aux zones importantes (comme le visage) et moins de place aux zones peu visibles.
    *   Laisser une marge de sécurité (Padding) entre les îles pour éviter les artefacts de texture.

## Étape 4 : Cuisson (Baking) et Texturing
**Objectif :** Transférer les détails haute résolution sur le modèle basse résolution et le peindre.
*   **Processus :**
    *   **Baking :** Calculer la "Normal Map" (et éventuellement l'Ambient Occlusion / Cavity / Thickness) depuis le modèle High-Poly vers le modèle Low-Poly. Les détails sculptés apparaîtront comme un effet d'optique sur le modèle allégé.
    *   **Texturing :** Peindre les couleurs (Albedo/Base Color) et configurer la rugosité (Roughness) ou la brillance.
*   **Approche Rétro (PS2) :** Pour un rendu fidèle à l'époque, privilégier des textures de basse résolution (ex: 256x256 ou 512x512) et utiliser du filtrage "Nearest Neighbor" ou "Point" dans le moteur pour garder un côté pixelisé net.

## Étape 5 : Squelette (Rigging) et Skinning
**Objectif :** Construire l'armature articulaire du modèle pour permettre ses mouvements.
*   **Processus :**
    *   **Rigging :** Placer la hiérarchie des os (Bones) à l'intérieur du modèle (colonne, bras, jambes, mâchoire, queue). Créer des contrôleurs d'animation (IK/FK) pour faciliter le travail de l'animateur.
    *   **Skinning (Pondération) :** Associer les sommets du maillage aux os correspondants. Peindre les poids (Weight Painting) pour définir l'influence exacte de chaque os sur la géométrie.
*   **Contraintes Moteur Temps Réel :** Limiter rigoureusement l'influence à **4 os maximum par sommet (Vertex)**, ce qui est le standard technique optimal pris en charge par les moteurs comme Bevy.

## Étape 6 : Préparation à l'Animation
**Objectif :** Créer et organiser les mouvements pour qu'ils soient exploitables par les programmeurs.
*   **Processus :**
    *   Animer les boucles et actions clés (Idle, Marche, Course, Attaque 1, Dégâts reçus, Mort).
    *   Créer une animation (Action/Clip) distincte pour chaque mouvement.
    *   S'assurer que les animations cycliques (comme la marche) bouclent parfaitement sans saccades.
    *   Fixer le personnage sur place (In-place animation) ou utiliser un os "Root" dynamique selon la méthode de déplacement codée dans le jeu.

## Étape 7 : Exportation pour Bevy
**Objectif :** Générer le fichier final qui sera lu par le moteur Rust.
*   **Prérequis techniques avant l'export :**
    *   Appliquer toutes les transformations (Scale à 1.0, Rotation à 0.0) sur le Mesh et l'Armature.
    *   Orientation : S'assurer que le personnage fait face à l'axe de profondeur conventionnel (-Z en général).
    *   Nettoyage : Supprimer l'historique de construction et nettoyer les sommets orphelins.
*   **Format cible :**
    *   Utiliser exclusivement le format **glTF 2.0**.
    *   Préférer le format **`.glb`** (binaire) qui empaquette la géométrie, l'armature, les animations et les textures dans un seul fichier facile à charger.
    *   Dans les options d'exportation de votre logiciel 3D (ex: Blender) :
        *   Exporter uniquement les objets sélectionnés (Mesh + Armature). Exclure les lumières et caméras.
        *   Cocher l'exportation du Skinning, des Morph Targets (si utilisés pour les expressions faciales) et de l'Animation (Bake Animations).
