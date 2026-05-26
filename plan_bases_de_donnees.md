# Plan d'Architecture : Bases de Données, Migrations, Index et Historiques (MMORPG)

Ce document détaille l'architecture complète des bases de données de notre MMORPG, incluant la conception du schéma, les stratégies d'indexation, la gestion des transactions, et la planification des migrations. Il couvre à la fois l'architecture initiale pour un lancement maîtrisé et l'architecture "Future-Proof" pilotée par l'IA.

---

## 1. Architecture Initiale (PostgreSQL)

Pour les phases d'Alpha, Bêta et le lancement initial, **PostgreSQL** est le choix privilégié. Il offre robustesse, respect des contraintes ACID, et est parfaitement adapté pour structurer les données transactionnelles d'un MMORPG.

### 1.1. Schéma Relationnel (Modèle de Données)

L'univers persistant s'articulera autour des tables principales suivantes :

*   **`users`** : Gère les comptes, l'authentification et les métadonnées globales.
    *   *Colonnes types* : `id`, `username`, `email`, `password_hash`, `created_at`, `status`.
*   **`characters`** : Stocke les personnages liés aux comptes.
    *   *Colonnes types* : `id`, `user_id`, `name`, `level`, `experience`, `class`, `health`, `mana`, `position_x`, `position_y`, `position_z`, `zone_id`.
*   **`inventory_items`** : Représente les objets stockés ou équipés.
    *   *Colonnes types* : `id`, `character_id`, `item_template_id`, `quantity`, `durability`, `is_equipped`, `slot_id`.
*   **`quests_progress`** : Suivi asynchrone des quêtes.
    *   *Colonnes types* : `id`, `character_id`, `quest_id`, `status` (active/completed/failed), `objectives_json`, `started_at`, `completed_at`.
*   **`skills`** : Compétences et talents débloqués.
    *   *Colonnes types* : `id`, `character_id`, `skill_id`, `level`, `cooldown_expires_at`.
*   **`guilds`** : Gestion des groupes de joueurs.
    *   *Colonnes types* : `id`, `name`, `tag`, `leader_id`, `created_at`.
*   **`guild_members`** : Associations entre personnages et guildes.
    *   *Colonnes types* : `guild_id`, `character_id`, `rank`, `joined_at`.
*   **`friends`** : Relations sociales.
    *   *Colonnes types* : `character_id_1`, `character_id_2`, `status` (pending/accepted).
*   **`transactions`** : Historique financier (Hôtel des ventes, commerce direct).
    *   *Colonnes types* : `id`, `sender_id`, `receiver_id`, `currency_type`, `amount`, `item_id`, `timestamp`.

### 1.2. Indexation Stratégique

L'indexation permet de maintenir des performances de lecture optimales.
*   **Recherches directes** : Index UNIQUE sur `users(email)`, `users(username)`, `characters(name)`, `guilds(name)`.
*   **Clés étrangères** : Index sur toutes les clés de liaison (`characters(user_id)`, `inventory_items(character_id)`).
*   **Recherches composées** : Index `(character_id, is_equipped)` sur `inventory_items` pour charger rapidement l'équipement au login. Index `(character_id, status)` sur `quests_progress`.
*   **Tri et Historique** : Index B-Tree sur `transactions(created_at)` pour la pagination.

### 1.3. Gestion des Transactions (Atomiques)

Toute modification touchant à l'économie ou au transfert d'objets doit se faire au sein de transactions ACID.
*   **Commerce entre joueurs** :
    ```sql
    BEGIN;
    UPDATE characters SET gold = gold - 100 WHERE id = :buyer_id AND gold >= 100;
    UPDATE characters SET gold = gold + 100 WHERE id = :seller_id;
    UPDATE inventory_items SET character_id = :buyer_id WHERE id = :item_id AND character_id = :seller_id;
    INSERT INTO transactions (sender_id, receiver_id, amount, item_id) VALUES (...);
    COMMIT;
    ```
*   **Anti-triche** : Le serveur est totalement autoritaire. Il vérifie l'existence des fonds et des objets avant d'exécuter la transaction en base.

---

## 2. Architecture Future-Proof (Horizon 2030)

Pour pallier aux limitations d'une base unique lors du passage à l'échelle mondiale, l'infrastructure migrera vers un système distribué et polyglotte.

### 2.1. Données Persistantes : CockroachDB (NewSQL)

*   **Remplacement de PostgreSQL** : CockroachDB permet le *sharding* transparent tout en conservant le SQL et l'intégrité transactionnelle.
*   **Survie aux pannes** : Les nœuds peuvent tomber sans affecter la disponibilité, idéal pour un MMO "Always-Online".

### 2.2. Mémoire Sémantique (Base Vectorielle)

*   **Outils** : Qdrant ou Milvus.
*   **Rôle** : Servir de cerveau aux agents IA (PNJ).
*   **Fonctionnement** : Au lieu d'arbres de dialogue statiques, les interactions génèrent des embeddings. Lors d'un dialogue, l'IA interroge la base via "Similarité Cosinus" pour retrouver un événement passé (ex: "Le joueur m'a sauvé des loups niveau 12") et générer un texte adapté.

---

## 3. Historique de Jeu, Télémétrie et Analytique

Il est vital de séparer les bases de production (jeu) des bases analytiques pour éviter la surcharge.

### 3.1. Base Analytique : ClickHouse

*   **Outil** : ClickHouse (Base orientée colonnes).
*   **Rôle** : Absorber des millions d'événements par seconde sans impacter le jeu.
*   **Tables Analytiques** :
    *   `combat_logs` : Dégâts infligés/reçus, sorts utilisés.
    *   `movement_telemetry` : Heatmaps des joueurs.
    *   `economy_ledger` : Vue macroscopique de la création et destruction de monnaie (faucets/sinks).

### 3.2. Flux de données asynchrone

Le serveur de jeu envoie les logs sous forme d'événements asynchrones vers un broker (ex: Kafka ou un bus interne en Rust) qui déverse ensuite les données en batch dans ClickHouse. Ainsi, les latences d'insertion analytiques n'impactent jamais le *tickrate* du serveur.

---

## 4. Stratégie de Migrations

Gérer un MMORPG signifie que la structure des données va muter constamment, idéalement sans interrompre le service ("Zero-Downtime Migration").

### 4.1. Outils de Migration

*   Utilisation d'outils versionnés (`sqlx-cli` ou `refinery` si le backend est en Rust, ou `Flyway`).
*   Les scripts sont structurés en `UP` et `DOWN` (ex: `V1__init.sql`, `V2__add_guilds.sql`).

### 4.2. Approche Zero-Downtime (Expand & Contract)

1.  **Phase Expand** : Ajout des nouvelles colonnes/tables (ex: `new_inventory_system`) sans supprimer l'ancien code.
2.  **Double Écriture** : Mise à jour du serveur. Le serveur écrit dans l'ancienne et la nouvelle structure en parallèle.
3.  **Backfill** : Un script migre les anciennes données vers la nouvelle structure en arrière-plan.
4.  **Basculement** : Le serveur ne lit plus que la nouvelle structure.
5.  **Phase Contract** : Un dernier script de migration supprime l'ancienne colonne/table devenue inutile.
