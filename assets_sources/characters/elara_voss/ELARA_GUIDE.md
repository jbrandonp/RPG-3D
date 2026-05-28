# GUIDE PERSONNAGE JOUEUR — ELARA VOSS

## Spécifications Techniques Obligatoires
- Triangles : 1500-4000 max
- Os : < 60 total, max 4 par vertex
- Texture : 512x512 px diffuse only (hand-painted)
- Format export : .glb (glTF 2.0)
- Coordonnées : +Y up, -Z forward

## Semaine 1 : Blockout & Proportions
### Étape 1 : Créer le corps de base
1. Ouvrir Blender → File → New → General
2. Supprimer le cube par défaut : `X` → Delete
3. Ajouter une UV Sphere : `Shift+A` → Mesh → UV Sphere
   - Segments : 8, Rings : 8 (low-poly volontaire)
4. Passer en Edit Mode : `Tab`
5. Ajuster la taille et la position pour correspondre aux proportions "Heroic" (tête = 1/6 du corps).
*Vous pouvez utiliser le script Python fourni (`scripts/blender/create_elara_blockout.py`) pour automatiser cette étape de blockout et la création du squelette de base.*

## Semaine 2 : Retopologie Low-Poly
### Étape 1 : Modéliser par-dessus le Blockout
1. Utilisez le blockout comme guide.
2. Créez de la nouvelle géométrie : `Shift+A` → Mesh → Plane, puis activez le "Snap to Face" (icône aimant en haut).
3. Extrudez (`E`) et déplacez (`G`) pour créer le maillage final.
4. **Validation :** Le compteur de triangles en bas de l'écran (ou dans l'Overlay "Statistics") doit afficher < 4000 Tris.

### Étape 2 : Edge Flow pour l'animation
1. Assurez-vous d'avoir au moins 3 boucles d'arêtes (`Ctrl+R`) autour de chaque articulation (épaules, coudes, genoux).

## Semaine 3 : UV Mapping
1. Marquez les coutures (Seams) dans des endroits discrets (intérieur des bras, jambes, sous les cheveux) : Sélectionnez l'arête → `Clic Droit` → Mark Seam.
2. Sélectionnez tout (`A`) → `U` → Unwrap.
3. Organisez les îles UV dans l'UV Editor pour maximiser l'espace.

## Semaine 4 : Textures Hand-Painted (Krita)
1. Exportez l'UV Layout depuis Blender : UV Editor → UV → Export UV Layout.
2. Ouvrez dans Krita. Peignez les couleurs de base (Albedo), puis ajoutez les ombres d'occlusion et les reflets directement dans la texture.
3. Résolution cible : 512x512 px. Exportez en `.png`.

## Semaine 5 : Rigging (Armature)
1. Si vous avez utilisé le script Python, ajustez le placement des os sur votre modèle Low-Poly en Edit Mode (`Tab`).
2. Appliquez le modèle à l'armature : Sélectionnez le Mesh, puis l'Armature → `Ctrl+P` → With Automatic Weights.
3. Allez en Weight Paint Mode. Corrigez les influences.
4. **Validation :** Assurez-vous que l'option Limit Total (dans Weights) est réglée sur 4.

## Semaine 6 : Animations de Base
1. Passez en Pose Mode.
2. Ouvrez la Dope Sheet (Action Editor) ou la Timeline.
3. Créez les actions : `Idle`, `Walk`, `Attack`, `Hit`.
4. Enregistrez les poses avec `I` (Location, Rotation).

## Semaine 7 : Export glTF + Validation
1. Suivez la checklist dans `CHECKLIST_ELARA.md`.
2. Fichier → Exporter → glTF 2.0 (.glb).
3. Cible d'export : `assets_export/characters/elara_voss.glb`.

## Semaine 8 : Intégration Bevy
1. Exécutez le script Node d'optimisation WGPU (`npm run optimize`).
2. Chargez l'asset optimisé (`assets/models/elara_voss.glb`) dans votre scène Bevy.
