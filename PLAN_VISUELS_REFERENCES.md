# Direction Artistique & Références Visuelles - Projet Mini-MMO

## 1. Vision et Piliers Visuels
Ce document définit les standards visuels et la direction artistique (Art Direction) du projet. L'esthétique s'inspire directement des MMORPG asiatiques et occidentaux du début des années 2000 (ex: *Metin2*, *World of Warcraft* "Classic"), en fusionnant un **réalisme sombre et vieilli** avec des **accents visuels typés "Arcade"**.

### Piliers de la Direction Artistique
- **Low-Poly & Hand-Painted :** Modèles 3D avec un faible nombre de polygones. Les détails (usure, ombres de contact, reflets métalliques) sont directement peints sur des textures diffuses (albedo). Pas de PBR (Physically Based Rendering) complexe.
- **Dualité Ambiante (Sombre vs Vif) :** Un fort contraste entre des environnements clos oppressants (donjons) aux palettes ternes, et des extérieurs (champs, arènes) ouverts, vibrants et hautement saturés.
- **Lisibilité avant tout :** Les silhouettes (personnages, monstres, objets interactifs) doivent être instantanément reconnaissables de loin, avec des formes géométriques fortes (gros épaulements, armes surdimensionnées).

---

## 2. Environnements et Éclairages

### 2.1 Intérieurs Sombres (Donjons, Catacombes)
*Ces zones doivent transmettre un sentiment d'ancienneté, de danger et de délabrement.*

- **Palette de Couleurs :** Dominante de gris cendre, anthracite, bordeaux oxydé, et rouille.
- **Matériaux & Textures :**
  - Murs et sols : Blocs de pierre massifs, mal taillés, avec des joints sombres et profonds peints sur la texture.
  - Éléments de décor : Bois pourri, fer forgé tordu, chaînes rouillées. Étoffes (tapis, bannières) déchirées, arborant des teintes de rouge sang séché.
- **Éclairage & VFX :**
  - Éclairage indirect quasi inexistant (zones d'ombre denses).
  - Sources de lumière ponctuelles (flambeaux, braseros) projetant un halo très chaud (orange/rouge incandescent) qui tranche radicalement avec les murs froids.

### 2.2 Extérieurs Ouverts (Champs, Arènes "Arcade")
*Inspirés des univers plus fantaisistes, ces environnements offrent une bouffée d'air frais, tout en conservant une géométrie stricte.*

- **Palette de Couleurs :** Très haute saturation. Vert pomme/fluo pour l'herbe, cyan profond et blanc pur pour les zones enneigées, bleu azur dégagé pour le ciel.
- **Matériaux & Textures :**
  - Sols : Aplats de couleurs vives (ex: herbe stylisée) avec des motifs répétitifs doux. Quelques touffes d'herbe ou blocs de glace surdimensionnés en 3D (billboards ou low-poly) pour casser la monotonie.
  - Reliefs : Falaises lisses avec des strates géologiques simples, aux arêtes prononcées.
- **Éclairage & VFX :**
  - Lumière globale (Sun directional light) forte et verticale, ombres portées nettes et dures (hard shadows).
  - Ciel dégagé avec des nuages volumétriques low-poly, aux bords francs (effet "cotonneux mais géométrique").

---

## 3. Personnages (Héros et PNJ)

### 3.1 Anatomie et Proportions (Style "Heroic Proportion")
- **Morphologie :** Proportions stylisées (ratio tête/corps de 1:7 ou 1:8). Épaules et mains légèrement surdimensionnées chez les classes martiales pour souligner la force ; silhouettes plus élancées et anguleuses pour les lanceurs de sorts.
- **Visages & Expressions :** Traits anguleux inspirés de l'animation japonaise des années 2000. Yeux expressifs avec de forts contrastes d'iris.
- **Chevelure :** Modélisée en "grappes" solides (pas de simulation de cheveux individuelle). Couleurs extravagantes et très saturées (Bleu Électrique, Rouge Feu, Blanc Pur) contrastant avec le reste de l'équipement.
- **Animation :** Poses d'attente (Idle) respirantes et ancrées au sol, marquant un rythme cardiaque lent mais puissant.

### 3.2 Personnages Non Joueurs (Exemple : Le Marchand)
- **Archétype :** Silhouette trapue, souvent en forme de "poire", soulignant un aspect jovial mais vénal.
- **Traits Caractéristiques :** Visage buriné, nez proéminent, accessoires ostentatoires (une dent en or brillant périodiquement, de grosses bagues).
- **Posture :** Statique, souvent assis sur un contenant de grande taille (caisse en bois renforcée, sac de jute débordant).

---

## 4. Costumes et Équipements

*L'équipement doit refléter la progression du joueur : d'une palette terne et de matériaux pauvres vers des teintes éclatantes, des matériaux nobles et des silhouettes imposantes.*

### 4.1 Tier 1 : Tenues de Base (Débutants)
- **Matériaux :** Lin écru, cuir brut usé, fer non poli.
- **Coupes :** Simples et utilitaires (tuniques asymétriques, pantalons amples fixés par des lanières).
- **Couleurs :** Dominante de tons neutres et terreux (beige, marron, vert olive), permettant aux cheveux et aux armes de ressortir.

### 4.2 Tier Avancé : Armures Lourdes (Guerriers / Paladins)
- **Matériaux :** Acier bleuté, plaques ornées d'or ou de bronze, liserés bordeaux.
- **Silhouette :** Massives, avec des épaulettes démesurées (souvent asymétriques) agissant comme point focal visuel.
- **Détails :** Reflets métalliques statiques peints sur la texture diffuse (fausses spécificités d'éclairage typiques des jeux PS2). Capes rigides et épaisses.

### 4.3 Tier Avancé : Robes (Mages / Soigneurs)
- **Matériaux :** Soie lourde, velours, broderies luminescentes.
- **Silhouette :** Pans de tissus larges et géométriques tombant droit. Capuches profondes projetant une ombre noire cachant la partie supérieure du visage.
- **Couleurs :** Teintes royales et profondes (Violet Améthyste, Rouge Cramoisi, Blanc Nacré).

---

## 5. Bestiaire (Créatures et Boss)

### 5.1 Faune Basique (Exemple : Loups Sauvages)
- **Silhouette :** Démusclée ou à l'inverse très charpentée sur l'avant-train. Crocs surdimensionnés.
- **Couleurs et Textures :** Pelage modélisé en pointes anguleuses. Fourrure gris anthracite, yeux émettant une légère lueur jaune (Emissive material), apportant un aspect agressif direct.

### 5.2 Monstres Élémentaires (Exemple : Golems de Glace/Roche)
- **Silhouette :** Assemblage de polyèdres asymétriques en lévitation partielle ou encastrés les uns dans les autres.
- **Couleurs et Textures :**
  - Glace : Cyan translucide avec de forts reflets blancs figés (peints).
  - Roche : Gris basalte traversé de veines géométriques fluorescentes (vert toxique ou magma orangé).
- **Animation :** Mouvements lourds, mécaniques, avec un "freeze-frame" (léger arrêt) lors des impacts au sol.

### 5.3 Boss et Gardiens
- **Silhouette :** Taille au minimum double par rapport au joueur. Architecture visuelle de type "Chevalier Noir" ou "Démon Cornu".
- **Design :** Armures corrodées foncées (Bordeaux/Noir), peau cendrée.
- **VFX & Identité Visuelle :** Utilisation intensive de particules (auras de flammes sombres, traînées de lumière rouge sur les armes lors des mouvements). L'arme du boss doit être une source de lumière autonome.

---

## 6. Arsenal (Armes)

*Les armes sont le principal vecteur de puissance visuelle du jeu.*

- **Armes de Mêlée (Épées, Haches) :**
  - Lames extrêmement larges (type *Buster Sword*).
  - Manche souvent enveloppé de cuir contrastant (rouge vif ou noir profond).
  - Textures intégrant des "coups d'éclat" : lignes blanches diagonales peintes pour simuler un reflet perpétuel.
- **Armes Magiques (Bâtons) :**
  - Bois tordu et noueux avec des contrastes d'écorce très marqués (dark brown / light beige).
  - Le sommet abrite un cristal massif (oversized) aux couleurs pures (RGB : pur Rouge, pur Bleu, pur Vert), généralement en lévitation rotative lente ou fermement serti.
- **Boucliers :**
  - Formes géométriques primaires (cercles parfaits ou pavois rectangulaires stricts).
  - Forte épaisseur de la tranche. Ornementation centrale voyante (emblème héraldique, crâne stylisé) en jaune/or sur fond très sombre.

---

## 7. Objets Interagissables et UI In-Game

*Tous les objets jetés au sol ou interactifs doivent avoir un impact visuel "Arcade" immédiat pour attirer l'œil du joueur.*

### 7.1 Consommables (Potions)
- **Design :** Fioles sphériques parfaites surmontées de bouchons en liège cubiques ou surdimensionnés.
- **Matériaux :** Verre simple avec un contenu de couleur néon (Rouge Écarlate = Soin, Bleu Cyan = Mana), émettant une légère aura lumineuse au sol.

### 7.2 Butin (Coffres et Monnaie)
- **Coffres :** Coffres en bois sombre à larges veines, cerclages de fer exagérés et un cadenas démesuré. À l'ouverture, émission de particules de type "Sparkles" et lumière volumétrique dorée sortant de l'intérieur.
- **Monnaie (Or) :** Modèles 3D de grosses pièces épaisses. Lorsqu'elles tombent, elles rebondissent de manière exagérée avec un effet de rotation (Billboard 2D ou vraie rotation 3D) et émettent un son aigu distinctif ("Ching").
