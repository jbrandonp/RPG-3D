# Sprint Backlog : Prochaines Phases et Horizon 2030

Ce document dresse la liste des sprints futurs, depuis la finalisation du Proof of Concept (PoC) jusqu'à la vision globale et distribuée "Horizon 2030".

---

## 1. Phase PoC / Pré-Alpha (Suite)
**Durée des sprints :** 2 semaines (Agile)
**Stack :** Bevy Headless + TCP/UDP simple + PostgreSQL

### Sprint 2 : Persistance et Authentification (PostgreSQL)
- Intégration de `sqlx` dans la crate `server`.
- Création de la DB PostgreSQL locale.
- Création des tables `users` et `characters` avec des UUIDv7.
- Ajout d'une connexion TCP (ou un mini serveur HTTP) pour le processus de login avant de basculer en UDP pour le jeu.
- Charger la position du joueur depuis la base de données lors du login.

### Sprint 3 : Base de Combat (Attaques Multi-cibles / Cleave)
- Implémentation du système de hitbox sur le serveur (`CombatPlugin`).
- Calcul des dégâts et modification des points de vie (Serveur Autoritaire).
- Envoi des `CombatResolution` (Deltas réseau) vers les clients.
- Effets visuels (VFX) simples dans le `client` déclenchés par les events réseau.

### Sprint 4 : Télémétrie et Finalisation Pré-Alpha
- Intégration de logs avancés (Tracing).
- Polishing du dead-reckoning sur le `client` pour masquer les lags.
- Clôture de la phase : le jeu est jouable en local pour plusieurs joueurs sur une seule instance serveur (jusqu'à une charge validée par benchmarks).

---

## 2. Phase Alpha : Optimisations Réseau
**Durée des sprints :** 2 semaines (Agile)
**Stack :** Ajout de QUIC (Quinn) et WebTransport

### Sprint 5 & 6 : Remplacement du Réseau (QUIC & WebTransport)
- Remplacer le transport UDP/TCP de base par une implémentation `WebTransport` (over QUIC) via `wtransport` ou `quinn`.
- Configuration des streams : Streams fiables pour les transactions (achats, dégâts critiques), et Datagrams non fiables pour le mouvement.
- Tests de charge réseau.

### Sprint 7 & 8 : Économie "Ledger"
- Ajout du système d'idempotence (clés générées par le client) pour empêcher le rejeu et la triche.
- Stockage des transactions en DB avec isolation `SERIALIZABLE`.
- Gestion stricte de l'inventaire côté serveur.

---

## 3. Phase Bêta : Scalabilité Base de Données
**Format :** Milestones (1 à 3 mois)
**Stack :** PostgreSQL avec Réplication, Monitoring

### Milestone Bêta 1 : Réplication et Sécurité
- Mise en place d'une réplication PostgreSQL en lecture (Read-replicas).
- Mise en place d'un *Login Server* complètement séparé (stateless via JWT).

### Milestone Bêta 2 : Observabilité
- Intégration de Prometheus / Grafana.
- Traçabilité complète du backend (temps de calcul des ticks, latence DB).

---

## 4. Phase "Horizon 2030"
**Format :** Milestones Majeures
**Stack :** K8s, Agones, CockroachDB, Qdrant, ClickHouse, IA MCP

### Milestone H1 : Orchestration et NewSQL
- Conteneurisation du serveur Bevy (Docker).
- Déploiement d'un cluster Kubernetes + Agones pour la gestion des Game Servers à la volée.
- Migration de PostgreSQL vers CockroachDB (sans impact sur les requêtes `sqlx`).

### Milestone H2 : Analytics et Événements Macro
- Ajout de ClickHouse pour la télémétrie économique massive (asynchrone).
- Création du pipeline Data.

### Milestone H3 : Intelligence Artificielle et MCP
- Intégration du serveur MCP pour exposer le contexte de jeu aux agents LLM.
- Mise en place de Qdrant (Base Vectorielle) pour le RAG des PNJ.
- Implémentation du système de "Gatekeeper" (Sandboxing) qui valide les opérations MCP initiées par l'IA (ex: spawn d'entités, ajustement économique) en garantissant la sécurité transactionnelle.
