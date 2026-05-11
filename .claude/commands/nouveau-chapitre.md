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

### Déterminer le domaine automatiquement depuis $NUM
| Numéro | Domaine | Skill à charger |
|--------|---------|-----------------|
| 01–05  | Algèbre | domaine-algebre |
| 06–10  | Géométrie | domaine-geometrie |
| 11–15  | Analyse | domaine-analyse |

Ne pas poser de question sur le domaine — le déduire du numéro.

---

## Étape 1 — Créer la structure

```bash
mkdir -p chapitres/ch$NUM_$SLUG/Images
```

Où $SLUG = titre en minuscules sans accents, espaces remplacés par _
Ex: ch03_equations_inequations

---

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
\begin{Solution}[ACTIVITÉ][1]

\end{Solution}

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
\begin{Solution}[APPLICATION][1]

\end{Solution}

% ────────────────────────────────────────────
%  2. [TITRE DEUXIÈME SECTION]
% ────────────────────────────────────────────

%% DEFINITION


%% PROPRIETE


%% APPLICATION
\begin{Application}[][$DUREE min]

\end{Application}

%% SOLUTION_APPLICATION
\begin{Solution}[APPLICATION][2]

\end{Solution}

% ────────────────────────────────────────────
%  EXERCICE DE SYNTHÈSE
% ────────────────────────────────────────────

%% EXERCICE
\begin{Exercice}[][$DUREE min]

\end{Exercice}

%% SOLUTION_EXERCICE
\begin{Solution}[EXERCICE DE SYNTHÈSE][1]

\end{Solution}
```

---

## Étape 2b — Créer CLAUDE.md local ← NOUVEAU

Créer chapitres/ch$NUM_$SLUG/CLAUDE.md avec ce contenu :

```markdown
# Chapitre $NUM — $TITRE
Niveau : Tronc Commun $NIVEAU | Masse horaire : $MASSE_HORAIRE

## Skill à charger
correction-commune + $DOMAINE_SKILL
(déterminé automatiquement depuis le numéro de chapitre)

## Statut
- source.tex       : ❌ non démarré
- fiche_prof.tex   : ❌ non généré
- td.tex           : ❌ non généré
- td_correction.tex: ❌ non généré

## Notations spécifiques à ce chapitre
% TODO : compléter après rédaction des premières sections

## Corrections en cours
Aucune

## Limites absolues (rappel local)
- \linewidth obligatoire dans les minipage — \textwidth interdit
- \begin{Solution}[TYPE][N] pour toutes les corrections
- Ne jamais modifier preamble/*.tex
```

---

## Étape 3 — Créer Page1.tex

Copier Page1.tex depuis ch11_fonctions/ et adapter :
- Numéro et titre du chapitre
- Niveau
- Masse horaire
- Laisser les sections "Capacités attendues" et
  "Orientations pédagogiques" VIDES avec ce commentaire :
  % TODO: compléter les capacités attendues
  % TODO: compléter les orientations pédagogiques

---

## Étape 4 — Créer les 3 templates vides

Créer fiche_prof.tex, td.tex, td_correction.tex
en copiant les templates de ch11_fonctions/ et en adaptant :
- Le numéro de série dans le header du td.tex
- Le titre dans le header de td_correction.tex
- Les chemins \input{../../preamble/...} (vérifier qu'ils sont corrects)

Laisser la zone contenu vide — elle sera remplie par /generer.

---

## Étape 5 — Copier le logo

```bash
cp "chapitres/ch11_fonctions/Images/MEN LOGO 2.png" \
   "chapitres/ch$NUM_$SLUG/Images/"
```

---

## Étape 6 — Mettre à jour STATUS.md

Ajouter une ligne dans STATUS.md à la racine :

```
| ch$NUM_$SLUG | $TITRE | ❌ | ❌ | ❌ | ❌ | 🔄 démarré le $DATE |
```

---

## Étape 7 — Rapport final

Afficher la structure créée :

```
✅ Chapitre $NUM créé : chapitres/ch$NUM_$SLUG/
   ├── CLAUDE.md          (skill : $DOMAINE_SKILL — statut initialisé)
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
1. Complète les notations spécifiques dans chapitres/ch$NUM_$SLUG/CLAUDE.md
2. Complète les objectifs dans Page1.tex
3. Rédige le contenu dans source.tex
4. Lance /generer ch$NUM_$SLUG quand tu es prêt"

---

## Étape 8 — Git push

```bash
git add chapitres/ch$NUM_$SLUG/
git add STATUS.md
git commit -m "[ch$NUM] : nouveau chapitre créé — $TITRE"
git push origin main
```
