# DOCUMENT DE CONCEPTION NARRATIVE (LORE.md)

| Propriété | Détail |
| :--- | :--- |
| **Projet** | ELARA'S BLACK MIST |
| **Statut** | Document de Travail (WIP) |
| **Version** | 3.3.0 |
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
11. [Direction Audio-Visuelle et Cinématographique](#11-direction-audio-visuelle-et-cinématographique)
12. [Spécifications Techniques IA & Infrastructure (Horizon 2030)](#12-spécifications-techniques-ia--infrastructure-horizon-2030)
13. [Glossaire Technique et Narratif](#13-glossaire-technique-et-narratif)

---

## 1. VISION NARRATIVE ET PRINCIPES DE CONCEPTION

### 1.1. Logline du Projet
> *« L'histoire est racontée comme un cauchemar réaliste et interactif où un monde virtuel immersif est devenu une prison mortelle et un purgatoire oppressant. L'espoir est une illusion systémique. »*

### 1.2. Ton et Atmosphère
Le ton principal est **nihiliste, cru, oppressant et désespéré**, avec des moments très rares de grâce qui sont inévitablement brisés. C'est une exploration viscérale de la vulnérabilité extrême face à une brutalité obsessionnelle. Le monde lui-même semble conscient et hostile. L'oppression, la trahison, la souffrance psychologique et physique sont les fondations du gameplay. Toutefois, une fine couche de mécaniques de jeu (notifications système, interface) maintient chez le joueur un faux sentiment de contrôle.

### 1.3. Point de Vue et Style
- **Point de Vue (POV) :** Troisième personne limitée, ancrée dans la perception d'**Elara Voss**.
- **Style d'Écriture :** Clinique et direct. Les descriptions s'attardent sur les détails sensoriels (odeur de putréfaction, froid surnaturel du Brouillard Noir) sans fioritures romantiques.
- **Narration Technique :** L'intrusion occasionnelle de la réalité virtuelle (ex. : *« Niveau 7 atteint. Compétence [Résistance à la Douleur] débloquée. »*) agit comme une dissonance cognitive, rappelant l'origine artificielle de cet enfer.

### 1.4. Thèmes Majeurs
- **Impuissance et Transformation :** L'évolution contrainte d'une entité vulnérable vers une force monstrueuse et pragmatique.
- **Prix du Pouvoir :** L'ascension hiérarchique nécessite l'abandon progressif de l'humanité.
- **Dissonance Ludique :** Les règles d'un ancien environnement contrôlé s'appliquent avec une rigidité implacable dans une réalité devenue organique et chaotique.
- **Illusion du Choix :** Fuir, survivre ou dominer dans un monde fondamentalement condamné.

---

## 2. STRUCTURE DU RÉCIT (PLAN EN ARCS)

**Arc 0 – Prologue (L'Incidence de Rupture)**
Elara initie une ultime connexion au réseau d'*Eternal Realms*. Rupture systémique et fusion ontologique. Elle s'éveille sans ressources ni protection dans les vestiges de Syphralis. Poursuivie par les entités du Brouillard Noir, elle rejoint le flux massif de réfugiés fuyant vers Velnor. Premier contact létal avec les Goblinoïds.

**Arc 1 – La Survie en Ville (État de Proie)**
Arrivée à Velnor, une métropole engorgée, rongée par la famine et dominée par les syndicats criminels. Focus sur la subsistance : accomplissement de tâches mineures, compromissions morales, et exploitation pour survivre. Établissement de connexions fragiles avec des figures locales (Griselda, Cocona, Capitaine Edward).

**Arc 2 – L'Extermination (Transition Prédatrice)**
Suite à un traumatisme sévère orchestré par un raid Goblinoïd, la psyché d'Elara se fragmente. Elle développe une focalisation obsessionnelle sur l'éradication des nids. Formation d'une escouade spécialisée s'appuyant sur des tactiques de guerre asymétrique (ingénierie mortelle, toxines, incendies tactiques).

**Arc 3 – L’Ascension (Gouvernance et Alliances)**
L'accumulation rapide d'expérience, favorisée par son statut "d'Élue" (ancien joueur), attire l'attention des puissances majeures. Découverte du Sanctuaire des Ossements et de son monarque, le Seigneur Liche Kazuki. Évaluation des trajectoires : subordination, machiavélisme, affrontement direct, ou élévation au rang de Souveraine Sombre.

**Arc 4 – La Guerre d'Attrition (Guerre Totale)**
Convergence des forces antagonistes majeures (Goblinoïds, Deep Ones, Entités de la Déesse Écarlate) aboutissant au siège de Velnor. Elara fait face au dilemme terminal : exode personnel, défense désespérée des vestiges humains, ou conquête martiale de l'île.

**Arc 5 – Terminaisons Multiples**
- **L'Exode Illusoire :** Fuite réussie via les voies maritimes, accompagnée de l'effondrement total de Velnora.
- **Terminaisons Fatales :** Asservissement perpétuel, assimilation par le Brouillard, ou mort organique irréversible.
- **L'Hégémonie Sombre :** Élévation au statut de Souveraine absolue de l'île.
- **L'Annihilation Mutuelle :** Destruction du noyau du Brouillard Noir au prix de sa propre existence.
- **La Croisade Infinie :** Survie dédiée exclusivement à la purification violente et sans fin, menant à une fracture psychologique irréversible.

---

## 3. COSMOGONIE ET CHRONOLOGIE UNIVERSELLE

### 3.1. Entités Primordiales
Du Vide Éternel (The Eternal Void) émergèrent trois concepts directeurs :
1. **La Justice (L'Ordonnateur Défunt) :** Créateur originel des constantes physiques et concepteur des entités océaniques primaires (Deep Ones) ainsi que de l'humanité. Actuellement dormant ou anéanti.
2. **La Mère Écarlate (The Crimson Mother) :** Avatar de la prolifération charnelle incontrôlée et de la corruption organique. Génitrice des espèces prédatrices (Goblinoïds) et des abominations mutagènes.
3. **L'Architecte (Le Concepteur Système) :** Entité représentant les protocoles, les règles logiques et les algorithmes de la simulation virtuelle *Eternal Realms*.

### 3.2. Chronologie Systémique
- **Ère Primordiale (An 0 – 800) :** Établissement des espèces. Prolifération des descendants de la Mère Écarlate. Conflit territorial entre les Deep Ones et les entités mutagènes.
- **Ère des Saints (An 1321 – 1500) :** Manifestation de six figures fondatrices (Porteurs de reliques transcendantes). Établissement de la cité de Syphralis.
- **Ère de la Colonisation (An 1550 – 1700) :** Arrivée des colons d'Ingeland. Conflits maritimes majeurs et refoulement des Deep Ones. Fondation de la capitale Velnor.
- **Ère du Brouillard (An 1771 – Présent) :** Échec d'une manifestation cataclysmique de la Mère Écarlate, provoquant l'oblitération de Syphralis et l'émergence exponentielle du **Brouillard Noir**.
- **La Singularité (An 2138 / Fin d'Eternal Realms) :** Colapsus et fusion des protocoles virtuels avec la trame du monde physique. Les derniers connectés, dont Kazuki, deviennent des "Élus" dotés d'attributs para-physiques.
- **Cycle Actuel (1772 in-game) :** Éveil d'Elara. Le continent insulaire devient une zone de confinement fermée, rongée par l'avancée entropique du Brouillard.

---

## 4. TOPOGRAPHIE ET LEVEL DESIGN NARRATIF

L’île de **Velnora** (180x90 km) présente la morphologie d'une main fracturée. Le Brouillard Noir fonctionne comme une **limite de zone temporelle** (Timer Asynchrone), consumant progressivement les secteurs sécurisés.

### 4.1. Carte de l'Île
- **Nord-Est :** Syphralis (Ruines Écarlates). Épicentre de l'anomalie, danger terminal.
- **Centre :** Sanctuaire des Ossements (domaine de l'Overlord), Forêt des Murmures (zones de reproduction Goblinoïds).
- **Ouest / Sud-Ouest :** Velnor (Secteur des Docks, Bidonvilles, Quartier Marchand, Enclave Noble), Plaines agricoles et Falaises d'Argent.
- **Sud :** Port de l'Exil (Zone d'extraction sous l'égide du Capitaine Edward), Marais Putrides.
- **Est :** Montagnes Brisées (Fortifications Orcs, réseaux de grottes).

### 4.2. Matrice de Progression (Level Design Narratif)
| Zone | Paramètres de Complexité (Lvl) | Indice de Danger | Composantes Narratives & Entités Hôtes |
| :--- | :--- | :--- | :--- |
| **Velnor (Bidonvilles & Docks)** | 1–10 | Faible/Moyen | Gestion de la survie, économie de subsistance. *Rats géants, pillards, éclaireurs goblins.* |
| **Plaines & Marais** | 8–18 | Moyen | Acquisition de compétences martiales primaires. *Patrouilles goblines, canidés corrompus.* |
| **Forêt des Murmures** | 15–30 | Élevé | Assauts stratégiques sur les structures de reproduction (Nids). *Goblinoïds supérieurs, arachnides géantes.* |
| **Montagnes Brisées** | 25–40 | Très élevé | Collecte de ressources critiques, artefacts. *Infanterie lourde Orc, Trolls, Sectateurs.* |
| **Falaises d'Argent** | 30-50 | Très élevé | Exploration sous-marine. *Civilisation des Deep Ones, Faune abyssale.* |
| **Syphralis Ruines** | 35–55 | Extrême | Cœur de la mutation. *Abominations majeures, entités cauchemardesques primordiales.* |
| **Sanctuaire des Ossements**| 40+ | Variable | Nœud diplomatique et tactique. *Garde squelettique d'élite, joueurs vétérans.* |

### 4.3. Principes Algorithmiques du Level Design
1. **Progression sous Contrainte :** Aucune zone de "grinding" pacifique. Chaque palier d'expérience s'acquiert via une attrition physique ou morale.
2. **Boucle de Rétroaction (Feedback Loop) :** L'accumulation de puissance martiale augmente la signature systémique du joueur, attirant l'agressivité environnementale.
3. **Zones Instanciées (Simulations isolées) :** Les nids souterrains génèrent des sous-niveaux procéduraux avec des comportements d'essaim et des figures de commandement.
4. **Rareté des Safe Zones :** Les abris sont transitoires. L'immunité nécessite une taxation économique (Velnor) ou politique (Sanctuaire).
5. **Dégradation Visuelle (Shader & Morphologie) :** L'exposition aux zones corrompues modifie dynamiquement le modèle 3D du joueur (textures de peau, colorimétrie des yeux).
6. **Points de Réémergence (Rebirth Zones) :** Lors d'un échec critique lié à une mécanique de capture, la renaissance se fait via un transfert de conscience hybride dans une zone non contrôlée.

---

## 5. ÉCOSYSTÈME FACTIONNEL

L'architecture géopolitique de Velnora est instable et sujette à un effondrement programmé en raison de l'expansion du Brouillard Noir.

### 5.1. Factions Humaines (Survivants et Structures Décadentes)
- **Le Conseil de Velnor :** Autocratie parasitaire dirigée par le Régent Harlan Voss. Gère l'allocation des ressources avec cynisme.
- **Les Boucliers de Fer (Iron Shields) :** Compagnie militaire privée sous le commandement de Rhea Vossler. Force de frappe mercenaire.
- **Les Sectateurs de l'Écarlate :** Fanatiques humains (Prophétesse Sylvara) cherchant l'accélération de la mutation globale.

### 5.2. Factions Endémiques et Parasitaires
- **La Horde Goblinoïde :** Force antagoniste majeure, menée par Grukk. Stratégie d'attrition par reproduction exponentielle et terreur psychologique.
- **Le Consortium des Deep Ones :** Vestiges de la civilisation originelle (La Sorcière des Mers). Ambitions territoriales marines et manipulations génétiques.
- **L'Essaim du Brouillard :** Extensions organiques directes de la Mère Écarlate. Opèrent sans hiérarchie classique, visant l'assimilation de la biomasse.

### 5.3. Factions Transcendantes (Entités de la Singularité)
- **Le Sanctuaire des Ossements :** Nécropole militarisée du Seigneur Liche Kazuki. Structure la plus stable, alimentée par la logique mathématique pure.
- **Les Élus (Joueurs Isolés) :** Variables chaotiques. Individus possédant l'accès aux interfaces système, agissant comme mercenaires, tyrans ou victimes de haut niveau.
- **La Voix de la Fortune :** Anomalie prédictive observant l'effondrement des variables, fournissant des données prophétiques sous forme d'énigmes.

### 5.4. Équilibre Dynamique (Triangle de Pouvoir)
- **Humains vs Horde :** Asymétrie totale. L'humanité est en perte constante de territoire.
- **Sanctuaire vs Reste du Monde :** L'Overlord intègre méthodiquement les ressources utiles, ignorant le reste.
- **Deep Ones vs Humains :** Actions de guérilla et d'enlèvements ciblés sur le littoral.
- **La Protagoniste (Variable Alpha) :** Les actions d'Elara agissent comme un poids modifiant l'équilibre des scripts de conflit.

---

## 6. PROFILS DES PERSONNAGES NON-JOUEURS (PNJ)

**Protagoniste : Elara Voss.** Entité joueuse réinitialisée. Son arc évolutif la fait transiter d'une posture de proie vulnérable à celle d'une anomalie prédatrice méthodique.

**Figures de Puissance Majeures :**
1. **Kazuki / Ainzuloth (L'Overlord) :** Administrateur d'alliance japonais transmuté en mort-vivant suprême. Rationalité absolue, analyse l'univers uniquement via des algorithmes statistiques. Mentor ou Némésis.
2. **La Voix de la Fortune :** Entité non combattante, avatar d'analyse prédictive.
3. **Capitaine Edward ("Le Dernier Navire") :** Opérateur logistique unique disposant d'un moyen d'exfiltration. Accès conditionné (Ressources critiques requises).

**Structures de Velnor :**
4. **Rhea "Iron Bitch" Vossler :** Opératrice tactique impitoyable, valorise l'efficacité brute.
5. **Régent Harlan Voss :** Nœud de corruption politique, gestionnaire de la misère urbaine.
6. **Cocona Vale :** Élément narratif de vulnérabilité. PNJ civil à haut risque de terminaison.
7. **Griselda (Big Mama) :** Gestionnaire de flux illicites, courtier d'informations et manipulatrice des réseaux souterrains.

**Cibles Prioritaires (Antagonistes) :**
8. **Chef de Guerre Grukk :** Hobgoblin massif (Alpha de la Horde). Stratège brutal focalisé sur l'expansion de son espèce.
9. **Sylvara (La Prophétesse) :** Catalyseur humain de l'infection écarlate.
10. **La Sorcière des Mers :** Matriarche abyssale, gardienne des anciennes lois aquatiques.

**Unités d'Assistance ou Modificateurs PNJ :**
11. **Elise :** Unité de soutien (Soin) souffrant de PTSD sévère (syndrome post-traumatique) affectant ses probabilités de lancer de sorts.
12. **Thorn :** Unité "Tank" Orc en rupture de ban. Marge d'erreur élevée sur les jets de loyauté.
13. **Mira :** Unité "Rogue" (Furtivité/Toxines). Cynisme et vénalité.
14. **Leroy "Jenkins" :** Unité d'Assaut incontrôlable, génère un chaos tactique élevé lors des déploiements.

---

## 7. BESTIAIRE : ANATOMIE DE LA CORRUPTION

### 7.1. Goblinoïds (L'Essaim Reproducteur)
- **Goblin (Lvl 3-12) :** Unités d'infanterie légère. Programmation comportementale axée sur l'agression de groupe et la capture (Comportement de harcèlement).
- **Hobgoblin (Lvl 12-25) :** Sous-officiers territoriaux. Statistiques de force et de résistance accrues.
- **Orc / Orkinds (Lvl 18-35) :** Infanterie lourde de choc. Vecteurs de génération d'hybrides puissants via capture.
- **Ogre (Lvl 30-45) :** Véhicules de siège biologiques. Dégâts cinétiques massifs.
- **Seigneur Goblin (Lvl 40+) :** Unités de commandement d'instance. Accès à l'équipement magique et au contrôle des foules.

### 7.2. Abominations du Brouillard (L'Infection)
- **Marche-Brume (Lvl 10-30) :** Unités d'infection de base. Leurs frappes incrémentent les jauges de Corruption du joueur.
- **Rejeton de Chair (Lvl 25-50) :** Aglomérats biologiques. Priorisent l'assimilation et génèrent des zones de dégâts persistantes (DoT).
- **Horreur Écarlate (Lvl 55+) :** Drones géants de la Mère Écarlate, capables d'altérer la topographie locale de l'arène.

### 7.3. Entités Abyssales (Les Deep Ones)
- **Guerrier des Profondeurs (Lvl 15-35) :** Combattants amphibies organisés, résistants aux dégâts physiques classiques.
- **Sirène Altérée (Lvl 20-40) :** Unités de contrôle (Crowd Control). Leurs émissions sonores génèrent des états de confusion ou de paralysie.
- **Kraken Spawn (Lvl 45+) :** Menaces environnementales maritimes massives.

### 7.4. Structures Nécromantiques
- **Garde Squelette (Lvl 15-30) :** Infanterie d'attrition de l'Overlord. Faible résistance, immunité aux toxines.
- **Chevalier de la Mort (Lvl 40-60) :** Garde prétorienne, lourdement armurée, générant des dégâts d'ombre et de froid.
- **Mange-Âme (Lvl 50+) :** Entités éthérées drainant spécifiquement les jauges de Santé Mentale/Trauma.

### 7.5. Faune et Menaces Périphériques
- **Rats Géants (Lvl 2-8) :** Nuisibles urbains, appliquent le débuff "Maladie".
- **Pillards (Lvl 5-18) :** Unités humaines équipées de pièges et d'armes à distance.
- **Loups Funestes (Lvl 10-20) :** Mobilité élevée, algorithmes de contournement et d'attaque dans le dos.
- **Zélotes (Lvl 15-30) :** Lanceurs de sorts humains suicidaires, explosant à 0 HP.
- **Arachnes (Lvl 20-35) :** Prédatrices embusquées. Poison incapacitant forçant des états de capture.
- **Ours Mutants (Lvl 22-32) :** Pools de points de vie massifs, enrage sous 30% de santé.
- **Trolls des Marais (Lvl 25-40) :** Régénération passive extrême. Vulnérabilité stricte aux dommages thermiques (feu).

### 7.6. Entités Alpha (World Bosses)
1. **Grukk le Briseur :** Mécaniques de vagues d'adds et d'étourdissement lourd.
2. **La Sorcière des Mers :** Manipulation des niveaux d'eau et conjuration d'entités abyssales.
3. **La Matriarche Écarlate :** Combat d'instance à phases multiples à Syphralis.
4. **Kazuki (Engagement Hostile) :** Combat de type "Puzzle" nécessitant le contournement de ses défenses algorithmiques parfaites.
5. **Le Noyau du Brouillard Noir :** Cœur du système corrompu, niveau de menace 70+.

---

## 8. ARCHITECTURE DES QUÊTES

Le système de progression repose sur une architecture de Machine d'États (State Machine) serveur (Rust/Bevy). Les bifurcations d'états peuvent générer des événements de capture ou d'infection plutôt que des game over stricts.

### 8.1. Arborescence Prototype : Q_MAIN_SURVIVAL — « Acquisition de Capitaux »
**Directives :** Accumuler des devises pour subvenir aux besoins primaires, conduisant à une embuscade inévitable.

| Nœud d'État | Directives UI | Triggers & Exécution Systémique |
| :--- | :--- | :--- |
| **0_Init** | *Générer un capital de départ.* | Localisation : Slums. Initialisation du timer de faim. -> Transition State = 1 |
| **1_Contrat** | *Exécuter la logistique pour Griselda.* | Condition : `inventory.gold >= 5`. -> Transition State = 2 |
| **2_Interception** | *Atteindre le point de livraison.* | Déclencheur : Collision avec Box(Alley_01). Invocation : `spawn_entities(Goblin_Scout, 3)`. -> Transition State = 3 |
| **3_Résolution** | *Survivez ou subissez les conséquences.* | Condition de Victoire : `kill_count == 3` -> State 5. <br> Condition d'Échec : `player.HP == 0` -> Déclenchement événement `Capture_01`, `player.trauma_index += 1`. -> Transition State = 4 |
| **4_Conséquence** | *Émergence post-traumatique.* | Activation : Réapparition instanciée. Ajout passif `Cold_Rage`. -> Transition State = 5 |

---

## 9. INGÉNIERIE DES DIALOGUES ET SCRIPTING

### 9.1. Paramètres d'Interface (Esthétique Rétro)
- **Contraintes de Rendu :** Système de bulles textuelles strict (Max 3 lignes, 60 caractères par ligne). Polices pixelisées (nearest-neighbor filtering).
- **Registre Linguistique :** Pragmatique, expurgé de tout lyrisme héroïque.
- **Système Dissonant :** Les alertes systémiques s'intercalent comme des diagnostics cliniques au milieu de la terreur humaine.

### 9.2. Exemple de Script : Négociation avec l'Overlord
> **KAZUKI :** "Sujet identifié. Niveau 34. Écart-type d'évolution statistiquement aberrant."
> **ELARA :** [Posture défensive. Animation Idle_Combat activée.]
> **KAZUKI :** "Cessez cette simulation d'hostilité. Si votre suppression était requise, le protocole serait déjà en cours d'exécution."
> **SYSTEM_UI :** *[Alerte critique : Évaluation de la cible impossible (Lvl ??). Retraite immédiate conseillée.]*
> **KAZUKI :** "Votre ratio d'élimination de la biomasse goblinoïde est pathologiquement efficace. Intégrez ma structure, et leur éradication sera systématique."

---

## 10. SYSTÈMES D'ÉVÉNEMENTS DYNAMIQUES

Gérés par l'orchestrateur serveur, ces événements forcent le joueur à s'adapter à une asymétrie croissante.

### 10.1. Routines Fréquentes (Génération Quotidienne)
- **Incursions Nocturnes :** Apparition de 15 à 40 unités goblinoïdes en bordure urbaine. Risque d'altération définitive des PNJ (mort/capture).
- **Expansion du Brouillard :** L'horloge macro-systémique. Modification asynchrone des chunks environnementaux (progression de 200 à 800m), appliquant un multiplicateur de statistiques aux entités corrompues locales.
- **Ruptures Logistiques :** Événements d'émeute civile dans les zones de concentration de population, altérant les prix de l'économie locale.
- **Opérations des Mercenaires :** Scripts de patrouille alliée croisant la trajectoire du joueur. Opportunités d'assistance tactique temporaire.
- **Traque des Élus :** Escouades d'élimination ciblées spécifiquement sur le tag `is_player`, forçant une vigilance spatiale constante.

### 10.2. Cycles Moyens (Génération Hebdomadaire/Mensuelle)
- **Redéploiement d'Essaim :** Migration de masse de la Horde, altérant le maillage de navigation (NavMesh) des routes principales.
- **Économie de l'Ombre :** Activation périodique du grand marché noir. Apparition de marchands d'artefacts rares et de l'entité prédictive (La Voix).
- **Assauts Littoraux :** Activité accrue des Deep Ones, modifiant la dangerosité des zones portuaires.
- **Épuration Civile :** Exécutions publiques modifiant le niveau de tension urbaine et les réactions des PNJ.
- **Logistique du Sanctuaire :** Déplacement d'actifs sécurisés de l'Overlord traversant le continent.

### 10.3. Événements Majeurs (Modifications Structurelles de l'Univers)
- **Ruptures Massives (Surge) :** Poussées brusques du Brouillard Noir instanciant des boss de haut niveau dans des zones précédemment sécurisées.
- **Guerre de Factions :** Affrontement scripté entre tribus ennemies, permettant au joueur d'opérer des frappes chirurgicales sur les flancs.
- **Insurrection Urbaine :** Perte temporaire ou définitive du contrôle de certains hubs urbains.
- **Manifestation Écarlate :** Invocation d'avatars majeurs de la corruption par les sectateurs.
- **Manœuvres de l'Overlord :** Opérations d'assimilation massive ou de destruction totale de certaines régions géographiques par les troupes squelettiques.

### 10.4. Traumatismes Personnels (Liés à l'État du Joueur)
- **Rupture Cognitive (Flashback) :** En cas d'accumulation critique de la jauge de Trauma, perte de contrôle momentanée avec application d'un buff de dégâts incontrôlable.
- **Cycle d'Incubation :** Conséquence des états de capture, menant à des pénalités massives d'endurance, et pouvant déclencher la routine de Renaissance (Rebirth).
- **Interférences Systémiques :** Rencontres scriptées avec d'autres entités portant le tag `is_player`.
- **Prophéties Analytiques :** L'entité de la Fortune compile les données d'action du joueur pour prédire de manière déterministe son pourcentage d'échec.
- **Assimilation Charnelle :** Augmentation de l'indice de Corruption conférant des résistances spécifiques en l'échange d'une altération du modèle 3D.

### 10.5. Routines Finales (Endgame)
- **Convergence Totale :** Assaut multicibles sur le dernier bastion urbain.
- **Singularité Écarlate :** Tentative de fusion complète de la Mère Écarlate avec l'interface serveur.
- **Dernier Acte Diplomatique :** Proposition de transfert de pouvoir ou de souveraineté par l'Overlord.
- **Fermeture des Ports :** Disparition progressive des vecteurs d'extraction maritimes.

---

## 11. DIRECTION AUDIO-VISUELLE ET CINÉMATOGRAPHIQUE

Le projet obéit à des contraintes techniques rétro-esthétiques sévères visant à instaurer un malaise cognitif. Le pipeline 3D suit un flux high-to-low poly (sculpt high-poly vers retopologie low-poly) pour atteindre l'esthétique PS2. Tous les assets sont exportés en glTF 2.0 (.glb) pour Bevy, respectant le système de coordonnées (+Y up, -Z forward), un os racine à (0,0,0) et un maximum de 4 os par vertex.

### 11.1. Contraintes Visuelles (Architecture Bevy / Esthétique PS2)
- **Modélisation Low-Poly :** Environnements et personnages bridés aux alentours de 5,000 triangles. Triangulation manuelle stricte (pas de Sub-D). L'optimisation des draw calls exige l'utilisation d'atlas de textures spécifiques par biome.
- **Éclairage Restreint :** Utilisation exclusive de matériaux "Unlit" (KHR_materials_unlit) soumis au filtrage Nearest-Neighbor. Les ombres et l'occlusion ambiante (AO) sont statiquement gravées (baking) dans les textures diffuses ou les couleurs de vertex. Absence de physically based rendering (PBR) ou de normal maps.
- **Architecture VFX (Effets Visuels) :** Les effets (magie, sang, corruption) utilisent des billboards 2D, des polygones très faibles, et de l'additive blending. Le client Bevy fonctionne comme un simple "terminal" : il reçoit des événements du serveur autoritaire pour déclencher des VFX locaux, ces derniers n'ayant absolument aucun impact ni calcul sur la logique de gameplay.
- **Cinématographie Algorithmique :** Utilisation de caméras à axes fixes lors des séquences d'événements, forçant un angle de vision oppressant et réduisant artificiellement la perception de l'espace.

### 11.2. Architecture Sonore Dissonante
- **Conception Audio :** Contraste majeur avec l'horreur visuelle. L'environnement sonore (BGM) repose sur des compositions classiques douces, apaisantes, évoquant les MMORPG médiévaux des années 2000. Les bruitages et l'ambiance restent ancrés dans un cadre de fantasy classique (bruits d'épées, arcs, forêts, cavernes).
- **Objectif Psychologique :** Cette musique "sans fatigue auditive" entre en dissonance totale avec la brutalité systémique, renforçant le sentiment que le "système du jeu" est indifférent à la souffrance de l'avatar. Le faux réconfort auditif exacerbe la réalité cauchemardesque.

---

## 12. SPÉCIFICATIONS TECHNIQUES IA & INFRASTRUCTURE (HORIZON 2030)

Le backend Rust/Bevy s'interface avec le Model Context Protocol (MCP) pour simuler une intelligence dynamique chez certains PNJ majeurs, soutenu par une infrastructure cloud-agnostique ultra-scalable.

### 12.1. Infrastructure Matérielle (Cible 2030)
- **Déploiement & Orchestration :** Les serveurs de jeu Bevy sont conteneurisés et orchestrés via Kubernetes, utilisant **Agones** pour la gestion dynamique des flottes de serveurs dédiés.
- **Persistance des Données :** L'état global du monde, l'économie et les profils des joueurs sont gérés par **CockroachDB** (PostgreSQL distribué).
- **Observabilité :** Centralisée via OpenTelemetry, Prometheus, Grafana pour les métriques/alertes, et Jaeger/Tempo pour le distributed tracing. Les logs massifs de combat et d'économie sont ingérés par **ClickHouse**.
- **Vectorisation IA :** Le système de mémoires RAG des PNJ est stocké et requêté via une base de données vectorielle (Qdrant ou Milvus).

### 12.2. Contrat de Données MCP (Profil Logique : Kazuki)
```json
{
  "agent_id": "kazuki_overlord_node",
  "system_directive": "Act as Kazuki, a highly intelligent, 400-year-old Lich Overlord who interprets the physical world entirely through RPG statistics, probability, and ruthless logic. Exhibit zero emotional resonance or empathy. Use clinical, formal terminology.",
  "dynamic_context": {
    "world_status": "mist_expansion_rate_critical, goblin_horde_population_spike",
    "player_metrics": {
      "level": 34,
      "corruption_index": 45.2,
      "trauma_index": 80.7,
      "active_class_path": "exterminator_hybrid"
    },
    "recent_event_log": "target_massacred_hive_node_03_using_incendiary_tactics"
  },
  "retrieved_memories": [
    "Target previously rejected alliance proposition #1.",
    "Target displays extreme behavioral bias against goblinoid entities."
  ],
  "allowed_operations": ["execute_pact_offer", "deploy_intimidation_aura", "provide_system_lore"]
}
```

---

## 13. GLOSSAIRE TECHNIQUE ET NARRATIF

- **Artéfacts Rares :** Objets systémiques d'une valeur inestimable, constituant la seule méthode d'outrepasser les protocoles de suppression définitive (mort permanente).
- **Brouillard Noir (Black Mist) :** Vecteur de corruption entropique, résultante de l'anomalie de fusion entre la simulation *Eternal Realms* et l'univers physique.
- **Classes Actives :** Voies de spécialisation remplaçant le modèle universel, permettant d'adopter des rôles asymétriques (Assassin, Thaumaturge corrompue) en fonction des variables de survie.
- **Élus (Players) :** Entités humaines importées, marquées par le tag systémique `is_player`, leur conférant une courbe d'apprentissage et de puissance logarithmique accélérée.
- **MCP (Model Context Protocol) :** Interface de standardisation permettant l'ingestion du contexte de jeu (ECS Bevy) par des modèles de langage externes pour l'animation des PNJ.
- **Renaissance Hybride (Rebirth) :** Sous-routine critique. Si le vecteur (joueur) est supprimé lors d'une période d'incubation forcée, le système génère un nouvel avatar au niveau 1 héritant de traits algorithmiques liés à l'espèce de l'agresseur.
- **Velnora :** Espace confiné, dernier nœud de résistance humaine sur une topographie insulaire programmée pour la destruction.

---
*Fin du Document LORE.md — Conformité requise avec les standards architecturaux Rust/Bevy et la direction artistique PS2.*
