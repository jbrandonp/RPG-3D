# Plan d'Action Stratégique : Sound Design & Ingénierie Audio

Ce document définit la vision stratégique et l'approche technique globale pour la conception sonore et l'intégration audio dans le projet Mini-MMO. Il fusionne les directives esthétiques du `SOUND_DESIGN.md` avec l'architecture technique du projet (Horizon 2030, Bevy, IA).

## 1. Vision Stratégique : La Dissonance Audio comme Pilier Narratif

La direction audio n'est pas qu'un habillage esthétique, c'est un outil narratif et psychologique fondamental de l'expérience de jeu. L'objectif est de créer une **dissonance cognitive** persistante chez le joueur.

*   **Le Réconfort Auditif :** L'audio global (BGM, ambiances, sons d'interface) est délibérément conçu pour être **doux, apaisant et classique**. Il évoque les MMORPG pacifiques des années 2000 (harpes, flûtes, nappes douces, sons chauds et feutrés).
*   **La Brutalité Visuelle & Systémique :** Cette douceur auditive entre en collision frontale avec la réalité cruelle du monde (système économique violent, combats sanglants, corruption).
*   **Objectif Psychologique :** L'indifférence absolue du "système de jeu" (représenté par la musique douce continue) face à la souffrance de l'avatar renforce le thème central du projet : **l'illusion du contrôle** et le caractère cauchemardesque du monde. Le son ne juge pas la violence, il l'ignore.

### 1.1. Philosophie de Confort (Zéro Ear-Fatigue)
Conçu pour des sessions de jeu très longues (farm de MMO) :
*   Forte atténuation des fréquences aiguës/stridentes (EQ "Low-Pass" systématisé).
*   Recherche systématique de sons ronds, mats, et réverbérés (esthétique "Rétro PS2").

---

## 2. Piliers d'Implémentation & Approche Solo Developer

En tant que développeur solo avec un budget restreint, la stratégie repose sur l'autonomie et l'utilisation de l'intelligence artificielle.

*   **Assets Audio (SFX/BGM) :** Génération via des outils comme BFXR, synthétiseurs (LMMS), IA musicales (Soundraw, AIVA), ou utilisation de banques de sons gratuites (OpenGameArt, Freesound).
*   **Voix (NPC) :** Remplacement des doublages traditionnels par des **voix générées en temps réel (TTS)** pilotées par l'architecture IA du serveur.

---

## 3. Architecture Technique de l'Audio (Moteur Bevy)

Conformément à l'architecture globale (Client "Terminal"), le moteur client Bevy ne fait que **réagir** aux instructions du serveur. L'audio suit ce principe.

### 3.1. Le Flux Audio (Serveur autoritaire -> Client)
Le client Bevy ne décide pas de jouer le son d'un coup d'épée de lui-même.
1.  Le joueur envoie l'input au serveur (via WebTransport/QUIC).
2.  Le serveur valide l'action et la calcule.
3.  Le serveur émet un événement réseau (RPC) : `PlaySoundEvent(Entity_ID, Action_Type, Position)`.
4.  Le client reçoit l'événement et joue l'asset correspondant via son `AudioManager`.

### 3.2. L'AudioManager (Client Bevy Rust)
Un composant central gérera différents sous-systèmes :
*   **BGM Manager :** Gère la musique principale, assure des **crossfades fluides (3-5 secondes minimum)** pour ne jamais casser l'immersion lors des transitions de zones.
*   **Ambient Manager :** Superpose les boucles d'ambiance (vent, eau) avec un système de timeout aléatoire entre les boucles pour casser la répétitivité.
*   **SFX Manager :** Gère les bruitages courts (combats, UI). Responsable du "voice stealing" (limiter les canaux simultanés pour éviter la saturation).
*   **Voice Manager (IA/MCP) :** Gère les flux audio TTS entrants.
*   **Spatial Audio :** Assure le positionnement 3D (atténuation logarithmique/linéaire selon la distance) basé sur le monde ECS Bevy.

### 3.3. Variations Aléatoires (Anti-répétition systémique)
Règle d'or pour la programmation Bevy : **Aucun son répété ne doit sonner exactement de la même manière.**
*   Application systématique d'une **variation de Pitch ($\pm 10\%$)**.
*   Légère **variation de volume ($\pm 2$ dB)**.
*   Mise en place de banques sonores miniatures (ex: 3 variantes de "coup d'épée" choisies au hasard).

---

## 4. Intégration IA, MCP et Mémoire Vectorielle

Le système de dialogue et de voix est entièrement géré par l'infrastructure IA (Horizon 2030).

1.  **Contexte & Mémoire :** Lorsqu'un joueur interagit avec un PNJ, le serveur IA consulte la base de données vectorielle (Qdrant/Milvus) pour retrouver les "souvenirs" pertinents (Similarité Cosinus).
2.  **Génération (LLM) :** Le LLM génère la réponse textuelle du PNJ via le protocole MCP (qui valide l'intention de l'IA).
3.  **Synthèse Vocale (TTS) :** La réponse textuelle est envoyée à un moteur TTS (ex: Coqui, ElevenLabs API) pour générer l'audio.
4.  **Diffusion (Client) :** Le client reçoit et joue le stream audio généré.

---

## 5. Contraintes Techniques Rétro

Pour correspondre aux capacités mémoires visées par le style "PS2" et optimiser les performances :

| Paramètre | Valeur standard exigée | Rôle / Justification |
| :--- | :--- | :--- |
| **Format long** | `.ogg` (Vorbis) | BGM et longues ambiances (compressé, conçu pour le streaming). |
| **Format court** | `.wav` (PCM) | SFX et UI (chargé en RAM, zéro latence au déclenchement). |
| **Sample Rate** | 44.1 kHz | Standard CD audio. Cohérence globale requise. |
| **Résolution** | 16-bit | Style rétro / Limitation du poids. |
| **Bitrate** | 128 kbps (Amb) / 192 kbps (BGM) | Économie de bande passante / espace disque. |
| **Canaux** | Mono (SFX) / Stéréo (BGM & UI) | La spatialisation 3D nécessite du mono pour les SFX. |
| **Poids max** | 5 MB par fichier | Respect strict du *memory budget* d'époque. |

### Cibles de Mixage (Loudness LUFS)
*   Musique : -20 à -24 LUFS
*   Ambiances : -24 à -28 LUFS
*   SFX Combats : -16 à -20 LUFS
*   Voix : -18 à -22 LUFS
*   Interface (UI) : -22 à -26 LUFS
