# Game Design Systems - MMORPG (Médiéval / Dark Fantasy)

Ce document centralise la conception des systèmes, l'économie, la progression, l'artisanat, les statistiques, et les simulateurs d'équilibrage pour un MMORPG de style Rétro (PS2/Metin2) avec une ambiance allant du Médiéval Fantastique classique à la Dark Fantasy.

---

## 1. Vision et Thème
* **Ambiance :** Médiéval Fantastique teinté de Dark Fantasy. Un monde rude, viscéral où la progression se mérite.
* **Système de Personnage :** **Sans classe (Classless)**. La façon dont le joueur dépense ses points de statistiques et choisit ses compétences définit son rôle.
* **Niveau Maximum (Level Cap) :** Niveau 100.
* **Économie :** Basée sur le troc (les objets ont une valeur d'échange universelle) et un système monétaire classique (Cuivre, Argent, Or).

---

## 2. Système Monétaire et Économie

L'économie est un mix de monnaie traditionnelle et de système de troc fondamental. Tout objet a une valeur intrinsèque.

### Système de Monnaie
* **1 Pièce d'Argent (PA)** = 100 Pièces de Cuivre (PC)
* **1 Pièce d'Or (PO)** = 100 Pièces d'Argent (PA) = 10 000 Pièces de Cuivre (PC)

### L'Économie par le Troc
Chaque ressource (minerai, plante, peau) possède une valeur d'échange. Les joueurs et PNJ peuvent accepter des objets en paiement direct si la valeur équivaut à la somme demandée, avec parfois une "décote" lors du troc avec les PNJ.

### Simulateur : Lutte contre l'Inflation (Long Terme)
Pour éviter la dévaluation de l'Or, des "Gold Sinks" (puits d'or) puissants sont nécessaires.

| Mécanique de Gold Sink | Description | Impact sur l'Inflation |
| --- | --- | --- |
| **Réparation & Usure** | Les équipements perdent en durabilité. Réparer coûte de l'or ou des matériaux précieux. | Fort (constant) |
| **Taxes de Marché** | Les échanges à l'hôtel de vente subissent une taxe de 5% à 10%. | Modéré (selon volume) |
| **Voyage Rapide / Montures** | Entretenir une monture ou utiliser les portails demande des pièces. | Faible à Modéré |
| **Housing & Guildes** | Achat de terrains, entretien de châteaux pour les guildes (Taxes de guilde). | Très Fort (end-game) |

**Formule de l'Inflation Théorique :**
`Masse_Monétaire_Active = (Gold_Généré_Monstres + Gold_Vente_PNJ) - (Gold_Sinks_Taxes + Gold_Sinks_Réparations)`
*L'objectif de l'équilibrage est de maintenir ce ratio proche de 1.*

---

## 3. Progression et Courbe d'XP (Simulateur)

La progression s'étend du niveau 1 au 100. Les premiers niveaux sont rapides, mais la courbe devient exponentielle pour marquer la rudesse du monde.

### Formule de la Courbe d'Expérience
* `XP_Requise(Niveau) = Base * (Niveau ^ Exposant)`
* Exemple d'équilibrage : `Base = 100`, `Exposant = 2.5`

### Simulateur de Progression (Tableau Exponentiel)
| Niveau | XP Nécessaire (pour le niveau) | XP Totale Cumulée | Remarque |
| --- | --- | --- | --- |
| 1 | 0 | 0 | Point de départ |
| 10 | 31,600 | ~100,000 | Fin de l'introduction |
| 25 | 312,500 | ~1,500,000 | Milieu du Early-Game |
| 50 | 1,767,700 | ~15,000,000 | Mid-Game, spécialisation marquée |
| 75 | 4,871,300 | ~60,000,000 | Début du End-Game |
| 90 | 7,684,300 | ~110,000,000 | Le "Mur" ("The Grind") |
| 100 | 10,000,000 | ~180,000,000 | Level Cap atteint |

---

## 4. Statistiques et Compétences (Système Sans Classe)

Puisqu'il n'y a pas de classes, le joueur investit des points de statistiques gagnés à chaque niveau.

### Statistiques Principales
* **Force (FOR) :** Augmente les dégâts physiques en mêlée, la capacité de port (inventaire), et le blocage.
* **Dextérité (DEX) :** Augmente les dégâts à distance, l'esquive, la vitesse d'attaque, et les chances de coup critique.
* **Intelligence (INT) :** Augmente la puissance magique (dégâts/soins), la réserve de Mana/Énergie, et la défense magique.
* **Constitution (CON) :** Augmente les Points de Vie (PV) max, la résistance aux malus, et l'endurance.

### L'Arbre de Compétences (Le "Grimoire Libre")
Le joueur gagne 1 Point de Compétence par niveau (100 points au total). Il peut investir dans différents arbres d'armes ou de magies (Épée, Arc, Magie du Sang, Magie de la Nature).
Des "pré-requis de stats" limitent les combinaisons (ex: *Boule de Feu requiert 30 INT* ; *Coup Lourd requiert 25 FOR*).

---

## 5. Formules de Combat (Simulateur Dégâts & Survie)

Pour assurer un équilibrage, les formules évitent l'inflation infinie des statistiques en utilisant des rendements décroissants.

### Calcul des Dégâts
`Dégâts_Bruts = (Puissance_Arme * (1 + (Stat_Associée / 100))) * Modificateur_Compétence`

### Calcul de la Réduction de Dégâts (Armure)
Pour éviter qu'un joueur devienne invulnérable, l'armure suit une formule asymétrique :
`Réduction_% = Armure / (Armure + (Niveau_Attaquant * 50))`
*Exemple avec Armure 500 contre un attaquant Lvl 10 :* `500 / (500 + 500) = 50% de réduction.`

### Formule Finale de Frappe
`Dégâts_Finaux = Dégâts_Bruts * (1 - Réduction_%) * (1 si Coup Normal, ou X si Critique)`

---

## 6. L'Artisanat (Crafting)

Les métiers sont primordiaux dans l'économie du jeu, d'autant plus que les objets servent de monnaie de troc. L'équipement crafté peut être supérieur à celui "looté".

### Métiers Génériques
1. **Mineur & Bûcheron (Récolte) :** Extraire du minerai et couper du bois.
2. **Forgeron :** Crée armes, armures lourdes, et outils. Demande de la Force pour exceller (bonus craft).
3. **Menuisier / Fabricant d'arcs :** Crée arcs, bâtons, et meubles (Housing).
4. **Tailleur / Tanneur :** Crée les armures légères, sacs (augmente capacité de port).
5. **Alchimiste :** Crée potions de soin, buffs, et poisons. Indispensable pour le PvE end-game et le PvP.

### La Boucle de Crafting
* L'équipement haut niveau demande des composants trouvés uniquement sur des boss (incite au groupe).
* Le craft a une **chance de réussite** et des **niveaux de qualité** (Normal, Supérieur, Épique). Le niveau du métier augmente ces probabilités.

---

## 7. Scripts de Simulation Mathématique (Outils de Design)

Pour équilibrer ces systèmes au quotidien, voici des algorithmes de simulation basiques (en Python) pouvant être utilisés par les Game Designers :

```python
# Simulateur de Dégâts
def simuler_degats(puissance_arme, stat, armure_cible, lvl_cible):
    degats_bruts = puissance_arme * (1 + (stat / 100))
    reduction = armure_cible / (armure_cible + (lvl_cible * 50))
    degats_finaux = degats_bruts * (1 - reduction)
    return round(degats_finaux, 2)

# Exemple : Épée (50 dégâts), 150 Force, contre armure 800 (Lvl 50)
# Résultat : 50 * 2.5 * (1 - (800/3300)) = ~94 dégâts perçants.
```

```python
# Simulateur Courbe d'XP
def calculer_xp_totale(niveau_max):
    base = 100
    exposant = 2.5
    xp_totale = 0
    for niv in range(1, niveau_max + 1):
        xp_niveau = base * (niv ** exposant)
        xp_totale += xp_niveau
        if niv in [10, 25, 50, 75, 100]:
            print(f"Niveau {niv} : {int(xp_niveau)} requise (Total: {int(xp_totale)})")

calculer_xp_totale(100)
```

## 8. Plan d'Action et Sprints (Roadmap sur 6 mois)

L'objectif de cette feuille de route est d'implémenter l'ensemble des systèmes de Game Design décrits précédemment dans l'architecture Rust/Bevy ECS, de manière itérative sur 6 mois.

### Mois 1 : Fondations des Simulateurs et Courbe de Progression
* **Sprint 1 : Outils de Simulation en Rust**
  * Traduire les scripts Python (Calcul des dégâts, Courbe d'XP) en modules de simulation Rust (CLI et tests unitaires) pour aider les Game Designers.
  * Créer les structures de données de base pour la configuration de la progression (base, exposant).
* **Sprint 2 : Implémentation de la Progression (ECS)**
  * Développer le composant `Level` et `Experience`.
  * Créer le système Bevy gérant le gain d'XP et le passage de niveau (Level Up) jusqu'au niveau 100.
  * Implémenter des tests d'intégration simulant l'XP gagnée de 1 à 100.

### Mois 2 : Système de Statistiques et de Compétences (Classless)
* **Sprint 3 : Statistiques Principales**
  * Créer le composant `Attributes` (FOR, DEX, INT, CON).
  * Implémenter le système de distribution des points de statistiques à chaque passage de niveau.
  * Lier les attributs aux sous-statistiques (PV max, endurance, mana, capacité de port).
* **Sprint 4 : Arbre de Compétences et Pré-requis**
  * Définir le format de données (ex: RON/JSON) pour l'arbre des compétences.
  * Implémenter la logique d'apprentissage des compétences avec vérification des pré-requis de statistiques.

### Mois 3 : Résolution du Combat et Formules WGPU/Bevy
* **Sprint 5 : Dégâts et Armures**
  * Implémenter les composants de combat (`Health`, `Armor`, `WeaponStats`).
  * Créer le `CombatSystem` Bevy utilisant les formules de rendements décroissants pour l'armure.
* **Sprint 6 : Modificateurs et Résolution Avancée**
  * Gérer les coups critiques, l'esquive, et les modificateurs de compétences.
  * Lier les statistiques (DEX, FOR, INT) directement au calcul final des dégâts dans l'ECS serveur.

### Mois 4 : Fondations de l'Économie et Inventaire
* **Sprint 7 : Système Monétaire**
  * Créer le composant `Wallet` (Cuivre, Argent, Or) avec conversion automatique.
  * Implémenter un gestionnaire d'inventaire rudimentaire (poids, emplacements limités par la Force).
* **Sprint 8 : Troc et Valeur Intrinsèque**
  * Attribuer des valeurs de base aux ressources.
  * Créer le système d'échange (Trade) entre joueurs et PNJ (validation côté serveur des valeurs équivalentes).

### Mois 5 : Artisanat (Crafting)
* **Sprint 9 : Métiers et Ressources**
  * Créer les entités de nœuds de ressources (Minerai, Arbres) et les systèmes de récolte liés aux statistiques.
  * Implémenter les composants de métiers (Niveau de métier, XP d'artisanat).
* **Sprint 10 : Boucle de Création et Qualité**
  * Développer le système de fusion de ressources pour créer un objet.
  * Introduire l'algorithme probabiliste de réussite et de génération de qualité (Normal, Supérieur, Épique) influencé par la Force ou le niveau du métier.

### Mois 6 : Économie Macro et Équilibrage Global (Gold Sinks)
* **Sprint 11 : Intégration des Gold Sinks**
  * Implémenter la durabilité et l'usure de l'équipement (Composant `Durability`).
  * Créer les systèmes de réparation, taxes de transaction, et coûts de voyage.
* **Sprint 12 : Tests et Équilibrage**
  * Utiliser les outils de simulation Rust créés au mois 1 pour faire tourner des batailles et des économies à grande échelle.
  * Ajustement final des valeurs (XP, taux de drop, coûts de réparation) pour s'assurer que le ratio de l'inflation reste proche de 1.
