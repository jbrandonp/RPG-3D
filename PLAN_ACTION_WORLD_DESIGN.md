# Plan d'Action Stratégique : World Design (Elara's Black Mist)

## 1. Vision et Objectifs
Le "World Design" de ce projet MMORPG Rétro PS2 repose sur une séparation stricte entre une esthétique "Low-Poly" volontairement datée et une architecture backend ultra-moderne, massivement scalable et "AI-Native".
L'environnement n'est pas qu'un décor statique : c'est une entité hostile, dynamique (via le Brouillard Noir) et profondément interconnectée avec l'état psychologique des joueurs (Trauma, Corruption, Rebirth).

## 2. Architecture Technique Fondamentale (Client vs Serveur)

### Le Serveur Autoritaire (Bevy Headless)
Le monde réel n'existe **que** sur le serveur.
- **Topologie et Collisions :** Calculées via des primitives mathématiques (sphères, boîtes) et un NavMesh statique. Aucun *Mesh Collider* complexe n'est utilisé.
- **Gestion Spatiale (Chunks) :** Le monde est découpé en grilles de 64x64 unités. Le serveur ne simule que les chunks contenant des joueurs actifs.
- **Navigation (IA) :** Exécutée à 100% côté serveur.

### Le Client "Terminal"
Le client est un visualiseur "stupide" et optimisé.
- **Streaming Asynchrone :** Il charge visuellement les `SceneBundle` (fichiers `.glb`) uniquement pour les chunks proches (rayon d'intérêt d'environ 200m).
- **Prédiction Locale :** Permet des mouvements et combats fluides, mais le serveur garde le mot de la fin (Rollback si nécessaire).

## 3. Topographie de Velnora et Écologie

L'Île de Velnora (180x90 km) est structurée comme une main fracturée, imposant une progression radiale et verticale :

| Zone | Niveaux | Danger | Entités | Mécanique Spéciale |
|---|---|---|---|---|
| **Velnor (Bidonvilles/Docks)** | 1-10 | Faible/Moyen | Rats, pillards, éclaireurs goblins | Économie urbaine, Safe Zone relative |
| **Plaines & Marais** | 8-18 | Moyen | Patrouilles goblines, canidés corrompus | Terrain limitant (Wet, ralentissement) |
| **Forêt des Murmures** | 15-30 | Élevé | Goblinoïds supérieurs, arachnides | Nids instanciés (procéduraux) |
| **Montagnes Brisées** | 25-40 | Très élevé | Orcs, Trolls, Sectateurs | Collecte de ressources critiques |
| **Falaises d'Argent** | 30-50 | Très élevé | Deep Ones, faune abyssale | Exploration sous-marine |
| **Syphralis Ruines** | 35-55 | Extrême | Abominations, entités primordiales | Zone finale, Brouillard dense |
| **Sanctuaire des Ossements** | 40+ | Variable | Garde squelettique, vétérans | Hub diplomatique géré par Kazuki |

## 4. Intégration des Systèmes Dynamiques (Horizon 2030)

### 4.1. Le Brouillard Noir (Black Mist)
- **Timer Asynchrone Macro :** Agit comme une pression temporelle globale. Il consume progressivement les zones sûres (200 à 800m par cycle).
- **Conséquences :** Multiplie les statistiques des entités ennemies locales, modifie l'éclairage et l'ambiance visuelle du client, et force le déplacement des joueurs.

### 4.2. Instances de Nids Goblinoïdes
- Les donjons souterrains sont des `World` Bevy instanciés séparément.
- Isolation totale du monde extérieur. Purger l'AoI est nécessaire pour progresser (portes verrouillées).

### 4.3. Trauma, Corruption et Rebirth
- L'exposition aux zones corrompues et la mort modifient l'état physique et psychologique du joueur (Corruption de l'apparence 3D, Trauma affectant le gameplay).
- La mort par capture en zone corrompue ne résulte pas en un "Game Over" standard, mais active le système de **Rebirth**, liant l'âme (`SoulLink`) à un nouveau corps de niveau 1 (avec mutations génomiques) généré dans un nid.

## 5. Roadmap Stratégique du World Design

1. **Fondations Physiques (Sprint 0-1) :** Mettre en place la grille spatiale, les structures ECS de zone, les collisions primitives et le mouvement avec prédiction/rollback.
2. **Écologie Basique (Sprint 2) :** Implémenter les modificateurs de terrain (vitesse dans les marais), les jauges de Trauma/Corruption et les premiers spawners.
3. **Monde Dynamique (Sprint 3) :** Activer la mécanique du Brouillard Noir, le système d'instances (Nids) et le processus de Rebirth.
4. **Hub et IA (Sprint 4) :** Finaliser l'économie et la navigation complexe des PNJ dans Velnor.
