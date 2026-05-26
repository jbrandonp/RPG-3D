# Document de Conception Architecturale (Technical Design Document) : Projet MMORPG Indépendant

**Statut du document :** Actif
**Objectif :** Définir les fondations techniques, les choix d'architecture, et la stratégie de scalabilité pour un projet MMORPG indépendant, en passant d'un prototype minimaliste à une infrastructure hautement scalable pilotée par l'Intelligence Artificielle (Architecture "Horizon 2030").

---

## 1. Vision Technique et Orientations Fondamentales

La stratégie d'ingénierie repose sur un parti pris radical : **minimiser la charge computationnelle du client au profit d'une infrastructure serveur ultra-performante et "AI-Native".**
En optant pour un rendu visuel volontairement rétro (esthétique PlayStation 2 / Low Poly), la bande passante et le CPU sont libérés pour traiter des volumes massifs d'entités, une IA complexe, et garantir une compatibilité matérielle maximale (y compris sur des machines âgées de plus de 15 ans).

### 1.1 Le Paradigme du "Client-Terminal"
Le client de jeu est dépourvu de logique métier décisionnelle. Il agit comme un terminal d'affichage ("Dumb Client") dont les responsabilités sont limitées à :
1. La captation et la transmission des *inputs* du joueur (Intentions).
2. L'exécution de la prédiction locale pour fluidifier l'expérience utilisateur (masquage de la latence).
3. Le rendu graphique basé sur les états dictés par le serveur.

---

## 2. Stack Technologique et Moteur

L'unification technologique entre le client et le serveur est assurée par le langage **Rust** et le paradigme **ECS (Entity Component System)**.

*   **Moteur Principal :** [Bevy Engine](https://bevyengine.org/) (Rust).
*   **Architecture Logique :** ECS natif. Les données (Composants) sont strictement séparées de la logique (Systèmes), stockées en mémoire contiguë (Data-Oriented Design). Cela garantit l'utilisation optimale des caches CPU L1/L2/L3 et élimine les pauses imprévisibles liées au ramasse-miettes (*Garbage Collector*).
*   **Rendu Client (WGPU) :** Abstraction bas niveau permettant la compilation croisée sans modification de code vers OpenGL ES 3.0 (anciennes machines), Vulkan, DirectX 12 ou Metal (machines récentes).
*   **Unification Client/Serveur :** Les structures de données (entités, composants, messages réseau) sont encapsulées dans un module ("Crate") partagé, garantissant une cohérence absolue des protocoles de communication.

---

## 3. Architecture Serveur et Réseau

### 3.1 Topologie et Synchronisation

L'architecture repose sur un modèle Client-Serveur avec un serveur **strictement autoritaire**.

```mermaid
flowchart TD
    subgraph Client [Client (Terminal d'Affichage)]
        I[Inputs Joueur] -->|Intention| N1[Couche Réseau]
        N1 -->|Réception d'État| R[Moteur de Rendu]
        P[Prédiction Locale] --> R
        I --> P
    end

    subgraph Serveur [Serveur Autoritaire (Headless ECS)]
        N2[Couche Réseau] -->|Validation| V[Logique Métier]
        V --> S[Simulation de l'État]
        S -->|Delta de Zone| N2
    end

    N1 <-->|UDP / QUIC / WebTransport| N2
```

*   **Serveur Headless :** Le moteur Bevy tourne côté serveur sans module de rendu. Il exécute la véritable simulation du monde à un *Tick Rate* fixe.
*   **Optimisation de la Bande Passante :**
    *   *Partitionnement Spatial (Interest Management) :* Le client ne reçoit que les événements des entités situées dans son champ de vision ou sa zone d'intérêt.
    *   *Transmission par Deltas :* Seuls les changements d'état (et non l'état complet) sont transmis à chaque *tick*.
*   **Réconciliation Mathématique :** Le nouvel état $S_t$ est calculé par la fonction de transition déterministe $\Phi$ : $S_t = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_t)$. En cas de divergence (lag ou triche), l'état serveur $S_t$ écrase immédiatement la prédiction locale du client.

---

## 4. Modèle de Persistance des Données

La gestion des données suit une approche polyglotte, adaptée aux spécificités de chaque type d'information.

### 4.1 Phase de Lancement (Architecture Standard)
*   **Mémoire Vive (RAM) :** Simulation du monde en temps réel et cache transactionnel de session.
*   **PostgreSQL :** Cœur persistant du système. Idéal pour la donnée structurée, hautement transactionnelle (Comptes, Inventaires, Monnaies, Progression). Respecte les propriétés ACID (Atomicité, Cohérence, Isolation, Durabilité).
*   **Service d'Authentification Isolé :** Séparation stricte (Token JWT / Sessions) de la couche base de données de jeu pour prévenir les failles de type injection et d'escalade de privilèges.

### 4.2 Évolution "Horizon 2030" (Scalabilité Massive)
*   **NewSQL (CockroachDB) :** Remplacement de PostgreSQL pour des transactions ACID distribuées à l'échelle mondiale sans point de défaillance unique (SPOF).
*   **Orienté Colonnes (ClickHouse) :** Absorption et requêtage des téraoctets de logs analytiques, de métriques de télémétrie et d'historique économique.
*   **Base Vectorielle (Qdrant / Milvus) :** Persistance de la "mémoire sémantique" pour les PNJ dotés d'IA, utilisant la Similarité Cosinus pour récupérer les souvenirs contextuels.

---

## 5. Systèmes de Jeu (Gameplay) et Interface (UI)

*   **Noyau du Gameplay :** Implémentation modulaire via ECS (Déplacement, Combat, Inventaire, Quêtes). Chaque module doit être testable de façon isolée (ex. un combat sans interface réseau).
*   **Économie et Sécurité :** Aucun calcul critique n'est délégué au client. Toute création, destruction ou transfert d'objet transite par une transaction serveur.
*   **Interface Utilisateur :**
    *   Le client gère un HUD réactif (Inventaire, Boutique, Carte).
    *   Séparation claire du modèle (Model-View-Controller/MVP). L'UI ne fait que refléter l'état local du client (mis à jour par le serveur).
    *   Outils : Wireframing via Figma, intégration native dans Bevy UI ou solution tierce (eg. Egui) respectant la direction artistique.

---

## 6. Intégration de l'Intelligence Artificielle (Ecosystème AI-Native)

L'architecture est préparée pour l'intégration d'agents autonomes basés sur des LLMs (Large Language Models).

*   **Protocole MCP (Model Context Protocol) :** Le serveur expose ses outils et l'état du monde via des contrats d'interface standardisés.
*   **Sandboxing de l'IA :** Un PNJ IA est considéré par le serveur avec la même "méfiance" qu'un joueur humain. Les intentions générées par l'IA (dialogues, déplacements, transferts d'objets) sont soumises aux mêmes règles de validation métier pour empêcher la corruption du monde.
*   **Génération Procédurale et Narration :** Utilisation d'agents pour l'équilibrage économique dynamique et la génération de quêtes réagissant en temps réel aux actions macro-économiques des joueurs.

---

## 7. Gestion des Risques, Pièges et Déploiement

### 7.1 Pièges Techniques Majeurs à Éviter
1.  **Surcharge de la Base de Données :** Ne jamais écrire les positions temps réel (X, Y, Z) en base de données. Les déplacements vivent en RAM, la position n'est sauvegardée qu'à la déconnexion ou lors d'un *checkpoint* (zone de transition).
2.  **Confiance au Client :** Rendre le client responsable des *hit detections* (détection de coups) ou des valeurs d'inventaire conduit inexorablement à l'exploitation (Triche/Hack).
3.  **Sharding Prématuré :** Ne pas partitionner la base de données (MongoDB sharding) avant d'avoir prouvé par les métriques (Profiling) que PostgreSQL en "Scale-Up" (grosse machine + réplication de lecture) a atteint ses limites physiques.

### 7.2 Scalabilité Opérationnelle
L'évolution de l'infrastructure passera d'un déploiement simple (VPS monolithique avec Nginx) à une orchestration cloud-native :
*   **Kubernetes (K8s) & Agones :** Déploiement élastique. Agones permet de gérer les serveurs de jeu comme des entités à part entière (GameServer, Fleet, FleetAutoscaler) allouant automatiquement des serveurs en fonction de la population dans les zones du jeu.
*   **Observabilité :** Implémentation dès l'Alpha de l'observabilité structurée (Prometheus / Grafana) et de la centralisation des logs. Sans cela, le débogage réseau asynchrone est impossible.
