# Backlog Sprints World Building (Post-PoC)

Ce document contient le backlog des futurs Sprints (Sprints 1 à 5) ainsi que les objectifs pour la phase Post-Alpha. Il s'appuie sur la fondation validée lors du Sprint 0 (PoC Pipeline).

---

## Sprint 1 : Zone de Test Flat
**Durée estimée** : 2 semaines.
**Objectif** : Valider le pipeline artistique Rétro PS2 et le concept d'Atlas de Biome sur un environnement plat et minimaliste.

### User Stories
*   **US 1.1 - Création de l'Atlas de Biome** : En tant qu'Artiste 3D, je veux créer un atlas de texture unique (`512x512` ou `1024x1024`) pour regrouper les textures d'un sol basique et de 3 décors (ex: baril, caisse, mur).
*   **US 1.2 - Création des Assets Test** : En tant qu'Artiste 3D, je veux modéliser un segment de sol plat et 3 petits objets décoratifs en appliquant la méthode d'UV Mapping sur le nouvel Atlas.
*   **US 1.3 - Export et Intégration Client** : En tant que Développeur Client, je veux importer ces 4 modèles (`.glb` visuels) dans Bevy et vérifier qu'ils utilisent le même matériel (validation d'un seul draw call si instanciés massivement).
*   **US 1.4 - Définition Logique Serveur** : En tant que Développeur Serveur, je veux associer des colliders basiques (Box/Cylinder) aux 3 objets de décor, et un collider de sol infini (ou mesh simple) pour le terrain.

### Critères d'Acceptation
- [ ] Un seul fichier texture (Atlas) est utilisé pour tous les objets du Sprint 1.
- [ ] Les objets s'affichent correctement dans le client avec le style "hand-painted".
- [ ] Le joueur (serveur) peut marcher sur le sol et buter contre les 3 objets.

---

## Sprint 2 : Velnor (Bidonvilles) - Zone 1 Partielle
**Durée estimée** : 2 semaines.
**Objectif** : Amorcer la production d'un biome urbain (Niveau 1-10) en commençant par le quartier pauvre (Bidonvilles/Docks).

### User Stories
*   **US 2.1 - Atlas Bidonvilles** : Création de l'Atlas de texture spécifique au biome `VelnorSlums` (bois pourri, tôle, terre, cordes).
*   **US 2.2 - Modélisation des Habitations Précaires** : Modélisation de 2 ou 3 variantes de cabanes/tentes (Low Poly ~1000 tris max).
*   **US 2.3 - Modélisation des Props** : Modélisation d'assets environnementaux (caisses cassées, braseros, petits pontons).
*   **US 2.4 - Level Design (Blocage)** : En tant que Level Designer, je veux placer ces assets pour former un petit quartier cohérent de la zone de Velnor.
*   **US 2.5 - Navigation Serveur** : En tant que Développeur Serveur, je veux générer (Bake) le NavMesh pour ce quartier afin de préparer le pathfinding des futurs PNJ (gobelins/voleurs).

---

## Sprint 3 : Velnor (Ville Complète et Intérieur)
**Durée estimée** : 2 semaines.
**Objectif** : Terminer la ville de départ et implémenter le chargement fluide (ou la transition) entre l'extérieur et l'intérieur d'un bâtiment majeur.

### User Stories
*   **US 3.1 - Atlas Ville Principale** : Ajout des textures nobles à l'Atlas de Velnor (pierre taillée, toits en tuiles, vitraux).
*   **US 3.2 - Modélisation Bâtiment Majeur** : Modélisation d'un grand bâtiment (ex: Guilde, Temple) avec son enveloppe extérieure et son mesh intérieur séparé.
*   **US 3.3 - Système de Chunks/Transition** : En tant que Développeur Client/Serveur, je veux implémenter un système permettant au joueur de passer la porte du bâtiment (déclenchement via `TriggerVolume`) et de charger l'intérieur tout en cachant/déchargeant l'extérieur (ou gestion par occlusion).
*   **US 3.4 - Level Design (Velnor Centre)** : Assemblage du centre-ville autour du bâtiment majeur.

---

## Sprint 4 : Plaines et Marais (Zone 2)
**Durée estimée** : 2 semaines.
**Objectif** : Créer de vastes espaces ouverts (Niveau 8-18) et valider le système d'Instanciation Massive (Instanced Rendering) pour la végétation.

### User Stories
*   **US 4.1 - Modélisation de la Végétation** : Modélisation d'herbes, de roseaux et d'arbres clairsemés. Utilisation de plans croisés (billboards/alpha) pour minimiser le nombre de triangles.
*   **US 4.2 - Moteur de Rendu Instancié (Client)** : En tant que Développeur Client, je veux implémenter l'*Instanced Rendering* dans Bevy pour afficher des centaines d'herbes/arbres identiques en un seul draw call.
*   **US 4.3 - Spawns et Triggers (Serveur)** : Définition de `SpawnZone` vastes dans les plaines pour les futurs monstres de bas niveau.
*   **US 4.4 - Modélisation du Terrain (Heightmap/Mesh)** : Création d'un terrain vallonné pour la plaine (modélisation de collines douces).

---

## Sprint 5 : Forêt des Murmures (Zone 3) et Mécanique de Nids
**Durée estimée** : 2 semaines.
**Objectif** : Créer un environnement très dense (Niveau 15-30) et introduire une logique environnementale serveur ("Nids" qui spawnent des ennemis).

### User Stories
*   **US 5.1 - Végétation Dense** : Modélisation de grands arbres (pins sombres, racines noueuses) et d'un nouveau biome `WhisperingForest`.
*   **US 5.2 - Modélisation des Nids (Gobelinoïdes)** : Création d'assets de campements ou de structures organiques (Nids).
*   **US 5.3 - Logique de Spawn (Serveur)** : Implémenter le comportement du composant `SpawnZone` lié à un objet destructible (Le Nid). Si le nid est détruit, le spawn s'arrête.

---

## Phase Post-Alpha (Horizons)

### 1. Le Brouillard Noir (Black Mist)
Le Brouillard Noir est la menace dynamique principale du monde.
*   **US - Variantes de Shaders (Client)** : Développer un shader ou un tint pour assombrir/corrompre les matériaux des chunks affectés sans modifier le fichier `.glb`.
*   **US - VFX (Client)** : Ajouter des systèmes de particules (billboards 2D) de brume noire sur les chunks corrompus.
*   **US - Altération Logique (Serveur)** : Mettre à jour les `SpawnZone` d'un chunk corrompu pour générer des monstres d'ombre, et potentiellement modifier le NavMesh ou ajouter des colliders d'obstacles organiques temporaires.

### 2. Biomes Avancés
*   **Montagnes Brisées (Lvl 25-40)** : Focus sur la verticalité, les ponts suspendus, les grottes peu profondes.
*   **Falaises d'Argent (Lvl 30-50)** : Architecture navale et nids de monstres volants.
*   **Syphralis Ruines (Lvl 35-55)** : La cité originelle corrompue. Focus sur les grands bâtiments détruits (assets complexes).
*   **Sanctuaire des Ossements (Lvl 40+)** : Donjons fermés de haut niveau. Validation de la mécanique d'instanciation de donjon (Worlds Bevy isolés côté serveur).
