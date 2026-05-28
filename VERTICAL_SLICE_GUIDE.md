# VERTICAL SLICE GUIDE — Validation du Jalon (Mois 6)

Ce document décrit le plan de test manuel permettant de valider la "Vertical Slice" du projet à la fin du Sprint de 6 mois. L'objectif est de vérifier que tous les éléments (Personnage, Mobs, Décor, HUD) s'affichent correctement et respectent la direction artistique Rétro (style PS2) et les contraintes techniques (faible nombre de Draw Calls).

## 1. Préparation de l'environnement

### Prérequis (Assurez-vous que les étapes précédentes ont été réalisées)
1. **Assets exportés :** Les modèles `elara_voss.glb`, `goblin_base.glb`, et les props de l'environnement (`prop_floor_tile.glb`, `prop_barrel.glb`, etc.) sont présents dans le dossier `assets/models/`.
2. **Assets optimisés :** Le script d'optimisation Node.js a été exécuté (`npm run optimize`) et s'est terminé sans erreur.
3. **Compilation :** Le projet Bevy compile correctement (`cargo build`).

## 2. Lancement du Test

1. Ouvrez un terminal.
2. Exécutez la commande : `cargo run --bin elaras_black_mist`.
3. La fenêtre du jeu s'ouvre.

## 3. Scénario de Test et Critères de Validation

### Test A : Rendu Global et Direction Artistique
- **Action :** Observez l'environnement de base (Velnor Slums).
- **Critères de Succès :**
    - L'éclairage PBR complexe est désactivé (les matériaux doivent paraître "Unlit" avec des ombres peintes sur la texture, si elles sont présentes).
    - Les textures sont nettes et pixelisées de près (le filtrage "Nearest Neighbor" est bien actif).
    - Les modèles 3D affichent clairement leur aspect "Low-Poly" (arêtes visibles).
- **Critère d'Échec :** Les textures sont floues, les modèles réagissent anormalement à la lumière (reflets brillants inattendus).

### Test B : Interface Utilisateur (HUD)
- **Action :** Vérifiez la surimpression sur l'écran.
- **Critères de Succès :**
    - Les jauges (HP, MP, Stamina) sont visibles en haut à gauche.
    - L'emplacement de la minimap (carré sombre provisoire) est visible en haut à droite.
    - La barre d'action (5 emplacements) est centrée en bas de l'écran.
    - L'interface ne bloque pas la vue 3D de manière excessive.
- **Critère d'Échec :** L'UI est absente, déformée ou masque la majeure partie de la scène 3D.

### Test C : Déplacement et Caméra (Dummy Player)
- **Action :** Utilisez les touches `Z, Q, S, D` (ou `W, A, S, D` selon clavier) pour déplacer le personnage "Dummy". Utilisez la souris pour orienter la caméra (si un mode *Freelook* est activé) ou vérifiez que la caméra suit correctement le joueur.
- **Critères de Succès :**
    - Le joueur "Dummy" se déplace fluidement sur les pavés (tuiles instanciées).
    - La caméra reste ancrée derrière le joueur ou permet une observation claire de la scène.
    - Les personnages (Elara, Gobelin) sont positionnés correctement et ne clignotent pas.
- **Critère d'Échec :** Le joueur passe à travers le sol, la caméra s'emballe ou les contrôles ne répondent pas.

### Test D : Performance et Draw Calls
- **Action :** Suivez la procédure du fichier `scripts/ci_check_drawcalls.md` en utilisant **RenderDoc**.
- **Critères de Succès :**
    - L'Event Browser affiche un nombre très restreint de `DrawIndexed` ou d'appels équivalents pour le décor, prouvant que les tuiles et objets partageant l'Atlas sont bien regroupés.
- **Critère d'Échec :** Un appel de dessin (Draw Call) est émis pour chaque objet individuel (ex: 25 appels pour 25 tuiles identiques).

## 4. Conclusion du Sprint

Si tous les critères de succès sont remplis, la **Vertical Slice est validée**.
Le socle technique et visuel est solide, prêt pour l'implémentation de la logique réseau (Serveur Autoritaire) et des systèmes de gameplay (Combat, Inventaire) dans les phases ultérieures.
