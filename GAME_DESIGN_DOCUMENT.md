# Document de Conception de Jeu (GDD) : Projet Horizon

## 1. Introduction et Vision Globale

**Projet Horizon** est un MMORPG indépendant s'articulant autour d'un paradoxe volontaire : une direction artistique rétro et volontairement minimaliste couplée à une architecture backend d'une complexité et d'une modernité de pointe.

L'objectif n'est pas d'offrir une claque graphique, mais de proposer un monde persistant, massif, dont les mécaniques de jeu, l'économie et la narration sont générées, régulées et adaptées dynamiquement par une architecture d'intelligence artificielle.

* **Thème :** Un monde de transition oscillant entre le Médiéval-Fantastique classique (zones de départ, capitales florissantes, plaines lumineuses) et la Dark Fantasy (zones contestées, terres corrompues, donjons abyssaux).
* **Paradigme Technique :** Le "Client Terminal". Le jeu client (développé via Bevy en WGPU) est un simple afficheur, très peu gourmand en ressources, garantissant une compatibilité maximale (des PC de dernière génération aux configurations datant de 15 ans). L'intégralité de la logique métier, des calculs de collision et de l'équilibrage est opérée par un serveur autoritaire (Rust / Bevy ECS Headless).

---

## 2. Système de Combat : L'Action Hybride

Le système de combat s'éloigne du ciblage statique ("Tab-targeting") pour proposer un gameplay dynamique, viscéral et orienté sur la gestion de groupes (inspiré des standards comme *Metin2*).

### 2.1. Mécaniques de Base
* **Frappes Multi-Cibles (Cleave) :** Les attaques de mêlée possèdent de larges *hitboxes* coniques ou circulaires. Un joueur ne combat que très rarement un ennemi unique ; le système encourage le "pull" (rassemblement) de grappes d'ennemis (5 à 15 simultanément) pour maximiser l'efficacité.
* **Mobilité et Kiting :** L'absence d'animation d'attaque verrouillée (Animation Lock) permet au joueur de se déplacer constamment ("Kiting"). Le positionnement est la compétence principale pour survivre.
* **Serveur Autoritaire & Prédiction Locale :** Pour garantir la réactivité sans compromettre la sécurité, le client prédit l'impact visuel et sonore des attaques. Cependant, le serveur valide l'équation mathématique $S_{t} = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_{t})$ pour chaque entité. Aucun calcul de dégâts ou de mort ne provient du client.

### 2.2. Crowd Control et Réactivité
* **Compétences Actives :** Les compétences consomment de la ressource (Mana/Endurance) et appliquent des effets physiques : projection arrière (Knockback), étourdissement de zone (Stun), ou ralentissement (Snare). Ces effets sont essentiels pour briser l'encerclement.

---

## 3. Évolution et Progression : Le Système Organique "Sans Classe"

L'architecture rejette les archétypes rigides (Guerrier, Mage, Soigneur) choisis à la création du personnage. La fonction d'un joueur est dictée par ses choix d'équipement et ses investissements d'attributs.

### 3.1. Attributs Fondamentaux
Chaque niveau octroie des points à répartir librement :
* **Force (STR) :** Augmente les dégâts physiques bruts et la capacité de charge de l'inventaire.
* **Dextérité (DEX) :** Améliore la vitesse d'attaque, les chances d'esquive et les dégâts des armes à distance.
* **Intelligence (INT) :** Détermine la puissance magique, la réserve de Mana et la résistance aux altérations d'état.
* **Vitalité (VIT) :** Définit le pool de points de vie (HP) et la régénération hors combat.

### 3.2. Maîtrises d'Armes et Synergies
* **Apprentissage par l'usage :** Utiliser une arme (ex: Épée à deux mains) génère de l'expérience spécifique pour cette maîtrise. Franchir des paliers de maîtrise débloque les compétences actives associées à cette arme.
* **Hybridation :** Un joueur ayant investi en Intelligence (INT) mais s'équipant d'une armure lourde (Nécessitant de la Force) créera de facto un "Battlemage". Le système récompense les *builds* spécialisés (Glass Cannon) comme les *builds* utilitaires.

---

## 4. Écosystème Économique et Artisanat

L'économie du jeu se veut réaliste, impitoyable et totalement dépendante des joueurs. Le butin (Loot) des monstres fournit des matières premières, pas les meilleurs équipements.

### 4.1. Récolte et Artisanat Interdépendant
* Les ressources sont divisées en Tiers de rareté.
* Les métiers de transformation (Forge, Couture, Alchimie) dépendent intrinsèquement des métiers de récolte (Minage, Dépeçage, Herboristerie).
* L'artisanat de haut niveau nécessite des composants croisés, forçant la coopération ou le commerce entre artisans spécialisés.

### 4.2. Usure, Durabilité et Destruction (Risk/Reward)
* **Économie de consommation :** Tous les équipements perdent en durabilité lors des combats et des morts.
* **Amélioration risquée :** Le système de perfectionnement des objets (ex: de +1 à +9) intègre des probabilités de réussite décroissantes. À partir d'un certain palier, un échec n'entraîne pas seulement la perte des matériaux, mais la **destruction définitive de l'objet**. Ce mécanisme crée une demande constante et endigue l'inflation des équipements "Parfaits".

---

## 5. Régulation Économique par Intelligence Artificielle

L'innovation majeure réside dans le pilotage macro-économique par une IA (Agent Économique via protocole MCP et base de données ClickHouse).

### 5.1. La Main Invisible du Serveur
* **Analyse en Temps Réel :** L'Agent Économique monitore la masse monétaire, les stocks en hôtels de vente, et le volume de ressources généré.
* **Ajustement Dynamique de l'Offre :** Si l'IA détecte une surproduction d'un minerai (ex: Or), elle réduit dynamiquement son taux de *spawn* géographique et augmente les taxes de transaction sur cette ressource.
* **Création de Pénuries :** Pour dynamiser certaines régions, l'IA peut provoquer intentionnellement des pénuries (ex: baisse drastique de la récupération de cuir). Les PNJ marchands générés par LLM proposeront alors des contrats extrêmement lucratifs (quêtes publiques temporaires) pour cette ressource spécifique.

---

## 6. L'Impact Macro-économique du Joueur contre Joueur (PvP)

Le PvP est le moteur end-game. Il justifie l'artisanat, la progression, et dynamise l'économie.

### 6.1. Territoires et Taxes
* **Contrôle de Zone :** Les guildes peuvent revendiquer des forteresses ou des relais marchands. La guilde souveraine fixe et prélève un pourcentage de taxe sur l'ensemble des hôtels de vente et PNJ de sa région.
* **Guerre de Factions :** Des guerres planifiées permettent le siège de ces forteresses.

### 6.2. Monopole des Ressources (Open PvP)
* Les minerais de Tiers maximum ou les herbes mythiques n'apparaissent que dans des zones contestées. Ces zones imposent un statut "PvP Ouvert". Pour exploiter ces ressources, une guilde doit sécuriser la zone, escortant ses récolteurs et repoussant les factions adverses.

### 6.3. Le Système de Caravanes
* Les hôtels de vente sont locaux (spécifiques à une ville). Le prix du Fer peut être dérisoire à la capitale minière, mais très élevé dans la capitale elfique.
* **Arbitrage Commercial :** Les joueurs peuvent créer des caravanes pour transporter de grands volumes. Celles-ci sont des cibles légitimes en zone contestée. La protection d'une caravane (ou son pillage) est une activité PvP hautement rémunératrice.

---

## 7. IA Sémantique : Des PNJ et Quêtes Vivants

L'univers abandonne les interactions statiques au profit de modèles génératifs contrôlés et gardés dans un cadre strict par le serveur.

### 7.1. Mémoire Sémantique (Système RAG)
* Les PNJ majeurs utilisent une base de données vectorielle (Qdrant/Milvus) pour stocker leurs "souvenirs". La Similarité Cosinus permet à un PNJ de se rappeler des actes du joueur (ex: "Vous avez tué le chef bandit il y a 3 jours") et d'adapter ses lignes de dialogues et ses prix de manière organique.

### 7.2. Quêtes Générées Procéduralement par IA
* Plutôt que des séries de quêtes figées, le monde génère des événements basés sur la simulation. Si les données montrent qu'une guilde a décimé trop de cerfs dans la forêt de l'Est, la chaîne alimentaire simulée se brise : l'IA génère des quêtes pour contrer l'invasion de loups affamés qui se rabattent sur le village.
* Ces quêtes sont traduites en dialogues narratifs uniques par les LLM, offrant une expérience renouvelée à chaque cycle économique.

---

## 8. Résumé des Boucles d'Engagement

1. **Boucle Court-terme (La Minute) :** Un système de combat action nerveux, exigeant un bon placement et permettant la satisfaction de vaincre des hordes d'ennemis.
2. **Boucle Moyen-terme (L'Heure) :** Retour en ville, sécurisation de l'inventaire, utilisation du système d'artisanat, et arbitrage commercial pour optimiser ses ressources en surveillant les fluctuations de l'IA.
3. **Boucle Long-terme (La Semaine/Le Mois) :** Implication sociale, politique et militaire. Sécurisation de monopoles économiques dans les zones PvP, prise de territoires avec la guilde, et maîtrise approfondie des armes et statistiques du personnage.
