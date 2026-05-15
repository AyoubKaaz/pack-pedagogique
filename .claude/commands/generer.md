---
name: generer
description: Générer les 3 documents (fiche_prof, td, td_correction) depuis source.tex
---

# /generer — Génération des 3 documents

Ignorer tout ce qui se trouve entre
%% HEADER_APERCU et %% FIN_HEADER_APERCU
et entre %% FOOTER_APERCU et %% FIN_FOOTER_APERCU

## Étape 0 — Identifier le chapitre
Si le chapitre n'est pas précisé dans la commande, demande :
"Quel chapitre veux-tu générer ? (ex: ch11_fonctions)"

## Étape 0.5 — Extraire le titre depuis CLAUDE.md local
Lire `chapitres/$CHAPITRE/CLAUDE.md` et extraire la première ligne `# Chapitre XX — Titre`.
- `$CH_NUM` = le numéro à deux chiffres (ex: `01`)
- `$CH_TITRE` = le texte après le tiret (ex: `Arithmétique`)
- `$FOOTER_GAUCHE` = `Ch $CH_NUM. $CH_TITRE`  (ex: `Ch 01. Arithmétique`)

Ce footer sera injecté localement dans chaque fichier généré,
**sans aucune modification de `preamble/`**.

## Étape 1 — Lire et analyser source.tex
Lire chapitres/$CHAPITRE/source.tex et produire un rapport rapide :
- Nombre de blocs par type (ACTIVITE, APPLICATION, EXERCICE, etc.)
- Corrections manquantes (bloc sans son SOLUTION_ correspondant)
- Avertir si un bloc %% n'est pas reconnu

Si des corrections sont manquantes, demander :
"Il manque X corrections. Je génère quand même ou tu veux les compléter d'abord ?"

## Étape 2 — Générer fiche_prof.tex
Balises incluses : ACTIVITE, DEFINITION, PROPRIETE,
                   TECHNIQUES, EXEMPLE, REMARQUE,
                   APPLICATION, EXERCICE
Balises exclues  : SOLUTION_ACTIVITE, SOLUTION_APPLICATION,
                   SOLUTION_EXERCICE

Structure du fichier :
```
\documentclass[10pt, a4paper]{article}
\input{../../preamble/01_packages}
\input{../../preamble/02_style}
\input{../../preamble/03_macros}
\begin{document}
\input{Page1}
\fancypagestyle{cours}{\fancyfoot[L]{\small $FOOTER_GAUCHE}}
\pagestyle{cours}
[TOUT le contenu de source.tex]
\end{document}
```

## Étape 3 — Générer td.tex
Contenu : UNIQUEMENT les blocs ACTIVITE + APPLICATION + EXERCICE.
Les blocs SOLUTION_*, DEFINITION, PROPRIETE, TECHNIQUES, EXEMPLE, REMARQUE
sont EXCLUS.

Structure du fichier :
```
\documentclass[10pt, a4paper]{article}
\input{../../preamble/01_packages}
\input{../../preamble/02_style}
\input{../../preamble/03_macros}
\geometry{a4paper, left=0.6cm, right=0.6cm, top=0.6cm, bottom=1.5cm}
\begin{document}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\fancyfoot[L]{\small $FOOTER_GAUCHE}
[HEADER complet — copié depuis le td.tex existant du chapitre]
\vspace{0.4cm}
\begin{multicols*}{2}
[ACTIVITE + APPLICATION + EXERCICE uniquement]
\end{multicols*}
\end{document}
```

## Étape 4 — Générer td_correction.tex
Contenu : UNIQUEMENT les blocs SOLUTION_ACTIVITE + SOLUTION_APPLICATION
+ SOLUTION_EXERCICE.

Structure du fichier :
```
\documentclass[10pt, a4paper]{article}
\input{../../preamble/01_packages}
\input{../../preamble/02_style}
\input{../../preamble/03_macros}
\begin{document}
\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[C]{\thepage}
\fancyfoot[L]{\small $FOOTER_GAUCHE}
[HEADER CORRECTION — copié depuis td_correction.tex existant]
\vspace{0.4cm}
\begin{multicols*}{2}
[SOLUTION_* uniquement dans l'ordre]
\end{multicols*}
\end{document}
```

## Étape 5 — Vérification
Vérifier que :
- [ ] Chaque \begin{...} a son \end{...} dans les 3 fichiers
- [ ] Pas de \textwidth dans les minipage (uniquement \linewidth)
- [ ] Les chemins \input{../../preamble/...} sont corrects
- [ ] Le header du td.tex est complet
- [ ] \fancyfoot[L] présent dans les 3 fichiers avec le bon titre
- [ ] \begin{multicols*}{2} présent dans td.tex ET td_correction.tex

## Étape 6 — Git push automatique
```bash
cd pack-pedagogique
git add chapitres/$CHAPITRE/
git commit -m "[$CHAPITRE] : fiche_prof + td + td_correction générés"
git push origin main
```

Confirmer : "✅ 3 documents générés et pushés sur GitHub.
Overleaf : Menu → GitHub → Pull changes."
