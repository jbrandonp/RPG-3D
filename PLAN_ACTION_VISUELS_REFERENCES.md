# Plan d'Action & Références Visuelles : Direction Artistique "PS2 / Metin2"

Ce document synthétise la roadmap stratégique et l'analyse de la production visuelle pour le projet de MMORPG indépendant, aligné avec l'architecture backend ultra-moderne et le client "Terminal".

## 1. Analyse de la Vision Visuelle

L'objectif est d'atteindre un paradoxe visuel fort : des graphismes volontairement limités (style PlayStation 2 / début des années 2000) pour garantir des performances extrêmes sur des machines âgées (jusqu'à 15 ans), permettant ainsi au serveur de gérer massivement l'IA et l'économie.

### Piliers de la Direction Artistique
- **Low-Poly Strict :** Tous les modèles sont sous la barre des 5000 triangles.
- **Hand-Painted & Diffuse Only :** Aucun calcul PBR (pas de normal, specular, ou roughness maps). La lumière, les ombres et les reflets sont "fake" et peints directement dans la texture diffuse de base.
- **Matériaux Unlit :** L'export glTF utilise l'extension `KHR_materials_unlit` pour annuler la lumière dynamique du moteur.
- **Rendu Pixelisé :** Filtrage "Nearest-Neighbor" appliqué systématiquement dans le moteur WGPU (Bevy) pour annuler l'anti-aliasing sur les textures.

### Pourquoi ce choix technique ?
1. **Performance Client :** Le client est un afficheur passif, les calculs de rendu doivent être proches de zéro.
2. **Identification visuelle (Silhouettes) :** Des contrastes forts et des proportions "Heroic" (gros épaulements, armes massives) facilitent la lecture de l'action, un point clé pour un jeu axé sur le combat multi-cibles.
3. **Workflow Solo Réaliste :** Un seul développeur (Brandon) peut produire ces assets sans passer des semaines sur la topologie Sub-D complexe ou la configuration PBR.

---

## 2. Roadmap Stratégique : 6 Sprints jusqu'à la Pré-Alpha

La production visuelle s'étale sur **12 semaines** (6 sprints de 2 semaines), menant à une version Pré-Alpha où la base visuelle et le workflow seront totalement verrouillés.

### Sprint 0 : Validation du Pipeline (Pipeline Visuel)
- **Objectif :** S'assurer que le chemin `Blender -> glTF 2.0 -> Bevy` fonctionne sans accroc technique (Unlit, Nearest-Neighbor, hiérarchie).
- **Livrables :**
  - Un cube texturé simple exporté de Blender et affiché dans Bevy.
  - Configuration du système de matériaux Bevy pour annuler les filtres de texture.

### Sprint 1 : The Vertical Slice (La Tranche Verticale)
- **Objectif :** Produire le minimum viable pour prouver la direction artistique in-game.
- **Focus Principal :** Le workflow hand-painted sur les personnages.
- **Livrables :**
  - 1 Tuile de sol extérieur (plaines).
  - 1 Personnage "Dummy" (Elara Voss - 1500 à 4000 polys) avec une boucle d'animation Idle de 2s.
  - 1 Épée basique (< 500 polys).
  - 1 Arbre/Décor.

### Sprint 2 : Les Environnements (Fondations)
- **Objectif :** Créer la base modulaire pour habiller le monde.
- **Livrables :**
  - Textures en Atlas par biome pour optimiser les "draw calls" (Plaines, Marais, Forêt, Ville).
  - 4 tuiles de sol, 8 arbres, 10 rochers, 2 bâtiments, 1 entrée de donjon.

### Sprint 3 : Personnages et PNJ
- **Objectif :** Peupler le monde et valider le squelette de rigging sur différentes morphologies.
- **Livrables :**
  - 3 gobelins (Low, Mid, High tier).
  - 1 Orc.
  - 1 PNJ Marchand et 1 PNJ Guerrier.

### Sprint 4 : UI Arcade et Effets Visuels (VFX)
- **Objectif :** Habiller le combat et l'interface sans surcharger le moteur.
- **Focus :** L'UI rétro (pixel font, contraintes de caractères) et les billboards 2D.
- **Livrables :**
  - Interface : Fenêtres de chat (3 lignes max, 60 char/ligne), barres de vie, polices pixelisées.
  - VFX : Éclaboussures de sang, sort Boule de Feu, sort de Soin, marques d'impact (hitmarks). Modèles 2D additifs.

### Sprint 5 : Polissage (Polish) et Optimisation
- **Objectif :** Consolider les assets avant le build Pré-Alpha.
- **Livrables :**
  - Fusion finale des atlas de textures.
  - Ajustement des UV maps.
  - Nettoyage des fichiers `.blend` et validation des contraintes d'os par vertex.

---

## 3. Le Pipeline High-to-Low et Contraintes

### Étapes du workflow 3D :
1. **High-Poly Sculpt (Blender / ZBrush) :** Pour dégager les formes principales.
2. **Retopology Manuelle :** Viser 5000 triangles grand maximum. Aucune surface de subdivision (Sub-D) permise lors de l'export. Triangulation manuelle.
3. **UV Mapping :** Dépliage manuel.
4. **Texturing Hand-Painted (Krita / GIMP) :** Dessiner la lumière, les ombres de contact et l'Ambient Occlusion (AO). Texture Diffuse (Albedo) uniquement.
5. **Rigging :** MAX 4 os par vertex (Contrainte PS2 absolue pour compatibilité WGPU). Os racine ("Root bone") positionné en `(0,0,0)`.
6. **Export :** Format `glTF 2.0` (`.glb`), repère `+Y up, -Z forward`.
7. **Import Bevy :** Utilisation de `bevy_gltf`, rendu WGPU.
