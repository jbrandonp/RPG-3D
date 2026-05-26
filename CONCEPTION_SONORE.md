# Document de Conception Sonore (Audio Design Document) - Mini-MMO

**Version :** 1.0
**Statut :** Brouillon / Phase de Préproduction
**Projet :** Mini-MMO (Architecture Bevy ECS)
**Esthétique Cible :** Rétro PS2 / Classic MMORPG (ex. Metin2, Lineage II)

---

## 1. Vision et Direction Artistique

### 1.1. Intention Globale
La direction audio de ce projet a pour objectif de recréer la nostalgie des premiers MMORPG en 3D des années 2000. Elle repose sur une approche **orchestrale synthétique** caractéristique de l'ère PlayStation 2. La musique doit évoquer un monde épique et mystérieux, tandis que le sound design s'assure d'ancrer les actions du joueur avec clarté et satisfaction.

### 1.2. Esthétique et Tonalité
*   **Identité Sonore** : Utilisation volontaire de banques de sons classiques (romplers de type Roland SC-88, Korg M1, ou bibliothèques orchestrales compressées) pour obtenir ce grain "rétro" spécifique.
*   **Traitement Audio** : Légère compression et utilisation de réverbérations algorithmiques d'époque (types "Hall" ou "Plate" denses) pour simuler l'espace sans nécessiter de calculs modernes coûteux (ray-tracing audio).
*   **Palette Instrumentale** :
    *   *Mélodique* : Cordes staccato/legato, chœurs synthétiques, bois (flûtes, hautbois).
    *   *Rythmique* : Timbales d'orchestre, percussions martiales, pizzicatos.
    *   *Harmonique* : Nappes (pads) évolutives, harpes, pianos légèrement détunés.

---

## 2. Spécifications Techniques et Intégration

### 2.1. Moteur Audio et Implémentation
*   **Moteur** : Intégration native via le moteur **Bevy** (utilisation de `bevy_audio` ou d'un plugin dédié comme `bevy_kira_audio` pour une gestion avancée).
*   **Format des Fichiers** :
    *   *Musiques (BGM)* : Ogg Vorbis (`.ogg`) à 128 kbps (optimisation de l'espace mémoire tout en conservant la qualité requise pour le style rétro).
    *   *Bruitages (SFX)* : WAV (`.wav`) en 16-bit / 44.1 kHz pour les sons nécessitant du punch (impacts, UI).
*   **Spatialisation (3D Audio)** : Utilisation d'un modèle d'atténuation logarithmique pour les effets diégétiques (bruits de pas, monstres). Les sons ambiants globaux seront lus en stéréo standard (2D).

### 2.2. Gestion Dynamique
*   **Crossfades** : Temps de transition de 2.5 secondes (Fade In / Fade Out) entre les zones ou lors des entrées en combat.
*   **Système d'États** : La musique réagit aux "États" du joueur (Exploration, Danger imminent, Combat engagé, Mort).

---

## 3. Musique et Thèmes (BGM - Background Music)

### 3.1. Thème Principal (Écran Titre & Connexion)
*   **Titre Suggéré** : *L'Appel du Nouveau Monde*
*   **Rôle** : Introduire le joueur à l'univers avant la connexion au serveur. Doit être mémorable et héroïque.
*   **Structure Musicale** :
    *   *Tonalité* : Do mineur (C minor), évoluant vers un mode Dorien pour le mystère.
    *   *Tempo* : Moderato (~85 BPM).
    *   *Arrangement* : Introduction éthérée (harpe, pads), suivie de l'exposition du thème principal par les cuivres (cors). Climax orchestral complet avec chœurs.

### 3.2. Musiques de Zones

#### 3.2.1. Le Village (Hub Principal)
*   **Ambiance** : Chaleureuse, diurne et sécurisante. Inviter au commerce et à l'interaction sociale.
*   **Structure Musicale** :
    *   *Tonalité* : Fa majeur (F Major).
    *   *Tempo* : Andante (~95 BPM).
    *   *Instrumentation* : Dominante acoustique (guitare, flûte traversière, tambourins).
*   **Intégration** : Boucle fermée de 2 à 3 minutes, mixage en arrière-plan pour laisser la place aux bruits de foule, de forge et aux interfaces.

#### 3.2.2. La Forêt (Zone Extérieure Initiale)
*   **Ambiance** : Mystique, paisible mais parsemée d'inconnus.
*   **Structure Musicale** :
    *   *Tonalité* : La mineur (A minor).
    *   *Tempo* : Adagio (~70 BPM).
    *   *Instrumentation* : Hautbois solo, cordes jouées en sourdine, nappes éthérées.
*   **Intégration** : Morceau très aéré (silences intentionnels) pour mettre en valeur le *soundscape* de la nature (vent, faune).

#### 3.2.3. La Zone Dangereuse (Haut Niveau)
*   **Ambiance** : Oppressante, aride et menaçante. Sensation de danger constant.
*   **Structure Musicale** :
    *   *Tonalité* : Ré mineur harmonique (D harmonic minor).
    *   *Tempo* : Lento (~60 BPM).
    *   *Instrumentation* : Contrebasses staccato lourdes, cuivres dissonants en arrière-plan, percussions sourdes aléatoires.

#### 3.2.4. Le Donjon (Instance d'Équipe)
*   **Ambiance** : Claustrophobique et tendue. L'acoustique simulée (réverbération) y sera virtuellement augmentée.
*   **Structure Musicale** :
    *   *Tempo* : Évolutif, accélérant subtilement au fur et à mesure de la progression (de 75 BPM à 95 BPM).
    *   *Instrumentation* : Chœurs graves (basses/barytons), cloches tubulaires, ostinatos frénétiques aux violoncelles.

---

## 4. Musiques Interactives et Combats

### 4.1. Combat Standard
*   **Déclencheur** : Génération d'agro par un monstre (Event `CombatState::Engaged`).
*   **Ambiance** : Nerveuse et rythmée.
*   **Structure Musicale** :
    *   *Tempo* : Allegro (~130 BPM).
    *   *Boucle* : Courte (45 secondes) pour ne pas être répétitive lors du "farming".
*   **Sortie** : À la mort de l'ennemi (Event `CombatState::Disengaged`), accord résolutif de 2 secondes puis fondu de retour vers la musique d'exploration.

### 4.2. Combat de Boss
*   **Déclencheur** : Entrée dans l'arène du boss ou début de la rencontre.
*   **Ambiance** : Épique, démesurée, soulignant l'enjeu majeur.
*   **Structure Musicale** :
    *   *Tempo* : Presto (~150 BPM).
    *   *Mesure* : Asymétrique (ex: 7/8) pour créer une urgence et désorienter l'auditeur.
    *   *Instrumentation* : Orchestre complet (Tutti), roulements frénétiques de timbales, chœurs scandés.

### 4.3. Jingles et Fanfares
Courtes séquences musicales (Non-Diégétiques) marquant un accomplissement :
*   **Montée de Niveau (Level Up)** : Cuivres éclatants et arpège de harpe ascendant (Durée : 3s).
*   **Quête Accomplie** : Petite mélodie triomphale aux bois (Durée : 4s).
*   **Mort du Personnage** : Accord mineur dissonant descendant et long déclin de réverbération.

---

## 5. Conception Sonore (Sound Design / SFX)

Le sound design doit rester clair et lisible, même lorsque de multiples joueurs exécutent des actions simultanément (gestion de la polyphonie).

### 5.1. Interface Utilisateur (UI)
*   **Esthétique** : Sons "vitreux", clairs et percussifs, typiques des RPG asiatiques des années 2000.
*   **Exemples** :
    *   *Hover (Survol)* : Bruit de "tic" très léger, aigu.
    *   *Clic/Validation* : Son de "cristal" ou "goutte" net.
    *   *Avertissement/Erreur* : Bruit sourd et grave (bruit d'erreur classique).

### 5.2. Sonorités Diégétiques (In-Game)
*   **Foley (Bruitages des personnages)** :
    *   *Mouvements* : Bruits de pas dynamiques selon la surface (herbe, pierre, bois).
    *   *Armes* : Sons d'impacts exagérés et gratifiants (tranchant aigu pour les épées, choc sourd avec écho grave pour les masses).
*   **Environnement (Ambiance)** :
    *   Boucles de fond stéréophoniques gérées par zones (vent dans la forêt, brouhaha lointain dans le village).
    *   Émetteurs audio 3D positionnels (torches crépitantes, forgeron martelant une enclume).
