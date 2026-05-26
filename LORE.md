# LORE.md — Monde, Histoire, Quêtes, PNJ & Arcs Narratifs

> Document de référence narratif pour le projet MMORPG rétro / style PS2.
> Architecture bicouche : **Prototype jouable** (Pré-Alpha) + **Mythologie étendue** (Horizon 2030).

---

## Table des Matières

1. [Concept Central & Philosophie Narrative](#1-concept-central--philosophie-narrative)
2. [Cosmogonie — L'Origine du Monde](#2-cosmogonie--lorigine-du-monde)
3. [Géographie & Zones (Roadmap narrative)](#3-géographie--zones-roadmap-narrative)
4. [Factions & Puissances](#4-factions--puissances)
5. [PNJ — Fiches Personnages](#5-pnj--fiches-personnages)
6. [Bestiaire — Les Corrompus](#6-bestiaire--les-corrompus)
7. [Système de Quêtes](#7-système-de-quêtes)
   - 7.1 [Quête Prototype (Pré-Alpha)](#71-quête-prototype-pré-alpha)
   - 7.2 [Quêtes Secondaires (Alpha)](#72-quêtes-secondaires-alpha)
   - 7.3 [Arc Narratif Principal (Vision 2030)](#73-arc-narratif-principal-vision-2030)
8. [Dialogues & Scènes](#8-dialogues--scènes)
9. [Événements Dynamiques](#9-événements-dynamiques)
10. [Cinématiques (Cutscenes)](#10-cinématiques-cutscenes)
11. [Intégration LLM / Mémoire PNJ (Horizon 2030)](#11-intégration-llm--mémoire-pnj-horizon-2030)
12. [Glossaire](#12-glossaire)

---

## 1. Concept Central & Philosophie Narrative

### Titre du jeu (placeholder)
**AETHON CHRONICLES**
*(Du grec Αἴθων — "ardent, brûlant" — la lumière qui consume autant qu'elle éclaire.)*

### Logline
> Dans un monde où les dieux se sont tus, les hommes ont construit des empires sur leurs cendres. Mais les cendres ne refroidissent jamais vraiment.

### Philosophie
L'histoire ne s'impose pas au joueur — elle **l'attend**. Chaque quête, même la plus minuscule ("tue 3 monstres"), est le symptôme visible d'une cause profonde. Le joueur perçoit d'abord la surface : un village apeuré, une forêt corrompue. Puis, couche par couche, il découvre que chaque détail est un fragment d'un mythe oublié.

**Principe de narration :** *Iceberg storytelling* — 10 % visible dans le prototype, 90 % sous la surface, révélé progressivement.

---

## 2. Cosmogonie — L'Origine du Monde

### Les Trois Ères

#### Ère I — L'Âge des Aethons (Temps mythique)
Les **Aethons** étaient des êtres de lumière pure, ni dieux ni hommes, qui tissaient le monde à partir d'une matière appelée le **Filament**. Ils bâtirent des cités-étoiles et gravèrent leurs lois dans des pierres vivantes appelées **Nexolithes**.

Un jour, l'un d'eux — **Varek le Délieur** — tenta de tisser le néant lui-même pour comprendre ce qui existait avant le commencement. Il y réussit. Et le néant entra dans le monde.

Ce néant prit une forme : une noirceur visqueuse que les anciens textes nomment **la Tache** *(la Gangrène du Filament)*. Les Aethons disparurent — certains disent qu'ils se sacrifièrent pour la contenir, d'autres qu'ils fuirent vers un plan d'existence inaccessible.

#### Ère II — L'Âge des Royaumes (Temps historique, -3000 à -200 ans)
Les races mortelles (humains, Sylvarins, Koraths) héritèrent d'un monde partiellement guéri. Elles ignoraient presque tout des Aethons, sauf ce que contenaient les Nexolithes — des artefacts incompréhensibles, parfois dangereux, souvent convoités.

Des empires se bâtirent, guerres se succédèrent, équilibres s'établirent. La Tache était oubliée — réduite à une métaphore dans les religions populaires, symbole du péché ou de la folie.

#### Ère III — L'Âge du Silence (Temps actuel, -200 à aujourd'hui)
Il y a deux cents ans, **quelque chose** a brisé le sceau primordial que les Aethons avaient posé sur la Tache. Personne ne sait quoi — pas encore. La corruption s'infiltre lentement dans les zones sauvages : forêts, mines, ruines. Les animaux dégénèrent. Les morts se relèvent parfois. Les Nexolithes vibrent étrangement.

Les grandes cités font semblant de ne pas voir. Les petits villages, eux, voient.

---

## 3. Géographie & Zones (Roadmap narrative)

```
CARTE NARRATIVE — AETHON CHRONICLES
─────────────────────────────────────────────────────────
PHASE          ZONE                    STATUT
─────────────────────────────────────────────────────────
Pré-Alpha  →  Village de Cendrecroix   [ JOUABLE ]
               Forêt de Varek           [ JOUABLE ]
Alpha      →  Ruines du Nexe de Sel    [ planifié ]
               Marécages de l'Oubli     [ planifié ]
Beta       →  Cité de Port-Ardente     [ planifié ]
               Les Mines Profondes      [ planifié ]
1.0        →  Plateau des Cendres      [ planifié ]
               Citadelle du Délieur     [ planifié ]
─────────────────────────────────────────────────────────
```

### Zone 0 — Village de Cendrecroix *(Pré-Alpha)*

**Description visuelle (style PS2) :**
Petit village de bois et de pierre grise posé à l'orée d'une forêt dense. Une fontaine centrale, quelques maisons au toit de chaume, une forge abandonnée. Lumière ambrée de fin de journée permanente — ciel légèrement orangé, particules de cendres flottantes. Textures basse résolution volontairement : bois granuleux, sols en terre compactée, ombres dures.

**Ambiance sonore :** Vent faible, craquement de bois, un coq lointain. Musique : luth + percussion douce, mélodie mélancolique en boucle.

**Lore local :**
Cendrecroix fut nommé ainsi car le village fut fondé sur les ruines calcinées d'un avant-poste Aethon. Les habitants d'origine n'ont gardé de cette histoire qu'une superstition vague : "Ne brûle pas de bois de la Forêt de Varek la nuit — cela attire les Corrompus."

---

### Zone 1 — Forêt de Varek *(Pré-Alpha)*

**Description visuelle :**
Forêt dense aux arbres tordus, feuilles sombres tirant sur le pourpre et le brun. Pas de ciel visible sous la canopée. Lumière filtrée verdâtre. Particules noires flottantes (spores corrompues). Zones de sol noirci progressivement plus fréquentes en profondeur.

**Lore local :**
La forêt porte le nom de Varek le Délieur, non par hommage mais par avertissement. Une ancienne stèle à l'entrée, illisible pour la majorité, indique en dialecte Aethon : *"Ici commence le fil défait."* Les bûcherons évitent la forêt depuis six mois. Les animaux qui en ressortent ne ressemblent plus tout à fait à ce qu'ils étaient.

---

## 4. Factions & Puissances

| Faction | Rôle narratif | Alignement | Présence Prototype |
|---|---|---|---|
| **Les Gardiens du Filament** | Ordre secret veillant sur les Nexolithes | Neutre / Bien | Mention dans dialogues |
| **La Guilde des Marchands Libres** | Commerce inter-cités, réseau d'information | Neutre | Aldric (marchand) |
| **Les Corrompus** | Créatures / humains touchés par la Tache | Hostile | 3 monstres en forêt |
| **Le Conseil des Trois Cités** | Pouvoir politique officiel, dans le déni | Neutre / Mal | Mention future |
| **Les Murmureurs** | Cultistes vénérant Varek le Délieur | Antagoniste | Indice caché |

---

## 5. PNJ — Fiches Personnages

---

### PNJ-01 : Maren Asheld — La Gardienne de Cendrecroix

**Rôle dans le prototype :** PNJ de quête principale. Point de départ et point de retour de la quête 01.

**Apparence (style PS2) :**
Femme d'une soixantaine d'années. Cheveux gris attachés en chignon serré. Tablier de laine, mains calleuses, regard direct et fatigué. Modèle polygonal simplifié, animation d'idle : elle s'essuie les mains sur son tablier en boucle.

**Personnalité :**
Pragmatique, directe, ne cède pas à la panique mais la dissimule mal. Elle est la mémoire vivante du village — elle connaît les vieilles histoires mais n'y croit qu'à moitié. Jusqu'à maintenant.

**Histoire :**
Maren est veuve depuis que son mari, bûcheron, a disparu en forêt il y a trois mois. Elle n'a pas dit aux autres villageois ce qu'elle a réellement vu la nuit de sa disparition : une silhouette à l'orée des arbres, immobile, qui ressemblait à lui mais ne l'était plus.

**Rôle narratif étendu (Alpha+) :**
Elle deviendra un personnage pivot quand le joueur découvrira que son mari est devenu l'un des Corrompus — et qu'elle le sait depuis le début. Elle sera alors confrontée à un choix moral que le joueur devra influencer.

**Données LLM (Horizon 2030) :**
```json
{
  "npc_id": "maren_asheld",
  "personality_traits": ["pragmatique", "protectrice", "coupable", "mélancolique"],
  "secret": "Son mari est un Corrompu. Elle l'a vu mais n'a rien dit.",
  "knowledge": {
    "village": "haute",
    "forêt": "moyenne",
    "lore_aethon": "faible — superstitions uniquement",
    "corrompus": "moderate — expérience directe non avouée"
  },
  "memory_triggers": ["mention du mari", "retour de la forêt", "Nexolithe", "Varek"],
  "emotional_state": "anxiété contenue / soulagement si quête réussie"
}
```

---

### PNJ-02 : Aldric Sorel — Le Marchand au Chariot Brisé

**Rôle dans le prototype :** Marchand. Vend des consommables. Donne des informations sur le monde extérieur.

**Apparence (style PS2) :**
Homme d'une quarantaine d'années, corpulent, moustache en guidon. Bonnet de fourrure, manteau de voyage usé. Assis sur son chariot à roue cassée qu'il n'a toujours pas réparé. Animation d'idle : il taille un bout de bois en regardant le ciel.

**Personnalité :**
Bavard compulsif, optimiste de façade, peureux en réalité. Il fait semblant d'être bloqué par la roue cassée mais la vérité est qu'il n'ose pas reprendre la route à travers la forêt. Il compense sa peur par un flux ininterrompu d'anecdotes commerciales.

**Inventaire (Prototype) :**
- Bandage de toile (restaure 20 PV) — 5 pièces d'or
- Fiole d'eau de source (restaure 10 PM) — 8 pièces d'or
- Pain rassis (restaure 5 PV) — 2 pièces d'or

**Histoire :**
Aldric appartient à la Guilde des Marchands Libres. Il transporte en secret un colis scellé qu'il ne doit pas ouvrir — commande d'un "client anonyme" dans la cité de Port-Ardente. Il ne sait pas ce qu'il contient. (Le joueur non plus. Pour l'instant.)

**Rôle narratif étendu (Beta+) :**
Le colis contient un fragment de Nexolithe. Le client anonyme est un Murmureur. Aldric sera soit une victime soit un complice involontaire d'un événement déclencheur majeur.

**Données LLM (Horizon 2030) :**
```json
{
  "npc_id": "aldric_sorel",
  "personality_traits": ["bavard", "peureux", "opportuniste", "bon fond"],
  "secret": "Il transporte un colis scellé pour un client anonyme qu'il ne connaît pas.",
  "knowledge": {
    "routes_commerciales": "très haute",
    "politique_cités": "moyenne",
    "forêt_varek": "peur — refuse d'en parler longtemps",
    "guilde": "haute"
  },
  "memory_triggers": ["colis", "Port-Ardente", "roue du chariot", "Guilde"],
  "emotional_state": "nerveux / détendu si le joueur est amical"
}
```

---

### PNJ-03 : Torvyn l'Ancien — L'Ermite de la Lisière

**Rôle dans le prototype :** PNJ optionnel. Donne des informations de lore en échange d'un objet. Non essentiel à la quête principale.

**Apparence (style PS2) :**
Vieillard voûté, longue barbe blanche emmêlée, yeux d'un blanc laiteux (aveugle). Robe en lambeaux, pieds nus. Assis près d'un feu de camp à l'entrée de la forêt. Il s'oriente au son.

**Personnalité :**
Mystérieux sans être cliché — il ne parle pas par énigmes mais par associations d'idées, comme quelqu'un dont l'esprit est partiellement ailleurs. Il est en réalité un ancien Gardien du Filament, complètement oublié de l'ordre.

**Histoire :**
Il a perdu la vue en touchant une Nexolithe active il y a quarante ans. En compensation, il voit quelque chose d'autre — des filaments de lumière qui relient les choses entre elles. Il ne peut pas expliquer ce qu'il voit, mais il sait que la Forêt de Varek saigne depuis des mois.

**Rôle narratif étendu (Alpha+) :**
Torvyn sera le premier à nommer la Tache devant le joueur. Il deviendra un mentor de facto, puis disparaîtra mystérieusement — laissant un indice vers les ruines du Nexe de Sel.

---

### PNJ-04 (futur) : Le Corrompu-Mémoire *(Alpha)*

Un Corrompu qui n'attaque pas immédiatement. Il tente de parler. Ses mots sont fragmentés, ses phrases incomplètes. Il était un villageois. En l'écoutant assez longtemps, le joueur peut reconstituer ce qui s'est passé.
Mécaniquement : le premier PNJ-ennemi avec un système de dialogue. Sa mise à mort est un choix narratif.

---

## 6. Bestiaire — Les Corrompus

### Philosophie du Bestiaire
Chaque monstre est un animal (ou humain) ordinaire transformé par la Tache. Leur design conserve des traces reconnaissables de ce qu'ils étaient — ce qui les rend plus troublants que des créatures entièrement fantastiques.

---

### Monstre-01 : Le Rôdeur des Sous-Bois *(Loup Corrompu)*

**Nom de code :** `CORRUPTED_WOLF_01`
**Zone :** Forêt de Varek, zones extérieures (distance faible du village)
**Niveau prototype :** 1-3

**Apparence (style PS2) :**
Loup de taille normale, mais sa fourrure est maculée de taches noires qui semblent se déplacer lentement. Un œil blanc, l'autre noir. Animation d'idle : il se gratte frénétiquement une oreille, comme si quelque chose le dérangeait à l'intérieur.

**Comportement :**
- Aggro si le joueur s'approche à moins de 8 unités
- Attaque de base : morsure frontale (5-8 dégâts physiques)
- Capacité spéciale (rare) : *Hurlement Noir* — immobilise le joueur 1.5 secondes

**Lore :**
Ce loup a été le premier animal à sortir corrompu de la forêt, trois mois avant le début du jeu. Les villageois ont cru à une maladie ordinaire et l'ont tué — mal. D'autres sont apparus. La Tache ne corrompt pas seulement le corps : elle amplifie l'instinct de prédation et éteint tout le reste.

**Récompenses :**
- Griffe Noircie (matériau) — 60% de drop
- Fourrure Ternée (matériau) — 40% de drop
- 2-4 pièces d'or

---

### Monstre-02 : L'Effaré *(Humanoïde Corrompu, ancien villageois)*

**Nom de code :** `CORRUPTED_HUMAN_01`
**Zone :** Forêt de Varek, zones médianes (distance moyenne)
**Niveau prototype :** 3-5

**Apparence (style PS2) :**
Silhouette humaine en haillons. Posture anormale : tête légèrement trop inclinée, mouvements saccadés. Veines noires visibles sur les bras et le cou. Aucun visage reconnaissable — la Tache a déformé les traits. Animation d'idle : il se retourne dans une direction, puis l'autre, sans logique apparente.

**Comportement :**
- Attaque : coup de poing lourd (8-12 dégâts)
- Capacité : *Regard Vide* — réduit la régénération du joueur de 30% pendant 10 secondes
- Note narrative : si on l'examine (touche d'interaction), une phrase fragmentée s'affiche — un résidu de mémoire.

**Lore :**
Bûcherons, chasseurs, explorateurs imprudents. La transformation dure entre 48 et 72 heures. La conscience s'efface progressivement — il reste parfois un fragment d'identité, comme une trace sur du verre embrumé. Ce fragment n'a plus les moyens de contrôler le corps.

**Récompenses :**
- Tissu Corrompu — 55% de drop
- Éclat de Tache (matériau rare, usage futur) — 15% de drop
- 5-10 pièces d'or

---

### Monstre-03 : La Mère-Arbre *(Entité végétale corrompue)*

**Nom de code :** `CORRUPTED_TREE_ENTITY_01`
**Zone :** Forêt de Varek, zone profonde (mini-boss de zone)
**Niveau prototype :** 6-8

**Apparence (style PS2) :**
Un vieux chêne dont le tronc s'est partiellement animé. Des "bras" de branches l'entourent, certains se terminant par des griffes. Le cœur du tronc pulse d'une lumière noire. Animation d'idle : les branches ondulent lentement, comme sous l'eau.

**Comportement :**
- Semi-statique (se déplace très lentement sur une zone de 10 unités autour de son point d'ancrage)
- Attaque 1 : *Vrille de Racine* — une racine jaillit du sol sous le joueur (6-14 dégâts, renversement)
- Attaque 2 : *Spores Noires* — nuage de zone, 3 dégâts/seconde pendant 5 secondes
- Phase critique (< 30% PV) : *Écorce Frénétique* — vitesse d'attaque x1.5

**Lore :**
La Mère-Arbre n'est pas un monstre isolé. Elle est un nœud — un point où la Tache s'est concentrée suffisamment pour créer une présence quasi-intentionnelle. Elle ne cherche pas à survivre : elle cherche à répandre. Torvyn la connaît. Il dit qu'elle "se souvient de quelque chose qu'elle ne devrait pas savoir."

**Récompenses :**
- Cœur-Tache (objet de quête potentiel) — 100% (mini-boss)
- Résine Corrompue — 70% de drop
- 20-30 pièces d'or

---

## 7. Système de Quêtes

### 7.1 Quête Prototype (Pré-Alpha)

---

#### QUÊTE-01 : "Ce qui revient de la forêt"

**Type :** Quête principale
**Donneur :** Maren Asheld (village, fontaine centrale)
**Niveau recommandé :** 1
**Durée estimée :** 15-25 minutes

---

**Résumé narratif :**
Maren demande au joueur d'aller en forêt éliminer les créatures qui rôdent depuis trois mois. Elle dit que c'est pour protéger le village. Ce n'est pas toute la vérité : elle espère aussi retrouver un signe de son mari.

---

**Structure en 4 actes :**

**Acte 1 — L'Approche**
- Parler à Maren Asheld → déclenchement de la quête
- Objectif affiché : *"Renseignez-vous sur la forêt avant d'y entrer."*
- Optionnel : parler à Aldric (donne des consommables à prix réduit + rumeur sur la forêt)
- Optionnel : parler à Torvyn (donne un Fragment d'Avertissement + lore)
- Entrer dans la Forêt de Varek → transition de zone

**Acte 2 — La Forêt**
- Objectif affiché : *"Éliminez 3 Corrompus dans la Forêt de Varek."*
- Monstres valides : tout ennemi de la zone (Rôdeurs, Effarés)
- Compteur UI : [0/3 Corrompus éliminés]
- Découverte optionnelle : un effaré porte des restes d'une veste de bûcheron (item : "Veste Déchirée aux Initiales M.A.")

**Acte 3 — La Cicatrice**
- Après 3 éliminations, un marqueur de quête apparaît au centre de la forêt
- Le joueur trouve une clairière calcinée — sol noir, arbre central mort
- Interaction avec l'arbre : une Nexolithe est incrustée dans l'écorce. Elle pulse.
- Choix : [Toucher la Nexolithe] ou [Ignorer et partir]
  - Si touché : flash de vision (2 secondes) — silhouette d'un homme dans la forêt, voix fragmentée : *"...Maren... je ne... peux plus..."*
  - Message journal : *"Cette pierre vibre d'une énergie que vous ne reconnaissez pas. Vous avez vu quelque chose. Ou quelqu'un."*

**Acte 4 — Le Retour**
- Retour à Cendrecroix, parler à Maren
- Dialogue conditionnel selon les choix :
  - Si touché la Nexolithe → Maren pâlit. Elle reconnaît la description. Récompense augmentée + fragment de lore.
  - Si ignoré → Retour classique. Récompense standard.
- Récompense : XP + pièces d'or + item (voir ci-dessous)
- Déclenchement flag : `quest_01_complete = true` → Torvyn a un nouveau dialogue disponible

---

**Récompenses :**
| Condition | Récompense |
|---|---|
| Retour standard | 150 XP, 25 pièces d'or, Bandage Renforcé x3 |
| + Nexolithe touchée | +50 XP, +10 pièces d'or, "Fragment de Vision" (item lore) |
| + Veste trouvée et montrée à Maren | +Dialogue unique, +item : "Clé Rouillée" (ouvre une zone future) |

---

**Flags et états narratifs déclenchés :**
```
quest_01_complete          → true
maren_knows_husband_alive  → true (si Nexolithe touchée)
nexolithe_forêt_discovered → true
torvyn_new_dialogue        → true (si quest_01_complete)
```

---

### 7.2 Quêtes Secondaires (Alpha)

*(Conçues pour l'Alpha — non jouables en prototype)*

---

#### QUÊTE-S01 : "La Roue d'Aldric"
**Donneur :** Aldric Sorel
**Type :** Quête de service / Comic relief
**Résumé :** Aldric demande au joueur de récupérer des pièces métalliques en forêt pour réparer sa roue. La vraie raison : il veut partir mais a besoin d'une excuse pour ne pas avoir l'air lâche. En chemin, le joueur trouve que les pièces sont des fragments d'une armure ancienne — Aethon.
**Récompense :** Réduction permanente de 10% chez Aldric + "Fragment d'Armure Aethon" (objet de collection).

---

#### QUÊTE-S02 : "Le Feu de Torvyn"
**Donneur :** Torvyn l'Ancien
**Type :** Quête de lore
**Résumé :** Torvyn demande au joueur de ramener de la résine corrompue (drop de la Mère-Arbre). Il veut l'analyser. Si le joueur revient, Torvyn révèle que la résine "chante" — elle émet une fréquence identique à celle d'une Nexolithe. Ce n'est pas une coïncidence.
**Récompense :** "Parchemin de Torvyn" (objet lore, donne +5% résistance corruption), accès au lore des Gardiens du Filament.

---

#### QUÊTE-S03 : "L'Effaré qui Parlait"
**Donneur :** Aucun (découverte libre)
**Type :** Quête mystère / Choix moral
**Résumé :** En errant en forêt après la quête principale, le joueur tombe sur un Effaré qui ne l'attaque pas immédiatement. Il murmure des fragments : *"...la lumière noire... il m'a dit... j'avais faim..."*. Le joueur peut l'écouter jusqu'au bout (5 échanges) pour reconstituer son histoire, ou l'éliminer immédiatement.
**Récompense écoute :** "Mémoire Fragmentée n°01" (objet lore collectible), flag `murmureur_trace_01 = true`.
**Récompense élimination :** XP standard.
**Impact narratif :** Si écouté, une ligne de dialogue supplémentaire apparaît chez Maren — elle reconnaît certains détails.

---

### 7.3 Arc Narratif Principal (Vision 2030)

#### Vue d'ensemble en 4 Chapitres

```
CHAPITRE 1 — "Les Symptômes"          [Zones : Cendrecroix, Forêt de Varek]
  → Prototype + Alpha
  → Le joueur découvre la corruption locale. Il rencontre les premiers PNJ.
  → Climax : Destruction de la Mère-Arbre → la Tache recule... mais migre ailleurs.

CHAPITRE 2 — "Les Cicatrices"         [Zones : Ruines du Nexe de Sel, Marécages]
  → Alpha + Beta
  → Le joueur découvre les Nexolithes et leur rôle. Les Murmureurs apparaissent.
  → Climax : Le joueur découvre l'identité du "client anonyme" d'Aldric.
             Premier contact avec un Gardien du Filament actif.

CHAPITRE 3 — "Le Nom Oublié"          [Zones : Port-Ardente, Mines Profondes]
  → Beta
  → Le Conseil des Trois Cités est infiltré par les Murmureurs.
  → Varek le Délieur est invoqué partiellement — pas encore pleinement réveillé.
  → Le joueur doit choisir une faction : Gardiens du Filament OU chemin solitaire.
  → Climax : Destruction d'une cité — événement monde permanent.

CHAPITRE 4 — "Le Fil Défait"          [Zones : Plateau des Cendres, Citadelle]
  → Version 1.0
  → Varek est pleinement réveillé. La réalité se déforme dans certaines zones.
  → Le joueur doit tisser un nouveau Filament — mécaniquement : résoudre des
     puzzles narratifs basés sur les choix de toutes les quêtes précédentes.
  → Fin A (Lumière) : Le joueur sacrifice la Nexolithe centrale pour sceller
    à nouveau la Tache. Les Aethons reviennent brièvement.
  → Fin B (Ombre) : Le joueur utilise la Tache contre Varek — victoire, mais
    la corruption ne disparaît pas. Elle change juste de maître.
  → Fin C (Équilibre) : Découverte uniquement si toutes les quêtes secondaires
    ont été complétées. Le joueur comprend que la Tache ET le Filament sont
    deux moitiés du même tout. Il ne détruit rien — il tisse les deux ensemble.
```

---

## 8. Dialogues & Scènes

### Conventions d'écriture

- Ligne de dialogue max : 80 caractères (lisibilité style PS2, boîte de texte)
- Pas d'exposition info-dump : chaque PNJ révèle au maximum **une** information de lore par échange
- Tone général : grave mais humain, sans ironie moderne
- Les PNJ ne savent jamais tout — ils supposent, craignent, se trompent parfois

---

### Scène 01 — Première interaction avec Maren (quête non déclenchée)

```
[Le joueur s'approche de Maren près de la fontaine]

MAREN : "Tu n'es pas d'ici. Je le vois à ta façon de regarder les arbres."
        "Comme si tu ne savais pas encore qu'il vaut mieux ne pas les regarder."

[Choix du joueur]
  → "Qu'est-ce qui se passe dans cette forêt ?"
  → "Tu as besoin d'aide ?"
  → "Je ne fais que passer."

[Si → "Qu'est-ce qui se passe dans cette forêt ?"]
MAREN : "Des choses reviennent. Des choses qui sont parties d'ici."
        "Certaines avaient un nom, avant."
        [pause]
        "Si tu n'as pas peur, parle-moi. J'ai peut-être quelque chose pour toi."
        → [Déclenche l'option de quête principale]

[Si → "Tu as besoin d'aide ?"]
MAREN : "Tout le monde a besoin d'aide. Mais la plupart des gens s'enfuient"
        "quand ils comprennent de quelle sorte d'aide il s'agit."
        "Reviens si tu changes d'avis."

[Si → "Je ne fais que passer."]
MAREN : "Personne ne fait que passer à Cendrecroix."
        "La forêt n'est pas praticable. Tu le sais déjà, sinon tu serais reparti."
```

---

### Scène 02 — Déclenchement de la quête principale

```
[Maren explique la situation]

MAREN : "Ça fait trois mois que des bêtes sortent de la forêt la nuit."
        "Des loups. Des... autres choses. On ne sait plus ce qu'elles sont."
        "Mes hommes ont peur. Moi aussi, mais je ne peux pas me le permettre."
        [pause]
        "J'ai besoin que quelqu'un entre là-dedans et en tue quelques-uns."
        "Juste pour que les gens puissent dormir."

JOUEUR : "Combien ?"
MAREN : "Trois. C'est symbolique plus qu'utile. Mais ça ferait du bien au village."
        "Et peut-être... peut-être que tu verras quelque chose."
        "Si tu vois quelque chose que je devrais savoir — tu me le dis."
        [Elle détourne les yeux]
        "C'est tout."

[Journal mis à jour : QUÊTE-01 démarrée]
```

---

### Scène 03 — Interaction avec Aldric (première fois)

```
[Aldric est assis sur son chariot, taille un bout de bois]

ALDRIC : "Ah, un voyageur ! Bienvenue à Cendrecroix, le village qui se demande"
         "pourquoi il n'a pas encore été évacué."
         [petit rire nerveux]
         "Je m'appelle Aldric. Marchand. Normalement en transit."
         "Normalement."

JOUEUR : "Ton chariot est cassé ?"
ALDRIC : "La roue. Oui. Depuis... six jours. Je pourrais la réparer."
         [pause]
         "Je vais la réparer. Bientôt."
         "En attendant, j'ai des bandages, de l'eau de source, et du pain."
         "Rien d'utile contre ce qui est dans cette forêt, mais ça aide après."
         → [Ouvre l'interface de boutique]
```

---

### Scène 04 — Torvyn à l'entrée de la forêt

```
[Le joueur s'approche du vieillard assis près du feu]

TORVYN : [sans se retourner] "Je t'entends depuis la fontaine."
         "Pas tes pas. Tes hésitations."
         [pause]
         "Tu vas entrer dans la forêt. Tout le monde hésite de la même façon."

JOUEUR : "Tu peux voir ça ?"
TORVYN : "Je ne vois plus rien. Justement."
         "Mais je sens les fils. Et les tiens tirent vers les arbres sombres."
         [Il se retourne. Ses yeux sont blancs.]
         "Deux conseils. Gratuits."
         "Premier : si quelque chose te parle dans la forêt — écoute-le."
         "Deuxième : si quelque chose brille au sol — ne le touche pas."
         [pause]
         "Sauf si tu es prêt à voir ce que tu ne pourras pas oublier."
```

---

### Scène 05 — Retour chez Maren (Nexolithe touchée)

```
[Le joueur revient, a touché la Nexolithe]

JOUEUR : "C'est fait. Mais j'ai trouvé quelque chose dans la forêt."
         "Une pierre. Dans un arbre mort. Elle m'a montré... une silhouette."

[Maren se fige. Un long silence.]

MAREN : "Une silhouette."
JOUEUR : "Un homme. Il disait un nom. Maren."
         [silence]
MAREN : [voix très basse] "Il était... comment ?"
JOUEUR : "Il ne contrôlait plus son corps. Mais il essayait de parler."
         [Maren se retourne. Elle ne pleure pas. C'est pire.]
MAREN : "Je le savais. Je savais que c'était lui."
         "Je ne voulais pas le savoir."
         [pause]
         "Merci. Et... pardonne-moi. J'aurais dû te dire pourquoi je t'envoyais là."
         [Elle sort une bourse plus lourde]
         "Prends ça. Et si tu retournes en forêt un jour..."
         "Si tu le trouves... dis-lui que je ne suis pas en colère."
```

---

## 9. Événements Dynamiques

*(Système prévu pour l'Alpha — conçu maintenant pour cohérence narrative)*

### Événement-01 : "Invasion Nocturne"

**Déclencheur :** Tous les soirs en jeu (cycle jour/nuit, environ toutes les 30 min réelles)
**Description :** 2-4 Rôdeurs sortent de la forêt et attaquent les abords du village. Les villageois se barricadent. Les joueurs présents peuvent défendre le village.
**Récompense :** XP de défense + "Gratitude de Cendrecroix" (buff temporaire : +5% or dans les échanges avec les villageois)
**Lore intégré :** Si l'invasion réussit (trop peu de joueurs présents), Maren a un dialogue spécial le lendemain : *"Ils ont encore frappé la nuit dernière. On répare ce qu'on peut."*

---

### Événement-02 : "Le Chuchoteur" *(rare)*

**Déclencheur :** 1 chance sur 20 lorsqu'un joueur entre seul dans la forêt
**Description :** Un Effaré isolé ne s'approche pas mais suit le joueur à distance. Si le joueur s'arrête et l'observe, il murmure des mots. Si le joueur l'approche, il fuit.
**Mécanique :** En suivant le Chuchoteur, le joueur est guidé vers la clairière de la Nexolithe (même hors quête).
**Lore intégré :** Renforce l'idée que certains Corrompus conservent un fragment de conscience.

---

### Événement-03 : "Brume du Délieur" *(Alpha)*

**Déclencheur :** Événement mondial, toutes les 2 heures réelles
**Description :** Une brume noire recouvre la Forêt de Varek pendant 10 minutes. Dans cette fenêtre, tous les ennemis sont de niveau +2, dropent 2x plus, et une version élite de la Mère-Arbre apparaît.
**Lore intégré :** La brume est appelée "le Souffle de Varek" dans les textes de Torvyn. C'est la manifestation physique de la Tache qui pulse.

---

## 10. Cinématiques (Cutscenes)

*(Style PS2 : caméra fixe, modèles in-engine, pas de voix off — texte uniquement)*

---

### Cinématique 00 — Intro du jeu (30 secondes)

```
CADRE 1 : Vue aérienne d'une forêt sombre. Nuit. Silence.
TEXTE : "Il y a deux cents ans, quelque chose s'est réveillé."

CADRE 2 : Zoom lent sur une clairière. Une lumière noire pulse au sol.
TEXTE : "Les grandes cités ont choisi de ne pas voir."

CADRE 3 : Vue d'un village endormi — Cendrecroix. Une fenêtre s'allume.
TEXTE : "Les petits villages n'ont pas ce luxe."

CADRE 4 : Fondu au noir. Le personnage du joueur apparaît à l'entrée du village.
TEXTE : "Toi non plus."
→ [Contrôle rendu au joueur]
```

---

### Cinématique 01 — Découverte de la Nexolithe (in-zone)

*(Se joue automatiquement quand le joueur s'approche à moins de 3 unités de la Nexolithe dans la clairière)*

```
CADRE 1 : Gros plan sur la Nexolithe dans l'arbre mort. Elle pulse lentement.
TEXTE : Aucun — ambiance sonore : battement sourd, régulier.

CADRE 2 : [Si le joueur choisit de toucher]
          La main du personnage s'approche. Contact.

CADRE 3 : Flash blanc. Puis noir. Puis une image fragmentée :
          Une silhouette d'homme dans la forêt, dos au joueur.
          Il est immobile. Ses épaules tremblent.
VOIX (texte fragmenté) : "...tu ne... dois pas... rester ici..."
                          "...Maren... dis-lui que..."
                          [Statique. Fondu au noir.]

CADRE 4 : Retour en jeu. Le personnage titube légèrement.
JOURNAL : "Vous avez touché quelque chose d'ancien. Et quelqu'un a essayé de parler."
```

---

### Cinématique 02 — Élimination de la Mère-Arbre *(fin de zone, Alpha)*

```
CADRE 1 : La Mère-Arbre s'effondre lentement. Les branches se figent.
          Le cœur noir s'éteint.

CADRE 2 : La forêt autour change très légèrement — quelques feuilles
          reprennent une couleur verte. Microscopique. À peine visible.

CADRE 3 : Au loin — hors champ — un bruit sourd. Comme si quelque chose
          de lourd venait de tomber, très loin.

TEXTE : "La corruption ne disparaît pas. Elle se déplace."
→ [Flag : nexe_corruption_migre = true]
```

---

## 11. Intégration LLM / Mémoire PNJ (Horizon 2030)

### Architecture narrative pour agents IA

Chaque PNJ est conçu avec deux couches :
1. **Couche statique** (prototype) — dialogues scriptés, arbre de choix
2. **Couche dynamique** (Horizon 2030) — agent LLM avec contexte narratif injecté

---

### Schéma de prompt système (PNJ-LLM)

```
SYSTEM PROMPT TEMPLATE — NPC AGENT v1

Tu es [NOM_PNJ], habitant(e) de [ZONE] dans le monde d'Aethon Chronicles.

PERSONNALITÉ : [traits]
SITUATION ACTUELLE : [état émotionnel]
SECRETS (ne jamais révéler directement) : [liste]
CE QUE TU SAIS : [knowledge_map]
CE QUE TU NE SAIS PAS : [ignorance_map]

RÈGLES DE DIALOGUE :
- Tu ne parles jamais de mécaniques de jeu (PV, XP, niveaux)
- Tu ne révèles jamais plus d'une information de lore par échange
- Si le joueur insiste sur un secret, tu montres du malaise — tu ne confirmes pas
- Tes réponses font 1 à 3 phrases maximum
- Tu te souviens des échanges précédents avec CE joueur (via mémoire vectorielle)

MÉMOIRE CONTEXTUELLE : [injected from Qdrant — last 5 player interactions]
```

---

### Exemples de mémoire vectorielle PNJ

**Scénario :** Le joueur a complété la quête 01, montré la Veste Déchirée à Maren, et revient lui parler 2 heures plus tard.

**Mémoire injectée :**
```
- Il y a 2h : joueur a montré la Veste aux Initiales M.A.
- Maren a eu une réaction émotionnelle forte (flag: maren_mari_confirmed)
- Le joueur n'a pas posé de question sur la Clé Rouillée
- Dernière émotion de Maren : tristesse + gratitude
```

**Réponse LLM générée (exemple) :**
> "Tu es revenu. Je me demandais si tu reviendrais."
> "J'ai pensé à ce que tu m'as dit. Toute la nuit."
> "Il y a une vieille cave sous la forge abandonnée. Mon mari y allait parfois."
> "Je ne sais pas si tu devrais y aller. Mais je ne peux pas y aller moi-même."

*Le PNJ a fait avancer l'histoire de manière organique, basé sur la mémoire de l'interaction précédente — sans script préécrit.*

---

## 12. Glossaire

| Terme | Définition |
|---|---|
| **Aethons** | Êtres de lumière de l'Ère I, créateurs du monde via le Filament |
| **Filament** | Matière primordiale dont le monde est tissé — invisible aux mortels ordinaires |
| **La Tache** | Corruption issue du Néant, libérée par Varek le Délieur |
| **Nexolithe** | Pierre vivante gravée par les Aethons — stocke de l'information, émet de l'énergie |
| **Varek le Délieur** | Aethon renégat ayant ouvert le Néant — partiellement conscient à l'Ère III |
| **Les Corrompus** | Êtres vivants (animaux ou humains) transformés par la Tache |
| **Gardiens du Filament** | Ordre secret maintenant la connaissance Aethon — affaibli, presque disparu |
| **Murmureurs** | Cultistes vénérant Varek — cherchent son réveil complet |
| **Cendrecroix** | Village de départ — fondé sur les ruines d'un avant-poste Aethon |
| **Forêt de Varek** | Zone de corruption principale — porte le nom de l'Aethon renégat |

---

*— Fin du document LORE.md v1.0 —*
*Dernière mise à jour : Pré-Alpha*
*Prochaine révision prévue : Alpha (ajout Chapitre 2, Quêtes S01-S03, Zone Ruines du Nexe)*
