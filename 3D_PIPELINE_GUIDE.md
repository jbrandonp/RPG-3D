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

---

## PLAN D'ACTION ET SPRINTS — 6 MOIS (24 SEMAINES)

### Sprint 1 — Mois 1 : Outils & Pipeline PoC
#### Semaine 1 : Installation et Configuration
*   Mise en place de l'environnement de travail (Blender, exportateurs, outils de validation).
*   Définition des conventions de nommage et de la structure des dossiers.

#### Semaine 2 : Premier Mesh Low-Poly (Cube Test)
*   **Action Blender :** Créer un objet primitif (Cube), assigner un matériau simple, préparer un UV map basique.
*   **Triangulation stricte :** Dans Blender : Sélectionne le mesh → Tab (Edit Mode) → A (tout sélectionner) → Face Select (touche 3) → Mesh → Face → Triangulate Faces. Vérifie en bas à gauche que le compteur affiche < 5000 Tris.

#### Semaine 3 : Premier Export glTF → Bevy
*   Exécuter les instructions d'export (voir section **Export glTF 2.0 depuis Blender** ci-dessous).
*   Intégration du Cube dans une scène Bevy de test pour valider le chargement.

#### Semaine 4 : Validation Pipeline Complète
*   Validation des matériaux (Unlit), du filtrage (Nearest-Neighbor), et de l'orientation (+Y Up).
*   Automatisation basique avec des scripts gltf-transform si nécessaire pour optimiser les assets exportés.

---

### Sprint 2 — Mois 2 : Personnage Joueur (Elara Voss)
#### Semaine 5 : Modélisation High-Poly
*   Sculpture détaillée d'Elara Voss. Priorité à la silhouette et aux volumes primaires.

#### Semaine 6 : Retopologie Low-Poly
*   Création du mesh final optimisé (cible : 1500 - 4000 triangles).
*   Respect du flux d'arêtes pour les futures déformations (coudes, genoux).

#### Semaine 7 : UV + Textures Hand-Painted
*   Dépliage UV optimisé.
*   Peinture des textures avec éclairage (AO/Cavité) intégré (style PS2).

#### Semaine 8 : Rigging + Animations de base
*   Création de l'armature (max 4 os par vertex, os racine en 0,0,0).
*   Animations : Idle, Walk, Attack, Hit, Die.
*   **Intégration Bevy :** Ajout du client (rendu) et du collider côté serveur (CapsuleCollider).

---

### Sprint 3 — Mois 3 : Monstres (Goblin + Orc)
#### Semaine 9 : Modélisation et Retopologie (Goblin & Orc)
*   Goblin (500-1500 tris) et Orc (1000-2500 tris).

#### Semaine 10 : Texturing
*   Application du style Hand-Painted sur les deux monstres.

#### Semaine 11 : Rigging et Animation
*   Rigging partagé si possible. Animations : Idle, Walk, Attack, Die.

#### Semaine 12 : Intégration et Tests
*   Intégration Bevy : Validation des animations in-game et configuration des colliders (Capsule/Sphere).

---

### Sprint 4 — Mois 4 : PNJ + Environnement Velnor Bidonvilles
#### Semaine 13 : Création du PNJ (Griselda)
*   Modélisation (1000-2000 tris) et texturing du marchand. Animation : Idle seulement. Intégration Bevy (Client).

#### Semaine 14 : Modélisation de l'Environnement (Sol + Bâtiments)
*   Modélisation du sol de Velnor et des 5 premiers bâtiments (max 5000 tris par bâtiment).

#### Semaine 15 : Décorations (Props) et Texturing
*   Création de 3 éléments de décor. Application d'atlas de textures partagés.

#### Semaine 16 : Intégration de l'Environnement
*   Placement dans Bevy. Génération du NavMesh côté serveur pour les déplacements. Configuration des AABB Colliders statiques.

---

### Sprint 5 — Mois 5 : Intégration Bevy complète + Serveur Headless
#### Semaine 17 : Finalisation de l'intégration des Assets
*   Vérification que tous les assets (PJ, Monstres, PNJ, Environnement) se chargent correctement et respectent les contraintes techniques (triangulation, < 5000 tris, Unlit).

#### Semaine 18 : Logique Serveur - Collisions
*   Implémentation et test exhaustif de la logique de collision primitive (AABB, Capsule, Sphere) sur le serveur Headless.

#### Semaine 19 : Logique Client - Matériaux et Rendu
*   Validation de l'implémentation du filtrage Nearest-Neighbor et des matériaux Unlit sur l'ensemble de la scène.

#### Semaine 20 : Sync Client-Serveur
*   Tests de synchronisation basiques (déplacements, détection de collisions) entre le client graphique et le serveur Headless.

---

### Sprint 6 — Mois 6 : Polissage + Vertical Slice jouable
#### Semaine 21 : Intégration HUD
*   Implémentation du HUD minimal dans Bevy (Barres de vie/mana, mini-map basique).

#### Semaine 22 : Debugging Visuel et Technique
*   Correction des bugs d'affichage (Z-fighting, problèmes d'animation, coutures UV visibles).
*   Analyse des performances (Draw calls, budget polygonal global).

#### Semaine 23 : Équilibrage et Tests de Gameplay
*   Ajustement des zones de collision et des timings d'animation pour les combats (PJ vs Goblin/Orc).

#### Semaine 24 : Livraison Vertical Slice
*   Version jouable finalisée : Elara Voss peut naviguer dans Velnor, interagir (visuellement) avec Griselda, et combattre les Goblins/Orcs, avec une validation serveur stricte.

---

## INTÉGRATION TECHNIQUE BEVY — EXEMPLES DE CODE

### Chargement glTF dans Bevy

```rust
// client/src/plugins/assets.rs

use bevy::prelude::*;

pub struct AssetsPlugin;

impl Plugin for AssetsPlugin {
    fn build(&self, app: &mut App) {
        app.add_systems(Startup, spawn_player_model);
    }
}

fn spawn_player_model(
    mut commands: Commands,
    asset_server: Res<AssetServer>,
) {
    // Charger le modèle glTF Elara Voss
    commands.spawn(SceneBundle {
        scene: asset_server.load("models/characters/elara_voss.glb#Scene0"),
        transform: Transform {
            translation: Vec3::new(0.0, 0.0, 0.0),
            scale: Vec3::splat(1.0),
            ..default()
        },
        ..default()
    });
}
```

### Configuration Matériau Unlit

```rust
// client/src/systems/materials.rs
// Force tous les matériaux en Unlit après chargement glTF

use bevy::prelude::*;
use bevy::pbr::StandardMaterial;

pub fn force_unlit_materials(
    mut materials: ResMut<Assets<StandardMaterial>>,
    query: Query<&Handle<StandardMaterial>, Added<Handle<StandardMaterial>>>,
) {
    for handle in query.iter() {
        if let Some(material) = materials.get_mut(handle) {
            // Désactiver l'éclairage PBR → style PS2 Unlit
            material.unlit = true;
            // Désactiver les ombres reçues
            material.reflectance = 0.0;
            material.metallic = 0.0;
            material.perceptual_roughness = 1.0;
        }
    }
}
```

### Filtrage Nearest-Neighbor

```rust
// client/src/plugins/render.rs

use bevy::prelude::*;
use bevy::render::texture::ImageSamplerDescriptor;

pub fn configure_nearest_neighbor_sampling(
    mut images: ResMut<Assets<Image>>,
    query: Query<&Handle<Image>, Added<Handle<Image>>>,
) {
    for handle in query.iter() {
        if let Some(image) = images.get_mut(handle) {
            // Nearest-Neighbor = style pixelisé PS2
            image.sampler = bevy::render::texture::ImageSampler::nearest();
        }
    }
}
```

### Colliders Serveur Headless

```rust
// server/src/systems/physics.rs
// Colliders primitifs côté serveur (SANS Bevy Rapier côté client)

use bevy::prelude::*;

// Collider AABB simple pour objets statiques (bâtiments, murs)
#[derive(Component)]
pub struct AabbCollider {
    pub min: Vec3,
    pub max: Vec3,
}

// Collider Capsule pour personnages (adapté aux formes humanoïdes)
#[derive(Component)]
pub struct CapsuleCollider {
    pub center: Vec3,
    pub radius: f32,
    pub half_height: f32,
}

// Collider Sphere pour projectiles et zones
#[derive(Component)]
pub struct SphereCollider {
    pub center: Vec3,
    pub radius: f32,
}

// Système de détection AABB vs Capsule
pub fn check_aabb_capsule_collision(
    aabb: &AabbCollider,
    capsule: &CapsuleCollider,
    capsule_pos: &Vec3,
) -> bool {
    let capsule_world_center = *capsule_pos + capsule.center;
    let closest = capsule_world_center.clamp(aabb.min, aabb.max);
    let distance = capsule_world_center.distance(closest);
    distance < capsule.radius
}

// Spawn automatique des colliders sur les assets statiques
pub fn spawn_environment_colliders(
    mut commands: Commands,
    query: Query<(Entity, &Transform, &Name), Added<Name>>,
) {
    for (entity, transform, name) in query.iter() {
        if name.as_str().contains("_collision") {
            commands.entity(entity).insert(AabbCollider {
                min: transform.translation - Vec3::splat(0.5),
                max: transform.translation + Vec3::splat(0.5),
            });
        }
    }
}
```

---

## INSTRUCTIONS BLENDER AU MILLIMÈTRE

#### Étape : Export glTF 2.0 depuis Blender

1. Sélectionne TOUS les objets du modèle → `A`
2. Menu File → Export → glTF 2.0 (.glb/.gltf)
3. Dans le panneau d'export (à droite) :
   ✅ Format : **glTF Binary (.glb)**
   ✅ Include : Selected Objects seulement
   ✅ Transform : **+Y Up** (CRITIQUE — Bevy utilise +Y)
   ✅ Mesh : Apply Modifiers ✅
   ✅ Mesh : UVs ✅
   ✅ Mesh : Normals ✅
   ✅ Mesh : Vertex Colors ✅
   ✅ Mesh : Triangulate Mesh ✅ (OBLIGATOIRE)
   ❌ Materials : Désactiver PBR (ou utiliser KHR_materials_unlit)
   ✅ Animation : Include Animation ✅
   ✅ Animation : Export Deformation Bones Only ✅
4. Nom du fichier : `nom_asset_v01.glb` (minuscules, underscores)
5. Dossier : `assets_export/characters/` ou `assets_export/environment/`
6. Clic → **Export glTF 2.0**

#### Vérification Post-Export (OBLIGATOIRE)
1. Aller sur https://gltf-viewer.donmccurdy.com/
2. Drag & Drop le fichier .glb
3. Vérifier :
   ✅ Le modèle est visible et correctement orienté (+Y = haut)
   ✅ Textures apparaissent (couleurs hand-painted visibles)
   ✅ Animations jouent correctement (onglet Animations)
   ✅ Pas de faces noires ou inversées
4. Si un problème → Retour Blender, corriger, re-exporter
