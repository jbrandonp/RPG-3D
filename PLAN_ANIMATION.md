# Plan d'Animation : Personnages, Créatures, Sorts et Effets (MMORPG 3D Bevy)

## 1. Vision et Style Visuel

### Style Rétro PS2 / Metin2
L'esthétique globale vise un rendu 3D rétro, inspiré de l'ère PS2 (faible nombre de polygones, textures peintes à la main, absence de PBR complexe).
- **Format de fichier :** Les modèles et animations utiliseront le format **glTF** (`.glb`), parfaitement supporté par Bevy.
- **Squelettes (Rigging) :** Animations squelettiques (Skeletal Animation) avec un nombre limité d'os pour préserver les performances et le style "low poly".
- **Blending :** Utilisation de transitions franches ou de fondus très courts entre les animations pour un ressenti "arcade" et réactif typique des jeux de cette époque.

---

## 2. Architecture Technique (Moteur Bevy)

Dans Bevy, l'animation s'intègre naturellement dans l'architecture ECS (Entity Component System).

### Composants Bevy Utilisés
- `AnimationPlayer` : Composant standard de Bevy pour jouer les clips d'animation glTF.
- `AnimationGraph` / `AnimationTransitions` : Pour gérer les fondus et le passage d'une animation à l'autre (ex: Marche -> Course).
- `StateMachine` (Crate externe comme `seldom_state` ou logique custom) : Pour définir formellement les états d'une entité (ex: `Idle`, `Running`, `Attacking`, `Stunned`).

### Workflow ECS
1. **Input / Réseau :** Une action est détectée (touche pressée par le joueur local, ou paquet réseau reçu pour une autre entité).
2. **Changement d'État :** Le composant `ActionState` ou `PlayerState` de l'entité est mis à jour (ex: `State::Attacking`).
3. **Système de Résolution :** Un système observe les changements de `State`. Lorsqu'un état change, il envoie un ordre à l'`AnimationPlayer` associé pour jouer le clip correspondant.
4. **Événements d'Animation :** L'utilisation de timers ou d'événements liés aux frames d'animation pour déclencher des effets sonores (bruits de pas) ou des effets visuels (particules d'un sort).

---

## 3. Synchronisation Réseau et Fluidité

Pour un MMORPG, la latence est le principal ennemi. Le serveur est autoritaire, mais le client doit être réactif.

### Prédiction Locale (Joueur Local)
- Lorsqu'un joueur appuie sur le bouton d'attaque, le client **n'attend pas** le serveur. Il joue immédiatement l'animation d'attaque et déclenche les effets visuels/sonores.
- Le client envoie l'intention (`ActionRequest::Attack`) au serveur.
- Si l'action est invalide (ex: cooldown non respecté, étourdissement), le serveur envoie une correction (`ActionDenied`), forçant le client à annuler l'animation (rollback) et revenir à l'état `Idle`.

### Interpolation et Extrapolation (Autres Joueurs et Monstres)
- Les animations des autres entités sont pilotées par les paquets du serveur.
- Si le serveur envoie un paquet de déplacement, le client place l'entité en état `Running` et interpole sa position.
- Les attaques ennemies sont affichées au moment où le client reçoit l'événement du serveur (`EntityAttacked`). Pour compenser la latence visuelle, la "hitbox" ou la confirmation des dégâts est calculée par le serveur de manière rétroactive (lag compensation) ou au moment de l'impact serveur.

### Séparation de la Logique et de l'Esthétique
- Le serveur tourne en mode "headless" (sans rendu) : il ne charge **jamais** les meshs ou les `AnimationPlayer`.
- Le serveur ne connaît que les boîtes de collision (colliders), les temps de cast (incantation) et les cooldowns.
- Le client lie la durée de l'animation à la durée de l'action dictée par le serveur.

---

## 4. Catalogue des Animations et États

### A. Personnages Joueurs (PJ)
Chaque classe ou type d'arme (Épée, Arc, Bâton) aura un set d'animations ("Animation Set").

**États de base :**
- `Idle` (Repos) : Légère respiration, posture de combat si l'arme est dégainée.
- `Walk` / `Run` : Déplacement classique.
- `Jump` : (Si applicable) Saut et atterrissage.
- `HitReact` (Touché) : Tressaillement lors de la réception d'un coup lourd.
- `Death` : Effondrement au sol.

**États de Combat :**
- `Attack_Melee_1, 2, 3` : Combo d'attaques de mêlée.
- `Cast_Start` : Début d'incantation d'un sort (mains en l'air, concentration).
- `Cast_Release` : Relâchement de la magie (projection).
- `Ranged_Draw` / `Ranged_Fire` : Bande l'arc, puis tire.

### B. Créatures et Monstres (PNJ)
Les monstres auront des sets plus simples pour économiser la mémoire.

- **Bête (ex: Loup) :** `Idle`, `Trot`, `Run`, `Bite` (Morsure), `Howl` (Hurlement/Aggro), `Death`.
- **Humanoïde (ex: Gobelin) :** `Idle`, `Run`, `SwingWeapon` (Coup grossier), `Flee` (Fuite), `Death`.
- **Boss :** Animations spécifiques pour des attaques de zone (ex: `GroundSmash` - Frappe au sol).

### C. Sorts et Effets Visuels (VFX)
Les sorts ne sont pas seulement des animations de personnages, mais des entités à part entière (particules, géométries).

- **Particules (CPU/GPU) :** Utilisation d'un système de particules (ex: `bevy_hanabi`) pour le feu, la glace, les étincelles.
- **Projectiles :** Boules de feu, flèches. Entités avec une vitesse, un composant `Transform`, et un modèle/particule attaché. L'animation est gérée par le mouvement lui-même.
- **Effets de Zone (AoE) :** Cercles magiques au sol. Animations de shaders (défilement de textures UV, transparence) plutôt que des animations squelettiques.
- **Hit Effects :** Petits flashs ou éclaboussures de sang (sprites 2D sous forme de billboards faisant face à la caméra) apparaissant brièvement lors d'un impact, très typiques des jeux PS2.

---

## 5. Étapes d'Implémentation Recommandées

1. **Intégration d'un modèle de test :** Charger un modèle glTF simple avec une animation `Idle` et `Run`.
2. **Machine à états du joueur :** Créer le système Bevy qui passe de `Idle` à `Run` selon les inputs locaux.
3. **Contrôle d'Animation :** Connecter l'état au `AnimationPlayer` avec `AnimationTransitions` pour des passages fluides.
4. **Synchronisation Réseau :** Recevoir la position d'un "Dummy" (joueur factice) depuis le réseau et faire jouer son animation `Run` quand sa position interpolée change.
5. **Combats et Événements :** Ajouter l'animation d'attaque, bloquer le mouvement pendant l'attaque, et synchroniser l'apparition d'un effet visuel (particule) à une frame précise de l'animation.
