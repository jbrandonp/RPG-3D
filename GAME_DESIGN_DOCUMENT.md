# Game Design Document (GDD) - Mini-MMO (Projet Horizon)

Ce document définit les règles, l'équilibre, la progression et les systèmes fondamentaux du jeu, en s'appuyant sur l'architecture Serveur/IA (Bevy/Rust) décrite dans le README.

## 1. Vision et Univers

**Thème :** Dark Fantasy et Médiéval Fantastique. L'ambiance visuelle et narrative varie selon les zones : des prairies ensoleillées et royaumes florissants (Médiéval Fantastique classique) aux marais corrompus, catacombes lugubres et terres désolées ravagées par la magie noire (Dark Fantasy).
**Style Visuel :** Rétro, esthétique type "PlayStation 2" ou "Metin2". L'objectif est de garder un client très léger (le "client terminal") pour allouer la puissance de calcul aux systèmes d'intelligence artificielle et à un écosystème massivement multi-joueurs.

---

## 2. Système de Combat (Hybride Action type Metin2)

Le système de combat est viscéral, orienté action et gère de multiples ennemis simultanément.

* **Attaques Multi-cibles (Cleave) :** Contrairement au "tab-targeting" classique, les attaques de base en mêlée touchent toutes les entités se trouvant dans un cône ou une zone devant le joueur. Un joueur peut ainsi combattre 5 ou 10 monstres en même temps.
* **Mobilité et Kiting :** Le positionnement est crucial. Les joueurs doivent rassembler les monstres (pull) et frapper au bon moment pour optimiser les dégâts tout en évitant les encerclements fatals.
* **Compétences Actives :** Les compétences déclenchent des effets de zone (AoE), des étourdissements ou des repoussements (knockbacks), essentiels pour contrôler les foules (crowd control).
* **Serveur Autoritaire :** Le client prédit l'animation (ex: un coup d'épée), mais le serveur calcule mathématiquement l'impact et les dégâts réels en fonction des positions exactes pour éviter la triche.

---

## 3. Boucles de Progression (Système "Sans Classe")

Il n'y a pas de sélection de classe stricte (Guerrier, Mage, etc.) à la création du personnage. Vous êtes ce que vous portez et ce que vous pratiquez.

* **Progression par l'Équipement et les Statistiques :** Le joueur distribue ses points d'attributs (Force, Dextérité, Intelligence, Vitalité). L'arme équipée définit le set de compétences disponible.
* **Maîtrise d'Arme :** Utiliser une épée à deux mains augmente la "Maîtrise de l'Épée Lourde", débloquant progressivement de nouvelles compétences (tourbillons, brise-armure). Passer à un bâton magique donne accès à des sorts de feu ou de soin, mais nécessite de monter la "Maîtrise du Bâton".
* **Arbre de Passifs Universel :** Les joueurs débloquent des points de talent permettant d'hybrider leur personnage (ex: un mage en armure lourde ou un assassin utilisant de la magie de sang).

---

## 4. Métiers et Récolte

L'artisanat est le moteur principal de la création d'équipement. Les meilleurs équipements ne "tombent" pas directement des monstres, ils sont fabriqués.

* **Récolte (Gathering) :** Minage, Bûcheronnage, Herboristerie, Dépeçage. Les ressources ont différents tiers de rareté.
* **Artisanat (Crafting) :** Forgeron, Tailleur, Alchimiste, Enchanteur. L'artisanat nécessite souvent l'interaction de plusieurs métiers (ex: le forgeron a besoin de cuir du dépeceur pour les poignées d'épées).
* **Usure et Destruction :** Pour maintenir l'économie active, les objets ont une durabilité. L'amélioration d'équipement à haut niveau a un pourcentage d'échec pouvant entraîner la destruction de l'objet (ajoutant un risque/récompense intense).

---

## 5. L'Économie gérée par l'IA

L'économie n'est pas statique ; elle est régulée en temps réel par une Intelligence Artificielle (L'Agent Économique) fonctionnant via le Model Context Protocol (MCP) et l'analyse de données (ClickHouse).

* **Régulation Dynamique :** L'IA analyse les stocks mondiaux. S'il y a trop de Fer dans le monde, l'IA baisse le prix d'achat par les PNJ marchands et réduit le taux d'apparition (spawn) des filons de fer. À l'inverse, si une ressource vient à manquer, l'IA génère des "pénuries" qui augmentent drastiquement les prix et incitent les joueurs à aller miner dans des zones dangereuses.
* **Contrats Commerciaux :** Les PNJ (animés par des LLM) peuvent proposer des contrats commerciaux dynamiques selon les besoins de leur village (ex: "La milice manque de flèches, le prix de rachat du bois double pendant 4 heures").
* **Marché Global ou Local :** Les hôtels de vente (ou places marchandes) sont taxés dynamiquement selon l'inflation du serveur.

---

## 6. L'Impact du PvP sur l'Économie

Le PvP n'est pas juste un affrontement pour la gloire, il est le principal levier économique à haut niveau.

* **Contrôle de Territoire (Guildes/Factions) :** Les guildes peuvent revendiquer certains territoires ou châteaux. Posséder un territoire permet à la guilde de prélever des taxes sur toutes les transactions marchandes ou ressources récoltées dans cette zone.
* **Mines et Zones de Récolte Contestées :** Les ressources les plus rares du jeu se trouvent exclusivement dans des zones "Open PvP" (PVP ouvert). Pour récolter du minerai mythique, une guilde doit escorter ses mineurs et défendre la zone contre les autres guildes.
* **Caravanes Marchandes :** Pour transporter d'énormes quantités de marchandises d'une ville à une autre (pour profiter des différences de prix générées par l'IA), les joueurs peuvent organiser des caravanes lourdement chargées. Celles-ci peuvent être attaquées et pillées par d'autres joueurs.

---

## 7. Quêtes et Intégration IA des PNJ

Fini les PNJ statiques avec des points d'exclamation jaunes qui répètent la même phrase depuis 10 ans.

* **Mémoire Sémantique (RAG) :** Les PNJ majeurs utilisent une base de données vectorielle pour se "souvenir" de leurs interactions passées avec les joueurs ou l'état du monde. (ex: Un garde se souviendra que vous avez aidé le village à repousser une invasion d'orcs la semaine passée).
* **Quêtes Dynamiques (LLM) :** L'IA Générative crée des événements et des quêtes en direct. Si les loups d'une forêt se reproduisent trop vite (donnée remontée par le serveur de simulation), le chef du village générera une quête d'extermination de loups pour les joueurs locaux, avec des dialogues uniques et contextuels.
* **Réputation Organique :** Trahir un PNJ ou échouer une quête majeure modifie la perception de la faction entière envers le joueur. Les dialogues générés par l'IA s'adapteront à cette réputation (ton méfiant, prix augmentés).

---

## 8. Résumé de l'Équilibre Général

* **Risque vs Récompense :** Plus une zone est dangereuse (présence de monstres forts ou de joueurs ennemis PvP), plus les ressources et le butin y sont lucratifs.
* **Rôle de l'IA :** L'IA n'est pas un gimmick textuel. Elle agit comme le Maître du Donjon qui s'assure que le monde est vivant, que l'économie ne s'effondre ni par l'hyperinflation ni par la pénurie, et que l'histoire du serveur s'écrit organiquement avec les actions des joueurs.
* **Philosophie de Conception :** Garder le gameplay de cœur viscéral (taper des monstres, récolter) extrêmement fun et fluide, tout en entourant le joueur d'un macro-système complexe, social et impitoyable.
