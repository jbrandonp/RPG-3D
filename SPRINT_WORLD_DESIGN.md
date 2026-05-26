# Sprints World Design : Feuille de Route (10 Semaines)

## Organisation Générale
- **Durée par sprint :** 2 semaines.
- **Approche :** 5 sprints jusqu'à la version Pré-Alpha.
- **Règle d'or :** Ne jamais passer au sprint suivant si le déplacement basique, les collisions et la persistance serveur de la zone actuelle ne sont pas validés.

---

## SPRINT 0 : Setup & Fondations (Focus Technique)
*Objectif : Mettre en place l'architecture ECS Bevy, le serveur Headless et une zone de test "Flat".*

**Semaine 1 : Architecture Serveur & Physique**
- **Jour 1-2 :** Initialisation du serveur Bevy Headless. Définition des structures réseaux (WebTransport/QUIC).
- **Jour 3-4 :** Création du système de découpage spatial (`ChunkManager`). Définition de la grille de 64x64u.
- **Jour 5 :** Intégration du moteur physique serveur (Rapier3D) avec des colliders primitifs exclusifs.

**Semaine 2 : Client Terminal & Synchronisation**
- **Jour 6-7 :** Initialisation du Client Bevy. Mise en place de la prédiction locale pour les déplacements.
- **Jour 8-9 :** Implémentation du système de Rollback et de `Zone d'Intérêt` (le serveur n'envoie que les entités à <200m).
- **Jour 10 :** Création d'une "Flat Zone" (0 décors, juste un sol plat avec un collider et des murs invisibles). Le joueur doit pouvoir s'y déplacer sans sortir des limites.

---

## SPRINT 1 : Zone 1 "Velnor Bidonvilles" (Prototype Jouable Lvl 1-10)
*Objectif : Rendre le premier environnement traversable avec collisions et instanciation du premier ennemi.*

**Semaine 1 : Topologie et Limites**
- **Jour 1-2 :** Définition ECS de la `Zone 1` (id, nom, bounds, niveau de danger).
- **Jour 3-4 :** Intégration du NavMesh côté serveur pour cette zone spécifique.
- **Jour 5 :** Intégration des `SceneBundle` côté client (blockouts 3D de Velnor Docks). Validation de la correspondance Client (Mesh) / Serveur (Collider).

**Semaine 2 : Entités et Spawn**
- **Jour 6-7 :** Création du système `SpawnSystem`. Définition du composant `SpawnPoint`.
- **Jour 8-9 :** Paramétrage d'un `SpawnPoint` pour "Éclaireur Goblin" (Niveau 3-12). L'ennemi apparait sur le serveur et est streamé au client.
- **Jour 10 :** Tests de franchissement de limites. Validation absolue : le personnage évolue dans un monde fini, avec un ennemi statique ou à navigation basique.

---

## SPRINT 2 : Plaines & Marais (Lvl 8-18) + Écologie
*Objectif : Transition de zones, modificateurs de terrain et jauges psychologiques.*

- **Game Design :** Implémentation des Marais (modificateurs `Wet` et malus de vitesse).
- **Technique :** Transition transparente entre la Zone 1 (Velnor) et la Zone 2 (Marais) via le Chunk Streaming.
- **Systèmes (NOTES_GDD_UPDATE) :** Implémentation des composants `PsychologicalState` (`TraumaIndex`, `CorruptionIndex`). Mise en place des triggers d'évolution de ces jauges en fonction du biome.

---

## SPRINT 3 : Forêt des Murmures (Lvl 15-30) + Nids & Brouillard Noir
*Objectif : Mécaniques systémiques complexes de survie et instances fermées.*

- **Game Design :** Le Brouillard Noir s'active. Implémentation du `FogExpansionSystem` (timer asynchrone modifiant les zones et les stats des ennemis).
- **Instances :** Création de l'architecture pour les "Nids instanciés". Le serveur doit être capable de spawner un `World` indépendant (Donjon procédural).
- **Systèmes (NOTES_GDD_UPDATE) :** Mécanique de **Rebirth**. Si le joueur meurt dans le Brouillard, destruction de l'entité corporelle, conservation du `SoulLink`, et respawn dans un Nid avec un `GenomeSeed`.

---

## SPRINT 4 : Hub Velnor & Économie (Finalisation Pré-Alpha)
*Objectif : Ville complète, PNJ naviguant, et préparation au PVP économique.*

- **Game Design :** Complétion de Velnor (Bâtiments majeurs 2000-5000 polys, zones sécurisées).
- **IA Serveur :** Navigation complexe des PNJ via NavMesh. Patrouilles et interactions marchandes.
- **Tests Pré-Alpha :** L'économie réagit aux actions (inflation dynamique). Vérification globale de la charge serveur (streaming chunks, validation physique) avec joueurs simulés.
