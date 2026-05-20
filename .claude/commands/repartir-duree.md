# /repartir-duree

## Objectif
Vérifier et redistribuer le volume horaire sur les sections d'un chapitre.
Lecture seule jusqu'à validation explicite de l'utilisateur.

## Syntaxe
```
/repartir-duree ch01_arithmetique
/repartir-duree ch11_fonctions
```

---

## Règle fondamentale — Deux catégories de durées

### Catégorie A — Durées AFFICHÉES dans le PDF (multiples de 5 uniquement)

| Environnement  | \duree{} affiché ? | Contrainte          |
|----------------|--------------------|---------------------|
| \section{}     | ✅ OUI             | multiple de 5 min   |
| Activite       | ✅ OUI             | multiple de 5 min   |
| Exemple        | ✅ OUI             | multiple de 5 min   |
| Application    | ✅ OUI             | multiple de 5 min   |
| Exercice       | ✅ OUI             | multiple de 5 min   |

### Catégorie B — Durées NON AFFICHÉES (commentaire uniquement, entiers naturels libres)

| Environnement  | \duree{} affiché ? | Contrainte                        |
|----------------|--------------------|-----------------------------------|
| Definition     | ❌ NON             | entier naturel libre (1, 2, 3...) |
| Propriete      | ❌ NON             | entier naturel libre (1, 2, 3...) |
| Theoreme       | ❌ NON             | entier naturel libre (1, 2, 3...) |
| Remarque       | ❌ NON             | entier naturel libre (1, 2, 3...) |
| Techniques     | ❌ NON             | entier naturel libre (1, 2, 3...) |
| Preuve         | ❌ NON             | entier naturel libre (1, 2, 3...) |

> **Exemples valides catégorie B :**
> - Une Remarque courte (1 phrase) → `% durée estimée : 2 min` ✅
> - Un Théorème avec démonstration → `% durée estimée : 7 min` ✅
> - Une Définition simple → `% durée estimée : 3 min` ✅

---

## Calcul du volume d'une section

```
Durée section (affichée, multiple de 5) =
    Activité(s)    [multiple de 5]
  + Exemple(s)     [multiple de 5]
  + Application(s) [multiple de 5]
  + Exercice(s)    [multiple de 5]
  + Définition(s)  [entier libre, commentaire]
  + Propriété(s)   [entier libre, commentaire]
  + Théorème(s)    [entier libre, commentaire]
  + Remarque(s)    [entier libre, commentaire]
  + Techniques     [entier libre, commentaire]
```

Exemple correct :
```
Section 1 — \duree{1h} = 60 min
  ✅ Activité 1     : 10 min  [multiple de 5 — affiché]
  💬 Définition     :  5 min  [entier libre  — commentaire]
  💬 Propriété      :  5 min  [entier libre  — commentaire]
  💬 Remarque       :  3 min  [entier libre  — commentaire]
  💬 Théorème       :  5 min  [entier libre  — commentaire]
  ✅ Exemple 1      :  5 min  [multiple de 5 — affiché]
  ✅ Application 1  : 15 min  [multiple de 5 — affiché]
  ✅ Exercice       : 20 min  [multiple de 5 — affiché]
  ──────────────────────────
  TOTAL             : 68 min → arrondir \duree{} à 70 min ← (multiple de 5)
```

> ⚠️ Si la somme exacte n'est pas un multiple de 5 → arrondir la \duree{} de la section
> au multiple de 5 le plus proche (jamais en dessous du total réel).

---

## Procédure

### Étape 1 — Lire le volume horaire officiel
- Lire `chapitres/chXX/CLAUDE.md` local
- Extraire `Masse horaire : Xh` → convertir en minutes
- Si absent → demander à l'utilisateur

### Étape 2 — Inventaire dans source.tex
Pour chaque bloc `%% SECTION` :
- Relever le `\duree{}` de la section (durée globale affichée)
- Catégorie A : Activite, Exemple, Application, Exercice → lire leur `\duree{}`
- Catégorie B : Definition, Propriete, Theoreme, Remarque, Techniques → lire `% durée estimée : X min`
- Si commentaire absent → estimer selon le contenu (entier naturel raisonnable) et l'ajouter

### Étape 3 — Afficher le tableau complet
Afficher OBLIGATOIREMENT avant toute modification :

```
═══════════════════════════════════════════════════════════════════
  RÉPARTITION DU VOLUME HORAIRE — ch01_arithmetique
  Volume officiel : 5h (300 min)
═══════════════════════════════════════════════════════════════════

Section 1 — \duree{1h} = 60 min
  ✅ Activité 1          : 10 min   [multiple de 5 — affiché]
  💬 Définition          :  5 min   [commentaire]
  💬 Propriété           :  5 min   [commentaire]
  💬 Remarque            :  3 min   [commentaire]
  💬 Théorème            :  5 min   [commentaire]
  ✅ Exemple 1           :  5 min   [multiple de 5 — affiché]
  ✅ Application 1       : 15 min   [multiple de 5 — affiché]
  ✅ Exercice synthèse 1 : 20 min   [multiple de 5 — affiché]
  ─────────────────────────────────────────────────────────
  Calculé : 68 min | \duree{} section : 60 min ⚠️ écart -8 min

Section 2 — \duree{45 min}
  ...

───────────────────────────────────────────────────────────────────
TOTAL \duree{} sections  : XXX min
VOLUME OFFICIEL          : XXX min
ÉCART                    : +/- XX min
═══════════════════════════════════════════════════════════════════
```

### Étape 4 — Diagnostic (deux niveaux)

**Niveau section :** la \duree{} de la section correspond-elle à la somme de ses environnements ?
- ✅ Cohérent (écart ≤ 2 min) → OK
- ⚠️ Incohérent → signaler, proposer correction

**Niveau chapitre :** la somme des \duree{} sections correspond-elle au volume officiel ?
- ✅ Cohérent (écart ≤ 5 min) → "Volume horaire respecté."
- ⚠️ Écart > 5 min → proposer redistribution (Étape 5)

Signaler aussi :
- Durée catégorie A non multiple de 5 → à corriger
- Commentaire `% durée estimée` absent → à ajouter

### Étape 5 — Proposition de redistribution (si nécessaire)

```
PROPOSITION DE REDISTRIBUTION
───────────────────────────────────────────────────────────────────
Section 1 — \duree{1h} → \duree{1h10}  (correction cohérence interne)
  Activité 1          : 10 min  (inchangé)   ✅ multiple de 5
  Définition          :  5 min  (commentaire, inchangé)
  Propriété           :  5 min  (commentaire, inchangé)
  Remarque            :  3 min  (commentaire, inchangé)
  Théorème            :  5 min  (commentaire, inchangé)
  Exemple 1           :  5 min  (inchangé)   ✅ multiple de 5
  Application 1       : 15 min  (inchangé)   ✅ multiple de 5
  Exercice synthèse 1 : 20 min  (inchangé)   ✅ multiple de 5
  Calculé : 68 min → \duree{1h10} = 70 min ✅

NOUVEAU TOTAL sections : XXX min (≈ volume officiel)
───────────────────────────────────────────────────────────────────
Appliquer ? (répondre "OK" pour confirmer)
```

### Étape 6 — Attendre validation
- NE RIEN MODIFIER sans "OK" explicite de l'utilisateur
- Si l'utilisateur propose ses propres valeurs → les utiliser

### Étape 7 — Appliquer (après "OK" uniquement)
1. Mettre à jour `\duree{}` catégorie A (section, Activite, Exemple, Application, Exercice)
2. Mettre à jour ou ajouter `% durée estimée : X min` catégorie B
3. Format commentaire : ligne juste avant `\begin{Definition}` etc.
4. Afficher résumé des lignes modifiées
5. git push : `[chXX] : redistribution volume horaire`

---

## Format dans source.tex après application

```latex
%% SECTION
\section{Divisibilité \duree{1h15min}}          % ← multiple de 5 ✅

%% ACTIVITE
\begin{Activite}[][10 min]                  % ← multiple de 5 ✅
...
\end{Activite}

%% DEFINITION
% durée estimée : 5 min                     % ← entier libre ✅ (pas de \duree{})
\begin{Definition}[Divisibilité]
...
\end{Definition}

%% PROPRIETE
% durée estimée : 5 min                     % ← entier libre ✅
\begin{Propriete}[...]
...
\end{Propriete}

%% REMARQUE
% durée estimée : 3 min                     % ← entier libre ✅ (remarque courte)
\begin{Remarque}
...
\end{Remarque}

%% EXEMPLE
\begin{Exemple}[][5 min]                    % ← multiple de 5 ✅
...
\end{Exemple}

%% APPLICATION
\begin{Application}[][15 min]               % ← multiple de 5 ✅
...
\end{Application}

%% EXERCICE
\begin{Exercice}[][20 min]                  % ← multiple de 5 ✅
...
\end{Exercice}
```

---

## Durées par défaut si absentes

| Environnement | Défaut         | Contrainte        |
|---------------|----------------|-------------------|
| Activite      | 10 min         | multiple de 5     |
| Exemple       | 5 min          | multiple de 5     |
| Application   | 15 min         | multiple de 5     |
| Exercice      | 20 min         | multiple de 5     |
| Definition    | 3 min          | entier libre      |
| Propriete     | 3 min          | entier libre      |
| Theoreme      | 5 min          | entier libre      |
| Remarque      | 2 min          | entier libre      |
| Techniques    | 4 min          | entier libre      |
| Preuve        | 3 min          | entier libre      |

---

## Règles absolues
- Catégorie A (\duree{} affiché) : **multiples de 5 min uniquement**
- Catégorie B (commentaire) : **entiers naturels libres** (1, 2, 3, 4, 7...)
- Durée section = somme exacte (arrondie au multiple de 5 supérieur si besoin)
- Ne jamais utiliser `\duree{}` dans Definition, Propriete, Theoreme, Remarque, Techniques
- Ne jamais modifier `fiche_prof.tex`, `td.tex`, `td_correction.tex`
- Ne jamais modifier le contenu mathématique de `source.tex`
- Lecture seule par défaut — modification uniquement après "OK"
- git push uniquement après modification validée
