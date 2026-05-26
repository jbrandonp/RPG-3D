# Plan de Sprint : Production Audio & Ingénierie (Pré-Alpha)

Ce document détaille la roadmap tactique pour la réalisation complète des systèmes audio et la production des assets de la Pré-Alpha. Le travail est découpé en **4 sprints de 2 semaines** (8 semaines au total), conçu pour un développeur solo.

**Objectif final (Fin du Sprint 3) :** Une expérience audio minimaliste mais totalement fonctionnelle, avec la base de l'ingénierie Bevy en place, intégrant la dissonance audio requise pour la Pré-Alpha.

---

## ⚙️ Sprint 0 : Setup, Tooling & Architecture Bevy (Semaines 1-2)

**Objectif :** Poser les fondations techniques dans le moteur Bevy et configurer l'environnement de création sonore.

*   **Jour 1-2 : Setup des outils de production**
    *   Installation et configuration DAW (LMMS, Audacity).
    *   Recherche et test des outils génératifs (BFXR, Soundraw/AIVA).
    *   Sélection d'une API ou d'un outil local pour le TTS (Coqui, etc.) à intégrer plus tard.
*   **Jour 3-5 : Architecture Bevy de base (AudioManager)**
    *   Création de l'architecture du plugin audio dans Bevy (`AudioPlugin`).
    *   Mise en place de la réception des événements RPC du serveur (`PlaySoundEvent`).
    *   Implémentation du `SFX Manager` pour la lecture de base des `.wav` en mémoire.
*   **Jour 6-8 : Spatialisation & Randomisation (Bevy)**
    *   Intégration de l'audio spatial 3D (atténuation selon la distance entre la caméra/joueur et la source de l'entité).
    *   Programmation du système de variation aléatoire : ajout automatique d'une variation de pitch ($\pm 10\%$) et de volume ($\pm 2$ dB) lors du déclenchement d'un SFX.
*   **Jour 9-10 : BGM & Crossfade (Bevy)**
    *   Implémentation du `BGM Manager` pour la gestion des pistes `.ogg` en streaming.
    *   Création de la logique de crossfade (fondu enchaîné de 3-5s) lors des changements d'état/zone.

---

## ⚔️ Sprint 1 : Core SFX (Combats & Interface) (Semaines 3-4)

**Objectif :** Produire et intégrer les sons d'interaction immédiate (gamefeel et UI).

*   **Jour 1-3 : Production SFX - Armes de mêlée**
    *   Création de 3 variantes de "Swing" (fendant l'air, grave).
    *   Création de 3 variantes d'Impact "Mat/Lourd" (pas de cliquetis métallique).
    *   Mixage et export au format `.wav` (Mono, 44.1kHz, 16-bit, cible : -16 à -20 LUFS).
*   **Jour 4-5 : Production SFX - Armes à distance & Magie**
    *   Arc : Sons de tension de la corde, décochage de flèche.
    *   Magie : 3 sons cristallins/doux pour l'incantation, 1 son d'impact (feu/glace filtré Low-Pass).
*   **Jour 6-7 : Production SFX - Mouvements (Foley)**
    *   Sons de pas (Herbe, Pierre, Terre). Minimum 3 variantes par type de sol.
    *   Bruits de saut/atterrissage étouffés.
*   **Jour 8-9 : Production SFX - Interface (UI ASMR)**
    *   Survol (Hover) : tapotement liège.
    *   Clic (Confirm) : Xylophone réverbéré.
    *   Erreur : "bop-bop" grave et doux.
    *   Inventaire : Tintement lourd d'or ancien.
    *   Mixage : -22 à -26 LUFS.
*   **Jour 10 : Intégration & Test en jeu**
    *   Connexion des assets aux événements RPC Bevy.
    *   Test de "voice stealing" (que se passe-t-il si 10 monstres frappent en même temps ?).

---

## 🌲 Sprint 2 : Ambiances Environnementales (Semaines 5-6)

**Objectif :** Donner vie aux zones de la Pré-Alpha (Village, Forêt, Grottes/Marais) sans musique, uniquement avec les sons de fond.

*   **Jour 1-3 : Ambiance Village de Départ (Velnor)**
    *   Création d'une boucle `.ogg` (1-2 minutes).
    *   Sons : Vent très léger, murmures très lointains, feu de camp crépitant doucement.
    *   Mixage : -24 à -28 LUFS.
*   **Jour 4-5 : Ambiance Forêt Paisible**
    *   Boucle : Vent dans les feuilles (filtre Low-Pass pour adoucir le souffle), chant d'oiseaux très espacé.
*   **Jour 6-7 : Ambiance Zone Danger (Marais / Grottes)**
    *   Grottes : Gouttes d'eau réverbérées, vent sourd dans les tunnels.
    *   Marais : Bulles de gaz graves, bruits mouillés mats, criquets rabaissés en fréquence.
*   **Jour 8-9 : Système de Météo (Pluie/Vent)**
    *   Boucle Pluie : Bruit blanc doux type ASMR (coupe-haut sévère).
    *   Boucle Orage : Tonnerre lointain (grondement sourd, zéro claquement).
*   **Jour 10 : Intégration de l'Ambient Manager**
    *   Mise en place dans Bevy de la superposition des boucles de zone et de la météo.
    *   Test des timeouts aléatoires entre les événements environnementaux (ex: oiseau qui chante toutes les 15-45s).

---

## 🎼 Sprint 3 : Musique & Système de Voix IA (Semaines 7-8)

**Objectif :** Implémenter la dissonance narrative (BGM) et finaliser l'architecture des dialogues générés par l'IA.

*   **Jour 1-3 : BGM - Thème Principal / Village**
    *   Composition ou génération assistée par IA (style 2000s, harpe/flûte/guitares).
    *   Piste très apaisante, tempo lent.
    *   Mixage `.ogg` (Stéréo, cible : -20 à -24 LUFS).
*   **Jour 4-5 : BGM - Exploration (Forêt)**
    *   Composition minimaliste (nappes de synthé, notes espacées).
*   **Jour 6-7 : Intégration TTS (Mockup & Tests)**
    *   Connexion du moteur Bevy à une source de génération vocale (simulateur du MCP/LLM pour les tests en local).
    *   Création du pipeline de réception du flux audio généré par le serveur et lecture via le `Voice Manager`.
*   **Jour 8-9 : Équilibrage Global & Playtest de la Dissonance**
    *   **Phase critique :** Jouer au jeu avec tous les éléments (combats visuellement brutaux VS musique douce classique).
    *   Ajustement des niveaux (Mastering in-engine). La musique ne doit jamais être masquée par les SFX, et les SFX ne doivent jamais percer les tympans.
*   **Jour 10 : Polish & Validation Pré-Alpha**
    *   Revue du code audio Rust.
    *   Vérification du budget mémoire (fichiers < 5MB).
    *   Session de test d'une heure pour valider l'**absence totale de fatigue auditive**.
