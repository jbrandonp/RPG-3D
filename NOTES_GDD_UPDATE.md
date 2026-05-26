# NOTES DE MISE À JOUR : GAME DESIGN DOCUMENT (GDD)

Suite à la bascule narrative vers l'univers de **"Elara's Black Mist"**, le fichier `GAME_DESIGN_DOCUMENT.md` actuel doit être revu en profondeur. Voici les directives techniques et conceptuelles à intégrer lors de la prochaine refonte du GDD :

## 1. NOUVELLES STATISTIQUES JOUEUR (Variables d'État)
Le profil de personnage d'Elara n'est plus classique (HP/MP/Endurance). Il faut ajouter des jauges de survie psychologique et physique :
- **Trauma (Traumatisme) :** Jauge (0-100). Augmente lors de combats extrêmes, embuscades, ou défaites (viols/tortures). À partir de 75, débloque des malus de fuite mais potentiellement des buffs de type "Rage Froide" ou "Berserk".
- **Corruption :** Jauge (0-100). Augmente lors de l'exposition prolongée au *Black Mist* ou via contact avec les Abominations. Influence l'apparence physique (yeux rouges, peau pâle) et les interactions PNJ (rejet dans les Slums, acceptation chez les Cultistes).
- **Pregnancy (Grossesse) & Race Seed :** Mécanique conditionnelle si la HP tombe à 0 face à des Goblinoïds ou Deep Ones. Déclenche des debuffs massifs de vitesse et d'endurance pendant un cycle in-game.

## 2. MÉCANIQUE DE REBIRTH (Renaissance Hybride)
La mort définitive existe pour les PNJ, mais pas pour le Joueur ("Élu").
- **Système de Rebirth Actuel :** Si Elara meurt *pendant une grossesse*, la mécanique de Rebirth s'active. Elle réapparaît au niveau 1 (ou avec un malus d'XP sévère), mais hérite de traits raciaux liés au "père" du cycle précédent.
- **Exemple d'Implémentation Bevy (Rust) :**
  - `Goblin_Trait`: +20% Vitesse d'attaque, Vision nocturne, -30% Charisme Humain.
  - `DeepOne_Trait`: Respiration aquatique, +15% Résistance magique.
  - Le `PlayerBundle` devra accepter un vecteur de `Traits` persistants lors de la recréation de l'entité.

## 3. REFONTE DES CONDITIONS D'ÉCHEC (Game Over / Defeat States)
- Remplacer l'écran de mort classique par des **Scènes de Défaite** (Defeat Events).
- Tomber à 0 HP face à un groupe de Goblinoïds ne tue pas instantanément : cela déclenche un `State::Captured` ou `State::Traumatized`. Le joueur réapparaît dans un nid (donjon) ou est jeté à moitié mort dans les bois, avec l'inventaire vidé (sauf équipement "Soulbound").

## 4. SYSTÈME DE LOOT ET EXPÉRIENCE (L'Avantage "Player")
- Les joueurs (Elara, Kazuki) possèdent un tag `is_player: true` caché dans la base de données.
- **Modification de la courbe d'XP :** Gagner de l'XP sur les humains rapporte peu. Massacrer des Goblinoïds applique un multiplicateur occulte (`XP_Mult = 1.5`), encourageant le style de jeu obsessionnel type "Goblin Slayer".

## 5. DYNAMIQUES DE MONDE (Le Brouillard Noir)
- Le serveur doit implémenter un chronomètre global (World Clock) gérant l'avancée du **Black Mist**.
- Techniquement, cela implique de modifier la configuration des "Chunks" du monde dans Bevy : modifier le `BiomeType` de `Plains` vers `Corrupted_Mist` de manière asynchrone, modifiant la table de spawn des monstres (Spawn Tables) et la colorimétrie des shaders de la zone.
