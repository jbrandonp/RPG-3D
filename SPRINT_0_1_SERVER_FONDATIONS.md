# Sprints 0 & 1 : Fondations Serveur (PoC Pré-Alpha)

Ce document décrit en détail les tâches pour les deux premiers sprints du projet, avec pour but d'établir une base saine (architecture "Client Terminal", Serveur Autoritaire).

## Sprint 0 : Initialisation et Déploiement Headless (Durée: 2 semaines)

**Objectif :** Obtenir un projet compilable séparant la logique serveur, client et partagée. Le serveur Bevy Headless doit démarrer et tourner à 20 TPS sans interface graphique.

### Tâches :
1. **Initialisation du Workspace Cargo**
   - Créer le fichier `Cargo.toml` à la racine pour définir le workspace avec trois crates : `server`, `client`, et `shared`.
   - `shared` : contiendra les composants ECS (`Position`, `Velocity`, `Health`) et les structures de messages (sérialisation `bincode`).
   - `server` : contiendra la boucle principale Bevy (Headless), dépendances `tokio`, `sqlx`.
   - `client` : contiendra le jeu visuel Bevy avec les dépendances d'affichage standard (WGPU).
2. **Implémentation de `shared`**
   - Définir `struct Position(Vec3)`.
   - Définir les messages réseau de base (`ClientMessage::Move`, `ServerMessage::StateSnapshot`).
3. **Mise en place de `server`**
   - Démarrer une `App` Bevy.
   - Configurer le plugin `ScheduleRunnerPlugin` pour un fonctionnement headless avec un run loop fixé à 20 TPS (Tick = 50ms).
   - Ajouter un log basique vérifiant que le serveur "tick" correctement.
4. **Mise en place de `client`**
   - Démarrer une `App` Bevy avec rendu par défaut.
   - Intégrer une caméra basique.

---

## Sprint 1 : Réseau Basique (TCP/UDP) et Premier Mouvement (Durée: 2 semaines)

**Objectif :** Permettre à un client de se connecter au serveur. Le client envoie une commande de mouvement, le serveur la valide, applique la formule de tick, et renvoie la nouvelle position.

### Tâches :
1. **Socket Serveur (TCP/UDP)**
   - Intégrer un système de socket basique (via `tokio-net` / UDP) côté serveur pour écouter les paquets entrants.
2. **Socket Client**
   - Configurer le client pour envoyer des messages UDP formatés (via `bincode` / `shared`).
3. **Simulation Serveur (Authoritative Movement)**
   - Le serveur reçoit `ClientMessage::Move(direction)`.
   - Le serveur met à jour `InputBuffer` de l'entité concernée.
   - Le système de Tick du serveur applique : $S_t = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_t)$.
   - *(Validation Anti-Triche)* : S'assurer que le déplacement respecte la `move_speed` définie dans `CharacterStats`.
4. **Replication vers le Client**
   - Le serveur envoie `ServerMessage::StateSnapshot` en UDP vers le client à chaque tick.
   - Le client lit le snapshot et met à jour la position visuelle de l'entité locale (application basique de dead-reckoning).
