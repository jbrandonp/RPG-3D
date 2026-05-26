# Backlog Général des Assets Visuels (Vers Pré-Alpha)

Ce document liste l'ensemble des assets visuels (3D, 2D, VFX) nécessaires pour atteindre la phase de Pré-Alpha du MMORPG. Ces assets doivent tous respecter le pipeline technique : `Low-Poly (< 5000 tris)`, `Unlit (Diffuse Only)`, `Nearest-Neighbor` et `Max 4 os/vertex`.

---

## 1. Environnements (Sprints 2 & 3)

### Tuiles de Terrain (Sols)
*Atlas de textures dédié par biome.*
- [ ] Tuile de base "Plaines Agricoles" (Sprint 1)
- [ ] Tuile de base "Forêt Sombre"
- [ ] Tuile de base "Marais Corrompu"
- [ ] Tuile de base "Pavés de Ville"

### Végétation et Décor (Props)
- [ ] Arbre générique - Plaine (Sprint 1)
- [ ] Arbre type "Pin mort" - Forêt/Marais (x2 variantes)
- [ ] Buissons et hautes herbes (Planes croisés) (x3 variantes)
- [ ] Rochers et formations rocheuses (x5 variantes de taille/forme)
- [ ] Caisse en bois cassable (Loot)
- [ ] Tonneau en bois

### Architecture
- [ ] Bâtiment "Maison de PNJ basique"
- [ ] Bâtiment "Forge / Marchand"
- [ ] Élément "Entrée de Donjon" (Porte de pierre massive)
- [ ] Muraille en ruine (Section droite et angle)

---

## 2. Personnages et Créatures (Sprints 1, 3 & 4)

### Personnages Joueurs (PJ)
- [ ] Modèle Base - Elara Voss (Dummy Sprint 1) (1500 - 4000 tris)
- [ ] *Variante Textures :* Armure Cuir (Tier 1)
- [ ] *Variante Textures :* Armure Fer (Tier 2)

### Créatures (Bestiaire)
- [ ] Gobelin - Tireur (Arc/Cailloux) (Low Tier)
- [ ] Gobelin - Mêlée (Dague) (Mid Tier)
- [ ] Gobelin - Chaman (Bâton) (High Tier)
- [ ] Orc - Guerrier Lourd (Hache à 2 mains)
- [ ] Bête - Loup (Modèle quadrupède de base)

### Personnages Non-Joueurs (PNJ)
- [ ] PNJ Marchand (Silhouette trapue, sac de jute)
- [ ] PNJ Garde / Guerrier (Armure lourde statique)

---

## 3. Arsenal et Objets (Sprint 1 & 2)

### Armes
- [ ] Épée à une main basique (< 500 tris)
- [ ] Hache à deux mains (Lourde)
- [ ] Arc court en bois
- [ ] Bâton de Mage (Avec cristal coloré texturé)
- [ ] Bouclier en bois cerclé de fer

### Objets Interagissables
- [ ] Potion de Soin (Fiole ronde, texture rouge vif émissive/hand-painted)
- [ ] Potion de Mana (Fiole carrée, texture bleu cyan)
- [ ] Bourse d'Or (Loot au sol)
- [ ] Coffre au trésor (Animé : Fermé/Ouvert)

---

## 4. Effets Visuels (VFX) (Sprint 4)

*Rappel : Tous les VFX sont constitués de billboards 2D (polygones simples) avec Additive Blending.*

### Combats (Impacts)
- [ ] Hitmark Mêlée (Coupure blanche stylisée)
- [ ] Blood Splash - Variante 1 (Petite)
- [ ] Blood Splash - Variante 2 (Lourde)
- [ ] Blood Splash - Variante 3 (Critique)

### Magie
- [ ] Sort : Boule de Feu (Projectile 2D animé + Traînée de particules)
- [ ] Sort : Soin (Pilier de lumière montant + symboles dorés)
- [ ] Sort : Zone de corruption (Cercle au sol, marécageux)

---

## 5. Interface Utilisateur (UI) (Sprint 4)

*UI "Arcade", polices pixelisées.*

### Éléments HUD
- [ ] Jauge de Vie (Bordure fer/pierre + remplissage Rouge)
- [ ] Jauge de Mana (Bordure fer/pierre + remplissage Bleu)
- [ ] Hotbar (Cadres 64x64px pour les compétences, look métal lourd)

### Typographie et Interactions
- [ ] Pixel Font intégrée au projet Bevy.
- [ ] Bulles de dialogue flottantes (Fond parchemin, max 3 lignes / 60 char).
- [ ] "Floating Combat Text" (Sprites vectoriels ou polices bitmap avec ombres portées pour dégâts/soins).
