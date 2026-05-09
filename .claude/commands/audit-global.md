---
name: audit-global
description: Rapport d'état complet de tous les chapitres TCS
---

# /audit-global — Rapport global des 15 chapitres

## Objectif
Lecture seule — ne rien modifier.
Produire un rapport complet de l'état du projet TCS.

---

## Étape 1 — Lire STATUS.md
Lire le fichier STATUS.md à la racine.
Extraire le tableau de bord actuel.

---

## Étape 2 — Vérifier chaque chapitre existant

Pour chaque dossier présent dans `chapitres/` :

### 2a — Vérifier les fichiers présents
```
source.tex        → existe ? (✅ / ❌)
CLAUDE.md         → existe ? (✅ / ❌)
fiche_prof.tex    → existe et non vide ? (✅ / ❌)
td.tex            → existe et non vide ? (✅ / ❌)
td_correction.tex → existe et non vide ? (✅ / ❌)
Page1.tex         → existe ? (✅ / ❌)
```

### 2b — Scanner source.tex (si existant)
Compter les blocs présents sans solutions :
- Nombre de `%% ACTIVITE` sans `%% SOLUTION_ACTIVITE` correspondant
- Nombre de `%% APPLICATION` sans `%% SOLUTION_APPLICATION` correspondant
- Nombre de `%% EXERCICE` sans `%% SOLUTION_EXERCICE` correspondant

### 2c — Vérifier CLAUDE.md local (si existant)
- Le statut dans CLAUDE.md local est-il cohérent avec les fichiers réels ?
- Le skill indiqué est-il correct pour ce numéro de chapitre ?

---

## Étape 3 — Produire le rapport

Afficher dans cet ordre :

### Vue d'ensemble
```
AUDIT GLOBAL — Pack Pédagogique TCS
Date : [date du jour]
─────────────────────────────────────
Chapitres complets    : X / 15
Chapitres en cours    : X / 15
Chapitres non démarrés: X / 15
```

### Détail par chapitre
Pour chaque chapitre détecté :
```
[chXX — Titre]
  Fichiers   : source ✅  fiche ❌  td ❌  td_corr ❌
  CLAUDE.md  : ✅ (skill: domaine-algebre)
  Manquant   : 3 corrections (App.2, App.3, Exercice 1)
  Action     : /generer chXX  ou  rédiger corrections manquantes
```

### Chapitres non démarrés (liste simple)
```
❌ ch02, ch03, ch04, ch05, ch06, ch07, ch08, ch09, ch10, ch12, ch13, ch14, ch15
   → Utiliser /nouveau-chapitre pour créer la structure
```

### Alertes critiques
Signaler en priorité :
- CLAUDE.md local manquant dans un chapitre existant
- Skill incorrect pour le numéro de chapitre
- `\textwidth` détecté dans source.tex (chercher `\textwidth`)
- Environnement `\begin{Exemple}[Correction` utilisé à la place de `\begin{Solution}`

---

## Étape 4 — Proposer les prochaines actions

Suggérer dans l'ordre de priorité :
1. Chapitres avec source.tex complet mais fichiers non générés → `/generer chXX`
2. Chapitres avec corrections manquantes → "Génère la correction de l'Application X"
3. Chapitres sans CLAUDE.md local → créer le fichier
4. Chapitres non démarrés → `/nouveau-chapitre`

---

## Important
Ne jamais modifier de fichier pendant l'audit.
Afficher uniquement — attendre les instructions de l'utilisateur.
