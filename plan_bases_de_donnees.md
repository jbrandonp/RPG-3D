# Plan d'Architecture : Bases de Données, Migrations, Index et Historiques (MMORPG)

Ce document présente les directives d'ingénierie et l'architecture complète des bases de données de notre MMORPG. Il englobe la conception du schéma relationnel, les stratégies d'indexation ciblées, la gestion sécurisée des transactions, et la méthodologie de migration "zéro interruption". De plus, il détaille l'approche "Future-Proof" qui intègre une scalabilité globale via CockroachDB et l'intégration de bases vectorielles pour les agents conversationnels (IA).

---

## 1. Architecture Initiale (PostgreSQL)

Durant les phases de développement (Pré-Alpha, Alpha, Bêta) et lors du lancement initial, **PostgreSQL** s'impose comme la solution de référence. Il garantit une modélisation structurée, la fiabilité des données (propriétés ACID) et offre une mise à l'échelle verticale et de réplication très solide.

### 1.1. Modèle de Données (Schéma Relationnel)

La persistance de l'univers s'articule autour des entités fondamentales suivantes. L'objectif est d'isoler logiquement les données critiques pour simplifier le requêtage.

*   **`users`** : Gestion des comptes joueurs, de la sécurité et de l'authentification.
    *   *Colonnes suggérées* : `id` (UUID), `username`, `email`, `password_hash`, `created_at`, `last_login`, `status` (actif, banni).
*   **`characters`** : Représentation des avatars en jeu, dépendants des utilisateurs.
    *   *Colonnes suggérées* : `id` (UUID), `user_id` (FK), `name`, `level`, `experience`, `health`, `mana`, `currency_copper`, `position_x`, `position_y`, `position_z`, `zone_id`.
*   **`inventory_items`** : Enregistrement de tous les objets possédés ou équipés par les personnages.
    *   *Colonnes suggérées* : `id` (UUID), `character_id` (FK), `item_template_id`, `quantity`, `durability`, `is_equipped`, `slot_id`.
*   **`quests_progress`** : Suivi asynchrone de l'état des quêtes pour chaque joueur.
    *   *Colonnes suggérées* : `id` (UUID), `character_id` (FK), `quest_id`, `status` (active, completed, failed), `objectives_state` (JSONB pour les étapes), `started_at`, `completed_at`.
*   **`skills`** : Compétences, sorts et talents débloqués par les personnages.
    *   *Colonnes suggérées* : `id` (UUID), `character_id` (FK), `skill_id`, `level`, `cooldown_expires_at`.
*   **`guilds`** : Organisation sociale de base (Guildes / Clans).
    *   *Colonnes suggérées* : `id` (UUID), `name`, `tag`, `leader_id` (FK characters), `created_at`.
*   **`guild_members`** : Table de liaison pour les effectifs de guilde.
    *   *Colonnes suggérées* : `guild_id` (FK), `character_id` (FK), `rank_id`, `joined_at`.
*   **`friends`** : Graphe des relations sociales inter-joueurs.
    *   *Colonnes suggérées* : `character_id_1` (FK), `character_id_2` (FK), `status` (pending, accepted), `created_at`.
*   **`transactions`** : Registre inaltérable des flux économiques (commerce direct, hôtel des ventes).
    *   *Colonnes suggérées* : `id` (UUID), `sender_id` (FK), `receiver_id` (FK), `currency_type`, `amount`, `item_id` (FK, optionnel), `transaction_type`, `created_at`.

### 1.2. Stratégie d'Indexation

Afin de préserver les performances de lecture sous forte charge, les index doivent être rigoureusement appliqués :

*   **Identifiants et Clés Étrangères** : Un index B-Tree automatique sur chaque Primary Key (PK) et chaque Foreign Key (FK) pour garantir la rapidité des jointures (ex: `characters(user_id)`).
*   **Unicité et Recherches Directes** :
    *   `UNIQUE INDEX` sur `users(email)` et `users(username)` (gestion du login).
    *   `UNIQUE INDEX` sur `characters(name)` et `guilds(name)` (unicité dans le monde).
*   **Index Composés (Multicolonnes)** :
    *   `INDEX (character_id, is_equipped)` sur la table `inventory_items` pour un chargement instantané de l'équipement lors de la connexion.
    *   `INDEX (character_id, status)` sur la table `quests_progress` pour filtrer rapidement le journal de quêtes actif.
*   **Pagination et Historique** :
    *   `INDEX (created_at DESC)` sur la table `transactions` et certains logs pour accélérer les audits et les tris temporels.

### 1.3. Gestion des Transactions (ACID)

La sécurité de l'économie repose sur le principe d'**autorité du serveur**. Toute opération mutative (échange de monnaie, transfert d'objets, récompense de quête) doit être encapsulée dans une transaction base de données atomique (`BEGIN` ... `COMMIT`).

*   **Exemple : Commerce entre joueurs**
    Le serveur vérifie préalablement en mémoire que les conditions sont remplies, puis exécute la séquence SQL stricte :
    ```sql
    BEGIN;
    -- Verrouillage de la ligne acheteur et prélèvement (si solde suffisant)
    UPDATE characters SET currency_copper = currency_copper - 100 WHERE id = :buyer_id AND currency_copper >= 100 RETURNING currency_copper;

    -- Crédit du vendeur
    UPDATE characters SET currency_copper = currency_copper + 100 WHERE id = :seller_id;

    -- Transfert de propriété de l'objet
    UPDATE inventory_items SET character_id = :buyer_id, is_equipped = false WHERE id = :item_id AND character_id = :seller_id;

    -- Inscription au registre inaltérable
    INSERT INTO transactions (sender_id, receiver_id, amount, item_id, transaction_type, created_at)
    VALUES (:buyer_id, :seller_id, 100, :item_id, 'PLAYER_TRADE', NOW());

    COMMIT;
    ```
    Si l'une de ces opérations échoue (ex: l'acheteur n'a pas les fonds), un `ROLLBACK` est déclenché par le backend, annulant intégralement l'échange.

---

## 2. Architecture "Future-Proof" (Horizon 2030)

Pour assurer une évolutivité sans limite théorique (scalabilité massive et mondiale) et pour intégrer l'intelligence artificielle au cœur du *gameplay*, l'architecture migrera progressivement vers un modèle distribué et spécialisé.

### 2.1. Évolution des Données Persistantes : CockroachDB (NewSQL)

*   **L'Alternative Distribuée** : PostgreSQL sera migré vers **CockroachDB**. Ce SGBD NewSQL maintient une forte compatibilité avec la syntaxe PostgreSQL tout en automatisant le *sharding* (partitionnement des données) sur de multiples nœuds géographiques.
*   **Haute Disponibilité** : Il garantit une résilience totale. Un nœud (ou un data center) peut subir une défaillance sans provoquer d'interruption de service pour les joueurs.

### 2.2. Mémoire Sémantique de l'IA : Base Vectorielle (RAG)

Pour que les agents non-joueurs (PNJ) pilotés par des LLM agissent de manière organique et contextuelle, l'architecture requiert un moteur de mémoire sémantique.

*   **Outils Recommandés** : Qdrant, Milvus ou l'extension pgvector (si l'on reste dans un écosystème Postgres étendu).
*   **Fonctionnement (Embeddings)** :
    Au lieu de se limiter à un arbre de décision strict, chaque action marquante du joueur (un dialogue spécifique, une aide, un vol) est encodée sous forme de vecteur (Embedding) et stockée dans la base vectorielle.
*   **Recherche par Similarité** : Lorsqu'un joueur interagit de nouveau avec un PNJ, le serveur interroge la base via un calcul mathématique (ex: la distance cosinus). L'IA reçoit alors le contexte le plus pertinent ("Le joueur m'a vendu une épée rare hier") et génère une réponse appropriée.

---

## 3. Historique de Jeu, Télémétrie et Analytique

L'enregistrement de l'historique du jeu génère un volume d'écriture massif (télémétrie, actions de combat, déplacements). Mélanger ces données avec la base transactionnelle (PostgreSQL/CockroachDB) est une erreur critique de conception.

### 3.1. Base de Données Analytique : ClickHouse

*   **Choix Technologique** : **ClickHouse** (ou équivalent orienté colonnes). Il excelle dans l'ingestion massive de données (millions d'événements/seconde) et l'exécution d'agrégations lourdes.
*   **Modélisation Analytique (Tables)** :
    *   `combat_logs` : Dégâts, soins, sorts utilisés, type de monstres.
    *   `movement_telemetry` : Coordonnées temporelles permettant de tracer des *heatmaps* des zones saturées.
    *   `economy_ledger` : Vue macroscopique et quotidienne de l'inflation (création monétaire via le butin vs destruction monétaire via les taxes).
    *   `client_metrics` : Ping, framerate (FPS) moyen, version du client (pour le débuggage).

### 3.2. Flux de Données Asynchrone (Event-Driven)

Afin de garantir que le thread principal du serveur de jeu (*tickrate*) ne soit jamais ralenti par l'écriture de journaux :
1.  Le serveur de jeu émet des messages (événements) de manière non-bloquante.
2.  Ces événements transitent via un *message broker* (ex: Apache Kafka ou un système de *channels* natif en Rust).
3.  Des *workers* dédiés dépilent ces messages et effectuent des insertions groupées (*batch inserts*) dans ClickHouse.

---

## 4. Planification et Stratégie de Migrations

L'ajout continu de contenu dans un MMORPG implique des mutations de schéma régulières. Ces changements doivent s'opérer idéalement sans "Downtime" (arrêt des serveurs).

### 4.1. Gestionnaire de Migrations

*   **Méthodologie** : Tout changement de base de données est encodé dans des fichiers SQL versionnés (ex: `V001__create_users.sql`, `V002__add_guild_table.sql`).
*   **Outils** : Utilisation de `Flyway`, `Liquibase`, ou de crates spécifiques à l'écosystème Rust (`sqlx-cli`, `refinery`) pour appliquer ces scripts au démarrage ou via un pipeline CI/CD.

### 4.2. Pattern "Expand and Contract" (Zéro Interruption)

Pour modifier une table critique en production de façon transparente, la migration s'effectue en plusieurs étapes décorrelées :

1.  **Expand (Extension)** : Exécution de la migration SQL pour ajouter la nouvelle colonne/table (ex: un nouveau format de statistiques d'inventaire). L'ancien code n'est pas cassé.
2.  **Double Écriture (Déploiement Serveur)** : Mise en production d'une nouvelle version du serveur qui lit depuis l'ancienne structure, mais **écrit** en parallèle dans l'ancienne ET la nouvelle structure.
3.  **Backfill (Remplissage)** : Un script tourne en arrière-plan (sans surcharger la base) pour copier/convertir les données préexistantes vers la nouvelle structure.
4.  **Transition (Déploiement Serveur)** : Une fois les données synchronisées, déploiement d'une version du serveur qui lit et écrit **exclusivement** sur la nouvelle structure.
5.  **Contract (Nettoyage)** : Une ultime migration SQL supprime l'ancienne colonne/table devenue obsolète.
