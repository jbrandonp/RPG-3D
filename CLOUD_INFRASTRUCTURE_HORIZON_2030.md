# Plan d'Infrastructure Cloud : Horizon 2030 (AI-Native & Hautes Performances)

Ce document définit la vision d'infrastructure cloud cible (Horizon 2030) pour le MMO. L'architecture est pensée pour être **cloud-agnostique** (pouvant tourner sur AWS, Google Cloud, Azure ou du bare-metal Kubernetes) afin de garantir la souveraineté des données, la flexibilité des coûts et la scalabilité massive requise par l'intégration d'IA.

---

## 1. Architecture Cloud Globale et Serveurs

Le système repose sur un cluster orchestré dynamiquement, séparant clairement les services web/API des serveurs de jeu en temps réel.

*   **Orchestration :** **Kubernetes (K8s)**
    *   Le standard de facto de l'industrie. Permet de déployer, gérer et mettre à l'échelle tous les conteneurs du projet indépendamment du fournisseur Cloud (EKS, GKE, AKS, ou clusters auto-hébergés).
*   **Orchestration Serveurs de Jeu :** **Agones** (sur Kubernetes)
    *   Agones (développé par Google et Ubisoft) est l'outil parfait pour gérer les serveurs de jeu stateful en mémoire (Bevy headless en Rust).
    *   **Fleets & Autoscaling :** Agones gère des flottes de serveurs de jeu, allouant de nouveaux conteneurs Bevy à la volée en fonction de la population en jeu et du matchmaking, et les détruisant quand ils sont vides pour économiser les coûts.
*   **Communication & Réseau :**
    *   **Ingress Controller / API Gateway :** Nginx ou Traefik pour gérer le trafic HTTPS (authentification, requêtes API web).
    *   **Jeu Temps Réel :** Connexions QUIC ou WebTransport directement orientées vers les Game Servers alloués par Agones, minimisant la latence et contournant le head-of-line blocking du TCP.

---

## 2. Bases de Données et Stockage

L'architecture de données abandonne le modèle monolithique pour une approche polyglotte, adaptée aux très hauts débits et à l'IA.

*   **Données Transactionnelles (Personnages, Inventaires, Monnaie) :** **CockroachDB**
    *   Type : NewSQL distribué.
    *   Pourquoi : Garantit l'intégrité transactionnelle stricte (ACID) sans point de défaillance unique (SPOF). Si un nœud tombe, le jeu continue. Parfait pour l'économie critique du jeu.
*   **Mémoire IA et RAG (Souvenirs des PNJ) :** **Qdrant** ou **Milvus**
    *   Type : Base de données vectorielle.
    *   Pourquoi : Permet aux agents IA de requêter le contexte sémantique (via Similarité Cosinus) ultra-rapidement pour générer des réponses pertinentes.
*   **Logs Analytiques & Télémétrie Massive :** **ClickHouse**
    *   Type : Base de données orientée colonnes.
    *   Pourquoi : Conçu pour ingérer des millions d'événements par seconde (déplacements, statistiques de combat). Essentiel pour analyser les tricheurs et équilibrer le jeu.
*   **Stockage des Assets et Sauvegardes Froids :** **Stockage Objet compatible S3** (ex: MinIO, AWS S3)

---

## 3. Déploiements (CI/CD)

La philosophie est le **GitOps** : Git est la seule source de vérité pour le code et l'infrastructure.

*   **Intégration Continue (CI) :** **GitHub Actions** ou **GitLab CI**
    *   Build des binaires Rust (serveur Bevy et client).
    *   Exécution des tests unitaires, d'intégration, et des linters de sécurité.
    *   Création des images Docker (distroless pour réduire la surface d'attaque) et poussée vers un Container Registry privé.
*   **Déploiement Continu (CD) :** **ArgoCD**
    *   ArgoCD tourne dans Kubernetes, surveille le dépôt Git de configuration, et synchronise automatiquement l'état du cluster avec la configuration déclarée (YAML/Helm).
    *   Permet le déploiement de type "Blue/Green" ou "Canary" pour mettre à jour les API ou les serveurs de jeu sans interruption pour les joueurs existants.

---

## 4. Stratégie de Sauvegardes (Backups)

La donnée des joueurs est le cœur du MMO. La stratégie doit être paranoïaque.

*   **Base Transactionnelle (CockroachDB) :**
    *   **PITR (Point-in-Time Recovery) :** Activé par défaut. Permet de restaurer la base à la seconde près sur une fenêtre glissante (ex: 7 jours) en cas de corruption logique (ex: un bug duplique des objets).
    *   **Backups complets quotidiens :** Exportés de manière chiffrée vers un bucket S3.
*   **Base Vectorielle et Analytique :**
    *   Snapshots réguliers (toutes les 6 à 12 heures) vers le bucket S3. Si la donnée analytique d'une heure est perdue, c'est moins grave qu'un inventaire joueur.
*   **Plan de Reprise d'Activité (PRA) :**
    *   Les backups S3 doivent être répliqués de manière asynchrone dans une autre région géographique. (ex: Région principale à Paris, backup PRA à Francfort).

---

## 5. Surveillance (Logs & Monitoring)

Impossible de gérer un MMO sans observabilité complète, d'autant plus avec des agents IA agissant en autonomie.

*   **Collecte Unifiée :** **OpenTelemetry**
    *   Standardise la collecte des traces, métriques et logs générés par les serveurs Rust et les bases de données.
*   **Métriques et Alerting :** **Prometheus** + **Grafana**
    *   Prometheus agrège les données de performance (CPU/RAM des serveurs Bevy, latence QUIC, TPS de CockroachDB).
    *   Grafana visualise ces données. Des alertes (vers Slack ou PagerDuty) sont configurées (ex: si le délai de création d'un conteneur Agones > 5 secondes, ou si le CPU global > 80%).
*   **Logs Centralisés :** **Loki** (Grafana Stack) ou **ELK** (Elasticsearch Logstash Kibana)
    *   Tous les serveurs envoient leurs logs stdout/stderr vers Loki. Les logs sont indexés pour une recherche rapide. Crucial pour tracer les décisions des agents IA (auditabilité).

---

## 6. Mises à Jour (Patch Management)

Les mises à jour d'un MMO "AI-Native" se font sur plusieurs plans :

1.  **Mises à jour Client (WGPU) :** Les joueurs téléchargent un nouveau binaire. Rétrocompatibilité requise pendant les transitions.
2.  **Mises à jour Serveur de Jeu (Agones) :** Les nouvelles versions sont déployées sur de nouvelles flottes de serveurs. Les instances existantes (avec des joueurs actifs) ne sont pas tuées ; elles se drainent naturellement quand les joueurs se déconnectent.
3.  **Mises à jour IA (Modèles LLM) :** Les agents IA via MCP sont mis à jour côté serveur sans impacter le jeu, comme des microservices indépendants.
4.  **Mises à jour Schéma BDD :** Gérées par des outils de migration (ex: Flyway ou Liquibase intégré au CI), sans lock de table bloquant, supporté nativement par CockroachDB.

---

## 7. Sécurité Opérationnelle

Un MMO est une cible constante (DDoS, triche, exploitation économique). L'ajout d'IA augmente la surface d'attaque (Prompt Injection).

*   **Protection DDoS et WAF :** Un service comme Cloudflare (mode TCP/UDP proxy pour le jeu) ou AWS Shield pour absorber les attaques massives en périphérie du réseau.
*   **Zero Trust & Gestion des Secrets :** **HashiCorp Vault** ou le Secret Manager du Cloud.
    *   Aucun mot de passe de base de données en clair dans le code. Rotation automatique des credentials.
    *   Chaque pod Kubernetes tourne avec le minimum de privilèges IAM nécessaires.
*   **Sécurité des IA (Sandboxing) :**
    *   Les agents IA communiquant via MCP n'ont *aucun droit de modification direct* en base de données. Ils génèrent des *intentions* (ex: "donner 10 pièces d'or à X") qui sont vérifiées par les règles autoritaires du serveur Bevy en Rust (validation de limites de taux, de contexte).
*   **Rate Limiting :** Imposé strict aux niveaux réseau et applicatif, à la fois pour les joueurs (spam de requêtes) et pour les appels coûteux aux API LLM.
