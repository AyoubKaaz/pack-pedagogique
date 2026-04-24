# CLAUDE.md — Kaazouzi Ayyoub
# Pack Pédagogique Mathématiques — Tronc Commun Maroc
# Version : 5.0 — optimisée (< 200 lignes)

---

## 🎯 IDENTITÉ

Tu es l'assistant de Kaazouzi Ayyoub, professeur de mathématiques.
Tu travailles directement sur des fichiers `.tex`.
Tu génères du CONTENU uniquement.
Tu ne touches JAMAIS aux fichiers `preamble/`.

---

## 🗂️ STRUCTURE DU PROJET

```
pack-pedagogique/
├── CLAUDE.md
├── .claude/
│   ├── commands/        ← /generer /figure /tableau /audit /nouveau-chapitre
│   └── skills/
│       └── correction-mathematique/SKILL.md
├── preamble/            ← NE JAMAIS MODIFIER
│   ├── 01_packages.tex
│   ├── 02_style.tex
│   └── 03_macros.tex
└── chapitres/
    └── ch$N_$NOM/
        ├── source.tex         ← SOURCE UNIQUE — tu écris ici
        ├── Page1.tex
        ├── fiche_prof.tex     ← GÉNÉRÉ par /generer
        ├── td.tex             ← GÉNÉRÉ par /generer
        ├── td_correction.tex  ← GÉNÉRÉ par /generer
        └── Images/
```

---

## 📋 BALISES DE source.tex

Un bloc = sa balise %% + son contenu jusqu'à la balise suivante.

```
%% ACTIVITE              → td ✓   fiche_prof ✓
%% SOLUTION_ACTIVITE     → td_correction ✓  seulement
%% DEFINITION            → fiche_prof ✓   seulement
%% PROPRIETE             → fiche_prof ✓   seulement
%% TECHNIQUES            → fiche_prof ✓   seulement
%% EXEMPLE               → fiche_prof ✓   seulement
%% REMARQUE              → fiche_prof ✓   seulement
%% APPLICATION           → td ✓   fiche_prof ✓
%% SOLUTION_APPLICATION  → td_correction ✓  seulement
%% EXERCICE              → td ✓   fiche_prof ✓
%% SOLUTION_EXERCICE     → td_correction ✓  seulement
```

---

## 🧱 ENVIRONNEMENTS (preamble/02_style.tex)

Ne jamais inventer de nouveaux environnements.
Syntaxe : \begin{Nom}[titre][durée]

Disponibles :
Activite  Application  Exercice  Definition  Propriete
Theoreme  Exemple  Techniques  Remarque  Corollaire  Preuve  Solution

---

## 📐 RÈGLE GRAPHIQUE ABSOLUE

Dans source.tex : toujours \linewidth, jamais \textwidth.
Raison : source.tex compile en 1 colonne (fiche) ET 2 colonnes (td).

---

## ⚙️ COMMANDES DISPONIBLES

/generer          → Génère fiche_prof + td + td_correction
/nouveau-chapitre → Crée la structure d'un nouveau chapitre
/figure           → Insère une figure TikZ dans source.tex
/tableau          → Insère un tableau LaTeX dans source.tex
/audit            → Vérifie corrections manquantes (lecture seule)

---

## 🔒 RÈGLES GIT — OBLIGATOIRES

Après CHAQUE modification, sans demander la permission :
git add .
git commit -m "[chXX] : description courte"
git push origin main

Format des commits :
[ch11] : correction application 3 ajoutée
[ch03] : nouveau chapitre créé
[ch11] : figure TikZ activité 2 insérée

---

## 🚫 LIMITES ABSOLUES

- Ne jamais modifier preamble/*.tex
- Ne jamais modifier fiche_prof.tex, td.tex, td_correction.tex directement
- Ne jamais créer de nouveaux environnements tcolorbox
- Ne jamais utiliser \textwidth dans les minipage de source.tex
- Ne jamais supprimer du contenu validé

---

## 🔄 WORKFLOW D'UNE SESSION

1. Je dis le chapitre en cours
2. Tu lis source.tex
3. Tu résumes : blocs présents + corrections manquantes
4. Tu attends mes instructions
5. Tu agis → tu commites → tu confirmes

---

## 🧮 MACROS (preamble/03_macros.tex)

\N \Z \R \C       → ensembles de nombres
\vect{AB}         → vecteur avec flèche
\abs{x}           → valeur absolue
\frac{a}{b}       → dfrac automatique (ne jamais écrire \dfrac)
\duree{X min}     → badge horloge dans la boîte
\dd               → d droit pour intégrales
\e                → e droit pour exponentielle

---

Version 5.0 — Kaazouzi Ayyoub
Style de correction → .claude/skills/correction-mathematique/SKILL.md
