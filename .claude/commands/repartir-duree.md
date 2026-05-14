# /repartir-duree

## Objectif
Vérifier et redistribuer le volume horaire sur les sections d'un chapitre.
Lecture seule jusqu'à validation explicite de l'utilisateur.

## Syntaxe
```
/repartir-duree ch01_arithmetique
/repartir-duree ch11_fonctions
```

## Procédure

### Étape 1 — Lire le volume horaire officiel
- Lire `chapitres/chXX/CLAUDE.md` local
- Extraire la ligne `Masse horaire : Xh` → convertir en minutes
- Si absent → demander à l'utilisateur avant de continuer

### Étape 2 — Inventaire des \duree{} dans source.tex
- Lire `chapitres/chXX/source.tex`
- Pour chaque bloc `%% SECTION`, relever :
  - Le titre de la section
  - Tous les `\duree{X min}` trouvés dans cette section
  - Le type de chaque environnement (Activite, Application, Exercice, Exemple)
  - Le sous-total de la section

### Étape 3 — Afficher le tableau comparatif
Afficher OBLIGATOIREMENT ce tableau avant toute modification :

```
═══════════════════════════════════════════════════════════════
  RÉPARTITION DU VOLUME HORAIRE — ch01_arithmetique
  Volume officiel : 4h (240 min)
═══════════════════════════════════════════════════════════════

Section 1 — [Titre]
  • Activité 1          :  5 min
  • Application 1       : 10 min
  • Exercice 1          : 15 min
  Sous-total            : 30 min  ← 12,5% du total

Section 2 — [Titre]
  • Activité 2          :  5 min
  • Application 2       : 15 min
  Sous-total            : 20 min  ←  8,3% du total

...

───────────────────────────────────────────────────────────────
TOTAL CALCULÉ           : XX min
VOLUME OFFICIEL         : XX min
ÉCART                   : +/- XX min
═══════════════════════════════════════════════════════════════
```

### Étape 4 — Diagnostic
- **Écart ≤ 5 min** → afficher "✅ Volume horaire respecté." — ne rien modifier
- **Écart > 5 min** → proposer une redistribution (voir Étape 5)
- **\duree{} manquant** sur un environnement → signaler la liste

### Étape 5 — Proposition de redistribution (si écart > 5 min)
Afficher une proposition équilibrée :

```
PROPOSITION DE REDISTRIBUTION
───────────────────────────────────────────────────────────────
Section 1 — [Titre]        : XX min → XX min
  Activité 1               :  5 min →  5 min  (inchangé)
  Application 1            : 10 min → 12 min  (+2 min)
  Exercice 1               : 15 min → 18 min  (+3 min)

Section 2 — [Titre]        : XX min → XX min
  ...

NOUVEAU TOTAL              : XX min (= volume officiel)
───────────────────────────────────────────────────────────────
Appliquer cette redistribution ? (répondre "OK" pour confirmer)
```

### Étape 6 — Attendre validation
- NE RIEN MODIFIER sans réponse explicite "OK" de l'utilisateur
- Si l'utilisateur propose ses propres valeurs → les utiliser à la place

### Étape 7 — Appliquer les modifications (après "OK" uniquement)
- Modifier uniquement les `\duree{X min}` dans `source.tex`
- Ne jamais toucher au contenu mathématique ni aux environnements
- Afficher un résumé des lignes modifiées
- git push avec le message : `[chXX] : redistribution volume horaire`

---

## Règles de répartition

| Type d'environnement | Durée recommandée |
|---------------------|-------------------|
| Activite            | 5 – 10 min max    |
| Exemple             | 5 – 10 min        |
| Application         | 10 – 20 min       |
| Exercice de synthèse| 15 – 30 min       |

- Prioriser le temps sur les Applications et Exercices
- Les Activités ne doivent pas dépasser 10 min chacune
- Respecter la progression : sections de fin de chapitre plus longues

---

## Règles absolues
- Ne jamais dépasser le volume horaire officiel du CLAUDE.md local
- Afficher TOUJOURS le tableau (Étape 3) avant toute action
- Ne jamais modifier `fiche_prof.tex`, `td.tex`, `td_correction.tex`
- Ne jamais modifier le contenu mathématique de source.tex
- Commande lecture seule par défaut — modification uniquement après "OK"
- git push uniquement après modification validée
