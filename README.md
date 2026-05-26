# Guide complet : Créer un MMORPG indépendant

---

## 1. Les 8 blocs fondamentaux

### Bloc 1 — Vision du jeu

Avant de coder quoi que ce soit, tu dois fixer : le style du monde, la caméra, le type de combat, le nombre de joueurs visé, le ton visuel et ce qui rend ton jeu unique. Sans ça, tu risques de coder des systèmes inutiles.

### Bloc 2 — Gameplay de base

Déplacement, attaque, ennemis, points de vie, inventaire, objets, quêtes et progression. Ces systèmes forment le noyau absolu — sans eux, tu n'as pas un jeu, juste une démo technique.

### Bloc 3 — Le monde

Cartes, zones, villes, monstres, PNJ, ressources, donjons et règles de zone. Les zones, PNJ, compétences, quêtes et règles d'exploration sont les fondations du contenu jouable.

### Bloc 4 — Multijoueur et réseau

Communication client-serveur, RPC, synchronisation des joueurs et architecture réseau. À penser dès le début. Un **serveur autoritaire** contrôle la logique importante — le client ne décide jamais seul.

### Bloc 5 — Persistance des données

Comptes, personnages, inventaire, quêtes, positions, monnaies et état du monde. Sans persistance, ce n'est pas vraiment un monde — les joueurs repartent de zéro à chaque connexion.

### Bloc 6 — Interface utilisateur

Écrans de connexion, création de personnage, HUD, inventaire, boutique, carte, journal de quête, fenêtres de dialogue, menus, raccourcis clavier. L'UI est une vraie étape de production, pas un détail final.

### Bloc 7 — Contenu

Monstres, objets, quêtes, dialogues, zones, récompenses, événements et activités répétables. Un MMO sans contenu paraît vide, même techniquement parfait. Les donjons, talents, métiers, boss et systèmes de groupe arrivent une fois le noyau fonctionnel.

### Bloc 8 — Technique invisible

Performances, sécurité, logs, anti-triche, sauvegardes, stabilité serveur, gestion des erreurs, outils d'administration. Ces aspects deviennent vite essentiels dès que les données doivent rester fiables côté serveur.

---

## 2. Plan en 6 phases de développement

### Phase 1 — Préproduction

Choisis un **concept minuscule** : un mini-MMO 3D avec un village, une petite forêt, 4 joueurs max, 3 monstres, 1 marchand, 1 quête. La réduction du scope est la décision la plus importante de cette phase.

### Phase 2 — Prototype solo

Fais bouger un personnage sur une carte. Ajoute collision, attaque simple, ennemi, barre de vie et inventaire basique. **Tant que cette étape n'est pas agréable à jouer en solo, il ne sert à rien de passer au multijoueur.**

### Phase 3 — Prototype multijoueur

Connexion entre plusieurs joueurs, apparition des autres personnages, synchronisation des déplacements, quelques actions simples via la couche réseau Rust partagée entre client et serveur. Cette couche réseau demande une structure claire.

### Phase 4 — Persistance

Comptes, création de personnage, sauvegarde des stats, inventaire et progression. À partir de là, le projet commence à ressembler à un vrai petit MMO : le monde se souvient des joueurs.

### Phase 5 — Contenu jouable

PNJ, quêtes, objets, boutique, zones, monstres variés, petit donjon ou arène. Les systèmes de groupes, métiers, archétypes et quêtes enrichissent le cœur de jeu une fois les bases techniques en place.

### Phase 6 — Polish

Correction des bugs, amélioration de l'interface, sons, retours visuels, équilibre, outils admin, tests avec de vrais joueurs. Les retours servent à améliorer les fonctionnalités existantes avant d'ajouter encore plus de systèmes.

---

## 3. Plan concret en 12 blocs

| # | Tâche |
|---|---|
| 1 | Créer le projet Bevy |
| 2 | Faire bouger le personnage |
| 3 | Ajouter une carte |
| 4 | Ajouter un ennemi |
| 5 | Ajouter combat et vie |
| 6 | Ajouter inventaire |
| 7 | Faire apparaître 2 joueurs connectés |
| 8 | Synchroniser mouvements et attaques |
| 9 | Sauvegarder un personnage |
| 10 | Ajouter PNJ et quête |
| 11 | Ajouter boutique et objets |
| 12 | Faire un test avec quelques joueurs |

Chaque bloc peut devenir un **mini-projet autonome**, ce qui permet d'apprendre par petits prototypes progressifs.

---

## 4. Priorités initiales

Au démarrage, tes priorités ne sont **pas** :

- Les graphismes parfaits
- L'histoire géante
- Cent PNJ avec IA

Tes vraies priorités sont :

- Projet propre
- Personnage jouable
- Combat basique
- Petit monde
- Connexion multijoueur simple
- Sauvegarde fiable

---

## 5. Détail par phase de maturité

### Pré-Alpha

**Objectif** : prouver que le cœur du jeu fonctionne, pas construire un grand monde.

**Ce qu'on vise :**

- Prototype jouable (déplacement + combat très simple)
- Une petite zone de test
- Une quête basique : *parler à un PNJ → tuer 3 monstres → revenir*
- Connexion multijoueur minimale
- Séparation client / logique serveur

**Boucle de combat minimale :** déplacement → attaque de base → dégâts → mort → respawn → affichage PV

**Livrables techniques :**

- Client Bevy capable de se connecter
- Serveur de jeu rudimentaire
- Base de données minimale (comptes + personnages)
- Schéma de données simple
- Inventaire très léger
- Carte de test
- Quelques monstres
- Pipeline de sauvegarde de personnage

> **Risque principal :** le scope. La plus grande menace n'est pas la difficulté d'un système isolé, c'est l'envie d'en construire dix avant d'en avoir terminé un seul.

---

### Alpha

**Objectif** : transformer le prototype en vrai petit jeu persistant.

**Ce qu'on vise :**

- Combat fiable avec compétences de base, cooldowns, types d'ennemis, équilibrage minimal
- Quêtes à plusieurs types d'objectifs (collecte, exploration, dialogue)
- Petit hub + zone extérieure + zone dangereuse
- Serveur autoritaire unique, logs, redémarrage propre, sauvegarde périodique

**Livrables techniques :**

- Système de compte plus propre
- Création de personnage stable
- Persistance étendue (quêtes + inventaires)
- Boucle de combat complète
- Quelques zones jouables
- Journal de quêtes
- Boutique PNJ simple
- Fichiers de configuration propres
- Outils d'administration minimaux

> **Risque principal :** la dette technique. Si la Pré-Alpha a été bricolée trop vite, chaque nouveau système commence à casser les autres — surtout autour de la persistance, des RPC et des données joueur.

---

### Bêta

**Objectif** : rendre le jeu testable par de vraies personnes de manière continue.

**Ce qu'on vise :**

- Combat lisible, réactif et équilibré
- Quêtes couvrant plusieurs heures de jeu minimum
- Monde assez grand pour donner une impression d'exploration
- Serveurs survivant à plusieurs connexions simultanées sans corrompre les données
- Authentification sérieuse : mots de passe bien stockés, gestion des sessions, vérification de token, limitation des accès invalides, journalisation des erreurs

**Livrables techniques :**

- Client installable / distribuable
- Pipeline de patching ou méthode de mise à jour claire
- Système de logs centralisé
- Sauvegardes automatiques
- Tests de charge simples
- Métriques basiques
- Documentation de déploiement, redémarrage et restauration

> **Risque principal :** la stabilité opérationnelle. Un solo peut réussir à coder un jeu localement mais rencontrer de gros problèmes dès qu'il faut maintenir des comptes réels et quelques dizaines d'utilisateurs testeurs.

---

### Lancement

**Objectif** : version publique assez stable pour accueillir des joueurs sans catastrophe immédiate. Pour un solo, ça ressemble à un **accès anticipé très cadré**, pas à un MMORPG finalisé à grande échelle.

**Ce qu'on vise :**

- Stabilité du service
- Récupération après incident
- Sécurité minimale des comptes
- Cohérence de l'économie
- Quelques boucles de progression solides
- Contenu suffisant pour retenir les premiers joueurs

**Livrables techniques :**

- Procédure de déploiement reproductible
- Sauvegarde / restauration testée
- Base de monitoring
- Tableau de bord d'administration
- Politiques minimales de compte
- Page de statut serveur
- Page d'aide
- Calendrier de patchs

> **Risque principal :** le poids de l'exploitation. Même si le jeu fonctionne, le vrai défi devient de le faire tourner tous les jours, corriger les bugs sans casser les sauvegardes, et ne pas se laisser écraser par le support.

---

## 6. Architecture système

### Vue d'ensemble

Un MMORPG n'est pas un seul programme — c'est un ensemble de services coordonnés : client, passerelle réseau, authentification, simulation temps réel, persistance, analytics et outils d'administration.

**Règle fondamentale :** distinguer données temps réel et données persistantes.

| Type | Où ça vit | Exemples |
|---|---|---|
| Temps réel | Mémoire du serveur de simulation | Positions, déplacements, états de combat, projectiles |
| Persistant | Base de données | Comptes, inventaires, quêtes, monnaies |

```
[Client jeu]
     ↓
[Gateway / Load Balancer]
     ↓              ↓
[Service Auth]   [Serveur Monde / Zone]
     ↓                ↓         ↓         ↓
[Base comptes]  [Cache mémoire] [Base persistance] [Logs / Métriques]
                                        ↓
                                   [Backups]
```

---

### Flux de données joueur

1. Le client s'authentifie (email + mot de passe)
2. Le service auth vérifie le compte en base et renvoie un token de session
3. Le client envoie le token au serveur monde + son `character_id`
4. Le serveur charge le personnage (inventaire, quêtes) depuis la base
5. Le serveur envoie un snapshot initial du monde au client
6. Boucle temps réel :
   - Client envoie : `input(déplacement, attaque, interaction)`
   - Serveur valide + simule
   - Serveur renvoie : delta d'état / corrections au client + snapshots aux autres joueurs proches
7. Sauvegardes périodiques sur événements importants

**Règle centrale :** le client envoie des **intentions**, le serveur décide de l'**état réel** du monde.

---

### Synchronisation des joueurs

La synchronisation est organisée autour d'un **tick serveur régulier** :

- Client envoie des inputs horodatés ou numérotés
- Serveur les traite dans l'ordre et diffuse un nouvel état autorisé

Pour garder le jeu fluide malgré la latence :

- **Prédiction locale** côté client pour la sensation immédiate (déplacement, animation)
- **Réconciliation** quand la réponse serveur arrive
- **Interpolation** pour afficher les autres joueurs sans saccade

| Ce que fait le client | Ce que fait le serveur |
|---|---|
| "J'appuie vers le nord" | Décide si le déplacement est autorisé |
| "J'utilise la compétence 2" | Vérifie portée, cooldown, cible, dégâts |

**Bonnes pratiques :**

- Zones d'intérêt : chaque joueur reçoit surtout les données des entités proches
- Envoyer des deltas plutôt que l'état complet à chaque tick
- Les états ultra-fréquents restent en mémoire — ne pas écrire chaque mouvement en base
- Sauvegarder sur événements significatifs : changement d'inventaire, progression de quête, mort, déconnexion, checkpoint, transaction

---

### Autorité serveur et anti-triche

**Principe de base : ne jamais faire confiance au client.**

Le serveur doit valider au minimum : position, vitesse, collisions, lignes de vue, cooldowns, ressources consommées, dégâts, échanges économiques, récompenses.

> L'autorité serveur ne veut pas dire tout bloquer et être lent. Elle signifie : **le client propose, le serveur dispose.** Le client peut animer immédiatement un coup d'épée, mais le serveur confirme ou corrige l'effet réel.

| Contrôle | Rôle | Pourquoi c'est important |
|---|---|---|
| Validation vitesse / déplacement | Empêche téléportation et speed hacks | Le serveur compare input, tick et position autorisée |
| Validation cooldown / mana | Empêche spam de compétences | Le résultat doit venir de l'état serveur, pas de l'UI locale |
| Validation inventaire / monnaie | Empêche duplication et corruption économique | Les transactions doivent être atomiques côté backend |
| Validation cible / portée | Empêche attaques impossibles | Le serveur vérifie distance, visibilité, état de la cible |
| Journalisation d'anomalies | Permet modération et debug | Sans logs, la triche et les faux positifs sont difficiles à analyser |

---

### Base de données : PostgreSQL vs MongoDB

| Critère | PostgreSQL | MongoDB |
|---|---|---|
| Comptes, inventaires, monnaies | ✅ Très adapté (transactions + schéma structuré) | ⚠️ Possible mais demande une modélisation prudente |
| Données flexibles / polymorphes | ⚠️ Moins naturel si le schéma change souvent | ✅ Très adapté au document model |
| Scalabilité initiale simple | ✅ Scale-up puis réplication recommandés | ✅ Sharding et clusters pour large échelle |
| Risque solo débutant | ✅ Plus simple si besoins bien structurés | ⚠️ Bon modèle documentaire demande anticipation |

**Recommandation pour débuter :** PostgreSQL pour le cœur persistant + MongoDB optionnel plus tard pour analytics / télémétrie.

---

### Mise à l'échelle PostgreSQL

Progression recommandée (du plus simple au plus complexe) :

1. Instance unique bien monitorée
2. Optimisation SQL et index
3. Réplication en lecture si nécessaire
4. Partitionnement sur très gros volumes
5. Stratégies horizontales complexes (seulement si vraiment nécessaire)

**Bonnes pratiques :**

- Tables séparées : `users`, `characters`, `inventory_items`, `quests_progress`, `transactions`
- Transactions pour toute opération économique ou d'inventaire
- Index uniquement sur les vraies requêtes fréquentes
- Mise en cache côté application pour ce qui est lu souvent mais change peu
- Répliquer pour les lectures, mais garder une écriture maîtrisée sur le primaire tant que l'échelle reste modeste
- Partitionnement pour journaux d'événements, historiques et télémétrie volumineuse

---

### Mise à l'échelle MongoDB

**Bonnes pratiques :**

- Choisir une shard key alignée avec les lectures et écritures réelles
- Garder les documents de profil raisonnables en taille
- Séparer profils, sessions, télémétrie et inventaires si leurs patterns d'accès diffèrent
- Utiliser les secondaires pour certaines lectures globales
- Réserver MongoDB aux données où la flexibilité documentaire apporte un vrai gain

---

## 7. Ressources recommandées

| Ressource | Recommandation | Pourquoi | Risque |
|---|---|---|---|
| Moteur de jeu | **Bevy** (Rust) | ECS natif, stack Rust unifié client + serveur, WGPU (OpenGL ES / Vulkan / DX12 / Metal) | Pas d'éditeur visuel, écosystème plus jeune que les engines AAA |
| Langage backend | Rust (crate Tokio + Bevy ECS partageable) | Architecture ECS cohérente client-serveur, zéro garbage collector, très haute performance | Courbe d'apprentissage sévère si débutant en Rust |
| Base de données | PostgreSQL | Robuste, adapté à un petit projet persistant | Mauvais schéma peut casser les sauvegardes |
| Authentification | Service auth séparé simple (token/session) | Les schémas MMO séparent souvent auth et jeu | Mélanger auth et logique de jeu ouvre des failles |
| Infrastructure | VPS ou petite VM cloud | Mieux qu'une infra cloud trop ambitieuse | Coûts pénibles sans monitoring |
| Reverse proxy | Nginx | Route et protège les entrées réseau | Mauvaise config = connexions cassées |
| Design | Figma + éditeur pixel art simple | Suffisant pour UI, wireframes et petits assets | Temps perdu à trop designer avant de tester |
| Versioning | Git + dépôts séparés si besoin | Indispensable pour revenir en arrière | Sans discipline, chaque bug grave coûte très cher |
| Monitoring | Logs + métriques basiques | Essentiel dès l'Alpha | Sans logs, on devine au lieu de diagnostiquer |

---

## 8. Risques par phase

| Phase | Niveau de risque | Risque dominant | Lecture réaliste |
|---|---|---|---|
| Pré-Alpha | 🔴 Très élevé | Scope trop grand | Tu peux te perdre avant d'avoir une version jouable |
| Alpha | 🔴 Très élevé | Dette technique | Les systèmes commencent à se marcher dessus |
| Bêta | 🟠 Élevé à très élevé | Instabilité opérationnelle | Les vrais joueurs révèlent les failles invisibles en local |
| Lancement | 🟠 Élevé | Maintenance et support | Le produit existe, mais le faire vivre devient un second métier |

---

## 9. Pièges fréquents

1. **Écrire trop souvent en base de données** — ne jamais écrire chaque déplacement en base. La base n'est pas un moteur temps réel.
2. **Rendre le client responsable de valeurs critiques** — le client peut mentir. Toujours valider côté serveur.
3. **Sharder la base trop tôt** — mesurer, profiler, optimiser d'abord. Distribuer seulement si vraiment nécessaire.
4. **Mélanger des besoins très différents dans un seul stockage** — ne pas utiliser la même base comme ledger économique, cache de session, télémétrie et historique analytique à la fois.

---

## 10. Architecture recommandée pour débuter (résumé)

**Stack minimale réaliste pour un solo :**

```
Mini-MMO (retro style PS2)
├── Un seul serveur de jeu (autoritaire — Rust / Bevy ECS headless)
├── Un service d'authentification simple
├── Une seule base PostgreSQL
└── Une seule région de déploiement
```

**Modèle de données :**

- Temps réel en mémoire
- Vérité de simulation côté serveur
- Persistance structurée en base
- Écritures événementielles asynchrones quand possible
- Séparation claire entre auth, monde et données

---

## 11. Architecture « Future-Proof » (Horizon 2030) et Intégration IA

La stratégie d'ingénierie de ce projet repose sur un choix radical et assumé : maintenir un rendu visuel volontairement rétro (style PlayStation 2 / Metin2) pour allouer 100 % de la charge computationnelle à une architecture serveur ultra-moderne. Le but est de créer un écosystème massivement scalable, piloté par l'IA, tout en garantissant une exécution fluide sur des ordinateurs vieux de 15 ans comme sur les machines de dernière génération.

### Le Paradigme du Client "Terminal" (Compatibilité Maximale)

Pour tourner sur d'anciennes configurations, le client du jeu doit être perçu comme un simple terminal d'affichage. Il ne calcule aucune logique métier lourde.

**Rendu polymorphe via WGPU :** Bevy utilise WGPU pour abstraire le backend de rendu. Sur les vieilles machines : OpenGL ES 3 / DirectX 11. Sur les PC récents : Vulkan / DirectX 12 / Metal. Le même code Rust tourne sur les deux sans modification.

**Bande passante optimisée :** Chaque joueur reçoit surtout les données des entités proches. Le processeur du client n'est pas inondé de paquets réseau inutiles grâce à un partitionnement spatial strict (zones d'intérêt).

**Transmission chirurgicale :** Le serveur se contente d'envoyer des deltas plutôt que l'état complet à chaque tick.

**Prédiction locale isolée :** Le client peut animer immédiatement un coup d'épée, mais le serveur confirme ou corrige l'effet réel. Le résultat doit venir de l'état serveur, pas de l'UI locale.

**Avantage stack unifiée Rust :** Les structures de données ECS (composants, événements réseau, messages) sont définies une seule fois dans un crate partagé et compilées dans le client Bevy comme dans le serveur headless — zéro désynchronisation de protocole.

---

### Serveur de Simulation et Hautes Performances

L'infrastructure backend doit abandonner les paradigmes classiques pour un traitement de la donnée ultra-optimisé, pensé pour le très haut débit.

**Architecture ECS (Entity Component System) :** Bevy ECS en mode headless (sans rendu) côté serveur. Les composants sont stockés en mémoire contiguë (Data-Oriented Design), garantissant une utilisation maximale des cœurs du CPU sans garbage collector.

**Orchestration dynamique :** Remplacement des déploiements manuels par des orchestrateurs dédiés au jeu (ex: Agones sur Kubernetes) pour adapter le nombre de serveurs à la population réelle.

**Réconciliation mathématique :** La synchronisation s'appuie sur une prédiction absolue où le nouvel état autorisé $S_{t}$ dépend de l'ancien état $S_{t-1}$ et de l'intention du joueur $I_{t}$ :

$$S_{t} = S_{t-1} + \Delta t \times \Phi(S_{t-1}, I_{t})$$

---

### Persistance et Écosystème "AI-Native"

Pour rendre le jeu manipulable, testable et géré par des intelligences artificielles (LLMs, agents autonomes), les systèmes doivent être lisibles par des machines.

**Bases de données Polyglottes :** Évolution vers le NewSQL (CockroachDB) pour des transactions distribuées sans point de défaillance, couplée à des bases orientées colonnes (ClickHouse) pour des logs analytiques massifs.

**Protocole MCP (Model Context Protocol) :** Le serveur expose des outils standardisés via MCP. Cela permet à des agents IA (faisant office de Maîtres de Jeu ou d'équilibrage économique) de lire les logs et d'agir sur le monde via des contrats de données stricts.

**Mémoire Sémantique (Vectorielle) :** Ajout d'une base de données vectorielle (Qdrant/Milvus) pour gérer les "souvenirs" des PNJ. L'IA génère des réponses en calculant la similarité entre le contexte du joueur $\mathbf{A}$ et les événements en base $\mathbf{B}$ via la Similarité Cosinus :

$$CosineSimilarity(\mathbf{A}, \mathbf{B}) = \frac{\mathbf{A} \cdot \mathbf{B}}{\|\mathbf{A}\| \|\mathbf{B}\|}$$

**Sandboxing des IA :** L'IA est traitée avec la même méfiance qu'un client humain. Toutes ses intentions passent par la validation stricte du serveur pour éviter les hallucinations et la corruption économique.

---

### Comparatif : Stack Classique vs Stack Horizon 2030

| Composant | Stack Classique (Standard) | Stack Avancée (Horizon 2030 / AI-Native) |
|---|---|---|
| **Moteur Client** | Moteur généraliste (scripting dynamique) | Bevy (Rust natif, ECS partagé client + serveur) |
| **Simulation Serveur** | Node.js / Architecture Objet | Bevy headless ou serveur Rust custom / Architecture ECS |
| **Bases de données** | PostgreSQL | CockroachDB (NewSQL) + Base Vectorielle (RAG) |
| **Protocole Réseau** | TCP / UDP | QUIC / WebTransport |
| **Déploiement** | VPS Unique ou petite VM | Kubernetes + Agones (Flotte dynamique) |
| **Comportement PNJ** | Arbres de comportement statiques | Agents LLM connectés au serveur via MCP |
| **Client Graphique** | Rendu fixe et lourd | Rendu adaptatif WGPU (OpenGL ES 3 / Vulkan / DX12 / Metal) |








