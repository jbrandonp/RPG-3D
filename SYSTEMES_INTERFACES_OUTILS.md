# Document de Conception Technique et Fonctionnelle : Interfaces et Outils

Ce document détaille les spécifications professionnelles pour la conception des interfaces (UI/UX) et des outils (éditeurs, debug) d'un MMORPG à l'esthétique rétro (PS2/Metin2) propulsé par une architecture moderne (Rust, Bevy ECS, Serveur Autoritaire, Intégration IA via MCP).

---

## 1. Vision et Paradigme Architectural

*   **Le Client "Terminal" :** Conformément à l'architecture "Future-Proof", le client de jeu est passif. Il n'exécute aucune logique métier et se contente d'afficher l'état calculé par le serveur via le backend WGPU.
*   **Bevy UI & ECS :** Toutes les interfaces sont développées à l'aide des systèmes natifs de Bevy (ou bibliothèques compatibles comme `bevy_egui` pour les outils). L'UI réagit aux événements locaux (Data-Driven) qui sont de pures réflexions de l'état serveur.
*   **Sécurité ("Zero Trust") :** L'interface utilisateur client peut être manipulée. Tout signal provenant de l'UI (clic, glisser-déposer, achat) est traité comme une *intention* non fiable jusqu'à sa validation par le serveur.

---

## 2. Conception des Interfaces Joueurs (UI/UX)

### 2.1. Le HUD (Head-Up Display)
L'interface en jeu doit être minimaliste pour ne pas surcharger l'écran, tout en fournissant les données critiques.

*   **Wireframe / Disposition :**
    *   *Haut Gauche :* Portrait du personnage, Jauges (HP rouges, MP bleus, Stamina/Énergie verts), Niveau.
    *   *Haut Droit :* Minimap ronde (radar de proximité basé sur les données serveur), Nom de la zone, Ping/FPS.
    *   *Bas Centre :* Barre d'actions (Slots 1 à 0, R, F, etc.) avec cooldowns visuels.
    *   *Bas Gauche :* Fenêtre de Chat multicanal (Général, Groupe, Guilde, Combat Logs).
*   **Architecture Technique :**
    *   Les jauges lisent l'état local répliqué : `Query<(&Health, &Player), With<LocalPlayer>>`.
    *   Les actions de la barre envoient un événement réseau : `NetworkMessage::CastSpell(SpellId)`. Le refroidissement visuel (cooldown) est initié par une prédiction locale, mais corrigé ou annulé si le serveur rejette l'action (ex: pas assez de mana ou désynchronisation).

### 2.2. L'Inventaire et l'Équipement
Le cœur de la progression du joueur. Doit supporter les opérations rapides.

*   **Design :** Fenêtre scindée. À gauche, la silhouette du personnage ("Paperdoll") avec les emplacements d'équipement (Tête, Torse, Arme, etc.). À droite, une grille d'inventaire classique.
*   **Technique (Le cycle d'un Drag & Drop) :**
    1. Le joueur glisse un item du slot A au slot B de l'inventaire.
    2. L'UI locale simule visuellement le déplacement (pour la fluidité) et envoie l'intention : `Intent::MoveItem { from: A, to: B }`.
    3. Le serveur reçoit l'intention, vérifie les règles métiers (ex: poids max, emplacements valides, item non verrouillé).
    4. Le serveur exécute une transaction en base (PostgreSQL) et met à jour l'ECS côté serveur.
    5. Le serveur renvoie un `StateDelta::InventoryUpdate` au client. Si rejeté, l'item retourne au slot A sur le client ("Rubberbanding" d'UI contrôlé).

### 2.3. Les Menus, la Boutique et l'Économie
*   **Boutique (Cash Shop / In-Game Shop) :**
    *   La boutique est alimentée par une base de données transactionnelle séparée (CockroachDB ou partition stricte PostgreSQL).
    *   Les transactions financières et les achats in-game requièrent un "Two-Phase Commit" ou un système de file d'attente asynchrone (Kafka/RabbitMQ si mise à l'échelle massive) pour garantir qu'aucune monnaie n'est dupliquée.
*   **Menu Système :** Options graphiques, son, macros, macros de chat.

### 2.4. Le "Wiki Intégré" via IA (RAG)
Fini les encyclopédies statiques. Le Wiki prend la forme d'une "Bibliothèque" ou de "Maîtres du Savoir" in-game.
*   **Fonctionnalité :** Le joueur pose une question dans la barre de recherche du Wiki (ex: *"Où se trouvent les loups spectraux ?"* ou *"Qui est le roi de cette région ?"*).
*   **Intégration IA :**
    *   La requête est envoyée au serveur.
    *   Le serveur utilise le contexte (Retrieval-Augmented Generation) en interrogeant une base vectorielle (Qdrant/Milvus) contenant tout le Lore et les tables de loot/spawns.
    *   Un LLM génère une réponse immersive formatée et l'affiche dans le client, tout en respectant un ton "Roleplay".

---

## 3. Outils, Éditeurs et Administration (Backend & DevTools)

Ces outils ne sont pas distribués aux joueurs finaux. Ils s'exécutent soit en tant qu'application desktop distincte, soit via un mode "God" injecté dans le client de développement.

### 3.1. Éditeur de Map (Map Editor / World Builder)
*   **Interface :** App Bevy séparée (`bevy_egui` pour l'interface de développement).
*   **Fonctionnalités :**
    *   Placement de "Prefabs" 3D (Maisons, arbres, spawners).
    *   Peinture de NavMesh (zones de navigation pour les PNJ).
    *   Définition des "Zones d'Intérêt" (Quadtrees/Octrees) pour le partitionnement réseau, indispensable pour limiter la bande passante (seuls les joueurs dans la même grille reçoivent les updates).
*   **Export :** Génère des fichiers binaires optimisés ou des fichiers RON chargés par le serveur au démarrage.

### 3.2. Éditeur de Quêtes propulsé par l'IA
*   **Interface :** Outil web ou interface nodale (arbres de comportement).
*   **Intégration Model Context Protocol (MCP) :**
    *   Le serveur expose des APIs (ex: `CreateQuestNode`, `AddRequirement`, `SpawnNPC`) via MCP.
    *   Un Game Designer humain ou un Agent IA autonome peut concevoir une chaîne de quêtes complexe. Par exemple, l'IA détecte qu'une zone manque de contenu pour les niveaux 10-15 et génère dynamiquement une suite de quêtes pertinente avec des PNJ locaux.
    *   *Sécurité :* Le serveur valide formellement la cohérence de la quête (ex: l'objet demandé existe-t-il dans les tables de loot ?) avant de l'enregistrer dans PostgreSQL.

### 3.3. Outils de Debugging (Admin / God Mode)
*   **Console de commande :** Intégrée au client, accessible avec des permissions (rôles JWT). Commandes type `/spawn item_id`, `/teleport x y z`, `/kill_all`.
*   **Overlay ECS :** Affichage en temps réel des "Hitboxes" (AABB), des trajectoires des PNJ, et des graphes réseau (Ping, Gigue, Paquets perdus).
*   **Metrics Serveur :** Interfaçage avec Prometheus/Grafana pour surveiller le nombre d'entités actives, le tick rate (idéalement 20-30 ticks/sec pour un MMO), et la latence base de données.

### 3.4. Systèmes de Configuration ("Hot-Reload")
*   **Fichiers de données (Data-Driven) :** Stats des armes, taux de drop, XP par monstre stockés dans des fichiers (TOML/RON) ou une base NoSQL.
*   **Mécanisme :** Le serveur Bevy utilise la fonctionnalité `AssetServer` pour observer les modifications de ces fichiers. Dès qu'un fichier est modifié par un designer, le serveur met à jour les composants en mémoire sans redémarrer (Hot-reloading).

---

## 4. Synthèse des Flux de Communication

1.  **Boucle de Gameplay Classique :**
    *   `[Client]` Génère Intention (UI/Clavier) → Réseau → `[Serveur]` Validation → Calcul du Tick → `[Base de données]` Persistance si nécessaire → `[Serveur]` Deltas → Réseau → `[Client]` Rendu visuel.
2.  **Boucle IA / Outils (MCP) :**
    *   `[Agent IA]` Analyse les logs ou reçoit une requête → Interroge via `MCP` → `[Serveur Bevy]` Exécute un sous-système (ex: création dynamique de quête) → `[Base de Données]` et `[Bases Vectorielles]` Mises à jour.
