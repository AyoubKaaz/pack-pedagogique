# Pack Pédagogique TCS — Kaazouzi Ayyoub
## Règles universelles — s'appliquent à TOUS les chapitres

## Git — automatique après chaque modification
```bash
git add .
git commit -m "[chXX] : description courte"
git push origin main
```

## Limites absolues — ne jamais enfreindre
- Ne jamais modifier `preamble/*.tex`
- Ne jamais modifier `fiche_prof.tex`, `td.tex`, `td_correction.tex` directement
- Ne jamais créer de nouveaux environnements tcolorbox
- Ne jamais utiliser `\textwidth` dans les minipage de `source.tex`
- Ne jamais supprimer du contenu validé
- `\linewidth` obligatoire dans toutes les minipage
- Ne jamais déplacer `chapitres/Images/` — ressource globale partagée par tous les chapitres

## Règles délimiteurs mathématiques (police 10pt)
| Contexte | ✅ Correct | ❌ Interdit |
|---|---|---|
| Accolades d'ensembles `S = {...}` | `\big\{ \big\}` | `\{ \}` nu · `\left\{ \right\}` |
| Intervalles **sans** fraction | `\big[ \big]` · `\big] \big[` | `[ ]` nu |
| Intervalles **avec** fraction | `\left[ \right]` · `\left] \right[` | `\big[ \big]` |
> Raison : à 10pt, `\{ \}` et `[ ]` nus sont illisibles. `\left\{ \right\}` reste petit — inefficace.

## Système de balises source.tex
| Balise | fiche_prof | td | td_correction |
|--------|-----------|-----|--------------|
| SECTION / DEFINITION / PROPRIETE / TECHNIQUES / EXEMPLE / REMARQUE | ✓ | — | — |
| ACTIVITE / APPLICATION / EXERCICE | ✓ | ✓ | — |
| SOLUTION_ACTIVITE / SOLUTION_APPLICATION / SOLUTION_EXERCICE | — | — | ✓ |

## Environnement Solution — syntaxe obligatoire
```latex
\begin{Solution}[ACTIVITÉ][1]
\begin{Solution}[APPLICATION][2]
\begin{Solution}[EXERCICE DE SYNTHÈSE][1]
```

## Macros disponibles
`\N \Z \R \C` · `\vect{AB}` · `\abs{x}` · `\frac{}{}` (= dfrac) · `\duree{X min}` · `\dd` · `\e`
Ne jamais écrire `\dfrac` — `\frac` est redéfini automatiquement.

## Règle de session
1 session Claude Code = 1 seul chapitre. Lire le CLAUDE.md local avant toute action.
Le skill à charger est indiqué dans le CLAUDE.md local.

## Skills disponibles
- `correction-commune`            — base commune à tous les chapitres
- `domaine-algebre`               — ch01, ch05, ch07, ch08
- `domaine-arithmetique`          — ch02
- `domaine-geometrie-vectorielle` — ch03, ch04, ch13
- `domaine-geometrie-analytique`  — ch06
- `domaine-trigonometrie`         — ch09, ch11
- `domaine-statistiques`          — ch10
- `domaine-analyse`               — ch12
- `domaine-geometrie-plane`       — ch04, ch13, ch14
- `domaine-geometrie-espace`      — ch15
- `karpathy-guidelines`           — chargé automatiquement avec tout skill domaine

## Fichiers transversaux — lire au démarrage de chaque session
- log.md          → journal de bord, ajouter une entrée EN FIN de session
- index-concepts.md → index des notions, mise à jour automatique via /generer
- patterns/       → formulations validées, consulter avant toute correction

## Règle log.md
Fin de session obligatoire : ajouter dans log.md
  ## [DATE] chXX_nom — Session N
  - Fait : ...
  - Décision : ...
  - Restant : ...

## Règle patterns/
Avant de générer une correction :
  vérifier si patterns/ contient un fichier correspondant.
  Si oui → appliquer sa structure exacte.
  Si non → générer normalement puis proposer de verser le pattern.
