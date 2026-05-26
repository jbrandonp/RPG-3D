# Plan d'Action - Architecture Serveur (Projet Horizon)

Ce document centralise l'analyse de l'architecture serveur et la roadmap globale du développement, allant de la phase de validation (PoC / Pré-Alpha) jusqu'au déploiement final "Horizon 2030" basé sur l'IA et Kubernetes.

## 1. Principes Architecturaux et Règles d'Or

### 1.1. Serveur Autoritaire et Architecture "Client Terminal"
L'infrastructure sépare totalement la simulation logique de la représentation graphique :
- **Serveur (Bevy ECS Headless) :** C'est le détenteur exclusif de la vérité ("Autorité"). Il calcule les déplacements (à 20 TPS), vérifie les collisions, et arbitre le combat. Toute input client est validée.
- **Client (Bevy WGPU) :** Il s'agit d'un "terminal" d'affichage. Il utilise la prédiction locale (dead-reckoning) pour masquer la latence, mais le serveur aura toujours le dernier mot et appliquera un *rubberbanding* en cas de triche ou de forte désynchronisation.
- **Shared (Crate Partagée) :** Les définitions des composants ECS (ex: `Position`, `Health`) et les payloads réseau (sérialisés avec `bincode`) sont placés dans une crate partagée pour éviter toute désynchronisation entre client et serveur.

### 1.2. Architecture Évolutive, mais Pragmatique
L'architecture finale "Horizon 2030" (Kubernetes, CockroachDB, IA MCP) est extrêmement complexe. Pour éviter la paralysie :
- **Phase PoC :** Une seule instance serveur, TCP/UDP basique, PostgreSQL classique. Cela peut supporter des centaines de joueurs simultanés sans problème.
- **Phase Alpha :** Bascule sur un réseau moderne (QUIC / WebTransport).
- **Phase Horizon 2030 :** Déploiement distribué massif (K8s) et IA.

### 1.3. La Formule du Tick Serveur
La boucle de jeu (Tick) est fixée à **20 TPS (Δt = 50ms)**.
$$S_t = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_t)$$

## 2. Roadmap et Progression des Phases

| Phase | Stack Technique | Sprints | Objectif Principal |
|-------|-----------------|---------|--------------------|
| **PoC Pré-Alpha** | Bevy Headless + TCP/UDP simple + PostgreSQL + Tokio | 0 - 4 | Validation du socle technique, mouvement, persistance basique. |
| **Alpha** | + Quinn (QUIC) / WebTransport + Optimisations PostgreSQL | 5 - 8 | Netcode solide, intégration des mécaniques hybrides (combat). |
| **Bêta** | Réplication PostgreSQL + Monitoring avancé | 9 - 12 | Préparation à l'échelle, tests en charge. |
| **Horizon 2030** | Kubernetes, Agones, CockroachDB, Qdrant, ClickHouse, IA MCP | 13+ | Architecture distribuée complète, agents PNJ IA autonomes. |

---

*Voir `SPRINT_0_1_SERVER_FONDATIONS.md` pour le démarrage immédiat.*
*Voir `SPRINT_BACKLOG_ARCHITECTURE.md` pour la vision à long terme.*
