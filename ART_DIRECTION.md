# Direction Artistique & Identité Visuelle (Art Bible)

Ce document définit de manière formelle l'identité graphique, le style, les directives colorimétriques et la cohérence esthétique du projet MMORPG.
Il constitue le référentiel unique pour la production des assets et l'intégration UI/UX, s'alignant sur l'architecture « client terminal léger » (cf. README.md).

---

## 1. Vision Esthétique & Positionnement

L'univers prend place dans un cadre **Médiéval-Fantastique (Dark Fantasy)**.
Afin de maximiser les performances côté client, d'assurer une compatibilité transversale (des configurations anciennes aux machines modernes) et de dédier les ressources au calcul serveur, la direction artistique adopte un **style visuel Rétro 3D des années 2000 (génération PlayStation 2 / références : Metin2, World of Warcraft Vanilla, EverQuest)**.

**Piliers Visuels :**
* **Brut & Nostalgique :** Un retour aux sources du MMO, où l'accent est mis sur la clarté et l'atmosphère plutôt que sur le réalisme de rendu.
* **Lisibilité Immédiate :** L'action, les entités et l'interface doivent être déchiffrables en une fraction de seconde.
* **Sobriété Technique :** Les assets doivent être fondamentalement optimisés pour un rendu rapide.

---

## 2. Contraintes Techniques de Production

L'adoption d'un style "Retro 3D" impose des directives strictes quant à la création des assets (modèles, textures, éclairages).

* **Topologie (Low-Poly Strict) :**
  * Personnages jouables (Player Characters) et PNJ principaux : **1 500 à 3 000 polygones max**.
  * Monstres (Mobs) basiques : **500 à 1 500 polygones max**.
  * Décor statique : Utiliser le "culling" intensif. Topologie simplifiée à l'extrême.
* **Texturing (Hand-Painted & Dithering) :**
  * Approche "Diffuse Only" : Le volume et l'éclairage doivent être suggérés directement dans la texture peinte à la main (baking d'Ambient Occlusion toléré comme base de peinture).
  * Résolution des textures plafonnée (ex : 256x256 ou 512x512 pour les personnages).
  * Les matériaux PBR (Physically Based Rendering) sont strictement **interdits**.
* **Éclairage & Shading :**
  * Le rendu se fera via WGPU (OpenGL ES 3 / DirectX 11 pour la compatibilité).
  * L'environnement statique emploiera un éclairage précalculé (Baked Lighting / Lightmaps) ou du Vertex Coloring pour s'affranchir de calculs dynamiques coûteux.
  * Les ombres dynamiques (Shadow Mapping) seront limitées au joueur ou réduites à des ombres projetées (Blob Shadows) pour alléger le CPU/GPU.

---

## 3. Direction Colorimétrique & Ambiance par Zones

La palette globale est scindée en deux axes contrastants : une base oppressante (Terreuse) et des ruptures visuelles spectaculaires (Saturées).

### 3.1. Ton Général : Dark Fantasy
L'ossature visuelle du jeu doit évoquer la rudesse, le danger et la survie.

* **Palettes Dominantes :**
  * Ocre, brun cuirâtre, terre de Sienne.
  * Verts kaki, mousse, gris granit.
  * Bleu nuit, charbon.
* **Ambiance Environnementale :**
  * Villages ruraux : Boueux, pluvieux, architectures en bois sombre et pierre brute.
  * Extérieurs : Forêts épaisses où la lumière pénètre difficilement, marécages brumeux, montagnes arides.
* **Effet Psychologique :** Tension, mystère, isolement, réalisme âpre.

### 3.2. Contrastes Fonctionnels & Zones de Rupture
Pour casser la monotonie et récompenser l'exploration (ou signaler une menace élevée), des zones et éléments spécifiques utiliseront une saturation extrême, presque non naturelle.

* **Palettes d'Accentuation :**
  * Violet électrique, Émeraude bioluminescent, Cyan cristallin, Or irradiant, Magenta toxique.
* **Applications :**
  * **Environnements magiques :** Cratères corrompus, forêts féériques (éclairage néon), cavernes tapissées de cristaux lumineux.
  * **Gameplay :** Mettre en évidence les Effets Visuels (VFX) des compétences critiques, le "glow" des armes d'un niveau épique, ou l'aura d'un Boss (Elite).
* **Effet Psychologique :** Contraste violent, émerveillement, sensation de puissance ou d'alerte immédiate (Danger/Récompense).

---

## 4. Animation & Mise à l'Échelle

La cohérence esthétique passe aussi par le mouvement et la proportion.

* **Lisibilité des Silhouettes :** La règle d'or (Silhouette Test) : un ennemi vu en contre-jour doit être immédiatement identifiable par sa forme (ex : un gobelin doit avoir une posture voûtée très marquée).
* **Proportions "Heroic" :** Typique du début des années 2000. Mains, pieds, épaulettes et armes sont légèrement surdimensionnés par rapport au réalisme anatomique (ratio de ~1.2x). Cela améliore la lisibilité à la troisième personne (Third Person Camera).
* **Gabarits d'Animation (Animation Guidelines) :**
  * Poses fortes (Key poses) maintenues plus longtemps.
  * Moins d'interpolations de "blend" fluide, créant un mouvement légèrement rigide, incisif et percutant, caractéristique des jeux rétro.

---

## 5. Interface Utilisateur (UI) et Expérience (UX)

L'UI doit être le reflet de l'univers Médiéval-Fantastique sans jamais entraver la visibilité de la scène 3D. Le style sera lourd (matériaux solides) mais l'implémentation logicielle doit rester ultralégère.

### 5.1. Thématique et Matériaux
* **Inspiration :** Grimoires anciens, fer martelé, parchemin vieilli.
* **Rendu :** Opacité élevée (pas de flou "glassmorphism", très coûteux). Utilisation de textures imitant des matériaux physiques (cuir usé, bois brut, pierre). Bordures structurées (rivets, encadrements métalliques).

### 5.2. Schéma de Couleurs de l'UI
* **Fonds (Panels & Windows) :** Teintes profondes (Gris-brun anthracite #2c2520, Bordeaux-cuir #2a1a1b, Noir d'encre).
* **Contours et Séparateurs :** Fer rouillé, argent oxydé, laiton sombre.
* **Typographie :**
  * **Textes standards (Quêtes, Descriptions, Chat) :** Beige parchemin (#e8dcc4) ou Gris clair pour réduire la fatigue oculaire.
  * **Titres & Textes Importants :** Doré ancien ou Blanc pur.
* **Feedback visuel (Jauges) :** Couleurs primaires ultra-lisibles (Vie: Rouge carmin, Mana: Bleu cobalt, Endurance: Jaune ocre ou Vert).

### 5.3. Règles Typographiques
* **En-têtes et Menus :** Utilisation d'une police "Serif" au rendu médiéval ou une "Blackletter" (Gothique) modernisée, hautement lisible.
* **Textes de contenu :** "Sans Serif" très claire. Une "Bitmap Font" (police pixelisée lisse et nette) est conseillée pour renforcer l'aspect rétro et garantir l'affichage "pixel-perfect" sur de faibles résolutions.

### 5.4. HUD (Head-Up Display)
* **Design :** Le plus épuré possible, centré sur le bas ou les angles de l'écran.
* **Barre d'action (Hotbar) :** Icônes distinctives, souvent dessinées façon "pixel art" ou "low res" (64x64px), entourées d'un cadre métallique lourd.
* **Floating Combat Text (Dégâts Volants) :** Textes vectoriels nets, utilisant une hiérarchie stricte :
  * Dégâts normaux : Blanc
  * Dégâts critiques : Rouge ou Jaune intense, agrandis.
  * Soins : Vert vif.
  * (*Chaque texte flottant doit comporter une ombre portée dure (Drop Shadow) noire d'1 pixel pour se détacher du décor.*)

---
*Ce document sert de norme fondatrice (Art Bible) pour les infographistes, les animateurs et les développeurs front-end impliqués dans le développement du client.*
