# Backlog d'Implémentation : Base de Données

Ce backlog liste les objectifs et tâches pour les sprints 1 à 3 (Pré-Alpha) ainsi que la vision à long terme pour la phase Post-Alpha (Horizon 2030). Le Sprint 0 est détaillé dans le fichier `SPRINT_0_DATABASE_SETUP.md`.

---

## 🚀 Sprint 1 : Core Tables & Sauvegarde Initiale
**Objectif :** Poser les bases de la persistance de l'univers avec l'authentification et l'état du personnage. "Le serveur se souvient de qui je suis et où je suis."
**Durée :** 2 semaines

**Tâches :**
*   [ ] Définir et implémenter les requêtes (via macros `sqlx::query!`) pour la création et la récupération des comptes (`users`).
*   [ ] Implémenter le système de création de personnages (`characters`) lié à un `user_id`.
*   [ ] Créer le `LoadSystem` (Bevy) : Au login, récupérer les données du personnage de manière asynchrone et générer l'entité Bevy correspondante.
*   [ ] Créer le `SaveSystem` (Bevy) de base : Écrire les fonctions pour sauvegarder la position et l'état du joueur lors de la déconnexion (`on_disconnect`).

---

## ⚔️ Sprint 2 : Gameplay Tables (Inventaire, Quêtes, Économie)
**Objectif :** Rendre le monde matériel persistant. Sauvegarder les objets, la progression de l'aventure et sécuriser les échanges monétaires.
**Durée :** 2 semaines

**Tâches :**
*   [ ] Intégrer les requêtes de chargement (`SELECT`) et de sauvegarde (`INSERT`/`UPDATE`) pour la table `inventory_items`.
*   [ ] Implémenter le suivi d'état des quêtes (`quests_progress`) avec une mise à jour sur événement (`on_quest_progress`).
*   [ ] **CRITIQUE :** Mettre en place le moteur de transaction économique. Écrire le code Rust qui encapsule un échange d'objet et d'argent entre deux joueurs au sein d'une transaction SQL atomique (`BEGIN` / `COMMIT`).
*   [ ] Créer la fonction d'historisation systématique dans la table `transactions` lors d'un échange validé.

---

## ⚙️ Sprint 3 : Optimisation & Sécurisation (Pre-Alpha Polish)
**Objectif :** Assurer que la base de données résistera aux premiers tests de charge (Alpha) et garantir l'intégrité des données à long terme.
**Durée :** 2 semaines

**Tâches :**
*   [ ] Validation et test des Index : Vérifier (via `EXPLAIN ANALYZE`) que les index définis (ex: `idx_characters_user_id`) sont bien utilisés lors des requêtes de login.
*   [ ] Développer le système de cache applicatif au démarrage : Charger les templates statiques (items, configs) en mémoire (Ressource Bevy) pour éviter de requêter la base inutilement.
*   [ ] Déployer le job de sauvegarde automatisé (Cron Job PostgreSQL) configuré pour un *pg_dump* toutes les 6 heures avec une rotation de 7 jours.
*   [ ] Test de résilience (Chaos testing basique) : Tuer le processus serveur en pleine transaction pour vérifier que le `ROLLBACK` SQL natif s'effectue correctement.

---

## 🔮 Backlog Post-Alpha (Architecture Horizon 2030)
**Objectif :** Transformer l'architecture d'instance unique en une infrastructure massivement scalable et "AI-Native".

**Épopeés (Epics) :**
*   **Scale-Out Relationnel :** Migrer la base PostgreSQL vers un cluster distribué **CockroachDB**. Appliquer les stratégies de *sharding* si la population le justifie.
*   **Observabilité Massive :** Déployer **ClickHouse** pour ingérer la télémétrie asynchrone (combat logs, heatmaps de déplacement, ledger économique) afin de ne plus surcharger la base principale.
*   **Intégration IA (RAG) :** Instancier une base vectorielle (**Qdrant / Milvus**) pour stocker les mémoires (embeddings) des interactions joueurs/PNJ et permettre au Model Context Protocol (MCP) d'alimenter les LLMs.
