# SPRINT 1 : Core UI & Entrée en Jeu
**Priorité :** ABSOLUE (#1)
**Durée :** 2 Semaines (14 Jours)
**Objectif :** Implémenter la boucle de connexion complète (Login -> Création/Sélection Perso -> HUD in-game) permettant d'avoir un client "testable".

---

## Semaine 1 : Authentification et Sélection

### Jour 1 : Écran de Connexion (Layout)
- Générer un composant `LoginScreen`.
- Disposer un conteneur au centre de l'écran (Flexbox).
- Intégrer le titre du jeu (Texte ou Logo Sprite).
- **Point de blocage potentiel :** Gestion capricieuse du Flexbox Bevy (bien utiliser `AlignItems::Center`, `JustifyContent::Center`).

### Jour 2 : Écran de Connexion (Inputs)
- Ajouter 2 champs de texte (Email, Mot de passe). Le champ mdp doit idéalement masquer les caractères.
- Ajouter le bouton "Connexion".
- Lier le clic du bouton à un événement `NetworkIntent::LoginRequest(email, pwd)`.

### Jour 3 : Transition vers Sélection de Personnage
- Le "Mock Server" (implémenté Sprint 0) valide l'Event et déclenche un `StateTransition` vers `CharacterSelect`.
- Le système `cleanup_ui` doit détruire l'écran de login proprement.
- **Code Bevy de départ (Nettoyage) :**
```rust
pub fn cleanup_ui<T: Component>(mut commands: Commands, q_ui: Query<Entity, With<T>>) {
    for entity in q_ui.iter() {
        commands.entity(entity).despawn_recursive();
    }
}
```

### Jour 4 : Écran Sélection (Liste)
- Créer un layout avec un menu latéral gauche.
- Afficher 3 boutons placeholders représentant des "Slots" de personnages.
- L'affichage 3D du personnage (caméra render-to-texture ou superposition) est ignoré pour ce sprint. Uniquement l'UI.

### Jour 5 : Écran Sélection (Création)
- Si un slot vide est cliqué, afficher un champ texte "Nom du Personnage" et un bouton "Créer".
- Envoi de `NetworkIntent::CreateCharacter(name)`.
- Envoi de `NetworkIntent::EnterWorld(character_id)` si un personnage existant est sélectionné.

---

## Semaine 2 : Le HUD "In-Game"

### Jour 8 : Base du HUD et Setup In-Game
- Transition vers l'état `InGame`.
- Instancier le nœud racine du HUD (`HudRoot`, Width: 100%, Height: 100%, PositionType: Absolute).
- **Critère de succès :** Le HUD s'affiche en surimpression sans bloquer le rendu 3D.

### Jour 9 : Jauges de Survie (HP, MP, Trauma)
- En haut à gauche. Utiliser des `NodeBundle` superposés (Un Node noir pour le fond, un Node coloré pour la valeur).
- **Code Bevy de départ (Barre de vie) :**
```rust
// Dans la boucle de mise à jour (Update)
fn update_health_bar_ui(
    q_player: Query<&Health, With<LocalPlayer>>,
    mut q_hp_bar_style: Query<&mut Style, With<HpBarUIElement>>,
) {
    if let Ok(health) = q_player.get_single() {
        for mut style in q_hp_bar_style.iter_mut() {
            let percentage = health.current as f32 / health.max as f32;
            style.width = Val::Percent(percentage * 100.0);
        }
    }
}
```

### Jour 10 : La Minimap (Statique)
- En haut à droite. Créer un conteneur rond (Border Radius dans Bevy) ou carré selon les limitations actuelles du styling.
- Ajouter une texture de carte placeholder.
- **Point de blocage :** Bevy UI supporte les "border radius", bien s'assurer que `overflow: Hidden` masque les bords de l'image.

### Jour 11 : Barre d'Actions (Hotbar)
- En bas au centre. Flexbox Row.
- Générer 5 petits carrés (NodeBundles) avec des bordures pixel art.
- Ajouter des textes en incrustation ('1', '2', '3', '4', '5').

### Jour 12 : Raccourcis Clavier et Feedback Visuel
- Écouter `ButtonInput<KeyCode>`.
- Si `KeyCode::Digit1` est pressé, changer brièvement la couleur de fond du Slot 1 (simulation de l'appui bouton).
- Déclencher un événement dans la console `println!("Action 1 Triggered!")` (simule `NetworkIntent::CastSpell(slot_id)`).

### Jour 13 : Polish du HUD
- Ajustement des marges (Padding, Margin) pour s'adapter à plusieurs résolutions sans casser.
- S'assurer que tous les textes utilisent la police pixel art.

### Jour 14 : Bilan Sprint 1
- **Critère d'acceptation global :** On peut lancer le jeu, taper un faux mdp, cliquer sur un perso, arriver "en jeu", voir ses jauges réagir si on change manuellement les valeurs `Health` dans un script de debug, et appuyer sur '1' pour voir le slot clignoter.
