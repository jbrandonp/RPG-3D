# CHECKLIST ELARA VOSS — Validation Avant Export .glb

## ✅ Géométrie
- [ ] Triangles total < 4000 (vérifier: bas de l'écran Blender)
- [ ] Aucun N-gon (faces > 4 côtés) — Edit Mode → Face Select → Tris
- [ ] Triangulation manuelle appliquée (Mesh → Face → Triangulate)
- [ ] Aucune face dupliquée (Mesh → Cleanup → Merge by Distance)
- [ ] Normales correctes (aucune face noire) → Overlay → Face Orientation

## ✅ Rigging
- [ ] Nombre d'os < 60 total
- [ ] MAX 4 os par vertex (Weight Paint → vérifier les weights)
- [ ] Os root à (0, 0, 0)
- [ ] Tous les os nommés correctement (_L/_R pour gauche/droite)
- [ ] Squelette en pose Rest (Apply → Rest Position)

## ✅ Textures
- [ ] Texture diffuse uniquement (512x512 px minimum)
- [ ] Aucune normal map / specular / roughness
- [ ] UV unwrap complet (aucun vertex hors des UVs)
- [ ] Texture sauvegardée en PNG ou JPEG

## ✅ Matériaux
- [ ] 1 seul matériau par modèle (optimisation draw calls)
- [ ] Matériau nommé "elara_diffuse"

## ✅ Export glTF
- [ ] Format : glTF Binary (.glb)
- [ ] +Y Up coché
- [ ] Triangulate Mesh coché
- [ ] KHR_materials_unlit activé
- [ ] Validé sur gltf-viewer.donmccurdy.com
