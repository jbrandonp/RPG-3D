# 🛠 Sprint 0 : Database Setup (Fondation)

**Durée estimée :** 2 semaines
**Objectif principal :** Disposer d'un environnement PostgreSQL fonctionnel, capable d'exécuter des migrations via `sqlx-cli`, et correctement connecté au serveur de jeu Bevy.

Ce sprint est crucial : c'est la mise en place de la fondation technique ("Mauvais schéma = sauvegardes cassées"). Une attention particulière doit être portée sur l'environnement de développement.

---

## 📅 Planification Jour par Jour

### Semaine 1 : Infrastructure & Outillage

**Jour 1-2 : Installation et configuration de PostgreSQL**
*   Installer PostgreSQL (en local ou via Docker).
*   Créer l'utilisateur (rôle) dédié au jeu (ex: `horizon_server`).
*   Créer la base de données (ex: `elaras_black_mist`) avec les droits appropriés.
*   *Validation :* Pouvoir se connecter à la base de données via psql ou pgAdmin avec les credentials créés.

**Jour 3-4 : Configuration de sqlx et sqlx-cli**
*   Installer l'outil en ligne de commande : `cargo install sqlx-cli --no-default-features --features rustls,postgres`.
*   Configurer la variable d'environnement `DATABASE_URL` (dans un fichier `.env`).
*   Initialiser la structure de la base via la commande `sqlx database create`.
*   Tester la création du dossier migrations (déjà effectué : `migrations/`).

**Jour 5 : Exécution de la Migration Initiale (001)**
*   Lancer la commande `sqlx migrate run` pour exécuter le script `001_create_users.sql`.
*   Vérifier dans la base de données que la table `users` est correctement créée.

### Semaine 2 : Intégration Bevy & Code Rust

**Jour 6-7 : Ajout des Dépendances Rust**
*   Ajouter `sqlx` (avec les features `runtime-tokio-rustls`, `postgres`, `uuid`, `chrono`, `macros`) au fichier `Cargo.toml`.
*   S'assurer que `tokio` est configuré correctement pour supporter l'exécution asynchrone au sein de Bevy.

**Jour 8-9 : Création du DatabasePlugin (Bevy)**
*   Créer un plugin Bevy `DatabasePlugin`.
*   Initialiser un pool de connexion PostgreSQL (`sqlx::PgPoolOptions::new().max_connections(10).connect(&db_url).await`).
*   Injecter le `PgPool` dans le monde Bevy en tant que `Resource`.
*   *Validation :* Le serveur Bevy démarre, établit le pool de connexions avec succès et ne crash pas.

**Jour 10 : Requête de test Async ("Hello Database")**
*   Créer un système temporaire de test au démarrage (`Startup` system).
*   Utiliser la macro `sqlx::query!` pour insérer un utilisateur factice dans la table `users` et le relire immédiatement en console.
*   *Validation :* La macro compile correctement (vérification syntaxique au compile-time) et l'exécution insère bien la donnée en base.

---

## 🎯 Critères d'Acceptation (Definition of Done)
* [ ] Une base PostgreSQL locale/Docker tourne et accepte les connexions.
* [ ] Les variables d'environnement (`.env`) sont configurées.
* [ ] La commande `sqlx migrate run` exécute la migration sans erreur.
* [ ] Le serveur Bevy démarre et instancie la ressource `PgPool` sans paniquer.
* [ ] Une requête `INSERT`/`SELECT` factice via `sqlx` fonctionne dans le code Rust et passe la validation au moment de la compilation.
