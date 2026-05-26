# Plan d'Action et Roadmap de la Base de Données

## 1. Contexte et Objectifs
Le projet Horizon (MMORPG indépendant) adopte une architecture client/serveur autoritaire (Bevy/Rust). La stratégie de base de données privilégie la fiabilité, la simplicité initiale et la progression itérative avant toute complexité distribuée.

**Base de données cible pour les phases Pré-Alpha / Alpha :**
*   **Technologie :** PostgreSQL (instance unique bien monitorée)
*   **Outils de migration :** `sqlx-cli` (avec `sqlx` 0.7+ async en Rust)
*   **Scope :** Uniquement les données transactionnelles et l'état persistant du monde (comptes, personnages, inventaires, quêtes, économie).

**Architecture "Horizon 2030" (Backlog Post-Alpha) :**
*   Migration vers **CockroachDB** pour la distribution (Sharding automatique)
*   Implémentation de **ClickHouse** pour la télémétrie massive (logs, analytics)
*   Ajout de **Qdrant / Milvus** (Base vectorielle) pour la mémoire des IA (RAG)

## 2. Principes et Règles Critiques (Sprints 0-3)
Afin de prévenir la corruption des données et l'effondrement des performances :
1.  **Transactions Atomiques Obligatoires :** Toute opération touchant à l'économie (échanges, hôtels des ventes, taxes) ou à l'inventaire critique doit être encapsulée dans un `BEGIN ... COMMIT`. En Rust, on utilise `pool.begin().await?`.
2.  **Gestion Intelligente des Écritures :** Le client (et le serveur temps réel) garde les mouvements et l'état éphémère en mémoire. Les écritures en base (`INSERT` / `UPDATE`) se font exclusivement sur :
    *   Changement d'inventaire
    *   Progression de quête
    *   Mort du joueur / Déconnexion
    *   Checkpoint périodique
    *   Transaction économique
3.  **Mise en Cache Applicatif :** Les données lues fréquemment mais rarement modifiées (templates d'objets, configuration des zones, templates de quêtes) seront préchargées en mémoire (Ressource Bevy) au démarrage.

## 3. Schéma de Données Initial
Le modèle repose sur 5 tables principales et des index ciblés :
*   `users` : Gère l'authentification et les comptes.
*   `characters` : Gère l'état persistant d'un avatar (niveau, position sauvegardée, attributs).
*   `inventory_items` : Gère la possession et l'équipement des objets.
*   `quests_progress` : Suivi asynchrone des étapes de quêtes.
*   `transactions` : Registre inaltérable de tous les flux économiques.

*Les scripts SQL de création sont versionnés dans le dossier `/migrations/` pour garantir la reproductibilité.*

## 4. Architecture d'Intégration (Rust/Bevy)
L'intégration entre Bevy (ECS) et PostgreSQL s'effectue via un pool de connexions asynchrone hors de la boucle de jeu principale.

```text
[Bevy Headless Server]
     ↓
[DatabasePlugin (Ressource)]
     ├── PgPool (connection pool — ~10 connexions)
     ├── SaveSystem (écriture async sur événements Bevy)
     │   ├── on_inventory_change → INSERT/UPDATE inventory_items
     │   ├── on_quest_progress → UPDATE quests_progress
     │   ├── on_player_death → UPDATE characters
     │   ├── on_disconnect → UPDATE characters (position)
     │   └── on_transaction → INSERT transactions (atomique)
     └── LoadSystem (lecture async au login)
         ├── load_character → SELECT characters + inventory + quests
         └── cache_world_data → Données statiques en mémoire
```

## 5. Stratégie de Sauvegarde (Backup)
Une automatisation de la sauvegarde à chaud doit être planifiée très tôt :
*   **Dump complet :** `pg_dump` exécuté périodiquement (ex: toutes les 6 heures) via un Cron job.
*   **Rotation :** Les backups sont conservés 7 jours avant suppression automatique.
