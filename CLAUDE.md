# Pack Pédagogique TCS — Kaazouzi Ayyoub
## Règles universelles — s'appliquent à TOUS les chapitres
---

## Git — automatique après chaque modification
```bash
git add .
git commit -m "[chXX] : description courte"
git push origin main
```

---

## Limites absolues — ne jamais enfreindre
- Ne jamais modifier `preamble/*.tex`
- Ne jamais modifier `fiche_prof.tex`, `td.tex`, `td_correction.tex` directement
- Ne jamais créer de nouveaux environnements tcolorbox
- Ne jamais utiliser `\textwidth` dans les minipage de `source.tex`
- Ne jamais supprimer du contenu validé
- `\linewidth` obligatoire dans toutes les minipage

---

## Système de balises source.tex
```
%% SECTION              → fiche_prof ✓
%% ACTIVITE             → fiche_prof ✓  td ✓
%% SOLUTION_ACTIVITE    → td_correction ✓
%% DEFINITION           → fiche_prof ✓
%% PROPRIETE            → fiche_prof ✓
%% TECHNIQUES           → fiche_prof ✓
%% EXEMPLE              → fiche_prof ✓
%% REMARQUE             → fiche_prof ✓
%% APPLICATION          → fiche_prof ✓  td ✓
%% SOLUTION_APPLICATION → td_correction ✓
%% EXERCICE             → fiche_prof ✓  td ✓
%% SOLUTION_EXERCICE    → td_correction ✓
```

---

## Environnement Solution — syntaxe obligatoire
```latex
\begin{Solution}[ACTIVITÉ][1]
\begin{Solution}[APPLICATION][2]
\begin{Solution}[EXERCICE DE SYNTHÈSE][1]
```

---

## Macros disponibles
`\N \Z \R \C` · `\vect{AB}` · `\abs{x}` · `\frac{}{}` (= dfrac) · `\duree{X min}` · `\dd` · `\e`
Ne jamais écrire `\dfrac` — `\frac` est redéfini automatiquement.

---

## Vocabulaire officiel marocain
| ✅ Correct | ❌ Interdit |
|-----------|------------|
| ensemble de définition | domaine de définition |
| ensemble solution | solution générale |
| sens de l'inégalité | signe de l'inégalité |
| taux de variation | taux d'accroissement |
| membre gauche / droit | côté gauche / droit |

---

## Règle de session
1 session Claude Code = 1 seul chapitre.
Lire le CLAUDE.md local du chapitre avant toute action.
Le skill à charger est indiqué dans le CLAUDE.md local.

---

## Skills disponibles
- `correction-commune` — base commune à tous les chapitres
- `domaine-algebre` — ch01 à ch05
- `domaine-geometrie` — ch06 à ch10
- `domaine-analyse` — ch11 à ch15
