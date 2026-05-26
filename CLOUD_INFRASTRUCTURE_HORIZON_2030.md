# High-Level Architecture (HLA) : Infrastructure Cloud Horizon 2030 (AI-Native MMO)

Ce document définit l'architecture cible et la stratégie d'infrastructure cloud (Horizon 2030) pour le projet MMORPG. Conçu selon les principes de **Cloud-Agnosticisme**, de **Haute Disponibilité (HA)** et d'**Observabilité Globale**, ce document fait autorité sur les choix techniques régissant l'écosystème serveur, les bases de données, l'intégration de l'intelligence artificielle et la sécurité opérationnelle.

---

## 1. Topologie Réseau et Architecture Multi-Régions

Pour garantir une faible latence aux joueurs du monde entier et une résilience face aux pannes locales, l'infrastructure repose sur une architecture **Multi-Régions Active-Active**.

### 1.1. Modèle de Distribution Géographique
*   **Edge Network & Global Load Balancing :** Utilisation d'un CDN (ex: Cloudflare) et d'un Global Load Balancer (Anycast) pour router le trafic TCP/UDP et HTTPS des joueurs vers la région la plus proche.
*   **Régions Actives :** Déploiement sur plusieurs grandes plaques géographiques (ex: NA-East, EU-Central, AP-Northeast). Chaque région est autonome pour le traitement du jeu en temps réel.
*   **Virtual Private Cloud (VPC) & Sous-réseaux :** Chaque région dispose d'un VPC segmenté selon le principe du moindre privilège :
    *   **Public Subnets :** Load Balancers, API Gateways, Ingress Controllers.
    *   **Private Subnets (Compute) :** Clusters Kubernetes (microservices) et pools Agones (serveurs de jeu). Pas d'IP publique, accès via NAT Gateway.
    *   **Private Subnets (Data) :** Clusters de bases de données (CockroachDB, Qdrant). Accès strictement limité aux sous-réseaux Compute.

### 1.2. Service Mesh et Isolation
*   **Service Mesh (Istio / Linkerd) :** Déployé sur tous les clusters Kubernetes pour gérer le routage du trafic interne, implémenter le **mTLS (Mutual TLS)** par défaut entre tous les microservices, et fournir des métriques réseau granulaires.
*   **Network Policies (Calico / Cilium) :** Règles strictes définissant quels pods peuvent communiquer ensemble (ex: isolation totale entre les namespaces du jeu, de l'authentification et de l'analytique).

---

## 2. Orchestration et Serveurs de Jeu (Compute)

La séparation des préoccupations est stricte entre les services web (stateless) et la simulation de jeu (stateful).

*   **Kubernetes (K8s) :** Orchestrateur standardisé pour les microservices (Authentification, Matchmaking, Économie, IA Gateways). Les configurations sont indépendantes des fournisseurs cloud (EKS, GKE, AKS, ou Bare-Metal K8s).
*   **Agones (Game Server Management) :** Extension K8s dédiée au cycle de vie des serveurs de jeu Bevy (Rust, headless).
    *   **Autoscaling Dynamique :** Gestion des *Fleets* Agones basée sur des webhooks de matchmaking. Allocation de *GameServer* conteneurisés par instance/donjon.
    *   **Gestion du cycle de vie stateful :** Marquage des serveurs "En cours de partie" pour empêcher l'éviction par K8s lors d'opérations de maintenance (draining).
*   **Trafic Temps Réel :** Les clients s'y connectent via **QUIC / WebTransport**, permettant un multiplexage fiable ou non fiable avec une latence optimale, contournant le *Head-of-Line Blocking* du TCP.

---

## 3. Architecture des Données (Persistence Layer)

L'architecture s'appuie sur le paradigme **Polyglot Persistence**, chaque moteur de base de données étant choisi pour son profil de performance spécifique.

*   **Données Transactionnelles Cœur (CockroachDB) :**
    *   *Usage :* Identités, Inventaires, Transactions économiques.
    *   *Rôle :* NewSQL distribué garantissant une forte cohérence (ACID) à l'échelle globale. Les données des joueurs sont "épinglées" dans la région où ils jouent principalement pour minimiser la latence en écriture, tout en restant accessibles globalement.
*   **Mémoire Sémantique et IA (Qdrant / Milvus) :**
    *   *Usage :* Contexte des PNJ, historiques conversationnels (RAG - Retrieval-Augmented Generation).
    *   *Rôle :* Base de données vectorielle permettant la recherche par similarité cosinus avec une très faible latence (< 10ms) pour alimenter les agents IA.
*   **Télémétrie, Analytique et Logs d'Audit (ClickHouse) :**
    *   *Usage :* Analyse des comportements, détection de triche, logs système massifs.
    *   *Rôle :* Moteur OLAP orienté colonnes, capable d'ingérer et de requêter des millions de lignes par seconde.

---

## 4. Stratégie d'Intelligence Artificielle Hybride

Afin de combiner contrôle des coûts, confidentialité et capacités de pointe, l'infrastructure IA adopte une approche mixte.

*   **IA Interne (On-Premise / Hosted LLMs) :**
    *   Déploiement de modèles Open Source (ex: Llama 3, Mistral) sur des *Node Pools* Kubernetes dédiés équipés d'accélérateurs matériels (GPU).
    *   Utilisés pour des tâches massives et récurrentes (génération de PNJ mineurs, analyse de sentiment en temps réel, équilibrage dynamique) où le coût par token serait prohibitif chez un fournisseur externe.
*   **IA Externe (API Provider) :**
    *   Intégration d'API externes de pointe (OpenAI, Anthropic) réservées à des tâches complexes (génération de quêtes épiques, PNJs cruciaux nécessitant un haut raisonnement).
*   **AI API Gateway (ex: LiteLLM) :**
    *   Une gateway applicative unifie l'accès à ces modèles (internes et externes) pour le backend. Elle gère le routage, le cache sémantique, le rate limiting et l'observabilité des requêtes.

---

## 5. Haute Disponibilité (HA) et Plan de Reprise d'Activité (PRA)

La pérennité des données est assurée par des objectifs de résilience stricts mesurés via le **RTO** (Recovery Time Objective) et le **RPO** (Recovery Point Objective).

*   **HA et Tolérance aux pannes :**
    *   La perte d'une zone de disponibilité (AZ) au sein d'une région est transparente (failover automatique de CockroachDB et K8s).
    *   La perte d'une région entière redirige automatiquement les nouveaux joueurs vers la région survivante la plus proche.
*   **Plan de Sauvegarde et PRA :**
    *   **Bases Transactionnelles (RPO < 5 minutes, RTO < 1 heure) :** Sauvegardes continues dans le stockage objet (S3) et Point-in-Time Recovery (PITR) natif de CockroachDB permettant de rembobiner l'état exact de l'économie avant un incident.
    *   **Données Non-Critiques (Vector/Analytique) (RPO = 24 heures) :** Snapshots journaliers stockés à froid.
    *   **Infrastructure as Code (IaC) :** Toute l'infrastructure (Terraform) et le déploiement applicatif (ArgoCD / GitOps) peuvent être re-déployés *from scratch* dans une région vierge en moins de 30 minutes.

---

## 6. Observabilité Globale (Monitoring & Tracing)

L'opérabilité de cette architecture complexe est garantie par une pile d'observabilité centralisée.

*   **Collecte Unifiée :** Les agents **OpenTelemetry** déploient la télémétrie sur tous les conteneurs (traces distribuées, logs, métriques).
*   **Surveillance et Alerting :**
    *   **Prometheus** (métriques de l'infrastructure et de l'applicatif).
    *   **Grafana** (tableaux de bord unifiés, SLOs, SLIs). Alerting configuré via PagerDuty / Slack pour les seuils critiques (CPU/RAM des serveurs Bevy, latence P99).
*   **Traçabilité Distribuée :** Utilisation de **Jaeger** ou Tempo pour suivre le cycle de vie complet d'une requête, du client jusqu'aux appels des API LLM.

---

## 7. Sécurité Opérationnelle (SecOps)

Une architecture intégrant des agents IA requiert une sécurité de type *Zero Trust*.

*   **Périmètre et Protection Edge :** WAF (Web Application Firewall) et protection DDoS multi-couches gérés par le CDN.
*   **Gestion des Identités et des Secrets :**
    *   **HashiCorp Vault :** Injection dynamique de credentials éphémères pour les accès à la base de données (zéro mot de passe statique).
    *   IAM strict via Kube2IAM / Workload Identity pour limiter les accès aux buckets S3 et autres ressources cloud.
*   **Sandboxing IA et Contrôle d'Intégrité :**
    *   Les modèles IA utilisent le protocole **MCP (Model Context Protocol)** pour s'interfacer avec le moteur de jeu.
    *   *Principe de validation forte :* Les intentions générées par l'IA (transferts d'objets, altérations du monde) sont systématiquement validées par la logique autoritaire (Rust) du serveur Bevy. L'IA ne possède aucune permission d'écriture directe en base de données.
*   **Pipeline DevSecOps :** Scan continu des images Docker (Trivy), analyse statique de code (SAST), et vérification de la configuration Kubernetes (Checkov) intégrés au CI/CD.
