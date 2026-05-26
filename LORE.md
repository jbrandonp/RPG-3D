# DOCUMENT DE CONCEPTION NARRATIVE (LORE.md)

| Propriété | Détail |
| :--- | :--- |
| **Projet** | ELARA'S BLACK MIST |
| **Statut** | Document de Travail (WIP) |
| **Version** | 3.1.0 |
| **Périmètre** | Prototype (Pré-Alpha) & Vision étendue (Horizon 2030) |

> **Avertissement :** Ce document est le point de référence central pour la direction narrative, la conception des personnages, la structure des quêtes et l'intégration des systèmes d'intelligence artificielle (MCP). Toute modification de l'univers de jeu doit être documentée ici pour assurer la cohérence entre le gameplay, la technique et l'histoire.

---

## TABLE DES MATIÈRES

1. [Vision Narrative et Principes de Conception](#1-vision-narrative-et-principes-de-conception)
2. [Structure du Récit (Plan en Arcs)](#2-structure-du-récit-plan-en-arcs)
3. [Cosmogonie et Chronologie Universelle](#3-cosmogonie-et-chronologie-universelle)
4. [Topographie et Level Design Narratif](#4-topographie-et-level-design-narratif)
5. [Écosystème Factionnel](#5-écosystème-factionnel)
6. [Profils des Personnages Non-Joueurs (PNJ)](#6-profils-des-personnages-non-joueurs-pnj)
7. [Bestiaire : Anatomie de la Corruption](#7-bestiaire--anatomie-de-la-corruption)
8. [Architecture des Quêtes](#8-architecture-des-quêtes)
9. [Ingénierie des Dialogues et Scripting](#9-ingénierie-des-dialogues-et-scripting)
10. [Systèmes d'Événements Dynamiques](#10-systèmes-dévénements-dynamiques)
11. [Direction Cinématographique](#11-direction-cinématographique)
12. [Spécifications Techniques IA (Horizon 2030)](#12-spécifications-techniques-ia-horizon-2030)
13. [Glossaire Technique et Narratif](#13-glossaire-technique-et-narratif)

---

## 1. VISION NARRATIVE ET PRINCIPES DE CONCEPTION

### 1.1. Logline du Projet
> *« L'histoire est racontée comme un cauchemar réaliste et interactif où un jeu vidéo est devenu une prison mortelle et un enfer médiéval. L'espoir est une illusion. »*

### 1.2. Ton et Atmosphère
Extrêmement sombre, gritty, déprimant, avec très peu d’espoir. Le viol, la trahison, la souffrance et la mort sont courants. Mais il y a une mince couche de "game mechanics" (notifications RPG) qui donne un faux sentiment de contrôle.
- **Point de Vue (POV) :** Troisième personne limitée, strictement collée à **Elara Voss**.
- **Style d'Écriture :** Cru, réaliste. Phrases courtes dans l'action, longues et sensorielles pour décrire le traumatisme. Pas de métaphores fleuries ou de fanservice gratuit.

### 1.3. Thèmes Majeurs
L'impuissance face à un monde cruel, la transformation (de fille fragile à monstrueuse pour survivre), le prix du pouvoir, le traumatisme et la vengeance obsessionnelle, la fausse nature des jeux vidéo, et le choix moral entre fuir ou dominer un monde pourri.

---

## 2. STRUCTURE DU RÉCIT (PLAN EN ARCS)

**Arc 0 – Prologue (Inciting Incident)**
Elara se connecte pour une dernière session à *Eternal Realms*. Fusion du monde. Elle se réveille nue/faible dans les ruines de Syphralis, fuyant le Brouillard Noir avec des milliers de réfugiés vers Velnor. Première rencontre traumatisante.

**Arc 1 – La Survie en Ville (LonaRPG pur)**
Arrivée à Velnor (surpeuplée, famine, gangs, prostitution, esclavage). Mécaniques de survie basiques : quêtes bas niveau, prostitution forcée/choisie. Rencontres avec Big Mama, Cocona, Rhea Vossler.

**Arc 2 – La Chasse aux Gobelins (Goblin Slayer influence forte)**
Elara développe une haine viscérale après un viol/gangbang par des goblins. Elle forme un petit groupe pour exterminer systématiquement les nids de Goblinoïds (pièges, poison, feu).

**Arc 3 – L’Ascension**
Elle gagne des niveaux rapidement grâce à son statut de "Player". Rencontre avec l'Overlord Kazuki. Choix : s'allier avec lui, le combattre, ou devenir elle-même une Dark Lady.

**Arc 4 – La Guerre de l’Île**
Invasion massive (Goblinoïds + Deep Ones + Abominations). Siège de Velnor. Choix : fuir égoïstement, sauver des gens, ou conquérir l'île.

**Arc 5 – Climax & Endings**
Multiples fins amères : Fuite heureuse mais chute de l'île ; Bad Ends (esclave, mort, abomination) ; Overlord End ; Sacrifice End ; Goblin Slayer End (vie dédiée à la vengeance).

---

## 3. COSMOGONIE ET CHRONOLOGIE UNIVERSELLE

### 3.1. Entités Primordiales
Du Vide Éternel naquirent trois entités :
1. **Justice (Le Dieu Mort) :** Le créateur initial, forgea les lois physiques. Disparu/endormi.
2. **The Crimson Mother :** Déesse corrompue de la fertilité, de la chair et de la folie. Mère des Goblinoïds et abominations.
3. **The Architect :** Force abstraite représentant l'ordre, créateur du VRMMO *Eternal Realms*.

### 3.2. Chronologie Universelle
- **Ère Primordiale (An 0 – 800) :** Création. La Crimson Mother répand ses enfants. Guerre Deep Ones vs Abominations.
- **Ère des Saints (An 1321 – 1500) :** Apparition des Six Saints (artefacts divins). Fondation de Syphralis.
- **Ère de la Colonisation (An 1550 – 1700) :** Colons d'Ingeland. Victoire sur les Deep Ones. Fondation de Velnor.
- **Ère du Brouillard (An 1771 – Aujourd'hui) :** La Crimson Mother trébuche face à "l'Enfant". Syphralis détruite. Naissance officielle du **Brouillard Noir**.
- **Ère des Joueurs (An 2138 / Fusion) :** Fin d'Eternal Realms. Le jeu fusionne avec la réalité. Kazuki devient le Lich Overlord.
- **Début 1772 :** Elara se réveille niveau 1. L'île est un hybride maudit médiéval/lovefcraftien/RPG.

---

## 4. TOPOGRAPHIE ET LEVEL DESIGN NARRATIF

L’île de **Velnora** (180x90 km) ressemble à une main brisée. Le Brouillard Noir progresse du Nord-Est vers le Sud-Ouest.

| Zone | Niveau | Danger | Contenu Narratif / Monstres |
| :--- | :--- | :--- | :--- |
| **Velnor (Slums & Docks)** | 1–10 | Faible/Moyen | Survie urbaine, petits jobs. *Rats, bandits, goblins isolés.* |
| **Plaines de Velnor & Marais** | 8–18 | Moyen | Transition & premiers vrais combats. *Meutes goblins, loups.* |
| **Forêt des Murmures** | 15–30 | Élevé | Arc "Goblin Slayer", nids. *Goblinoïds, araignées.* |
| **Montagnes Brisées** | 25–40 | Très élevé | Ascension, artefacts. *Orcs organisés, trolls.* |
| **Falaises d'Argent** | 30-50 | Très élevé | Quêtes marines. *Deep Ones (Fishmen).* |
| **Syphralis Ruines** | 35–55 | Extrême | Climax lovecraftien, point zéro du Brouillard. *Abominations.* |
| **Sanctuaire des Ossements**| 40+ | Variable | Forteresse de l'Overlord. Choix politiques. *Non-morts.* |

---

## 5. ÉCOSYSTÈME FACTIONNEL

### 5.1. Factions Humaines (Fragiles et désunies)
- **Le Conseil de Velnor :** Gouvernement corrompu (Lord Regent Harlan Voss).
- **La Guilde des Mercenaires (Iron Shields) :** Protègent contre récompense (Captain Rhea Vossler).
- **Les Cultistes de la Crimson Mother :** Humains corrompus (La Prophétesse Sanglante).

### 5.2. Factions Monstrueuses (Dominantes)
- **La Horde des Goblinoïds :** L'ennemi principal (Grukk le Briseur). Extrêmement prolifiques et sadiques.
- **Les Deep Ones :** Créatures aquatiques voulant reprendre l'île (La Sea Witch).
- **Les Abominations du Brouillard :** Serviteurs sans leader fixe de la Crimson Mother.

### 5.3. Factions Transcendantes
- **Le Sanctuaire des Ossements :** Empire de l'Overlord Kazuki. Non-morts et joueurs.
- **Les Joueurs Indépendants ("Les Élus") :** Survivants du monde réel aux capacités RPG.
- **La Voix de la Fortune :** Entité neutre prophétisant la chute de l'île.

---

## 6. PROFILS DES PERSONNAGES NON-JOUEURS (PNJ)

**Protagoniste : Elara Voss (25 ans).** Avatar faible, passe de timide et terrifiée à froide et obsédée.

**PNJ Majeurs :**
1. **Kazuki / Ainzuloth (Overlord) :** Ancien guild master japonais, devenu Lich (niv 80+). Calme, manipulateur, roi du Sanctuaire des Ossements.
2. **La Voix de la Fortune :** Oracle cynique, femme aux yeux bandés, entourée de brume.
3. **Captain Edward "The Last Ship" :** Capitaine vénal mais pragmatique (demande 25 pièces d'or pour quitter l'île).

**PNJ de Velnor :**
4. **Rhea "Iron Bitch" Vossler :** Leader des Iron Shields, méprisante des faibles.
5. **Lord Regent Harlan Voss :** Chef corrompu de Velnor.
6. **Cocona Vale :** Réfugiée innocente, amie d'Elara (très vulnérable).
7. **Big Mama (Griselda) :** Tenancière de bordel / receleuse / nécromancienne mineure.

**Antagonistes :**
8. **Grand Chef Grukk le Briseur :** Hobgoblin colossal, roi de la Horde. Obsédé par la reproduction.
9. **La Prophétesse Sanglante (Sylvara) :** Leader folle des Cultistes.
10. **La Sea Witch :** Maîtresse des Deep Ones.

**PNJ Secondaires :**
- **Elise :** Prêtresse traumatisée.
- **Thorn :** Orc renégat.
- **Mira :** Voleuse des slums.
- **Leroy "Jenkins" :** Guerrier légendaire souvent saoul.

---

## 7. BESTIAIRE : ANATOMIE DE LA CORRUPTION

### 7.1. Goblinoïds (La Plaie Vivante)
- **Goblin (Lvl 3-12) :** Lâches en solo, sadiques en meute. Capturent pour reproduction. Gestation 3 semaines.
- **Hobgoblin (Lvl 12-25) :** Chefs territoriaux, brutaux.
- **Orc / Orkinds (Lvl 18-35) :** Massifs, très forts, engendrent des hybrides.
- **Ogre (Lvl 30-45) :** Brutes gigantesques.
- **Goblin Champion (Lvl 40+) :** Boss de nid.

### 7.2. Créatures du Brouillard & Abominations
- **Corrompu / Mist Walker (Lvl 10-30) :** Mutants infectant par contact.
- **Fleshspawn (Lvl 25-50) :** Amas de chair cherchant la fécondation.
- **Crimson Horror (Lvl 55+) :** Tentaculaire géant.

### 7.3. Deep Ones
- **Fishman (Lvl 15-35) :** Intelligents, peuvent s'hybrider.
- **Sirène Corrompue (Lvl 20-40) :** Chanteuses carnivores.

### 7.4. Non-Morts & Divers
- **Skeleton Warrior (Lvl 15-30) & Death Knight (Lvl 40-60) :** Serviteurs de l'Overlord.
- **Giant Rat (Lvl 2-8), Dire Wolf (Lvl 10-20), Arachne (Lvl 20-35).**

### 7.5. Boss Majeurs
- Grukk le Briseur, La Sea Witch, The Crimson Matriarch, Ainzuloth (si hostile), The Black Mist Heart (Lvl 70+).

---

## 8. ARCHITECTURE DES QUÊTES

Les quêtes utilisent la machine d'état du serveur (State Machine), avec des embranchements narratifs sombres (violences, échecs).

### 8.1. Quête Principale (Prototype) : Q_MAIN_SURVIVAL — « Le Prix du Sang »
**Contexte :** Elara doit amasser de l'or dans les Slums pour survivre, ce qui mène à son premier traumatisme majeur.

| Étape (State) | Objectif UI | Déclencheurs / Scripts (Conditions) |
| :--- | :--- | :--- |
| **0_Init** | *Trouvez un moyen de gagner de l'or.* | Arrivée dans les Slums de Velnor. -> State = 1 |
| **1_Job** | *Effectuez des tâches pour Big Mama.* | `gold_earned` >= 5. -> State = 2 |
| **2_Ambush** | *Livrez le paquet dans la ruelle sombre.* | Trigger box ruelle touchée. Spawn de 3 Goblins. -> State = 3 |
| **3_Trauma** | *Survivez (ou subissez).* | Si HP tombe à 0 : Lancement *Cutscene_Trauma_01*. Set `trauma_level += 1`. -> State = 4 |
| **4_WakeUp** | *Relevez-vous.* | Interaction avec l'environnement. Débloque *Rage Froide*. -> State = 5 (Complete) |

---

## 9. INGÉNIERIE DES DIALOGUES ET SCRIPTING

### 9.1. Standards de Rédaction (Format PS2 revisité)
- **Contrainte UI :** Max 3 lignes par bulle, 60 caractères par ligne.
- **Style :** Cru, direct. Pas de métaphores héroïques. Les notifications RPG (système) sont affichées comme des dialogues glacials.

### 9.2. Script : Scène de Rencontre (Kazuki & Elara)
> **KAZUKI :** "Une survivante. Niveau 34. Ta progression est... statistiquement improbable."
> **ELARA :** [Reste silencieuse. Main sur son arme.]
> **KAZUKI :** "Baisse cette dague. Si je voulais ta mort, le système l'aurait déjà actée."
> **SYSTEM_UI :** *[Alerte : Différence de niveau mortelle. Fuite recommandée.]*
> **KAZUKI :** "Tu massacres les goblins avec une efficacité pathologique. Sers-moi, et je t'offrirai leur extinction."

---

## 10. SYSTÈMES D'ÉVÉNEMENTS DYNAMIQUES

### 10.1. Événements Quotidiens / Fréquents
- **Raid Goblin :** Nuit. 15-40 goblins attaquent les Slums. Risque d'enlèvement.
- **Avancée du Brouillard Noir :** L'horloge narrative globale. Le brouillard avance de 200-800m.
- **Émeute de la Faim :** Pillage des entrepôts à Velnor.

### 10.2. Événements Hebdomadaires / Mensuels
- **Grande Migration Goblin :** Déplacement de milliers d'individus créant de nouveaux nids.
- **Festival du Désespoir :** Marché noir, prostitution massive, apparitions de la Voix de la Fortune.
- **Incursion des Deep Ones :** Enlèvements sur les côtes.

### 10.3. Événements Majeurs & Endgame
- **Surge du Brouillard :** Explosion recouvrant l'île. Spawn massif d'Abominations.
- **Siège de Velnor :** Alliance monstrueuse contre la ville (Endgame).
- **Le Dernier Bateau :** Edward annonce ses derniers voyages. Pression maximale.

### 10.4. Événements Personnels (Elara)
- **Traumatisme Collectif :** Flashback (mode Berserk).
- **Grossesse Forcée :** Capture prolongée menant à une potentielle mécanique de *Rebirth*.

---

## 11. DIRECTION CINÉMATOGRAPHIQUE

Caméras fixes et angles oppressants pour accentuer la vulnérabilité (Style PS2/Metin2).

**Cutscene : La Diseuse de Bonne Aventure**
- `CAMERA_01` : Plan en contre-plongée sur Elara marchant dans la boue.
- `AUDIO` : Bruits de pluie et respiration lourde.
- `VFX` : Apparition progressive de brume aux pieds.
- `CAMERA_02` : Gros plan sur le visage de la Diseuse de Bonne Aventure, yeux bandés.
- `TEXTE OVERLAY` : *"Peu importe tes choix, petite fille... l'île finit toujours par gagner."*
- `ACTION` : Disparition en un cut (fade to black rapide).

---

## 12. SPÉCIFICATIONS TECHNIQUES IA (HORIZON 2030)

Le backend Rust/Bevy utilise le MCP (Model Context Protocol) et le RAG (Retrieval-Augmented Generation) pour donner vie au monde oppressant.

### 12.1. Modèle de Contrat MCP pour l'Overlord (Exemple Kazuki)
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

## 13. GLOSSAIRE TECHNIQUE ET NARRATIF

- **Brouillard Noir (Black Mist) :** La corruption vivante issue de la fusion du jeu et de la Crimson Mother.
- **Élus (Players) :** Humains du monde réel coincés dans le jeu (Elara, Kazuki).
- **MCP :** Model Context Protocol, utilisé pour dynamiser les IA narratrices via LLM.
- **Rebirth :** Mécanique de mort hybride : une joueuse mourant en couche renaît avec les traits de la race paternelle.
- **Sanctuaire des Ossements :** Capitale imprenable de l'Overlord au centre de l'île.
- **Velnora :** L'île continentale, dernier bastion de l'humanité, lentement dévorée.

---
*Fin du Document LORE.md — Validation technique requise par l'équipe Backend et Game Design.*
