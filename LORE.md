# DOCUMENT DE CONCEPTION NARRATIVE (LORE.md)

| Propriété | Détail |
| :--- | :--- |
| **Projet** | AETHON CHRONICLES (Titre provisoire) |
| **Statut** | Document de Travail (WIP) |
| **Version** | 2.0.0 |
| **Périmètre** | Prototype (Pré-Alpha) & Vision étendue (Horizon 2030) |

> **Avertissement :** Ce document est le point de référence central pour la direction narrative, la conception des personnages, la structure des quêtes et l'intégration des systèmes d'intelligence artificielle. Toute modification de l'univers de jeu doit être documentée ici pour assurer la cohérence entre le gameplay, la technique et l'histoire.

---

## TABLE DES MATIÈRES

1. [Vision Narrative et Principes de Conception](#1-vision-narrative-et-principes-de-conception)
2. [Cosmogonie et Chronologie Universelle](#2-cosmogonie-et-chronologie-universelle)
3. [Topographie et Level Design Narratif](#3-topographie-et-level-design-narratif)
4. [Écosystème Factionnel](#4-écosystème-factionnel)
5. [Profils des Personnages Non-Joueurs (PNJ)](#5-profils-des-personnages-non-joueurs-pnj)
6. [Bestiaire : Anatomie de la Corruption](#6-bestiaire--anatomie-de-la-corruption)
7. [Architecture des Quêtes](#7-architecture-des-quêtes)
8. [Ingénierie des Dialogues et Scripting](#8-ingénierie-des-dialogues-et-scripting)
9. [Systèmes d'Événements Dynamiques](#9-systèmes-dévénements-dynamiques)
10. [Direction Cinématographique](#10-direction-cinématographique)
11. [Spécifications Techniques IA (Horizon 2030)](#11-spécifications-techniques-ia-horizon-2030)
12. [Glossaire Technique et Narratif](#12-glossaire-technique-et-narratif)

---

## 1. VISION NARRATIVE ET PRINCIPES DE CONCEPTION

### 1.1. Logline du Projet
> *« Dans un monde où les dieux se sont tus, les hommes ont bâti des empires sur leurs cendres. Mais les cendres ne refroidissent jamais vraiment. »*

### 1.2. Philosophie de Narration (« Iceberg Storytelling »)
Aethon Chronicles rejette l'exposition massive (info-dumping). L'histoire est incrustée dans l'environnement et le gameplay.
- **10% de Visibilité (Prototype) :** Le joueur est confronté aux symptômes — un village isolé, une forêt gangrenée, une faune agressive.
- **90% Sous la Surface (Horizon) :** Chaque symptôme est la conséquence d'une mythologie systémique, encodée dans la base de données du monde.
- **Règle d'Or :** Les PNJ ne sont pas des encyclopédies. Ils ont des connaissances limitées, des biais, des peurs, et mentent parfois par omission.

---

## 2. COSMOGONIE ET CHRONOLOGIE UNIVERSELLE

### 2.1. L'Âge des Aethons (Ère I — Le Temps Mythique)
Les **Aethons** étaient des architectes de la réalité, façonnant le monde par la manipulation d'une matrice primordiale nommée le **Filament**. Ils scellèrent leurs protocoles de création dans des terminaux physiques appelés **Nexolithes**.

L'entité connue sous le nom de **Varek le Délieur** chercha à interagir avec le vide extérieur à la matrice (le Néant). Cette brèche introduisit **La Tache** (ou *Gangrène du Filament*), une corruption entropique. Les Aethons disparurent lors d'un événement cataclysmique visant à sceller la brèche, laissant leurs infrastructures à l'abandon.

### 2.2. L'Âge des Royaumes (Ère II — -3000 à -200 ans)
Émergence des civilisations mortelles (Humains, Sylvarins, Koraths) sur les ruines Aethons. Les Nexolithes furent considérées comme des artefacts magiques ou divins, provoquant l'ascension et la chute d'empires. La Tache, contenue, glissa dans le domaine du mythe et de la superstition religieuse.

### 2.3. L'Âge du Silence (Ère III — -200 ans à Aujourd'hui)
Une rupture systémique inconnue a fracturé le sceau originel. La Tache fuit lentement dans la topographie. La faune mute, la nécromancie spontanée apparaît, et les Nexolithes entrent en résonance. Les métropoles nient l'évidence pour préserver l'économie, abandonnant les périphéries sauvages à leur sort.

---

## 3. TOPOGRAPHIE ET LEVEL DESIGN NARRATIF

La progression géographique suit la progression de la corruption.

| Phase de Dév. | Identifiant de Zone | Niveau de Menace | Rôle Narratif |
| :--- | :--- | :---: | :--- |
| **Pré-Alpha** | Zone 00 : Village de Cendrecroix | Faible | Zone refuge (Hub), exposition initiale |
| **Pré-Alpha** | Zone 01 : Forêt de Varek | Moyen | Première zone de combat, introduction à la Tache |
| **Alpha** | Zone 02 : Ruines du Nexe de Sel | Élevé | Donjon d'exposition (Mécanique des Nexolithes) |
| **Alpha** | Zone 03 : Marécages de l'Oubli | Élevé | Zone de transition, factions cultistes |
| **Bêta** | Zone 04 : Cité de Port-Ardente | Hub Majeur | Géopolitique, Guilde des Marchands, corruption interne |
| **Bêta** | Zone 05 : Les Mines Profondes | Très Élevé | Tache concentrée, lore industriel |
| **Release 1.0** | Zone 06 : Plateau des Cendres | Extrême | Front final avant le centre de résonance |
| **Release 1.0** | Zone 07 : Citadelle du Délieur | Épique | Raid final (Varek) |

### 3.1. Zone 00 : Village de Cendrecroix (Hub Pré-Alpha)
- **Concept Visuel (Rétro PS2) :** Polygones anguleux, textures de bois granuleux, brouillard de distance proche, éclairage ambré statique évoquant un crépuscule éternel.
- **Lore Environnemental :** Construit sur les fondations d'un dôme Aethon calciné. Des fragments de roche noire luisante sont parfois visibles sous les pavés usés.
- **Fonction Level Design :** Zone sûre (Safe Zone). Aucun aggro ennemi. Présence des services vitaux (Quêtes, Vendeur, Respawn).

### 3.2. Zone 01 : Forêt de Varek (Zone de Combat Pré-Alpha)
- **Concept Visuel :** Arbres tortueux, canopée dense bloquant la lumière (éclairage zénithal filtré verdâtre). Spores noires (particules 2D) flottant dans l'air. Sols tachés de noir au fur et à mesure que le joueur s'enfonce vers le centre.
- **Lore Environnemental :** Épicentre local d'une fuite du Filament. La flore et la faune perdent leur identité structurelle.
- **Fonction Level Design :** Points d'étranglement (choke points) naturels via des racines géantes. Le centre abrite une arène naturelle (clairière de la Nexolithe).

---

## 4. ÉCOSYSTÈME FACTIONNEL

L'écosystème politique et spirituel dicte l'équilibrage du monde.

1. **Gardiens du Filament :** Vestiges d'un ordre savant. Dépositaires du savoir Aethon. Actuellement décimés, considérés comme des fanatiques ou des mendiants. (Alignement : Neutre/Restaurateur).
2. **Guilde des Marchands Libres :** Cartel économique régissant les échanges inter-cités. Ils favorisent le statu quo et ignorent volontairement la montée de la Tache si elle n'impacte pas les routes commerciales. (Alignement : Pragmatique).
3. **Le Conseil des Trois Cités :** Autorité gouvernementale. Bureaucratique, lente, dans un profond déni du danger systémique. (Alignement : Conservateur).
4. **Les Murmureurs :** Secte apocalyptique vénérant la Tache comme évolution naturelle. Ils accélèrent la corruption des Nexolithes. (Alignement : Antagoniste).
5. **Les Corrompus :** Entités biologiques dont le code génétique a été altéré par la Tache. Sans réelle volonté politique, mus par l'instinct pur. (Alignement : Menace environnementale).

---

## 5. PROFILS DES PERSONNAGES NON-JOUEURS (PNJ)

Les PNJ sont conçus pour supporter des arbres de dialogue scriptés (Prototype) et des agents conversationnels LLM (Horizon 2030).

### 5.1. PNJ-01 : Maren Asheld (Veuve et Chef du Village)
- **Archétype :** Donneur de Quête Principal.
- **Design Visuel :** Traits durs, regard las, tablier de laine. Animation d'attente (Idle) : s'essuie nerveusement les mains.
- **Motivation Principale :** Assurer la survie du village à tout prix.
- **Faille / Secret :** Elle sait que son mari disparu est devenu une créature de la Tache, mais a caché l'information pour éviter la panique (et la honte).
- **Intégration LLM (Variables d'état) :**
  ```json
  {
    "id": "npc_maren_01",
    "core_traits": ["pragmatique", "protectrice", "culpabilité_refoulée"],
    "knowledge_base": ["cendrecroix_history", "husband_fate", "basic_corruption"],
    "behavioral_rules": [
      "Never admit fear openly.",
      "Deflect questions about the husband until quest_01_complete == true.",
      "Focus on practical survival."
    ]
  }
  ```

### 5.2. PNJ-02 : Aldric Sorel (Marchand Itinérant)
- **Archétype :** Vendeur de consommables / Source de rumeurs.
- **Design Visuel :** Corpulent, manteau usé, assis sur un chariot à la roue volontairement non réparée.
- **Motivation Principale :** Sécurité personnelle et profit.
- **Faille / Secret :** Il possède un colis scellé illégal à destination de Port-Ardente, contenant un fragment corrompu. Il simule la panne de son chariot par terreur de traverser la Forêt.
- **Intégration LLM (Variables d'état) :**
  ```json
  {
    "id": "npc_aldric_01",
    "core_traits": ["loquace", "lâche", "opportuniste"],
    "knowledge_base": ["trade_routes", "port_ardente_politics", "merchant_guild_secrets"],
    "behavioral_rules": [
      "Talk too much to cover up nervousness.",
      "Downplay the threat of the forest.",
      "Deny the existence of the sealed package if asked."
    ]
  }
  ```

### 5.3. PNJ-03 : Torvyn l'Ancien (Ermite Aveugle)
- **Archétype :** Distributeur de Lore (Exposition diégétique) / Gardien déchu.
- **Design Visuel :** Mendiant en haillons, yeux blancs laiteux. Positionné à l'orée de la zone de danger.
- **Motivation Principale :** Transmettre le savoir avant la chute inévitable.
- **Faille / Secret :** A perdu la vue physique en manipulant une Nexolithe, mais a gagné une perception du réseau de Filament.
- **Intégration LLM (Variables d'état) :**
  ```json
  {
    "id": "npc_torvyn_01",
    "core_traits": ["cryptique", "résigné", "omniscient_mais_fragmenté"],
    "knowledge_base": ["aethon_lore", "the_stain_mechanics", "filament_network"],
    "behavioral_rules": [
      "Speak in metaphors related to threads, weaving, and light.",
      "Do not show surprise.",
      "Offer warnings, not commands."
    ]
  }
  ```

---

## 6. BESTIAIRE : ANATOMIE DE LA CORRUPTION

La Tache ne crée pas la vie, elle la parasite et la redéfinit.

### 6.1. Mob 01 : Rôdeur des Sous-Bois (Loup Corrompu)
- **Niveau d'Épuration :** Bas (Trash mob).
- **Physiologie :** Canidé dont le système pileux est remplacé par des filaments noirs. Un œil hypertrophié et décoloré.
- **Schéma de Comportement (IA basique) :** Patrouille locale (radius 5m). Aggro à vue (FOV 120°, 8m).
- **Mécanique de Combat :** Attaque en mêlée (DPS faible/moyen). Attaque spéciale : *Hurlement Entropique* (Immobilisation 1.5s, cooldown 12s).
- **Drop Table :** Griffe noircie (60%), Fourrure ternie (40%), Or (2-4).

### 6.2. Mob 02 : L'Effaré (Humanoïde Corrompu)
- **Niveau d'Épuration :** Moyen.
- **Physiologie :** Ancien bûcheron ou voyageur. Posture asymétrique, spasmes musculaires (signe d'une structure neurologique en conflit avec le parasite).
- **Schéma de Comportement :** Immobile ou errance aléatoire. Aggro de proximité sonore (rayon 6m).
- **Mécanique de Combat :** Coups lourds lents (Fort DPS physique, esquivable). Attaque spéciale : *Aura de Vide* (-30% de régénération de santé du joueur dans un rayon de 4m).
- **Drop Table :** Tissu corrompu (55%), Éclat de Tache (15%), Or (5-10).

### 6.3. Mini-Boss 01 : La Mère-Arbre
- **Niveau d'Épuration :** Élevé (Élite de zone).
- **Physiologie :** Fusion d'un chêne tricentenaire et d'un noyau de Tache pur. Les racines agissent comme des tentacules.
- **Schéma de Comportement :** Ancré au sol (immobile). Gère des zones d'effet (AoE).
- **Mécanique de Combat :**
  - Attaque basique : *Frappe de Racine* (renversement, cible unique).
  - Compétence de zone : *Nuage de Spores* (DoT constant si le joueur est à moins de 3m).
  - Phase Enragée (HP < 30%) : Vitesse d'attaque augmentée de 50%.
- **Drop Table :** Cœur-Tache (Objet de quête - 100%), Résine Corrompue (70%), Or (20-30).

---

## 7. ARCHITECTURE DES QUÊTES

Les quêtes sont implémentées via un système d'états (State Machine) avec des déclencheurs booléens clairs.

### 7.1. Quête Principale : Q_MAIN_01 — « Les Cicatrices du Bois » (Prototype)

**Contexte :** Le joueur doit purger la lisière de la forêt pour prouver sa valeur à Maren.
**Conditions de déclenchement :** Arrivée du joueur à Cendrecroix.

| Étape (State) | Objectif UI | Déclencheurs / Scripts (Conditions) |
| :--- | :--- | :--- |
| **0_Init** | *Parlez à Maren près de la fontaine.* | Dialogue `MAREN_01` validé. -> State = 1 |
| **1_Hunt** | *Abattez les Corrompus dans la Forêt de Varek (0/3).* | `kill_count_corrupted` >= 3. -> State = 2 |
| **2_Investigate** | *Cherchez la source de la corruption au centre de la forêt.* | Trigger box dans la Clairière du Nexe touchée. -> State = 3 |
| **3_Interact** | *Examinez l'artefact noirci.* | Interaction avec `obj_nexolithe`. Lancement de la *Cutscene 01*. Set `flag_husband_seen = true`. -> State = 4 |
| **4_Report** | *Retournez faire votre rapport à Maren.* | Dialogue `MAREN_02` validé. Checking `flag_husband_seen`. -> State = 5 (Complete) |

**Récompenses de Complétion :**
- Base : 150 XP, 25 Or, 3x Bandages de fortune.
- Bonus (Si `flag_husband_seen` est True) : +50 XP, Objet Lore "Fragment de Souvenir".

### 7.2. Pipeline de Quêtes Secondaires (Phase Alpha)

- **Q_SIDE_01 — « La Roue Cassée » (Aldric) :** Fedex (Collecte). Récupérer 5 "Débris Métalliques" en forêt (taux de drop : 30% sur Effarés). *Twist narratif : Ce ne sont pas des débris de chariot, mais des fragments d'armure Aethon.*
- **Q_SIDE_02 — « Fréquence Entropique » (Torvyn) :** Collecte Ciblée. Ramener de la Résine de Mère-Arbre. Débloque un passif de résistance mineure à la Tache.

---

## 8. INGÉNIERIE DES DIALOGUES ET SCRIPTING

### 8.1. Standards de Rédaction (Format PS2)
- **Contrainte UI :** Max 3 lignes par bulle de dialogue, max 60 caractères par ligne.
- **Absence de voix (Voice-over) :** Le sous-texte doit passer par la ponctuation et les animations d'attente.
- **Style :** Phrases courtes. Langage utilitaire. L'héroïsme est remplacé par le pragmatisme et la survie.

### 8.2. Script : Scène de Résolution (Q_MAIN_01, État 4)

**Condition A : Le joueur a exploré la Nexolithe (`flag_husband_seen == true`)**
> **JOUEUR :** "La forêt est purgée. Mais j'ai trouvé une pierre qui battait comme un cœur."
> **MAREN :** [Se fige. L'animation d'idle s'arrête.]
> **JOUEUR :** "Elle a projeté l'image d'un homme. Il disait votre nom."
> **MAREN :** "Il était... comment ?"
> **JOUEUR :** "Infecté. Mais il luttait."
> **MAREN :** "Je le savais. Pardonne-moi de t'avoir envoyé dans cette horreur sans te dire la vérité."
> **MAREN :** "Prends ceci. Et si tu le revois un jour... abrège ses souffrances."

**Condition B : Le joueur a ignoré l'exploration (`flag_husband_seen == false`)**
> **JOUEUR :** "Les créatures sont mortes. La lisière est sûre."
> **MAREN :** [Soupire. L'animation d'idle continue.]
> **MAREN :** "Pour un temps, au moins. Tu as du cran. Prends ta récompense."
> **MAREN :** "Tu n'as rien vu de... particulier au cœur des bois ?"
> **JOUEUR :** "Seulement des monstres."
> **MAREN :** "... C'est sans doute mieux ainsi."

---

## 9. SYSTÈMES D'ÉVÉNEMENTS DYNAMIQUES

Des systèmes serveurs génèrent de l'incertitude dans l'open world.

### 9.1. Assaut Nocturne (World Event Mineur)
- **Condition de déclenchement :** Cycle nuit (Serveur) & Population Zone 00 > 1.
- **Action :** Apparition de 3 points de spawn temporaires à la bordure Zone 00 / Zone 01.
- **Mécanique :** Les joueurs doivent empêcher 5 Rôdeurs d'atteindre le centre du village. Si succès : buff de zone (XP +5% pendant 1h).

### 9.2. Le Miasme de Varek (World Event Moyen - Bêta)
- **Condition de déclenchement :** Timer aléatoire (entre 4h et 8h d'intervalle).
- **Action :** Brouillard noir dense sur la Forêt de Varek. Portée de vue réduite de 70%.
- **Mécanique :** Les statistiques des créatures corrompues augmentent de +30%. Les chances de loot rare sont doublées.

---

## 10. DIRECTION CINÉMATOGRAPHIQUE

Les cinématiques sont rendues in-engine, avec des angles de caméra fixes (à la Resident Evil classique ou Metin2) pour souligner la nostalgie et alléger le réseau.

**Cutscene 01 : Contact avec le Filament (Quête Principale)**
- `CAMERA_01` : Gros plan sur la Nexolithe noire incrustée dans l'écorce.
- `AUDIO` : Battement de cœur basses fréquences, volume croissant.
- `ACTION` : Le personnage avance la main (Animation scriptée).
- `VFX` : Flash blanc saturant l'écran (Overbloom).
- `CAMERA_02` : Plan flou, filtre statique/VHS. Silhouette humanoïde vacillante dans l'obscurité.
- `TEXTE OVERLAY` : *"Maren... le fil... se rompt..."*
- `ACTION` : Retour immédiat au jeu normal (Gameplay Camera). Un debuff inoffensif "Désorientation" s'applique pendant 3 secondes.

---

## 11. SPÉCIFICATIONS TECHNIQUES IA (HORIZON 2030)

Pour assurer la transition d'un jeu classique vers un écosystème dirigé par l'IA (via MCP), le backend (Rust/Bevy) doit structurer l'environnement sémantique dès le prototype.

### 11.1. Architecture RAG (Retrieval-Augmented Generation) pour PNJ
Les données narratives sont injectées en tant que "Souvenirs" dans une base vectorielle (ex: Qdrant/Milvus).

**Pipeline d'exécution :**
1. **Événement Client :** Le joueur interagit avec Maren.
2. **Requête Serveur :** Envoi du contexte (Statut des quêtes, inventaire, réputation).
3. **Recherche Vectorielle (Retrieval) :** Requête vers la DB vectorielle : *"Quels sont les souvenirs de Maren concernant ce joueur et la quête de la forêt ?"*
4. **Prompting (Generation) :** Le LLM génère une ligne de dialogue dynamique via l'API.
5. **Validation :** Le serveur valide la cohérence de la réponse (Contraintes : Pas de hors-sujet, max 60 caractères) avant envoi au client.

### 11.2. Modèle de Contrat MCP (Extrait JSON pour intégration LLM)
```json
{
  "agent_id": "maren_asheld",
  "system_directive": "Act as Maren, a grim village leader in a dark medieval setting. Do not break character. Keep responses under 150 characters total.",
  "dynamic_context": {
    "world_state": "night_time, forest_corrupted",
    "player_relationship_score": 15,
    "last_player_action": "completed_quest_01_killed_corrupted_husband"
  },
  "retrieved_memories": [
    "The player discovered my husband's fate.",
    "I gave the player my husband's ring."
  ],
  "allowed_actions": ["trade", "give_info", "reject_conversation"]
}
```

---

## 12. GLOSSAIRE TECHNIQUE ET NARRATIF

- **Aethons :** Entités fondatrices (lore). Disparues.
- **Corrompus (Corrupted) :** Mob standard affecté par la Tache.
- **Filament :** Le code/matrice magique constituant l'univers.
- **La Tache (The Stain) :** Virus ontologique détruisant le Filament. Ennemis et boss.
- **MCP (Model Context Protocol) :** Technologie d'interface standardisée permettant aux IA de lire l'état du serveur et de dicter des actions en jeu.
- **Nexolithe :** Monolithe de stockage Aethon. Agit comme des "bornes wifi" magiques, souvent corrompues.
- **Varek le Délieur :** Le grand antagoniste historique. Responsable de la brèche originelle.

---
*Fin du Document LORE.md — Validation technique requise par l'équipe Backend (Rust) et Game Design.*
