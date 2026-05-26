# SPRINT 0 : Setup & Tooling UI
**Durée :** 2 Semaines (14 Jours)
**Objectif :** Établir les fondations techniques de l'interface utilisateur avec Bevy, importer les assets de base (polices, thèmes) et préparer l'architecture State-Driven.

---

## Semaine 1 : Architecture & Rendu Bevy

### Jour 1 : Initialisation du Projet Bevy
- Créer/nettoyer le projet Rust (`cargo new`).
- Ajouter Bevy (0.14+) en dépendance.
- Configurer les plugins de base Bevy (WindowPlugin, WgpuPlugin) avec les paramètres de résolution (ratio 4:3 conseillé pour le rétro, ou 16:9 forcé).
- **Critère de succès :** Une fenêtre noire s'ouvre, sans erreur WGPU.

### Jour 2 : Gestion des États (States)
- Implémenter le système d'états Bevy : `#[derive(States)] enum AppState { Login, CharacterSelect, InGame }`.
- Configurer l'état initial sur `Login`.
- **Critère de succès :** Les `Update` systems sont filtrés correctement par `run_if(in_state(AppState::...))`.

### Jour 3 : Pipeline de Rendu & Assets Rétro
- Configurer l'AssetServer pour pointer vers le dossier `assets/`.
- Forcer le filtrage "Nearest Neighbor" global pour les textures et les polices afin de garantir l'aspect pixel-art.
- **Critère de succès :** Une image placeholder chargée s'affiche nette et non floutée.

### Jour 4 : Importer la Police d'Écriture (Font)
- Trouver ou créer une police au format `.ttf` ou `.fnt` (style PS2 bitmap).
- L'ajouter aux assets et la charger au démarrage.
- **Critère de succès :** Un simple texte "Test" s'affiche avec la police pixel art à l'écran.

### Jour 5 : Structure ECS pour l'UI
- Définir les composants racines (Markers) pour l'UI, ex: `LoginUIElement`, `HudUIElement` pour faciliter le nettoyage (`despawn_recursive`).
- Créer un système `cleanup_ui<T: Component>` générique exécuté lors des transitions d'état (`OnExit`).
- **Critère de succès :** Passer de `Login` à `CharacterSelect` supprime bien tous les éléments UI de la scène précédente.

---

## Semaine 2 : Composants UI Réutilisables

### Jour 8 : Préfabs UI - Boutons
- Créer une fonction de génération de boutons (`spawn_button`).
- Gérer l'interaction Bevy (`Interaction::Hovered`, `Interaction::Pressed`) pour changer la couleur ou le sprite du bouton.
- **Critère de succès :** Un bouton cliquable au centre de l'écran qui change visuellement d'état.

### Jour 9 : Préfabs UI - Champs de Texte (Inputs)
- Bevy n'a pas d'Input textuel natif complet. Implémenter un plugin communautaire (ex: `bevy_cosmic_edit`) ou coder un système basique écoutant `ReceivedCharacter`.
- **Critère de succès :** Pouvoir cliquer sur une zone UI et taper du texte visible à l'écran.

### Jour 10 : Préfabs UI - Panneaux & Conteneurs
- Configurer les Flexbox Bevy (Style, FlexDirection, AlignItems, JustifyContent).
- Créer un conteneur standard pour les futurs menus (Fond semi-transparent, bordure pixel art).
- **Critère de succès :** Un panneau centré contenant du texte et un bouton est généré dynamiquement.

### Jour 11 : Système de Thème Centralisé
- Créer une ressource `UiTheme` contenant les couleurs principales (Rouge HP, Bleu MP, Couleurs de fond, Tailles de police par défaut).
- L'utiliser dans toutes les fonctions génératrices d'UI.
- **Critère de succès :** Changer la couleur du texte dans la ressource `UiTheme` modifie la couleur de toute la nouvelle UI instanciée.

### Jour 12 & 13 : Architecture des Intentions (Network Mocking)
- Créer un enum `NetworkIntentEvent`.
- Créer un système qui écoute les interactions UI (ex: clic sur "Se Connecter") et déclenche un `NetworkIntentEvent::Login(user, pass)`.
- Mettre en place un système "Mock Server" local très simple qui lit ces événements et déclenche les changements de State (simulation du réseau).
- **Critère de succès :** Le clic sur un bouton "Connexion" envoie un Event, le Mock Server le reçoit, et change l'état du jeu à `CharacterSelect`.

### Jour 14 : Revue et Polish
- Revue du code, refactoring des fonctions redondantes.
- Validation finale de l'architecture d'UI avant d'attaquer le Sprint 1.
