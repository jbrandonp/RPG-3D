# Audio Design Document (ADD) - Mini-MMO Rétro

## 1. Vision Globale & Direction Artistique

Ce document définit l'univers sonore, les spécifications techniques et les normes d'intégration pour le Mini-MMO. La direction artistique s'inspire directement des MMORPG classiques des années 2000 (style *Metin2*, *Ragnarok Online*, *World of Warcraft Classic*).

L'objectif absolu de la conception sonore est le **confort d'écoute à long terme**. Le jeu étant conçu pour de longues sessions, l'audio doit être relaxant, nostalgique et prévenir toute forme de fatigue auditive (*ear fatigue*).

### 1.1. Piliers Esthétiques
*   **Musique "Classic 2000s" :** Orchestrations douces, tempo lent à modéré. Prédominance d'instruments acoustiques (harpe, flûte traversière, violoncelle, guitare acoustique, luth) et de nappes synthétiques discrètes (pads rétro).
*   **Mixage Chaleureux :** Atténuation drastique des hautes fréquences (aigus perçants) sur l'ensemble du spectre SFX (Sound Effects). Priorité à la rondeur et à la chaleur.
*   **Texture "Rétro PS2" :** Légère compression et utilisation de réverbérations algorithmiques rappelant les processeurs d'effets du début des années 2000, pour lier esthétique visuelle (low-poly) et identité sonore.

---

## 2. Ambiances, Biomes et Systèmes Dynamiques

L'univers est divisé en biomes distincts possédant une empreinte sonore unique, soutenue par un système de météo et de transition dynamique.

### 2.1. Le Village de Départ (Zone de sécurité)
*   **Musique :** Thème accueillant, mélodie pastorale (guitare acoustique, flûte en bois).
*   **Ambiance :** Bruissements feuillus légers, bruits de pas feutrés.
*   **Points d'Intérêt (POI) :** Forgeron (tintement mat et étouffé, non strident), brouhaha lointain et chaleureux des PNJ.

### 2.2. La Forêt Paisible (Zone de farm débutant)
*   **Musique :** Nappes de cordes minimalistes, notes de harpe espacées.
*   **Ambiance :** Chant d'oiseaux relaxant (filtré pour ne pas percer le mix), murmure de l'eau.
*   **Cycle Jour/Nuit :** Transition en douceur vers une ambiance nocturne (grillons apaisants, chouette lointaine). Disparition progressive de la piste musicale principale pour laisser place au silence et au vent.

### 2.3. Les Grottes et Cavernes (Zones de danger modéré)
*   **Musique :** Minimaliste et mystérieuse. Synthétiseurs graves et résonants, sans inciter à l'angoisse oppressante.
*   **Ambiance :** Gouttes d'eau fortement réverbérées, souffle d'air sourd dans les tunnels. Acoustique simulée de type *Hall/Cave* avec un renforcement des basses fréquences.

### 2.4. Météo Dynamique et Transitions
*   **Pluie et Orage :** La pluie doit être mixée comme un "bruit blanc" relaxant (type ASMR), sans fréquences aiguës agressives. Le tonnerre est lointain et grave (grondement sourd), jamais un craquement sec.
*   **Vent Fort :** Sifflement grave, évitant les harmoniques stridentes.
*   **Transitions (Crossfades) :** Lors d'un changement de biome ou de météo, le moteur (Bevy) doit effectuer un fondu enchaîné (crossfade) progressif d'au moins 3 à 5 secondes pour la musique et les ambiances, évitant toute coupure abrupte.

---

## 3. Bruitages (SFX) & Combats

Les bruitages d'action doivent transmettre le poids et l'impact sans jamais devenir agressifs.

### 3.1. Armes et Classes (Thème Médiéval-Fantastique)
*   **Corps-à-corps (Épées, Haches, Masses) :**
    *   *Swing :* "Woosh" grave fendant l'air.
    *   *Impact :* Choc mat et lourd (type coup dans du cuir ou du bois épais). **Interdiction des cliquetis métalliques aigus.**
*   **Distance (Arcs) :**
    *   *Tension :* Étirement doux de corde et de bois.
    *   *Tir :* Sifflement rapide, discret et fluide.
*   **Magie :**
    *   *Cast & Impact :* Sons cristallins, ronds, harmoniques (carillons adoucis, chœurs de synthé).
    *   *Éléments (Feu, Glace) :* Souffle d'air chaud ou léger craquement vitreux, systématiquement filtrés par un EQ "Low-Pass" (coupe-haut) pour adoucir le rendu.

### 3.2. Races, Créatures et Voix
*   **Humains :** Cris d'effort (saut, attaque, dégâts) mixés très bas, voix posées.
*   **Rôdeurs :** Voix rocailleuses, chaleureuses. Bruits de pas lourds (résonance sur la pierre).
*   **Effarés :** Grognements gutturaux mais feutrés. Déplacements rapides (pattes légères). Aucun cri perçant n'est toléré.
*   **Déplacements (Foley) :** Le bruit des pas (herbe, pierre, bois, terre) est le son le plus entendu du jeu. Il doit être rythmique, relaxant, et traité avec un soin extrême pour ne pas lasser.

---

## 4. UI Sounds (Sons d'Interface)

L'interface est omniprésente. Ses sons s'inspirent du concept de "UI ASMR" (interactions tactiles, organiques et satisfaisantes).

*   **Survol (Hover) :** "Tick" boisé très bas volume (tapotement sur du liège).
*   **Clic / Validation :** Son cristallin étouffé, légèrement réverbéré (petit xylophone).
*   **Erreur :** Double son mat et grave (bop-bop), doux et non punitif. Pas de buzzers agressifs.
*   **Ouverture de fenêtre :** Bruit de parchemin qui se déroule ou de frottement de cuir souple.
*   **Progression (Level Up) :** Courte fanfare dominée par des cordes, chœurs et cors d'harmonie graves. Pas de trompettes ou cuivres criards.
*   **Inventaire / Monnaie :** Tintement de pièces d'or lourd et antique, rond, sans sifflement métallique.

---

## 5. Spécifications Techniques & Moteur (Bevy)

Afin d'assurer une qualité professionnelle, l'intégration des assets sonores dans le moteur **Bevy** doit respecter les règles suivantes.

### 5.1. Normes de Fichiers
*   **Fréquence d'échantillonnage :** 48 kHz (uniformiser obligatoirement sur tout le projet).
*   **Profondeur de bit :** 16-bit ou 24-bit.
*   **Formats :**
    *   `.ogg` (Vorbis) : Pour les musiques, les longues ambiances et la météo (fichiers lourds, streaming).
    *   `.wav` (PCM) : Pour les SFX courts et les sons d'interface UI (chargement en RAM, lecture sans latence de décompression).

### 5.2. Mixage et Mastering (Cibles LUFS)
Pour garantir une cohérence de volume (loudness) et éviter de fatiguer le joueur :
*   **Musique :** -20 à -24 LUFS (True Peak -1.0 dB).
*   **Ambiances (BGM) :** -24 à -28 LUFS.
*   **SFX / Combats :** -16 à -20 LUFS.
*   **Voix / PNJ :** -18 à -22 LUFS.
*   **UI :** -22 à -26 LUFS.

### 5.3. Implémentation Bevy (Comportement Audio)
*   **Spatialisation (3D Audio) :** Les sons dans le monde (pas, combats, monstres, POI) doivent utiliser une courbe d'atténuation (falloff) logarithmique ou linéaire. Un joueur éloigné ne doit plus entendre l'action.
*   **Variation Aléatoire (Anti-Répétitivité) :**
    *   *Pitch :* Tout effet sonore répétitif (pas, coups d'épée) doit se voir appliquer un décalage aléatoire de pitch (ex: $\pm 5\%$) à chaque lecture par le moteur Bevy.
    *   *Volume :* Légère variation de volume (ex: $\pm 2$ dB) par lecture.
*   **Priorisation / Concurrency :** Limiter le nombre de sons simultanés. Si plus de 5 Effarés attaquent, les sons d'attaque doivent être limités (voice stealing / culling) pour ne pas créer un chaos sonore ou saturer la sortie master.

---

## 6. Charte de Nommage (Naming Convention)

Une organisation stricte est requise pour tous les fichiers audios importés dans le projet.

**Format général :** `[Catégorie]_[Sous-catégorie]_[Description]_[Action/Matière]_[NuméroVariation]`

**Exemples :**
*   **Musique (MUS) :**
    *   `MUS_BGM_VillageStart_01.ogg`
    *   `MUS_BGM_ForestPeaceful_Day_01.ogg`
*   **Ambiance (AMB) :**
    *   `AMB_Weather_Rain_Light_01.ogg`
    *   `AMB_Zone_Cave_DrippingWater_01.ogg`
*   **Effets Sonores (SFX) :**
    *   `SFX_Wpn_Sword_Swing_01.wav`
    *   `SFX_Wpn_Sword_ImpactFlesh_02.wav`
    *   `SFX_Wpn_Bow_Shoot_01.wav`
    *   `SFX_Magic_Fireball_Cast_01.wav`
*   **Mouvements / Foley (FOL) :**
    *   `FOL_Footstep_Grass_Run_01.wav`
    *   `FOL_Footstep_Stone_Walk_03.wav`
*   **Créatures (CRE) :**
    *   `CRE_Effare_Aggro_01.wav`
    *   `CRE_Rodeur_Effort_02.wav`
*   **Interface (UI) :**
    *   `UI_Hover_Button_01.wav`
    *   `UI_Click_Confirm_01.wav`
    *   `UI_Notification_LevelUp_01.wav`

---

*Note : Toute nouvelle intégration sonore doit être validée par une écoute de 30 minutes in-game pour confirmer l'absence de fatigue auditive.*
