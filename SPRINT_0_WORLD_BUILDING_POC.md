# Sprint 0 : World Building - Proof of Concept (PoC)

## 1. Objectif du Sprint
L'objectif unique et prioritaire de ce sprint est de **valider le pipeline technique de bout en bout** pour les assets 3D statiques du monde.
Avant de se lancer dans la production artistique de masse, la chaîne de travail complète (Blender -> glTF -> Bevy Client -> Bevy Serveur) doit être opérationnelle sur l'objet le plus simple possible : **un cube texturé**.

## 2. Périmètre Strict
*   **Asset cible** : Un simple cube. Pas de bâtiments, pas de biome.
*   **Validation visuelle Client** : Le cube est affiché dans le client Bevy.
*   **Validation physique Serveur** : Le cube dispose d'un collider fonctionnel reconnu par le serveur Headless.
*   **Durée estimée** : 2 semaines.

## 3. Séquencement des Tâches par Rôle
Afin d'éviter les changements de contexte coûteux, les tâches sont regroupées par rôle. Vous devez compléter les tâches d'un rôle avant de passer au suivant.

### 3.1. Phase 1 : Artiste 3D (Blender / Krita)
**User Story** : En tant qu'Artiste 3D, je veux créer et exporter un objet 3D basique respectant les contraintes techniques du moteur afin de garantir sa compatibilité.

*   [ ] **Tâche 1.1 : Création du Modèle (Blender)**
    *   Créer un Cube (Dimensions : 2m x 2m x 2m).
    *   S'assurer que la topologie est propre (composée de triangles).
*   [ ] **Tâche 1.2 : Dépliage UV et Texturisation (Blender / Krita)**
    *   Effectuer le dépliage UV (UV Unwrapping).
    *   Créer une texture simple (ex: `64x64` hand-painted).
    *   Assigner la texture au matériel du cube.
*   [ ] **Tâche 1.3 : Configuration du Matériau (Blender)**
    *   Configurer le matériel pour exporter avec l'extension `KHR_materials_unlit`. Le nœud de matériau dans Blender doit pointer vers un diffuse color, sans shader Principled BSDF complexe.
*   [ ] **Tâche 1.4 : Export glTF 2.0 (Blender)**
    *   Configurer l'exporteur glTF : Format binaire (`.glb`).
    *   Vérifier/Activer la conversion des coordonnées pour correspondre à Bevy : `+Y` up, `-Z` forward.
    *   Générer le fichier `test_cube_visual.glb`.

### 3.2. Phase 2 : Développeur Rust Client (Bevy Client)
**User Story** : En tant que Développeur Client, je veux charger l'asset 3D exporté et l'afficher correctement dans le moteur graphique pour valider le pipeline de rendu Rétro PS2.

*   [ ] **Tâche 2.1 : Configuration de l'Asset Server (Rust/Bevy)**
    *   Placer `test_cube_visual.glb` dans le dossier `assets/` du projet client.
*   [ ] **Tâche 2.2 : Instanciation du Modèle (Rust/Bevy)**
    *   Créer un système pour charger et instancier le modèle via un composant `SceneBundle`.
*   [ ] **Tâche 2.3 : Configuration du Shading WGPU (Rust/Bevy)**
    *   Configurer les paramètres de la caméra (ou du moteur) pour forcer le filtrage de texture `Nearest-Neighbor` (pixelisation de la texture).
    *   Vérifier visuellement (via la caméra client) que le cube s'affiche sans ombrage dynamique PBR (comportement Unlit validé).

### 3.3. Phase 3 : Développeur Rust Serveur (Bevy Headless / Rapier)
**User Story** : En tant que Développeur Serveur, je veux associer un collider invisible à l'entité du cube pour valider que le moteur physique (Anti-Cheat) reconnaît l'obstacle.

*   [ ] **Tâche 3.1 : Définition du Composant Collider (Rust/Bevy Serveur)**
    *   Dans le crate de composants partagés (`shared/components.rs`), définir ou utiliser un composant représentant un collider statique (ex: `StaticCollider { shape: ColliderShape::Cuboid }`).
*   [ ] **Tâche 3.2 : Instanciation de l'Entité Logique (Rust/Bevy Serveur)**
    *   Créer un système serveur qui instancie l'entité logique correspondant au cube.
    *   Attacher un composant `Transform` (position identique à celle du client).
    *   Attacher le composant `StaticCollider` (avec les dimensions du cube).
*   [ ] **Tâche 3.3 : Validation Physique (Rust/Bevy Serveur)**
    *   Mettre en place un test unitaire ou un mécanisme de log simple : faire avancer une entité "joueur" (avec collider) vers les coordonnées du cube.
    *   Vérifier dans les logs du serveur que la collision est détectée (blocage du mouvement).

## 4. Critères d'Acceptation (Definition of Done)
- [ ] Le fichier `test_cube_visual.glb` est exporté depuis Blender avec l'orientation `+Y` up, `-Z` forward.
- [ ] Le cube possède un matériau `KHR_materials_unlit`.
- [ ] Le client Bevy affiche le cube avec un filtrage `Nearest-Neighbor`.
- [ ] Le serveur Bevy Headless instancie un Collider AABB aux coordonnées du cube.
- [ ] La collision est détectée côté serveur.
