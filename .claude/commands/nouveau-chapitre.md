---
name: nouveau-chapitre
description: Créer la structure complète d'un nouveau chapitre
---

# /nouveau-chapitre — Créer un nouveau chapitre

## Étape 0 — Collecter les informations
Demander si non précisé :

1. "Numéro du chapitre ? (ex: 03)"
2. "Titre du chapitre ? (ex: Équations et Inéquations du Premier Degré)"
3. "Niveau : Tronc Commun Scientifique / Technologique / les deux ?"
4. "Masse horaire ? (ex: 8h)"
5. "Numéro de série TD ? (ex: Série 3)"

## Étape 1 — Créer la structure

```bash
mkdir -p chapitres/ch$NUM_$SLUG/Images
```

Où $SLUG = titre en minuscules sans accents, espaces remplacés par _
Ex: ch03_equations_inequations

## Étape 2 — Créer source.tex

Créer chapitres/ch$NUM_$SLUG/source.tex avec ce contenu :

```latex
% ============================================================
% SOURCE.TEX — Chapitre $NUM : $TITRE
% Niveau    : Tronc Commun $NIVEAU
% Auteur    : Kaazouzi Ayyoub
% Créé le   : $DATE
% ============================================================
% FICHIER MAÎTRE — Ne jamais modifier fiche_prof.tex,
% td.tex, td_correction.tex directement.
% ============================================================

% ────────────────────────────────────────────
%  1. [TITRE PREMIÈRE SECTION]
% ────────────────────────────────────────────

%% ACTIVITE
\begin{Activite}[][$DUREE min]

\end{Activite}

%% SOLUTION_ACTIVITE
\begin{Exemple}[Correction — Activité 1]

\end{Exemple}

%% DEFINITION
\begin{Definition}[]

\end{Definition}

%% PROPRIETE
\begin{Propriete}[]

\end{Propriete}

%% EXEMPLE
\begin{Exemple}[][$DUREE min]

\end{Exemple}

%% APPLICATION
\begin{Application}[][$DUREE min]

\end{Application}

%% SOLUTION_APPLICATION
\begin{Exemple}[Correction — Application 1]

\end{Exemple}

% ────────────────────────────────────────────
%  2. [TITRE DEUXIÈME SECTION]
% ────────────────────────────────────────────

%% DEFINITION


%% PROPRIETE


%% APPLICATION
\begin{Application}[][$DUREE min]

\end{Application}

%% SOLUTION_APPLICATION
\begin{Exemple}[Correction — Application 2]

\end{Exemple}

% ────────────────────────────────────────────
%  EXERCICE DE SYNTHÈSE
% ────────────────────────────────────────────

%% EXERCICE
\begin{Exercice}[][$DUREE min]

\end{Exercice}

%% SOLUTION_EXERCICE
\begin{Exemple}[Correction — Exercice de synthèse 1]

\end{Exemple}
```

## Étape 3 — Créer Page1.tex

Copier Page1.tex depuis ch11_fonctions/ et adapter :
- Numéro et titre du chapitre
- Niveau
- Masse horaire
- Laisser les sections "Capacités attendues" et
  "Orientations pédagogiques" VIDES avec ce commentaire :
  % TODO: compléter les capacités attendues
  % TODO: compléter les orientations pédagogiques

## Étape 4 — Créer les 3 templates vides

Créer fiche_prof.tex, td.tex, td_correction.tex
en copiant les templates de ch11_fonctions/ et en adaptant :
- Le numéro de série dans le header du td.tex
- Le titre dans le header de td_correction.tex
- Les chemins \input{../../preamble/...} (vérifier qu'ils sont corrects)

Laisser la zone contenu vide — elle sera remplie par /generer.

## Étape 5 — Copier le logo
```bash
copy chapitres\ch11_fonctions\Images\MEN LOGO 2.png
     chapitres\ch$NUM_$SLUG\Images\
```

## Étape 6 — Rapport final

Afficher la structure créée :
```
✅ Chapitre $NUM créé : chapitres/ch$NUM_$SLUG/
   ├── source.tex         (squelette prêt — à remplir)
   ├── Page1.tex          (à compléter : objectifs + orientations)
   ├── fiche_prof.tex     (template prêt)
   ├── td.tex             (template prêt)
   ├── td_correction.tex  (template prêt)
   └── Images/
       └── MEN LOGO 2.png
```

Rappeler :
"Prochaines étapes :
1. Complète les objectifs dans Page1.tex
2. Rédige le contenu dans source.tex
3. Lance /generer ch$NUM_$SLUG quand tu es prêt"

## Étape 7 — Git push
```bash
git add chapitres/ch$NUM_$SLUG/
git commit -m "[ch$NUM] : nouveau chapitre créé — $TITRE"
git push origin main
```
