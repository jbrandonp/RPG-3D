# Plan d'Action & Déroulement du Sprint 1 (Walking Skeleton)

Ce document définit la roadmap macroscopique du projet MMORPG "Horizon 2030" ainsi que le détail des tâches techniques et des livrables attendus pour le **Sprint 1**.

La documentation théorique étant intégralement validée et harmonisée, l'objectif actuel est de quitter la phase de conception pour entrer en phase de production technique.

---

## 1. Roadmap Macroscopique du Projet

La production est divisée en plusieurs grands jalons (Milestones), visant à prouver la faisabilité technique avant d'ajouter le contenu lourd (Assets, IA, Quêtes).

*   **Milestone 1 : Le "Walking Skeleton" (Sprint 1)**
    *   *Objectif :* Avoir un client capable de se connecter à un serveur headless, d'afficher un cube et de le déplacer avec synchronisation réseau de base.
*   **Milestone 2 : "First Blood" (Combat et Persistance)**
    *   *Objectif :* Intégration de la physique (Rapier3D), du calcul asymétrique d'armure, des attaques de base, et de la sauvegarde du joueur dans PostgreSQL.
*   **Milestone 3 : "Le Village" (Intégration Artistique)**
    *   *Objectif :* Remplacement des cubes par les assets 3D officiels (Low-poly PS2). Intégration du système de billboarding pour les particules et de l'audio 48 kHz.
*   **Milestone 4 : "Le Gardien" (Intégration IA / MCP)**
    *   *Objectif :* Intégration de la base vectorielle (Qdrant) et connexion d'un LLM via le protocole MCP pour gérer un PNJ interactif.

---

## 2. Plan du Sprint 1 : "Walking Skeleton"

**Durée estimée :** 2 semaines.
**Objectif principal :** Construire l'infrastructure fondamentale du moteur Bevy. Prouver que le paradigme "Client Terminal / Serveur Autoritaire" fonctionne.

### Épique 1 : Initialisation de l'Environnement (Workspace Rust)
*   **Tâche 1.1 :** Configurer le Cargo Workspace.
    *   Créer trois crates : `server` (backend headless), `client` (WGPU app), et `shared` (composants, événements et types réseau partagés).
*   **Tâche 1.2 :** Importer les dépendances de base.
    *   Ajouter `bevy` (configuré sans rendu pour le serveur).
    *   Ajouter les librairies de sérialisation (`serde`, `bincode`).

### Épique 2 : Infrastructure Réseau (UDP / QUIC)
*   **Tâche 2.1 :** Intégrer une solution réseau compatible Bevy (ex: `bevy_renet` ou implémentation QUIC/WebTransport custom via `quinn`).
*   **Tâche 2.2 :** Définir les protocoles dans le crate `shared`.
    *   Implémenter l'énumérateur `ClientCommand` (incluant `MovementInput` utilisant `bevy::math::Vec2`).
    *   Implémenter l'énumérateur `ServerResponse` (incluant `StateSnapshot`).
*   **Tâche 2.3 :** Établir la boucle de connexion.
    *   Le client peut initier un Handshake, le serveur peut attribuer un identifiant unique (NetworkId `u64`).

### Épique 3 : La Boucle de Gameplay Fondamentale (Déplacement)
*   **Tâche 3.1 :** Logique Serveur (Autorité).
    *   Créer le système `process_movement_commands`.
    *   Générer un `ServerResponse::StateSnapshot` envoyé à un *Tickrate* fixe (ex: 30 Hz).
*   **Tâche 3.2 :** Logique Client (Prédiction et Rendu).
    *   Instancier un `PbrBundle` minimal (une primitive "Cube") pour chaque entité connectée.
    *   Créer le système d'input local pour déplacer son propre cube immédiatement (Prédiction locale).
    *   Créer le système de réception réseau pour mettre à jour la position des autres joueurs et ajuster la sienne si le serveur détecte une désynchronisation (Rollback simple).

### Critères d'Acceptation (Definition of Done) du Sprint 1 :
- [ ] On peut lancer deux clients locaux et un serveur local.
- [ ] Les deux clients voient un cube.
- [ ] Lorsqu'un client appuie sur ZQSD / WASD, son cube bouge de manière fluide sur son écran.
- [ ] L'autre client voit le cube bouger avec un léger délai (Tickrate), confirmant que l'information transite par le serveur autoritaire.
- [ ] Aucune base de données ou IA n'est requise à cette étape.
