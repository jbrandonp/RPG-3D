# Sprint 0 & 1 : Validation du Pipeline Visuel (Vertical Slice)

Ce document décrit en détail les Sprints 0 et 1, conçus pour valider le workflow technique entre les outils de création 3D (Blender) et le moteur de jeu en Rust (Bevy), en respectant la direction artistique Rétro (style PS2/Metin2).

---

## 1. Contexte du Pipeline

L'enjeu majeur de ces deux premiers sprints est de **ne rien laisser au hasard techniquement**. La direction artistique impose des limitations drastiques qui assurent les performances et l'esthétique du jeu. Si une de ces règles est violée, l'asset ne pourra pas être utilisé.

### Règles d'Or (Rappel) :
- **Low-Poly :** Max 5000 triangles par objet complexe.
- **Diffuse Only (Unlit) :** Export glTF avec l'extension `KHR_materials_unlit`.
- **Triangulation Manuelle :** Pas de modification par Subdivision de Surface à l'export.
- **Skinning :** **Maximum 4 os par vertex** (règle stricte pour Bevy/WGPU).
- **Textures :** Filtrage `Nearest-Neighbor` dans Bevy.

---

## 2. SPRINT 0 : Validation Technique du Pipeline (Semaine 0)

Le but ici n'est pas de faire du "beau", mais de prouver que la chaîne d'outils communique correctement.

### Tâches (Backlog Sprint 0) :
1. [ ] **Blender - Création d'un Mesh Test :** Créer un modèle très simple (ex: un cube ou un cylindre articulé).
2. [ ] **Blender - Skinning basique :** Ajouter 2 ou 3 os et s'assurer que la limite de 4 os/vertex est respectée.
3. [ ] **Blender - Texturing Unlit :** Assigner une texture diffuse avec de fausses ombres (peintes) et exporter le `.glb` avec `KHR_materials_unlit`.
4. [ ] **Bevy - Code d'Import :** Écrire le code Rust/Bevy pour charger la scène (`SceneBundle`).
5. [ ] **Bevy - Configuration du Rendu :** Paramétrer les `ImagePlugin` de Bevy pour forcer l'échantillonnage de texture en `Nearest` (pixelisé).
6. [ ] **Validation :** Vérifier in-game que l'objet s'affiche, sans réagir à la lumière dynamique, et que l'animation se joue.

---

## 3. SPRINT 1 : La "Vertical Slice" (Semaines 1 & 2)

L'objectif du Sprint 1 est de livrer les assets de référence définitifs pour le projet. Ce sont les étalons sur lesquels tous les autres assets s'aligneront.

### Focus Prioritaire
**Le Workflow "Hand-Painted" sur les personnages.** C'est l'essence même du style visuel du projet. L'absence de normal/specular maps oblige à peindre le volume, les reflets métalliques et les ombres directement sur la texture.

### Tâches (Backlog Sprint 1) :

#### 1. Personnage "Dummy" (Elara Voss - Base)
- [ ] **Modélisation (Retopology manuelle) :** Viser 1500 à 4000 triangles. Proportions "Heroic".
- [ ] **Texturing (Hand-Painted) :** Texture diffuse (ex: 512x512). Fake lighting peint (ombres de contact sous les bras/cou).
- [ ] **Rigging :** Respect absolu de la limite des **4 os par vertex**. Root bone en `(0,0,0)`.
- [ ] **Animation :** Création d'une boucle *Idle* de 2 secondes. Exagération légère de la respiration (style arcade).

#### 2. L'Arme (Épée Basique)
- [ ] **Modélisation :** Moins de 500 polygones. Lame large (surdimensionnée).
- [ ] **Texturing :** Texture diffuse. Peindre le faux reflet blanc oblique pour simuler le métal brillant.
- [ ] **Intégration :** Attachement (parenting) à l'os de la main droite d'Elara dans Blender, ou gestion par code d'attache dans Bevy.

#### 3. L'Environnement de Base
- [ ] **Tuile de Sol (Plaines) :** Un bloc de 500x500. Texture hand-painted de gazon/terre.
- [ ] **L'Arbre Repère :** Tronc géométrique (low poly), feuillage sous forme de "grappes" ou de plans croisés (billboards/planes). Texture peinte.

#### 4. Intégration Finale dans Bevy
- [ ] Importation de tous les `.glb` du Sprint 1.
- [ ] Vérification des échelles (l'épée, le joueur et l'arbre doivent être cohérents ensemble).
- [ ] Test d'éclairage : Constater que même dans un environnement Bevy sans lumière, les assets sont parfaitement visibles et ombrés (grâce au hand-paint).

---
*Fin du Sprint 1 : Validation de l'allure générale ("Look and Feel") du jeu.*
