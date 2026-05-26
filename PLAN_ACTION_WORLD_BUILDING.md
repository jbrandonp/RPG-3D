# Plan d'Action : World Building

## 1. Introduction et Périmètre
Ce document définit la stratégie de production et l'architecture technique du monde du jeu. Il repose sur l'approche de validation technique avant production artistique, spécifiquement adaptée pour un développeur solo.

## 2. Contraintes Techniques Majeures (Rétro PS2)
La production d'assets environnementaux doit respecter rigoureusement le cahier des charges suivant :
*   **Format d'export** : glTF 2.0 binaire (`.glb`).
*   **Limites Polygonales** : ~5 000 triangles max par objet complexe (ex: bâtiments).
*   **Topologie** : Triangulation manuelle obligatoire (aucun modificateur de subdivision de surface `Sub-D`).
*   **Shading** : Matériaux *Unlit* obligatoires (via l'extension `KHR_materials_unlit` de glTF), aucune map PBR (ni Roughness, ni Normal).
*   **Système de Coordonnées** : `+Y` up, `-Z` forward (conversion cruciale depuis Blender où `+Z` est up).
*   **Optimisation Rendu** : Filtrage de texture *Nearest-Neighbor* (Pixelisé) et utilisation obligatoire d'**Atlas de textures par biome** pour limiter les draw calls.
*   **Armatures (Skinning)** : Limite stricte à 4 os par sommet.

## 3. Architecture ECS et Séparation Client/Serveur
Le jeu suit l'architecture « Client Terminal ». Chaque élément du monde possède deux représentations :
1.  **Côté Client (Visuel)** : Chargement dynamique (`Streaming Chunks`) de modèles `.glb` visuels de haute qualité (hand-painted), instanciés via `SceneBundle` dans Bevy avec rendu WGPU.
2.  **Côté Serveur Headless (Autoritaire)** : Représentation abstraite pour validation physique (Anti-Cheat) et pathfinding (NavMesh). Les colliders doivent utiliser des formes géométriques basiques (Box, Sphere, Capsule, Cylinder) configurées via des composants ECS (ex: `StaticCollider`).

## 4. Gestion des Ressources Solo (Séquencement)
Le projet étant développé en solo, le changement de contexte (Context Switching) est le principal risque de productivité. Le workflow doit séparer strictement les phases de travail :
*   Phase **Artiste 3D** (Blender / Krita).
*   Phase **Développeur Rust Client** (Import et Rendu WGPU).
*   Phase **Développeur Rust Serveur** (Logique ECS, Physiques, Triggers).
*   Phase **Level Designer** (Assemblage des scènes).

## 5. Roadmap des Sprints

*   **Sprint 0** : *PoC Pipeline Technique (Bout en bout).* Focus absolu sur la chaîne d'outils (Cube texturé -> Client Bevy -> Collider Serveur). **Priorité maximale**.
*   **Sprint 1** : *Zone de test flat.* Sol plat + 3 décors, validation du pipeline artistique PS2 et de l'Atlas de biome.
*   **Sprint 2** : *Velnor (Bidonvilles).* Production des premiers assets urbains (Zone 1 - Niveau 1-10).
*   **Sprint 3** : *Velnor (Ville et Intérieurs).* Finalisation de la zone de départ et gestion de la transition intérieur/extérieur.
*   **Sprint 4** : *Plaines et Marais.* Introduction de l'instanciation de végétation (Zone 2 - Niveau 8-18).
*   **Sprint 5** : *Forêt des Murmures.* Mise en place des mécaniques spécifiques (Nids) (Zone 3 - Niveau 15-30).
*   **Post-Alpha** : Implémentation de la corruption dynamique par le Brouillard Noir (Shader Variant / Particules), et développement des biomes avancés (Montagnes Brisées, Falaises d'Argent, Ruines, Sanctuaire).
