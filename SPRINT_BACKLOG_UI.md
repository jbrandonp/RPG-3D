# Backlog d'Interface Utilisateur (UI) - Projet Horizon

Ce backlog consolide toutes les User Stories (US) et tâches techniques pour la création des interfaces du client "Terminal" du Projet Horizon, menant à la Pré-Alpha.

---

## SPRINT 1 : Core UI & Entrée en Jeu (PRIORITÉ #1)
*Objectif : Rendre le jeu testable et implémenter la boucle de connexion au serveur.*

### US-1.1 : Écran de Connexion
- **En tant que** joueur, **je veux** pouvoir saisir mes identifiants (email/mot de passe) **afin de** m'authentifier auprès du serveur.
- **Tâches :**
  - Créer un layout Bevy UI centré avec deux champs de texte et un bouton "Connexion".
  - Gérer la capture du clavier (Input textuel Bevy).
  - Simuler (mock) l'envoi réseau et la transition vers l'état `CharacterSelect`.

### US-1.2 : Écran de Création / Sélection de Personnage
- **En tant que** joueur, **je veux** voir la liste de mes personnages ou en créer un nouveau **afin de** commencer à jouer.
- **Tâches :**
  - UI liste de personnages (placeholder).
  - Champ de texte pour le nom du personnage.
  - Bouton "Entrer dans le monde" déclenchant la transition vers l'état `InGame`.

### US-1.3 : HUD In-Game Basique
- **En tant que** joueur, **je veux** voir la santé, le mana, et l'état de mon personnage **afin de** survivre en combat.
- **Tâches :**
  - Placer les jauges HP (rouge), MP (bleu), Trauma/Corruption (vert/violet) en haut à gauche.
  - Lier les jauges aux composants `Health`, `PsychologicalState` via une `Query` Bevy.
  - Intégrer une Minimap ronde statique (haut droite) avec un marqueur central.

### US-1.4 : Barre d'Actions (Hotbar)
- **En tant que** joueur, **je veux** voir mes compétences disponibles **afin de** savoir quels raccourcis utiliser.
- **Tâches :**
  - Afficher une barre de 5 à 10 slots en bas au centre.
  - Binder visuellement les touches 1 à 5 sur l'UI.
  - Enregistrer les événements d'entrée clavier et logger une "Intention d'Action" dans la console.

---

## SPRINT 2 : Inventaire & Équipement
*Objectif : Gestion complexe des entités UI et validations.*

### US-2.1 : Grille d'Inventaire
- **En tant que** joueur, **je veux** voir les objets que je transporte **afin de** gérer mon équipement.
- **Tâches :**
  - Fenêtre UI ouvrable avec touche "I".
  - Générer une grille (ex: 5x5 slots).
  - Afficher des sprites d'objets (placeholders) selon un composant `Inventory` local.

### US-2.2 : Interface Équipement (Paperdoll)
- **En tant que** joueur, **je veux** voir ce que mon personnage porte sur lui.
- **Tâches :**
  - Placer des slots spécifiques (Tête, Torse, Armes, Anneaux) à côté de la grille d'inventaire.

### US-2.3 : Drag & Drop et Intention Réseau
- **En tant que** joueur, **je veux** glisser-déposer un objet pour l'équiper ou le déplacer.
- **Tâches techniques :**
  - Gestion du clic et maintien (Drag) d'une icône UI dans Bevy.
  - Créer un événement local d'intention : `NetworkIntent::MoveItem(SourceSlot, TargetSlot)`.
  - Implémenter le "Rubberbanding" UI : si pas de réponse "OK" du serveur (simulé) dans X ms, l'icône retourne à sa place.

---

## SPRINT 3 : Quêtes, Carte & Dialogues
*Objectif : Interactions narratives et repérage spatial.*

### US-3.1 : Bulles de Dialogue Rétro
- **En tant que** joueur, **je veux** lire ce que disent les PNJ **afin de** suivre l'histoire.
- **Tâches :**
  - Créer un composant UI flottant au-dessus d'une entité 3D.
  - Appliquer la contrainte stricte : Max 3 lignes, 60 caractères par ligne.
  - Gérer l'esthétique pixelisée (police spécifique, pas d'anti-aliasing).

### US-3.2 : Journal de Quêtes
- **En tant que** joueur, **je veux** voir mes objectifs en cours.
- **Tâches :**
  - Fenêtre de menu déroulant ou liste simple.
  - Affichage titre, description courte, progression (ex: 2/5 loups).

### US-3.3 : Carte Interactive (Map)
- **En tant que** joueur, **je veux** afficher la carte de la région.
- **Tâches :**
  - Ouvrir une grande image (texture) en plein écran via touche "M".
  - Calculer et placer un marqueur de joueur basé sur ses coordonnées X/Z mondiales converties en coordonnées UI.

---

## SPRINT 4 : Polish & Menus Systèmes
*Objectif : Finaliser le client de test Pré-Alpha.*

### US-4.1 : Fenêtre de Chat
- **En tant que** joueur, **je veux** lire les annonces serveurs et parler avec d'autres.
- **Tâches :**
  - Boîte de texte défilante en bas à gauche.
  - Canaux de couleurs (Général, Système/Clinique).

### US-4.2 : Menu d'Options
- **En tant que** joueur, **je veux** régler le son et voir les contrôles.
- **Tâches :**
  - Menu Echappement.
  - Sliders basiques pour le volume global.

### US-4.3 : Alertes Systémiques Dissonantes
- **En tant que** concepteur, **je veux** des pop-ups de diagnostic froid pour le lore.
- **Tâches :**
  - Système de notification central ("Toast") affichant des messages critiques (ex: "Défaillance synaptique détectée").

---

## BACKLOG POST-ALPHA — Outils Internes (HORS PÉRIMÈTRE SPRINTS 1-4)
*Ces éléments sont critiques pour la production, mais exclus du cycle de développement de l'interface client de la Pré-Alpha.*

- **Outil-1 : Éditeur de Map (In-Engine)** : Placement de prefabs, édition NavMesh, paramétrage de l'octree serveur via `bevy_egui`.
- **Outil-2 : Éditeur de Quêtes IA (MCP)** : Interface web ou locale permettant à un agent IA (via LLM) ou un designer de générer des nœuds de quête et de les injecter en base de données.
- **Outil-3 : Console Admin / God Mode** : Console UI avec permissions avancées (spawn, teleport, modifications statistiques).
- **Outil-4 : Overlay de Debug ECS** : Outil pour afficher les hitboxes, chemins des PNJ, metrics (Tickrate, DB latency).
- **Outil-5 : Hot-Reloading de Data** : Implémenter l'AssetServer Bevy pour recharger à chaud les fichiers TOML/RON sans redémarrer le serveur.
