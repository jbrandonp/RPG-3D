# Plan d'Action : Systèmes d'Interfaces (UI/UX) - Projet Horizon

Ce document établit la roadmap technique et fonctionnelle pour le développement des interfaces utilisateur (UI) du projet MMORPG "Elara's Black Mist" (Projet Horizon). Ce plan couvre les 5 premiers sprints de développement menant à une version Pré-Alpha jouable.

## 1. Contexte & Périmètre

### Architecture Cible
- **Client "Terminal" :** Le client gère uniquement l'affichage et l'envoi d'intentions. La logique métier et l'état de vérité résident exclusivement sur le Serveur Autoritaire.
- **Moteur :** Rust avec Bevy ECS (0.14+).
- **Rendu & Esthétique :** Style rétro PS2/Metin2, filtrage nearest-neighbor (pixel art net), polices non lissées.

### Périmètre des Sprints (Pré-Alpha)
- **INCLUS (Sprints 0 à 4) :** HUD minimal, Menu de Connexion, Création de personnage, Inventaire, Journal de quêtes basique, Carte, Menus d'options.
- **EXCLUS (Backlog Post-Alpha) :** Outils de développement internes (Éditeurs de map/quêtes, Outils admin, Hot-reload métier).

### Contraintes de Production
- **Équipe :** Développeur solo (Brandon) + IA (conception/PNJ).
- **Ressources Graphiques :** Minimalistes, générées ou placeholders. Pas de designer UI dédié.
- **Ton :** Pragmatique, UI clinique/systémique (ex: alertes système dissonantes), pas d'héroïsme. Bulles de texte strictes (max 3 lignes, 60 char/ligne).

---

## 2. Roadmap : Objectif Pré-Alpha (10 Semaines)

La cadence est fixée à des **sprints de 2 semaines**.

### SPRINT 0 : Setup & Tooling UI (Semaines 1-2)
*Fondations techniques pour l'interface en Bevy.*
- Mise en place de l'environnement WGPU/Bevy UI.
- Configuration du pipeline d'assets pour l'UI (polices pixel, matériaux Unlit, nearest-neighbor).
- Création d'une scène vide avec gestion d'états (State : `Login`, `CharacterSelect`, `InGame`).
- Structuration des événements d'UI (UI -> Intentions Réseau).

### SPRINT 1 : Core UI & Entrée en Jeu (Semaines 3-4) - **PRIORITÉ ABSOLUE**
*Premier contact jouable et boucle de connexion.*
- Écran de connexion (Email / Mot de passe simulé/mocké).
- Écran de création de personnage (minimaliste).
- HUD In-Game basique : Jauges (HP, MP, Trauma/Corruption), Minimap statique.
- Raccourcis clavier de base (1-5) affichés.

### SPRINT 2 : Inventaire & Équipement (Semaines 5-6)
*Manipulations complexes et validation serveur.*
- Interface "Paperdoll" (équipement) et grille d'inventaire.
- Implémentation du cycle Drag & Drop : Glisser local (simulation) -> Envoi d'intention -> Réponse Serveur -> Validation ou Rollback visuel.

### SPRINT 3 : Quêtes, Carte & Dialogues (Semaines 7-8)
*Interaction avec le monde.*
- Système de bulles de dialogue (respect de la contrainte 3x60).
- Fenêtre de journal de quêtes basique.
- Carte interactive / Radar de proximité lié au NavMesh serveur.

### SPRINT 4 : Polish & Menus Systèmes (Semaines 9-10)
*Finalisation pour la Pré-Alpha.*
- Menu d'options (Graphismes, Audio, Raccourcis).
- Fenêtre de Chat multicanal (Général, Système, Combat Logs).
- Intégration des alertes systémiques ("diagnostics cliniques").
- Nettoyage du code UI, optimisation WGPU pour l'interface.

---

## 3. Architecture Technique de l'UI (Bevy)

### Zéro Confiance (Zero Trust)
L'UI Bevy lit l'état à partir des composants synchronisés (`Replicated`) mais n'écrit **jamais** directement dans les composants de gameplay (comme `Health`).
Les boutons d'UI déclenchent des `NetworkIntentEvent`.

### Flux Standard
1. **Écoute** : L'UI lit `Query<&Health, With<LocalPlayer>>`.
2. **Action** : Clic sur une potion.
3. **Intention** : Envoi `NetworkIntent::UseItem(potion_id)`.
4. **Prédiction (Optionnel)** : Début d'un cooldown visuel temporaire en ECS local.
5. **Résolution** : Le serveur renvoie un `StateDelta`. Si refusé, annulation du cooldown visuel.
