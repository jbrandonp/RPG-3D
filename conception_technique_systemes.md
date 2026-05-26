# Conception Technique des Systèmes - Architecture Horizon 2030

Ce document présente l'intégration technique conceptuelle de très haut niveau des systèmes de jeu au sein d'une architecture moderne de type "Horizon 2030" (Serveur autoritaire Rust/Bevy ECS, Client "terminal" léger, Base de données polyglotte, et Écosystème piloté par l'IA via MCP).

## 1. Déplacement
Le système de déplacement repose sur un paradigme de **prédiction locale isolée et réconciliation serveur**. Le client (agissant comme un simple terminal d'affichage) exécute immédiatement l'intention de mouvement pour garantir une fluidité visuelle, mais ne détient aucune vérité métier. L'intention de mouvement est envoyée sous forme d'événement réseau au serveur. Ce dernier, exécutant Bevy en mode headless (ECS), calcule la simulation absolue (collisions, vitesse légale) et renvoie périodiquement l'état réel (des deltas de position). Si l'état prédit du client diffère de la vérité du serveur, le client corrige doucement la position (réconciliation).

## 2. Combat
La logique de combat est exclusivement régie par le serveur pour empêcher toute triche. Lorsqu'un joueur déclenche une attaque, le client lance l'animation locale et transmet l'intention d'attaque. Le serveur utilise l'architecture ECS pour vérifier instantanément la validité de l'action : le joueur est-il à portée ? Les délais de récupération (cooldowns) sont-ils respectés ? L'entité ciblée est-elle toujours vivante ? Une fois validé, le serveur applique les modifications (perte de points de vie) et transmet de manière chirurgicale les modifications d'état uniquement aux joueurs situés dans la zone d'intérêt pertinente.

## 3. Compétences
Les compétences sont implémentées en s'appuyant sur les principes du **Data-Oriented Design** propre à l'ECS. Plutôt que d'être des objets complexes instanciés, ce sont des assemblages de composants attachés aux entités (effets de dégâts, modificateurs de vitesse, durées, zones d'effet). Le serveur applique ces modificateurs en masse à chaque *tick* de simulation, offrant des performances extrêmes sans coût de nettoyage mémoire. Les états des compétences (déclenchements, recharges) sont synchronisés vers le client via des deltas d'état, le client se contentant de lire ces données pour piloter les effets visuels (particules) et les interfaces.

## 4. IA des Ennemis et PNJ
L'IA abandonne l'arbre de comportement statique classique au profit d'un écosystème **"AI-Native"**. Les ennemis et PNJ sont pilotés par des agents intelligents, souvent basés sur des LLMs, via le protocole MCP (Model Context Protocol). Pour interagir avec le monde, ces agents lisent un contexte fourni par le serveur de jeu.
Les souvenirs et comportements des PNJ s'appuient sur une **Mémoire Vectorielle**. L'IA calcule la similarité entre une situation donnée et son historique pour générer une réaction crédible. Cependant, pour éviter des conséquences catastrophiques (hallucinations ou corruption de l'état du jeu), chaque décision de l'IA est sévèrement **sandboxée** ; le serveur valide les actions de l'IA avec la même rigueur qu'il valide celles d'un joueur humain.

## 5. Quêtes
Le moteur de quêtes fonctionne via une écoute asynchrone d'événements au sein de l'architecture ECS. Chaque action majeure dans le monde (mort d'un ennemi, ramassage d'objet, arrivée dans une zone) déclenche un événement côté serveur. Un système ECS dédié aux quêtes consomme ces événements et met à jour les composants de progression des joueurs. Étant donné l'importance de ces données, les avancements significatifs (complétion de quête, obtention de récompenses) sont enregistrés durablement dans la base de données relationnelle persistante, garantissant qu'aucune progression n'est perdue en cas de crash du serveur.

## 6. Inventaire
L'inventaire est géré de manière transactionnelle. Lorsqu'un objet est ramassé, déplacé ou consommé, le client soumet une requête au serveur. Le serveur effectue l'opération dans son état en mémoire (ECS). La particularité réside dans le fait que les objets ne sont pas gérés par le client ; le client demande au serveur "puis-je équiper cette épée ?", le serveur valide selon les règles métier, puis met à jour l'inventaire en mémoire et enregistre l'action. Le client ne fait qu'afficher ce que le serveur lui dicte de posséder.

## 7. Économie
L'économie (or, échanges, hôtels de vente) est le système le plus critique en matière de sécurité. Elle est adossée à une base de données distribuée hautement résiliente (ex: NewSQL), fonctionnant avec des garanties transactionnelles strictes (ACID) pour prévenir la duplication de monnaie ou les pertes d'objets. De plus, l'économie est monitorée globalement par l'infrastructure et peut être régulée dynamiquement par des agents IA, capables de lire des journaux de flux économiques pour équilibrer les prix, détecter les bots ou injecter des ressources pour simuler une économie vivante.
