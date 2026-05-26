# DOCUMENT DE CONCEPTION NARRATIVE (LORE.md)

| Propriété | Détail |
| :--- | :--- |
| **Projet** | ELARA'S BLACK MIST |
| **Statut** | Document de Travail (WIP) |
| **Version** | 3.2.0 |
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
Le ton principal est **nihiliste, cru, oppressant et désespéré**, avec des moments très rares de beauté ou d’espoir qui sont immédiatement brisés. C’est un mélange viscéral entre la vulnérabilité extrême, la brutalité obsessionnelle, la solitude existentielle et l’ascension sombre. Le monde lui-même semble vivant et hostile. Le viol, la trahison, la souffrance et la mort sont courants. Mais il y a une mince couche de "game mechanics" (notifications RPG) qui donne un faux sentiment de contrôle.

### 1.3. Point de Vue et Style
- **Point de Vue (POV) :** Troisième personne limitée, strictement collée à **Elara Voss**.
- **Style d'Écriture :** Cru, direct. Phrases courtes et percutantes dans l'action. Descriptions longues et sensorielles pour la souffrance ou l'environnement (odeur du sang, sensation du Brouillard Noir). Pas de métaphores fleuries.
- **Narration Technique :** Utilisation occasionnelle de mécaniques de jeu (ex. : *« Niveau 7 atteint. Compétence [Résistance à la Douleur] débloquée. »*) pour rappeler que c'est un ancien jeu. Ces notifications deviennent de plus en plus froides et ironiques.

### 1.4. Thèmes Majeurs
- L’impuissance face à un monde cruel.
- La transformation : comment une fille fragile devient monstrueuse pour survivre.
- Le prix du pouvoir.
- Le traumatisme et la vengeance obsessionnelle.
- La fausse nature des jeux vidéo : ce qui était "juste un jeu" est réel.
- Vaut-il mieux fuir ou dominer un monde pourri ?

---

## 2. STRUCTURE DU RÉCIT (PLAN EN ARCS)

**Arc 0 – Prologue (Inciting Incident)**
Elara se connecte pour une dernière session à *Eternal Realms*. Fusion du monde. Elle se réveille nue/faible dans les ruines de Syphralis, fuyant le Brouillard Noir avec des milliers de réfugiés vers Velnor. Première rencontre traumatisante avec des Goblinoïds. Première mort et humiliation.

**Arc 1 – La Survie en Ville (La Proie)**
Arrivée à Velnor : surpeuplée, famine, gangs, prostitution, esclavage. Focus sur la survie quotidienne : quêtes bas niveau, prostitution forcée ou choisie, petits boulots dangereux. Rencontres avec Big Mama, Cocona, le Capitaine Edward.

**Arc 2 – La Chasse aux Gobelins (La Chasseresse)**
Elara développe une haine viscérale après un viol/gangbang par des goblins. Elle bascule et devient obsédée par l'extermination des nids de Goblinoïds (pièges, poison, feu).

**Arc 3 – L’Ascension**
Elle accumule du pouvoir et gagne des niveaux grâce à son statut de "Player". Découverte que l'Overlord Ainz-like (Kazuki) règne sur le centre de l'île. Choix : s'allier, manipuler, confronter, ou devenir elle-même une Dark Lady.

**Arc 4 – La Guerre de l’Île (La Souveraine ou la Fugitive)**
Invasion massive des Goblinoïds, Deep Ones et Abominations. Siège de Velnor. Elara doit choisir : fuir égoïstement, sauver des gens, ou conquérir l'île.

**Arc 5 – Climax & Endings**
Multiples fins amères :
- **Fuite "heureuse" :** Elle s'échappe, mais l'île chute totalement.
- **Bad Ends :** Esclave éternelle, morte en couche, transformée en abomination.
- **Overlord End :** Elle devient la souveraine sombre.
- **Sacrifice End :** Détruit le cœur du Brouillard Noir mais meurt.
- **Goblin Slayer End :** Passe sa vie à tuer des goblins, brisée à jamais.

---

## 3. COSMOGONIE ET CHRONOLOGIE UNIVERSELLE

### 3.1. Entités Primordiales
Du Vide Éternel naquirent trois entités :
1. **Justice (Le Dieu Mort) :** Créateur des lois physiques et de la réalité. Endormi ou mort. Il créa les Deep Ones et les humains.
2. **The Crimson Mother :** Déesse de la fertilité corrompue, de la chair et de la folie. Mère des Goblinoïds et abominations.
3. **The Architect :** Force abstraite représentant l'ordre, créateur du VRMMO *Eternal Realms* des millénaires plus tard.

### 3.2. Chronologie Universelle
- **Ère Primordiale (An 0 – 800) :** Création. La Crimson Mother répand ses enfants (Goblinoïds). Guerre Deep Ones vs Abominations.
- **Ère des Saints (An 1321 – 1500) :** Apparition des Six Saints. Fondation de Syphralis.
- **Ère de la Colonisation (An 1550 – 1700) :** Colons d'Ingeland. Victoire sur les Deep Ones grâce à un héros légendaire ("Leroy Jenkins"). Fondation de Velnor.
- **Ère du Brouillard (An 1771 – Aujourd'hui) :** La Crimson Mother trébuche face à "l'Enfant". Destruction de Syphralis. Naissance officielle du **Brouillard Noir**.
- **Ère des Joueurs (An 2138 / Fusion) :** Fin d'Eternal Realms. Le jeu fusionne avec la réalité. Kazuki devient le Lich Overlord.
- **Début 1772 :** Elara se réveille niveau 1. Le Brouillard s'étend. L'île est un piège mortel.

---

## 4. TOPOGRAPHIE ET LEVEL DESIGN NARRATIF

L’île de **Velnora** (180x90 km) ressemble à une main brisée. Le Brouillard Noir agit comme une **horloge narrative**, progressant et forçant Elara à avancer.

### 4.1. Carte de l'Île
- **Nord-Est :** Syphralis (Ruines Écarlates), Cradle of the Crimson Mother. (Point zéro, danger extrême).
- **Centre :** Sanctuaire des Ossements (Kazuki), Forêt des Murmures (Goblinoïds).
- **Ouest / Sud-Ouest :** Velnor (Slums, Docks, Merchant District, Noble Quarter), Plaines et Falaises d'Argent.
- **Sud :** Port de l'Exil (Captain Edward), Marais Putrides.
- **Est :** Montagnes Brisées (Orcs, Hobgoblins).

### 4.2. Level Design Narratif
| Zone | Niveau | Danger | Contenu Narratif / Monstres |
| :--- | :--- | :--- | :--- |
| **Velnor (Slums & Docks)** | 1–10 | Faible/Moyen | Survie urbaine, petits jobs. *Bandits humains, rats géants, goblins isolés.* |
| **Plaines & Marais** | 8–18 | Moyen | Transition & premiers traumatismes. *Meutes de goblins, loups mutants.* |
| **Forêt des Murmures** | 15–30 | Élevé | Arc "Goblin Slayer", nids. *Goblinoïds, araignées, plantes.* |
| **Montagnes Brisées** | 25–40 | Très élevé | Ascension, artefacts. *Orcs organisés, trolls, cultistes.* |
| **Falaises d'Argent** | 30-50 | Très élevé | Quêtes marines, artefacts. *Deep Ones, monstres aquatiques.* |
| **Syphralis Ruines** | 35–55 | Extrême | Climax lovecraftien, cœur du Brouillard. *Abominations, boss eldritch.* |
| **Sanctuaire des Ossements**| 40+ | Variable | Forteresse de l'Overlord. Alliances, trahisons. *Non-morts, joueurs.* |

### 4.3. Principes de Level Design Narratif
1. **Progression Organique :** Pas de grind libre. Chaque zone exige un coût narratif (traumatisme, perte d'humanité).
2. **Boucle de Feedback :** Plus elle tue, plus elle gagne en puissance, mais plus elle attire l'attention du Brouillard.
3. **Zones "Instanciées" :** Les nids ou grottes fonctionnent comme des donjons multi-étages avec boss.
4. **Safe Zones :** Très rares. Velnor est dangereuse la nuit. Le Sanctuaire l'est si on n'est pas utile à Kazuki.
5. **Évolution Visuelle :** L'apparence d'Elara change en s'enfonçant dans le Brouillard (peau pâle, yeux rouges).
6. **Rebirth Zones :** Mort en couche = réapparition dans une zone aléatoire avec des traits hybrides.

---

## 5. ÉCOSYSTÈME FACTIONNEL

L'île est instable par design. Aucune faction ne gagne tant que le Brouillard avance.

### 5.1. Factions Humaines (Fragiles et désunies)
- **Le Conseil de Velnor :** Gouvernement corrompu (Lord Regent Harlan Voss). Voit Elara comme esclave/chair à canon.
- **La Guilde des Mercenaires (Iron Shields) :** Protègent contre récompense (Captain Rhea Vossler). Employeurs/protecteurs potentiels.
- **Les Cultistes de la Crimson Mother :** Humains fanatiques (La Prophétesse Sanglante). Cherchent à corrompre ou sacrifier.

### 5.2. Factions Monstrueuses (Dominantes)
- **La Horde des Goblinoïds :** L'ennemi principal (Grukk le Briseur). Se reproduisent massivement. Obsédés par la capture de femelles.
- **Les Deep Ones :** Créatures aquatiques voulant reprendre l'île (La Sea Witch). Possibilité de pactes dangereux.
- **Les Abominations du Brouillard :** Serviteurs sans leader fixe de la Crimson Mother. Répandent la chair.

### 5.3. Factions Transcendantes
- **Le Sanctuaire des Ossements :** Empire de l'Overlord Kazuki. Faction la plus puissante. Non-morts, joueurs loyaux.
- **Les Joueurs Indépendants ("Les Élus") :** Survivants du monde réel (bandits, héros, fous).
- **La Voix de la Fortune :** Entité neutre prophétisant la chute de l'île.

### 5.4. Triangle de Pouvoir (Relations)
- **Humains vs Goblinoïds :** Guerre totale, humains perdants.
- **Overlord vs Tous :** Kazuki annexe les territoires faibles.
- **Deep Ones vs Humains :** Vengeance ancestrale.
- **Cultistes vs Overlord :** Rivalité (libération vs contrôle du Brouillard).
- **Elara (Joker) :** Peut devenir héroïne mercenaire, tueuse légendaire, vassale, ou Dark Lady.

---

## 6. PROFILS DES PERSONNAGES NON-JOUEURS (PNJ)

**Protagoniste : Elara Voss (25 ans).** Avatar féminin faible et mignon. Passe de timide, terrifiée et pleurnicharde ("Je ne suis qu'une petite fille...") à chasseresse froide, calculatrice et obsédée.

**PNJ Majeurs :**
1. **Kazuki / Ainzuloth (Overlord) :** Ancien guild master japonais (30 ans, Lich 400+ ans). Grand squelette en robe rouge/noire. Calme, manipulateur, poli mais glacial. Allié, mentor, ou maître.
2. **La Voix de la Fortune :** Oracle cynique (28-35 ans), yeux bandés, entourée de brume. Narratrice occasionnelle.
3. **Captain Edward "The Last Ship" :** Capitaine (52 ans), barbu, cigare. Pragmatique, demande 25 pièces d'or pour fuir l'île.

**PNJ de Velnor :**
4. **Rhea "Iron Bitch" Vossler :** Leader des Iron Shields (34 ans). Dure, méprisante, respecte la détermination.
5. **Lord Regent Harlan Voss :** Chef du Conseil (61 ans). Corrompu, opportuniste, lâche.
6. **Cocona Vale :** Réfugiée innocente (25 ans), amie d'Elara. Mignonne, sale, optimiste fragile.
7. **Big Mama (Griselda) :** Tenancière de bordel/nécromancienne mineure (48 ans). Énorme, maternelle en surface, sadique en dessous.

**Antagonistes :**
8. **Grand Chef Grukk le Briseur :** Leader de la Horde (29 ans). Hobgoblin colossal en armure d'os. Obsédé par la conquête.
9. **La Prophétesse Sanglante (Sylvara) :** Leader folle des Cultistes (27 ans). Nue, couverte de sang et symboles.
10. **La Sea Witch :** Maîtresse des Deep Ones. Mi-femme, mi-poisson. Manipulatrice, ancienne.

**PNJ Secondaires :**
11. **Elise :** Prêtresse traumatisée (style Goblin Slayer). Compagne possible.
12. **Thorn :** Orc renégat. Mercenaire massif détestant sa race.
13. **Mira :** Voleuse des slums. Experte en poison, très cynique.
14. **Leroy "Jenkins" :** Guerrier légendaire souvent saoul, très fort mais imprudent.

---

## 7. BESTIAIRE : ANATOMIE DE LA CORRUPTION

### 7.1. Goblinoïds (La Plaie Vivante)
- **Goblin (Lvl 3-12) :** Lâches en solo, sadiques en meute. Obsédés par la capture pour reproduction. Gestation 3 semaines.
- **Hobgoblin (Lvl 12-25) :** Chefs territoriaux, brutaux, aiment "marquer" les captives.
- **Orc / Orkinds (Lvl 18-35) :** Massifs, très forts, forte libido. Engendrent des demi-orcs.
- **Ogre (Lvl 30-45) :** Géants obèses (3-4m).
- **Goblin Champion / Goblin Lord (Lvl 40+) :** Boss de nid, intelligent, utilise des artefacts.

### 7.2. Créatures du Brouillard & Abominations
- **Corrompu / Mist Walker (Lvl 10-30) :** Mutants infectant par contact sexuel ou morsure.
- **Fleshspawn (Lvl 25-50) :** Amas de chair, tentacules, cherchant la fécondation.
- **Crimson Horror (Lvl 55+) :** Tentaculaire géant lié à la Déesse.

### 7.3. Deep Ones
- **Deep One (Fishman) (Lvl 15-35) :** Intelligents, organisés. Peuvent s'hybrider.
- **Sirène Corrompue (Lvl 20-40) :** Belles mais avec dents de requin, chantent pour noyer.
- **Kraken Spawn (Lvl 45+) :** Tentacules géants de la Crimson Mother.

### 7.4. Non-Morts & Serviteurs
- **Skeleton Warrior (Lvl 15-30) :** Soldats de base de l'Overlord.
- **Death Knight (Lvl 40-60) :** Élites de l'Overlord, très puissants.
- **Soul Eater (Lvl 50+) :** Esprits se nourrissant des traumatismes d'Elara.

### 7.5. Autres Créatures
- **Giant Rat (Lvl 2-8) :** Velnor Slums, vecteurs de maladie.
- **Bandit Humain (Lvl 5-18) :** Routes, souvent plus dangereux que les monstres.
- **Dire Wolf (Lvl 10-20) :** Forêts, chassent en meute.
- **Cultist Zealot (Lvl 15-30) :** Fanatiques utilisant la magie de chair.
- **Arachne (Lvl 20-35) :** Forêt, tisse des pièges, poison aphrodisiaque.
- **Mutated Bear (Lvl 22-32) :** Montagnes, corrompu par le Brouillard.
- **Troll des Marais (Lvl 25-40) :** Marais Putrides, régénère rapidement.

### 7.6. Boss Majeurs du Monde
1. **Grand Chef Grukk le Briseur**
2. **La Sea Witch**
3. **The Crimson Matriarch** (Avatar de la Déesse à Syphralis)
4. **Ainzuloth (Kazuki)** (Si devenu hostile)
5. **The Black Mist Heart** (Entité finale, Lvl 70+)

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

Les événements sont aléatoires ou déclenchés par les actions d'Elara. Le Brouillard Noir augmente leur fréquence/intensité.

### 10.1. Événements Quotidiens / Fréquents (Ambient)
- **Raid Goblin :** Nuit. 15-40 goblins attaquent les Slums. Très fréquent. Risque de viol/enlèvement.
- **Avancée du Brouillard Noir :** L'horloge narrative. Le brouillard avance de 200-800m, buffant les monstres.
- **Émeute de la Faim :** Les réfugiés attaquent les entrepôts du Conseil de Velnor (pillage/incendies).
- **Patrouille des Iron Shields :** Expédition des mercenaires. Possibilité de rejoindre pour une quête.
- **Chasse aux Joueurs :** Des cultistes ou bandits traquent les "Élus".

### 10.2. Événements Hebdomadaires / Mensuels
- **Grande Migration Goblin :** Déplacement massif, création de nouveaux nids, bloque les routes.
- **Festival du Désespoir :** (Tous les 15j). Marché noir géant, prostitution, gladiateurs, apparitions de la Fortune Teller.
- **Incursion des Deep Ones :** Attaques sur les docks, enlèvements pour hybridation.
- **Purge du Conseil :** Lord Harlan exécute des traîtres/réfugiés, augmentant la tension.
- **Convoi de l'Overlord :** Caravane du Sanctuaire. Sécurisée mais dangereuse pour les non-alliés.

### 10.3. Événements Majeurs (Story-Driven & Rares)
- **Surge du Brouillard :** Explosion couvrant l'île. Spawn massif de Fleshspawn, Velnor en danger extrême.
- **Guerre des Nids :** Tribus goblines s'entretuent. Elara peut exploiter la situation.
- **Rébellion des Réfugiés :** Soulèvement des Slums, massacre général ou changement de pouvoir.
- **Invocation de la Crimson Mother :** Rituel des cultistes, apparition d'un avatar mineur.
- **Recrutement du Sanctuaire / Punition :** Kazuki recrute des Players ou détruit une faction (ex: tribu goblin) pour s'affirmer.

### 10.4. Événements Personnels (Elara)
- **Traumatisme Collectif :** Après une capture/viol, déclenche un "Flashback" (Mode Berserk in-game).
- **Grossesse Forcée :** Capture longue. Événement de naissance menant potentiellement à *Rebirth*.
- **Rencontre avec un Ancien Joueur :** Croisement avec un Player (allié/rival, trahison possible).
- **Vision de la Fortune :** La Voix de la Fortune prophétise une fin amère basée sur les actions actuelles.
- **Marque de la Crimson :** Le Brouillard marque Elara (Corruption ++, donne des pouvoirs de chair).

### 10.5. Événements Endgame (Très Rares)
- **Siège de Velnor :** Alliance Goblinoïds/Deep Ones/Cultistes contre Velnor.
- **Réveil de la Crimson Mother :** Tentative de retour complet de la Déesse.
- **Offre de l'Overlord :** Kazuki propose à Elara de devenir sa vassale ou successeure.
- **Dernier Bateau :** Edward annonce ses deux derniers voyages (Pression de temps).

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
