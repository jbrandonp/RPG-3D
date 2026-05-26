# Plan d'Architecture du Mini-MMORPG

Ce document détaille l'architecture complète, le moteur, les systèmes de jeu, la gestion réseau, le gameplay, les animations et l'interface utilisateur (UI), conçus et structurés à partir du document de référence initial.

## 1. Moteur et Technologies Fondamentales

*   **Moteur de Jeu :** Bevy (Rust).
*   **Paradigme d'Architecture :** ECS (Entity Component System) partagé et unifié entre le client et le serveur. Permet une haute performance sans *garbage collector*, grâce à une gestion de la mémoire contiguë (Data-Oriented Design).
*   **Rendu Graphique (Client) :** Polymorphe via WGPU. Il abstrait le backend de rendu pour supporter OpenGL ES 3, Vulkan, DirectX 11/12 et Metal. L'objectif est de maintenir un rendu rétro (style PS2) et de tourner de manière fluide sur une très large gamme d'appareils, y compris les plus anciens.

## 2. Architecture Serveur et Bases de Données

*   **Topologie :** Architecture Client-Serveur avec un serveur purement **autoritaire**.
*   **Serveur de Simulation :** Tourne sur Bevy ECS en mode *headless* (sans rendu visuel). Il gère et valide l'intégralité de la logique métier.
*   **Authentification :** Service séparé (via token/session) pour isoler la logique d'identification de la logique du jeu, évitant ainsi des failles de sécurité majeures.
*   **Modèle de Données et Persistance :**
    *   *Mémoire Vive :* Simulation en temps réel de l'état du jeu.
    *   *Base de Données Principale :* PostgreSQL (idéal pour le stockage robuste, transactionnel et structuré des comptes, personnages, inventaires et économie).
    *   *Analytique & Télémétrie :* MongoDB (pour le *document model* et les logs volumineux) ou des bases orientées colonnes comme ClickHouse.
    *   *Architecture Future-Proof (Horizon 2030) :* Évolution vers le NewSQL (CockroachDB) pour la scalabilité distribuée sans point de défaillance, et utilisation d'une base de données vectorielle (Qdrant/Milvus) pour la mémoire sémantique des PNJ.

## 3. Réseau et Synchronisation

*   **Le Paradigme du Client "Terminal" :** Le client est allégé de toute logique métier lourde. Il transmet les intentions (inputs) du joueur et affiche l'état dicté par le serveur.
*   **Optimisation de la Bande Passante :**
    *   *Partitionnement Spatial :* Transmission des données filtrée selon les zones d'intérêt (les joueurs ne reçoivent que les informations des entités proches).
    *   *Transmission Chirurgicale :* Le serveur n'envoie que les deltas (changements d'état) au lieu de l'état complet à chaque *tick*.
*   **Couche Réseau :** L'approche classique utilise TCP/UDP, tandis que la stack avancée préconise QUIC / WebTransport pour optimiser la transmission continue.
*   **Déploiement et Orchestration :** La scalabilité s'appuie sur une flotte dynamique de serveurs de jeu gérée par Kubernetes + Agones pour adapter la capacité au nombre de joueurs réels.

## 4. Systèmes de Jeu (Gameplay & Logique)

*   **Fondations du Gameplay :** Déplacements, systèmes de combat, points de vie, gestion de l'inventaire, quêtes et progression.
*   **Validation et Économie :** Le client ne décide jamais seul. Toute transaction d'inventaire ou d'économie est validée par le serveur via des opérations transactionnelles.
*   **PNJ et Intelligence Artificielle (IA) :** Les PNJ ne reposent pas uniquement sur des arbres de comportement statiques. Ils sont connectés à des agents LLM fonctionnant via le protocole MCP (Model Context Protocol). L'IA est strictement "sandboxée" et agit en tant que simple client validé par le serveur pour prévenir toute hallucination, corruption économique ou triche.

## 5. Animation et Prédiction Locale

*   **Réactivité et Jouabilité :** Le client utilise le principe de **prédiction locale isolée**. Dès que le joueur effectue une action (ex. lancer une attaque, se déplacer), l'animation et le retour visuel s'exécutent immédiatement en local pour masquer la latence réseau.
*   **Réconciliation Côté Serveur :** Bien que l'animation soit immédiate, c'est le serveur qui calcule et confirme (ou corrige) l'effet réel de l'action de façon asynchrone. Si le client et le serveur sont désynchronisés (à cause du lag ou d'une triche), l'état du serveur écrase l'état local du client.
*   **Fondation Mathématique :** L'état $S_t$ est déterminé par $S_t = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_t)$, garantissant un comportement déterministe absolu sur le serveur.

## 6. Interface Utilisateur (UI)

*   **Conception et Pipeline :** La création de l'interface passe par un outil de prototypage (Figma) accompagné d'un éditeur de *pixel art* simple pour s'aligner sur la direction artistique (Rétro / PS2).
*   **Composants Essentiels :** HUD, inventaires, boutiques, carte, fenêtres de dialogue, et menus avec gestion fine des raccourcis clavier. L'UI est le lien critique entre l'information brute provenant du serveur (via les composants partagés ECS) et l'expérience du joueur.
