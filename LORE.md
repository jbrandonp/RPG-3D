# DOCUMENT DE CONCEPTION NARRATIVE (LORE.md)

| Propriété | Détail |
| :--- | :--- |
| **Projet** | ELARA'S BLACK MIST |
| **Statut** | Document de Travail (WIP) |
| **Version** | 3.0.0 |
| **Périmètre** | Prototype (Pré-Alpha) & Vision étendue (Horizon 2030) |

> **Avertissement :** Ce document est le point de référence central pour la direction narrative, la conception des personnages, la structure des quêtes et l'intégration des systèmes d'intelligence artificielle (MCP). Toute modification de l'univers de jeu doit être documentée ici pour assurer la cohérence entre le gameplay, la technique et l'histoire. Le ton de ce projet est **extrêmement sombre, nihiliste et cru**.

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
> *« L'histoire est racontée comme un cauchemar réaliste et interactif où un jeu vidéo est devenu une prison mortelle et un enfer médiéval. L'espoir est une illusion. »*

### 1.2. Philosophie de Narration (Ton & Atmosphère)
Le ton principal est **nihiliste, cru, oppressant et désespéré**. C’est un mélange viscéral entre la vulnérabilité extrême, la brutalité obsessionnelle, la solitude existentielle et l’ascension sombre.
- **Point de Vue (POV) :** Troisième personne limitée, strictement collée à **Elara Voss**.
- **Narration Technique :** Utilisation occasionnelle de mécaniques de jeu (ex. : *« Niveau 7 atteint. Compétence [Résistance à la Douleur] débloquée. »*) pour rappeler la nature VRMMO du monde. Ces notifications deviennent de plus en plus froides et ironiques.

---

## 2. COSMOGONIE ET CHRONOLOGIE UNIVERSELLE

### 2.1. L'Origine
Au commencement existait uniquement **le Vide Éternel**, dont naquirent trois entités :
1. **Justice (Le Dieu Mort) :** Créateur des lois physiques, aujourd'hui disparu ou endormi.
2. **The Crimson Mother :** Déesse de la fertilité corrompue, de la chair et de la folie. Mère des abominations et des Goblinoïds.
3. **The Architect :** Force abstraite de l'ordre, responsable du cadre du VRMMO *Eternal Realms*.

### 2.2. Le Grand Accident Cosmique (La Fusion)
Il y a environ 600 ans (in-game), la Crimson Mother tenta de créer un enfant transcendant, ce qui échoua et créa une faille. Cette faille permit à **Eternal Realms** (créé en 2138 dans le monde réel) de fusionner avec cet univers. Ainsi naquit le **Brouillard Noir (Black Mist)**, à la fois chair avortée divine et bug ultime du système.

### 2.3. Chronologie Récente
- **Dernier jour des serveurs (2138) :** Fusion définitive. Les joueurs piégés (dont Elara) deviennent des "Élus" avec des capacités RPG. Kazuki devient le Lich Overlord.
- **Début 1772 :** Elara se réveille, niveau 1, dans les ruines de Syphralis. Le Brouillard Noir s'étend inexorablement vers Velnor.

---

## 3. TOPOGRAPHIE ET LEVEL DESIGN NARRATIF

L’île de **Velnora** est une grande île (180x90 km) ressemblant à une main brisée. Le Level Design suit une progression de MMORPG organique, mais chaque avancée exige un coût narratif lourd.

| Zone | Niveau | Danger | Rôle Narratif / Monstres |
| :--- | :--- | :--- | :--- |
| **Velnor (Slums & Docks)** | 1–10 | Faible/Moyen | Survie urbaine, prostitution, vols. *Rats, bandits, goblins isolés.* |
| **Plaines & Marais** | 8–18 | Moyen | Premiers combats & traumatismes. *Meutes de goblins, loups mutants.* |
| **Forêt des Murmures** | 15–30 | Élevé | Arc d'extermination. Nids de goblins. *Goblinoïds, araignées.* |
| **Syphralis Ruines** | 35–55 | Extrême | Point zéro du Brouillard. Climax lovecraftien. *Abominations.* |
| **Sanctuaire des Ossements**| 40+ | Variable | Forteresse de l'Overlord. Choix moraux, politique. *Non-morts.* |

---

## 4. ÉCOSYSTÈME FACTIONNEL

### 4.1. Factions Humaines (Fragiles)
- **Le Conseil de Velnor :** Gouvernement corrompu (Lord Regent Harlan Voss). Voit les réfugiés comme de la chair à canon.
- **La Guilde des Mercenaires (Iron Shields) :** Dirigée par Rhea "Iron Bitch" Vossler. Protège contre récompense.
- **Les Cultistes de la Crimson Mother :** Vénèrent le Brouillard et cherchent à le répandre.

### 4.2. Factions Monstrueuses (Dominantes)
- **La Horde des Goblinoïds :** L'ennemi principal. Dirigée par Grukk le Briseur. Très prolifiques, utilisent le viol pour se reproduire massivement.
- **Les Deep Ones :** Créatures aquatiques voulant reprendre l'île.
- **Abominations du Brouillard :** Mutations directes de la Crimson Mother.

### 4.3. Factions Transcendantes
- **Sanctuaire des Ossements :** L'empire de Kazuki (Overlord). La force la plus organisée.
- **La Voix de la Fortune :** Entité neutre prophétisant le malheur.

---

## 5. PROFILS DES PERSONNAGES NON-JOUEURS (PNJ)

- **Elara Voss (Protagoniste) :** Joueuse coincée dans son avatar niveau 1. Passe de victime terrifiée à chasseresse froide.
- **Kazuki / Ainzuloth :** Ancien joueur japonais devenu Lich Overlord. Intelligent, manipulateur, roi du Sanctuaire des Ossements.
- **La Voix de la Fortune :** Narratrice cynique, oracle.
- **Captain Edward :** Capitaine pragmatique du seul navire pouvant quitter l'île. Demande 25 pièces d'or.
- **Cocona Vale :** Réfugiée innocente, amie d'Elara (haut risque de mort/capture).

---

## 6. BESTIAIRE : ANATOMIE DE LA CORRUPTION

### 6.1. Goblinoïds (La Menace Principale)
- **Goblin (Lvl 3-12) :** Lâches en solo, destructeurs en meute. Obsédés par la reproduction. Attaquent en priorité les femmes.
- **Hobgoblin (Lvl 12-25) :** Plus grands, brutaux, chefs de meute.
- **Orc (Lvl 18-35) :** Massifs, extrêmement violents, forte libido. Engendrent des demi-orcs.

### 6.2. Abominations (Créatures du Brouillard)
- **Corrompu / Mist Walker (Lvl 10-30) :** Mutants infectant par contact ou morsure.
- **Fleshspawn (Lvl 25-50) :** Amas de chair cherchant à féconder ou être fécondés.

### 6.3. Autres
- **Deep Ones (Fishmen) :** Intelligents, peuvent s'hybrider avec les humains.
- **Death Knight (Lvl 40-60) :** Élites de l'Overlord Kazuki.

---

## 7. ARCHITECTURE DES QUÊTES

Les quêtes utilisent toujours la machine d'état du serveur (State Machine), mais avec des embranchements narratifs sombres.

### 7.1. Quête Principale : Q_MAIN_SURVIVAL — « Le Prix du Sang »
**Contexte :** Elara doit amasser de l'or dans les Slums pour survivre, ce qui mène à son premier traumatisme.

| Étape (State) | Objectif UI | Déclencheurs / Scripts (Conditions) |
| :--- | :--- | :--- |
| **0_Init** | *Trouvez un moyen de gagner de l'or.* | Arrivée dans les Slums de Velnor. -> State = 1 |
| **1_Job** | *Effectuez des tâches pour Big Mama.* | `gold_earned` >= 5. -> State = 2 |
| **2_Ambush** | *Livrez le paquet dans la ruelle sombre.* | Trigger box ruelle touchée. Spawn de 3 Goblins. -> State = 3 |
| **3_Trauma** | *Survivez (ou subissez).* | Si HP tombe à 0 : Lancement *Cutscene_Trauma_01*. Set `trauma_level += 1`. -> State = 4 |
| **4_WakeUp** | *Relevez-vous.* | Interaction avec l'environnement. Débloque *Rage Froide*. -> State = 5 (Complete) |

---

## 8. INGÉNIERIE DES DIALOGUES ET SCRIPTING

### 8.1. Standards de Rédaction (Format PS2 revisité)
- **Contrainte UI :** Max 3 lignes par bulle.
- **Style :** Cru, direct. Pas de métaphores héroïques. Les notifications RPG (système) sont affichées comme des dialogues glacials.

### 8.2. Script : Scène de Rencontre (Kazuki & Elara)
**Condition : Elara entre dans la salle du trône du Sanctuaire.**
> **KAZUKI :** "Une survivante. Niveau 34. Ta progression est... statistiquement improbable."
> **ELARA :** [Reste silencieuse. Main sur son arme.]
> **KAZUKI :** "Baisse cette dague. Si je voulais ta mort, le système l'aurait déjà actée."
> **SYSTEM_UI :** *[Alerte : Différence de niveau mortelle. Fuite recommandée.]*
> **KAZUKI :** "Tu massacres les goblins avec une efficacité pathologique. Sers-moi, et je t'offrirai leur extinction."

---

## 9. SYSTÈMES D'ÉVÉNEMENTS DYNAMIQUES

### 9.1. Raid Goblin (Événement Fréquent)
- **Condition :** Cycle nuit, dans Velnor Slums ou Plaines.
- **Action :** Spawn de 15 à 40 Goblins.
- **Mécanique :** Les PNJ peuvent mourir définitivement ou être enlevés. Augmente le compteur de terreur de la ville.

### 9.2. Avancée du Brouillard Noir (Horloge Narrative)
- **Condition :** Basé sur le temps de jeu serveur (ex: chaque mois in-game).
- **Mécanique :** Le brouillard avance de 500m. Les stats des ennemis dans cette zone sont buffées. Les quêtes non terminées dans la zone engloutie échouent définitivement.

---

## 10. DIRECTION CINÉMATOGRAPHIQUE

Caméras fixes et angles oppressants pour accentuer la vulnérabilité, respectant les contraintes PS2.

**Cutscene : La Diseuse de Bonne Aventure**
- `CAMERA_01` : Plan en contre-plongée sur Elara marchant dans la boue.
- `AUDIO` : Bruits de pluie et respiration lourde.
- `VFX` : Apparition progressive de brume aux pieds.
- `CAMERA_02` : Gros plan sur le visage de la Diseuse de Bonne Aventure, yeux bandés.
- `TEXTE OVERLAY` : *"Peu importe tes choix, petite fille... l'île finit toujours par gagner."*
- `ACTION` : Disparition en un cut (fade to black rapide).

---

## 11. SPÉCIFICATIONS TECHNIQUES IA (HORIZON 2030)

Le backend Rust/Bevy utilise le MCP (Model Context Protocol) pour donner vie au monde oppressant.

### 11.1. Modèle de Contrat MCP pour l'Overlord (Exemple Kazuki)
```json
{
  "agent_id": "kazuki_overlord",
  "system_directive": "Act as Kazuki (Ainzuloth), a 400-year-old Lich Overlord who used to be a Japanese gamer. You are extremely intelligent, politely cold, and view the world through RPG mechanics and statistics. Do not show empathy.",
  "dynamic_context": {
    "world_state": "mist_advancing, goblin_horde_active",
    "player_stats": {
      "level": 34,
      "corruption_level": 45,
      "trauma_level": 80
    },
    "last_player_action": "massacred_goblin_nest_03"
  },
  "retrieved_memories": [
    "The player refused my first offer of alliance.",
    "The player uses poison and fire extensively against goblins."
  ],
  "allowed_actions": ["offer_pact", "cast_intimidation", "reveal_lore"]
}
```

---

## 12. GLOSSAIRE TECHNIQUE ET NARRATIF

- **Brouillard Noir (Black Mist) :** La corruption vivante issue de la fusion du jeu et de la Crimson Mother.
- **Élus (Players) :** Humains du monde réel coincés dans le jeu (Elara, Kazuki).
- **MCP :** Model Context Protocol, utilisé pour dynamiser les IA (comme Kazuki ou la Diseuse).
- **Rebirth :** Mécanique de mort où une joueuse enceinte renaît avec les traits de la race du père de l'enfant.
- **Sanctuaire des Ossements :** Capitale de l'Overlord au centre de l'île.

---
*Fin du Document LORE.md — Validation technique requise par l'équipe Backend et Game Design.*
