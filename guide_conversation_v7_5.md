# Guide Complet — Pack Pédagogique avec Claude Code
## Résumé de la conversation complète
**Auteur :** Kaazouzi Ayyoub · Tronc Commun Maroc · Version 7.5

---

## CHANGELOG v7.5

| Ajout | Section |
|-------|---------|
| **Nouvelle répartition officielle des 15 chapitres TCS** | §3, §2, §10 |
| Mise à jour architecture : dossiers chapitres renommés | §2 |
| Mise à jour skills par chapitre (domaines recalculés) | §10 |
| Mise à jour skills dans l'arbre .claude/skills/ | §2 |
| Mise à jour patterns/ : chapitre source recalculé | §5 |
| Mise à jour STATUS.md : nouveaux numéros ch02, ch12 | §2 |
| Note de migration : ancienne → nouvelle numérotation | §22 (nouveau) |
| Historique v7.5 | §21 |

---

## 0. NAVIGATION — UTILISER LE BON GUIDE

Ce projet dispose de **deux guides complémentaires** :

| Guide | Format | Usage |
|-------|--------|-------|
| `guide_conversation_v7_5.md` (ce fichier) | Markdown | Référence théorique, architecture, règles |
| `guide_workflow_ultra_detaille_v7_5.html` | HTML interactif | Opérationnel : prompts à copier, sessions pas à pas |

> ⭐ **Conseil :** ouvrir le guide HTML dans le navigateur pendant les sessions Claude Code.
> Il contient les prompts prêts à copier-coller, les checklists interactives et les sessions types.

---

## 1. CONTEXTE DU PROJET

### Pack Pédagogique — 2 cibles
**Pack Prof** (par chapitre) :
- Fiche pédagogique complète (PDF + LaTeX)
- Fiche TD (activités + applications + exercices)
- Fiche correction TD

**Pack Élève** (projet séparé, plus tard) :
- Essentiel du cours
- Exercices corrigés
- Contrôles corrigés

---

## 2. ARCHITECTURE FINALE DU PROJET (v7.5)

```
pack-pedagogique/
├── CLAUDE.md                        ← Cerveau global (< 80 lignes — règle stricte)
├── STATUS.md                        ← Tableau des 15 chapitres TCS
├── log.md                           ← Journal de bord (append-only)
├── index-concepts.md                ← Index des notions mathématiques
├── .gitignore
├── README.md
├── .claude/
│   ├── commands/
│   │   ├── generer.md               ← /generer (+ Étape 0 plan Karpathy)
│   │   ├── nouveau-chapitre.md      ← /nouveau-chapitre
│   │   ├── figure.md                ← /figure
│   │   ├── tableau.md               ← /tableau
│   │   ├── audit.md                 ← /audit (+ critères de succès Karpathy)
│   │   ├── audit-global.md          ← /audit-global
│   │   ├── repartir-duree.md        ← /repartir-duree
│   │   └── verificateur-graphes.md  ← /verificateur-graphes
│   └── skills/
│       ├── karpathy-guidelines.md        ← ⭐ v7.3 — chargé avec tout skill domaine
│       ├── correction-commune.md         ← Règles communes à tous les chapitres
│       ├── domaine-algebre.md            ← ch01, ch05, ch07, ch08
│       ├── domaine-arithmetique.md       ← ch02
│       ├── domaine-geometrie-vectorielle.md ← ch03, ch04
│       ├── domaine-geometrie-analytique.md  ← ch06, ch13
│       ├── domaine-trigonometrie.md      ← ch09, ch11
│       ├── domaine-statistiques.md       ← ch10
│       ├── domaine-analyse.md            ← ch12
│       ├── domaine-geometrie-plane.md    ← ch14
│       └── domaine-geometrie-espace.md   ← ch15
├── patterns/                        ← Corrections validées réutilisables
│   ├── README.md
│   ├── resolution-equation-1er-degre.md
│   ├── divisibilite-pgcd-ppcm.md
│   ├── taux-de-variation.md
│   └── parite-fonction.md
├── preamble/                        ← NE JAMAIS MODIFIER
│   ├── 01_packages.tex
│   ├── 02_style.tex
│   └── 03_macros.tex
└── chapitres/
    ├── Images/                      ← Ressource globale — utilisée par TOUS les chapitres
    │   └── MEN LOGO 2.png           ← ⚠️ VÉRIFIER après CHAQUE merge Overleaf
    ├── ch01_ensembles/
    │   ├── CLAUDE.md
    │   ├── source.tex
    │   ├── Page1.tex
    │   ├── fiche_prof.tex
    │   ├── td.tex
    │   └── td_correction.tex
    ├── ch02_arithmetique/
    │   ├── CLAUDE.md
    │   ├── source.tex
    │   ├── Page1.tex
    │   ├── fiche_prof.tex
    │   ├── td.tex
    │   └── td_correction.tex      ← ⚠️ En cours de rédaction (migré depuis ch01)
    └── ch12_fonctions/
        ├── CLAUDE.md
        ├── source.tex
        ├── Page1.tex
        ├── fiche_prof.tex
        ├── td.tex
        └── td_correction.tex
```

> ⚠️ **Alerte récurrente :** `MEN LOGO 2.png` a été supprimé lors d'un merge Overleaf/GitHub.
> Après **chaque** `Pull from GitHub`, vérifier que ce fichier est toujours présent.
> Récupération : `git log --diff-filter=D` puis `git checkout <hash>^ -- "chapitres/Images/MEN LOGO 2.png"`

> ⚠️ **Migration v7.5 :** Les anciens dossiers `ch01_arithmetique` et `ch11_fonctions`
> ont été renommés respectivement `ch02_arithmetique` et `ch12_fonctions`.
> Voir §22 pour le guide de migration complet.

### État actuel des chapitres (STATUS.md)

| Chapitre | source.tex | Page1.tex | fiche_prof | td | td_correction | Statut |
|---------|:----------:|:---------:|:----------:|:--:|:-------------:|--------|
| ch01_ensembles | ❌ | ❌ | ❌ | ❌ | ❌ | Non démarré |
| ch02_arithmetique | 🔄 | ✅ | ✅ | ✅ | 🔄 (89 lignes) | En rédaction (migré) |
| ch03…ch11, ch13…ch15 | ❌ | ❌ | ❌ | ❌ | ❌ | Non démarré |
| ch12_fonctions | ✅ | ✅ | ✅ | ✅ | ✅ | Complet (migré) |

---

## 3. PROGRAMME OFFICIEL TCS — 15 CHAPITRES ET DOMAINES (v7.5)

| Chapitre | Titre | Domaine | Skill |
|---------|-------|---------|-------|
| ch01 | Ensembles de nombres | Algèbre | `domaine-algebre` |
| ch02 | Arithmétique dans ℕ | Arithmétique | `domaine-arithmetique` |
| ch03 | Calcul vectoriel dans le plan | Géométrie vectorielle | `domaine-geometrie-vectorielle` |
| ch04 | La projection dans le plan | Géométrie vectorielle | `domaine-geometrie-vectorielle` |
| ch05 | L'ordre dans ℝ | Algèbre | `domaine-algebre` |
| ch06 | La droite dans le plan | Géométrie analytique | `domaine-geometrie-analytique` |
| ch07 | Les polynômes | Algèbre | `domaine-algebre` |
| ch08 | Équations, inéquations et systèmes | Algèbre | `domaine-algebre` |
| ch09 | Calcul trigonométrique | Trigonométrie | `domaine-trigonometrie` |
| ch10 | Statistiques | Statistiques | `domaine-statistiques` |
| ch11 | Calcul trigonométrique (partie 2) | Trigonométrie | `domaine-trigonometrie` |
| ch12 | Généralités sur les fonctions numériques | Analyse | `domaine-analyse` |
| ch13 | Le produit scalaire | Géométrie analytique | `domaine-geometrie-analytique` |
| ch14 | Les transformations dans le plan | Géométrie plane | `domaine-geometrie-plane` |
| ch15 | Géométrie dans l'espace | Géométrie dans l'espace | `domaine-geometrie-espace` |

---

## 4. HIÉRARCHIE CLAUDE.md (v7.5)

### CLAUDE.md global (racine) — < 80 lignes
Contient uniquement les règles universelles :
- Format commit git : `[chXX] : description courte`
- `\linewidth` obligatoire, `\textwidth` interdit dans les minipage
- Vocabulaire officiel marocain
- Règle : **1 session = 1 chapitre**
- Liste des skills par domaine (11 skills dont `karpathy-guidelines`)
- Git push après chaque modification
- **Règle log.md** : écrire une entrée en fin de chaque session
- **Règle patterns/** : consulter avant toute génération de correction
- **Règle index-concepts.md** : mettre à jour via /generer

### CLAUDE.md local (dans chaque dossier chapitre)
```markdown
# Chapitre 02 — Arithmétique dans ℕ
Niveau : Tronc Commun Scientifique | Masse horaire : 5h

## Skills à charger
karpathy-guidelines + correction-commune + domaine-arithmetique

## Statut
- source.tex        : 🔄 en rédaction
- Page1.tex         : ✅ créé
- fiche_prof.tex    : ✅ généré (486 lignes)
- td.tex            : ✅ généré (298 lignes)
- td_correction.tex : 🔄 partiel (89 lignes)

## Notations spécifiques
- Divisibilité : a | b (jamais a/b pour la relation)
- PGCD : PGCD(a,b) | PPCM : PPCM(a,b)
- Division euclidienne : a = b×q + r, 0 ≤ r < b

## Corrections en cours
[liste des applications/exercices restants]
```

> ⚠️ **Règle critique (v7.4+) :** `Masse horaire` dans le CLAUDE.md local doit **toujours**
> correspondre exactement à la valeur affichée dans `Page1.tex` (source de vérité PDF).
> Toute divergence rend `/repartir-duree` inutilisable.
> Procédure de vérification : `grep -i "masse\|horaire\|heure" chapitres/chXX/CLAUDE.md Page1.tex`

---

## 5. FICHIERS TRANSVERSAUX

Ces 3 fichiers assurent la cohérence et la mémoire entre les 15 chapitres.

### log.md — Journal de bord

**Format d'une entrée :**
```markdown
## [YYYY-MM-DD] chXX_nom — Session N
- Fait : ...
- Décision : ...
- Problème rencontré : ...
- Restant : ...
```

### index-concepts.md — Index des notions

**Format d'une entrée :**
```markdown
**Nom de la notion** → chXX (introduit / réutilisé / approfondi)
  - Notation : ...
  - Remarque : ...
```

### patterns/ — Bibliothèque de corrections validées

| Fichier | Chapitre source (v7.5) | Type |
|---------|------------------------|------|
| `resolution-equation-1er-degre.md` | ch02 | APPLICATION |
| `divisibilite-pgcd-ppcm.md` | ch02 | APPLICATION |
| `taux-de-variation.md` | ch12 | APPLICATION |
| `parite-fonction.md` | ch12 | APPLICATION |

---

## 6. PRINCIPE FONDAMENTAL — source.tex

**source.tex est la source unique.** Les 3 documents sont générés depuis lui.

### Table de distribution des balises %%

| Balise | fiche_prof | td | td_correction |
|--------|:----------:|:--:|:-------------:|
| SECTION | ✅ | ❌ | ❌ |
| ACTIVITE | ✅ | ✅ | ❌ |
| SOLUTION_ACTIVITE | ❌ | ❌ | ✅ |
| DEFINITION | ✅ | ❌ | ❌ |
| PROPRIETE | ✅ | ❌ | ❌ |
| TECHNIQUES | ✅ | ❌ | ❌ |
| EXEMPLE | ✅ | ❌ | ❌ |
| REMARQUE | ✅ | ❌ | ❌ |
| APPLICATION | ✅ | ✅ | ❌ |
| SOLUTION_APPLICATION | ❌ | ❌ | ✅ |
| EXERCICE | ✅ | ✅ | ❌ |
| SOLUTION_EXERCICE | ❌ | ❌ | ✅ |

### Règle graphique absolue
```
\linewidth  ← TOUJOURS dans les minipage de source.tex
\textwidth  ← INTERDIT dans source.tex
```

### Structure type de source.tex
```latex
%% SECTION
\section{Titre de section \duree{15 min}}

%% ACTIVITE
\begin{Activite}[][5 min]
...
\end{Activite}

%% SOLUTION_ACTIVITE
\begin{Solution}[ACTIVITÉ][1]
...
\end{Solution}

%% DEFINITION
\begin{Definition}[Titre]
...
\end{Definition}

%% APPLICATION
\begin{Application}[][10 min]
...
\end{Application}

%% SOLUTION_APPLICATION
\begin{Solution}[APPLICATION][1]
...
\end{Solution}
```

---

## 7. ENVIRONNEMENTS DISPONIBLES

| Environnement | Usage | Syntaxe |
|---------------|-------|---------|
| Activite | Activités d'éveil | `\begin{Activite}[titre][durée]` |
| Definition | Définitions | `\begin{Definition}[titre]` |
| Propriete | Propriétés | `\begin{Propriete}[titre]` |
| Theoreme | Théorèmes | `\begin{Theoreme}[titre]` |
| Exemple | Exemples corrigés | `\begin{Exemple}[][durée]` |
| Application | Applications | `\begin{Application}[][durée]` |
| Exercice | Exercices de synthèse | `\begin{Exercice}[][durée]` |
| Techniques | Tableaux techniques | `\begin{Techniques}` |
| Remarque | Remarques | `\begin{Remarque}` |
| Preuve | Preuves | `\begin{Preuve}` |
| Solution | Corrections | `\begin{Solution}[TYPE][N]` |

> ⚠️ **Interdit :** `\begin{Exemple}[Correction ...]` — toujours `\begin{Solution}[TYPE][N]`

---

## 8. RÈGLES DES DURÉES (v7.1)

### Catégorie A — Durées AFFICHÉES (`\duree{}`) — multiple de 5 min
`\section{}` · `Activite` · `Exemple` · `Application` · `Exercice`

### Catégorie B — Durées NON AFFICHÉES (commentaire LaTeX)
`Definition` · `Propriete` · `Theoreme` · `Remarque` · `Techniques` · `Preuve`
Format : `% durée estimée : X min` — entier libre.

### Règle de cohérence de section
```
\duree{} section = somme(A + B) arrondie au multiple de 5 supérieur
```

---

## 9. COMMANDES DISPONIBLES (v7.5)

### /generer
```
/generer ch02_arithmetique
```
- **Étape 0 (Karpathy)** : liste tous les blocs SOLUTION manquants, vérifie patterns/, affiche le plan complet et **attend confirmation**
- Lit source.tex
- Génère fiche_prof.tex, td.tex, td_correction.tex
- Met à jour index-concepts.md
- git push

### /audit
```
/audit ch02_arithmetique
```
Lecture seule — rapport des corrections manquantes.
**Section Critères de succès Karpathy :**
```
□ Chaque SOLUTION insérée = uniquement le bloc demandé modifié
□ Diff source.tex = zéro ligne hors du bloc SOLUTION concerné
□ Checklist ✓ affichée avant insertion de chaque correction
```

### /nouveau-chapitre
```
/nouveau-chapitre
```
Pose 5 questions → crée chapitres/chXX_nom/ + CLAUDE.md local + Page1.tex vide → initialise log.md et index-concepts.md.

### /audit-global
```
/audit-global
```
Affiche l'état transversal (log, index, patterns) puis les 15 chapitres.

### /repartir-duree
```
/repartir-duree ch02_arithmetique
```
Vérifie et redistribue le volume horaire. Lecture seule jusqu'à "OK".

### /figure · /tableau · /verificateur-graphes
Inchangés depuis v7.2.

---

## 10. SKILLS — STRUCTURE COMPLÈTE (v7.5)

### Vue d'ensemble des 11 skills

| Skill | Chapitres (v7.5) | Domaine officiel |
|-------|------------------|-----------------|
| `karpathy-guidelines` | **Tous** ⭐ | Qualité & rigueur |
| `correction-commune` | Tous | Base commune |
| `domaine-algebre` | ch01, ch05, ch07, ch08 | Algèbre |
| `domaine-arithmetique` | ch02 | Arithmétique |
| `domaine-geometrie-vectorielle` | ch03, ch04 | Géométrie vectorielle |
| `domaine-geometrie-analytique` | ch06, ch13 | Géométrie analytique |
| `domaine-trigonometrie` | ch09, ch11 | Trigonométrie |
| `domaine-statistiques` | ch10 | Statistiques |
| `domaine-analyse` | ch12 | Analyse |
| `domaine-geometrie-plane` | ch14 | Géométrie plane |
| `domaine-geometrie-espace` | ch15 | Géométrie dans l'espace |

> **Règle :** toujours charger `karpathy-guidelines` + `correction-commune` + le skill du domaine.

---

## 10 BIS. KARPATHY GUIDELINES — CONTENU DU SKILL ⭐

Le fichier `.claude/skills/karpathy-guidelines.md` contient les 4 principes
**adaptés au projet LaTeX pédagogique**.

### Principe 1 — Réfléchir avant d'agir
- Lire le bloc `%%` concerné **et les 2 blocs adjacents**
- Vérifier `patterns/` : existe-t-il un pattern applicable ?
- Énoncer : *"Je vais modifier [bloc], pattern utilisé : [nom ou aucun]"*
- **Attendre la confirmation** avant d'insérer

### Principe 2 — Simplicité stricte
- Minimum de code qui satisfait `correction-commune` + skill domaine
- Zéro `\textbf{}` décoratif non prévu par le skill
- Zéro phrase au-delà des justifications obligatoires
- Si une étape dépasse 3 lignes pour un calcul simple → réécrire

### Principe 3 — Modifications chirurgicales
- **Seul le bloc `%%` SOLUTION demandé est modifié**
- Les blocs `%%` voisins sont intouchables
- Les commentaires `% durée estimée : X min` ne sont jamais touchés
- **Test :** diff = uniquement les lignes du bloc concerné

### Principe 4 — Checklist obligatoire avant insertion
```
✓ Bloc ciblé      : %% SOLUTION_[TYPE] [N]
✓ Pattern appliqué : [nom] ou [aucun]
✓ Style           : SOLUTION_ACTIVITE ou SOLUTION_APPLICATION
✓ Phrase ▶        : présente / absente (selon le type)
✓ Conclusion      : présente / absente (selon le type)
✓ Blocs voisins   : non modifiés
```

---

## 11. STYLES DE CORRECTION — correction-commune

### Connecteurs logiques
| Connecteur | Quand |
|-----------|-------|
| `On a :` | Introduire la première ligne |
| `\Leftrightarrow` | Entre chaque étape équivalente |
| `Donc` | Conclusion |
| `D'où` | Conséquence directe |
| `Or` | Information connue |

### Justifications obligatoires
| Opération | Justification |
|-----------|---------------|
| Développer | `(distributivité)` |
| Regrouper | `(on regroupe les termes semblables)` |
| Diviser par c > 0 | `(on divise par c, c > 0)` |
| Diviser par c < 0 | `(on divise par c < 0, le sens de l'inégalité s'inverse)` |
| Multiplier par PPCM | `(on multiplie par n, PPCM de a et b)` |
| Factoriser | `(factorisation)` |

### Conclusions standard
| Type | Format |
|------|--------|
| Équation | `Donc $S = \{valeur\}$.` |
| Inéquation | `Donc $S = [a \; ; \; +\infty[$.` |
| Pas solution | `Donc $S = \emptyset$.` |
| Tout réel | `Donc $S = \R$.` |

---

## 12. DISTINCTION FONDAMENTALE — SOLUTION_ACTIVITE vs SOLUTION_APPLICATION

### SOLUTION_ACTIVITE — Phase de construction (découverte)
- Pont explicite vers les acquis du collège
- Ne jamais sauter une étape de calcul
- Phrase d'institutionnalisation obligatoire :
```latex
$\blacktriangleright$ \textbf{Ceci illustre la notion de
\textcolor{PrimaryColor}{nom de la notion}.}
```
- Ton accessible, début lycée
- Ne jamais écrire "Conclusion"

### SOLUTION_APPLICATION — Phase d'entraînement (mobilisation)
- Style du skill domaine appliqué
- Connecteurs logiques de correction-commune
- Justifications à chaque étape
- **Phrase `$\blacktriangleright$` INTERDITE**
- Conclusion standard obligatoire

### Résumé comparatif

| Critère | SOLUTION_ACTIVITE | SOLUTION_APPLICATION |
|---|---|---|
| Rôle | Construire la notion | Mobiliser la notion |
| Ton | Guidant, accessible | Rigoureux, modèle |
| Pont collège | Obligatoire | Inutile |
| Phrase ▶ | Obligatoire | **Interdite** |
| Connecteurs `\Leftrightarrow` | Si pertinent | Obligatoires |
| Conclusion `Donc S = ...` | Selon contexte | Obligatoire |

---

## 13. AGENT — correcteur-fiche

```
Lance l'agent correcteur-fiche sur ch02_arithmetique
```

**4 axes :**
- **Axe 1 — Rigueur mathématique** *(validation requise)*
- **Axe 2 — Pédagogie des solutions** *(validation requise)*
- **Axe 3 — Syntaxe LaTeX** *(automatique)*
- **Axe 4 — Orthographe et typographie** *(automatique)*

---

## 14. NOTEBOOKLM MCP

### Installation
```bash
npx notebooklm-mcp@latest
claude mcp add notebooklm -- npx notebooklm-mcp@latest -s user
```

### Commande de génération source.tex
```
En utilisant le notebook chXX dans NotebookLM,
pose la question section par section :
"Liste les définitions de la section [nom]"

Crée source.tex :
- %% SECTION, %% DEFINITION, %% PROPRIETE, %% REMARQUE
- Environnements du preamble uniquement
- \linewidth partout
- Montre les 80 premières lignes avant de sauvegarder.
git push après validation.
```

> ⚠️ Demander section par section pour éviter les timeouts.

---

## 15. WORKFLOW QUOTIDIEN (v7.5)

**Règle d'or :** 1 session Claude Code = 1 chapitre.

### Démarrage de session (toutes sessions)
```
1. cd pack-pedagogique && claude
2. Lire log.md → voir la dernière entrée du chapitre concerné
3. Lire index-concepts.md → avoir la vision transversale
4. Commencer le travail
```

### Pour un chapitre existant
```
1. /audit ch02_arithmetique
2. /repartir-duree ch02_arithmetique → "OK"
3. Générer corrections UNE PAR UNE (Karpathy)
4. /generer ch02_arithmetique → Étape 0 → "OK"
5. Overleaf → Pull from GitHub
6. Vérifier MEN LOGO 2.png présent (ch12)
7. [FIN] log.md mis à jour
```

### Pour un nouveau chapitre
```
1. /nouveau-chapitre → 5 questions → structure créée
2. Remplir Page1.tex manuellement
   ⚠️ Masse horaire CLAUDE.md local = valeur Page1.tex (OBLIGATOIRE)
3. NotebookLM → extraire source.tex section par section
4. /audit chXX → /repartir-duree chXX → /generer chXX
5. Overleaf → Pull from GitHub
```

---

## 16. SYNCHRONISATION GITHUB ↔ OVERLEAF

```
Claude Code → git push automatique
Overleaf    : Menu → GitHub → Pull from GitHub

Overleaf modifié → Menu → GitHub → Push to GitHub
Terminal    : git pull
```

**Conflit git :**
```bash
git status && git add . && git commit -m "[chXX] : résolution conflit" && git push origin main
```

**Éditeur Vim lors d'un merge :**
```
:wq   ← valider et quitter
```

**Fichier supprimé lors d'un merge :**
```bash
git log --diff-filter=D --summary
git checkout <hash>^ -- chemin/vers/fichier
```

---

## 17. FORMULATION DES DEMANDES À CLAUDE CODE (v7.5)

### Principe de génération incrémentale (v7.4+)
> ⭐ **Règle renforcée :** toujours générer **une correction à la fois**.
> Ne jamais demander "génère toutes les corrections".
> Chaque correction = un prompt + une checklist + une validation explicite.
> Cela réduit les erreurs en cascade et permet d'interrompre sans perte.

### Prompt de démarrage universel
```
Lis chapitres/chXX_nom/CLAUDE.md.
Charge les skills : karpathy-guidelines + correction-commune + domaine-[NOM].
Lis source.tex de ce chapitre.
Lis patterns/ pour identifier les patterns applicables.
Affiche le plan complet des corrections manquantes avec pattern identifié pour chacune.
Attends mon OK avant de commencer.
```

### Prompt correction APPLICATION
```
Génère la correction de l'Application N du chXX.
Pattern à appliquer : [nom du pattern] (ou "aucun").
Skills : karpathy-guidelines + correction-commune + domaine-[NOM].
Règles Karpathy :
  - Touche UNIQUEMENT %% SOLUTION_APPLICATION Application N
  - Blocs adjacents intouchables
  - Minimum de code : connecteurs + justifications + conclusion
  - Zéro décoration non prévue par le skill
Affiche la checklist ✓ avant d'insérer. Attends ma validation.
```

### Prompt correction ACTIVITE
```
Génère la correction de l'Activité N du chXX.
Skills : karpathy-guidelines + correction-commune + domaine-[NOM].
Règles SOLUTION_ACTIVITE :
  - Pont explicite avec acquis du collège
  - Phrase ▶ \blacktriangleright après chaque notion
  - Vocabulaire accessible TCS
  - Jamais le mot "Conclusion"
Règles Karpathy :
  - Touche UNIQUEMENT %% SOLUTION_ACTIVITE Activité N
  - Blocs adjacents intouchables
Affiche la checklist ✓ avant d'insérer. Attends ma validation.
```

### Prompt verser un pattern
```
La correction de [type] [N] du [chXX] est validée.
Verse ce pattern dans patterns/[nom-du-pattern].md avec :
  - Validé dans : chXX, session [date]
  - Skill domaine : domaine-[NOM]
  - Structure type : [résumé de la structure]
  - Règles spécifiques : [liste]
git push.
```

### Prompt fin de session
```
Session terminée sur chXX_nom.
Écris dans log.md :
## [DATE] chXX_nom — Session N
- Fait : [liste]
- Décision : [patterns versés, règles établies]
- Problème rencontré : [ou "aucun"]
- Restant : [liste]
git push.
```

---

## 18. MACROS DISPONIBLES

```latex
\N, \Z, \R, \C     → ensembles de nombres
\vect{AB}          → vecteur avec flèche
\abs{x}            → valeur absolue |x|
\frac{a}{b}        → dfrac automatique
\duree{X min}      → badge horloge dans la boîte
\dd                → d droit pour intégrales
\e                 → e droit (exponentielle)
```

---

## 19. VOCABULAIRE OFFICIEL MAROCAIN

| ✅ Correct | ❌ Incorrect |
|-----------|-------------|
| ensemble de définition | domaine de définition |
| ensemble solution | solution générale |
| sens de l'inégalité | signe de l'inégalité |
| taux de variation | taux d'accroissement |
| membre gauche / droit | côté gauche / droit |
| strictement croissante | croissante strictement |

---

## 20. DÉPANNAGE RAPIDE (v7.5)

| Problème | Solution |
|---------|---------|
| `source.tex` ne compile pas | Normal — compiler `fiche_prof.tex` |
| git push échoue (port 443) | Vérifier WiFi / désactiver VPN |
| Claude ignore les règles | CLAUDE.md global > 80 lignes → réduire |
| Figure trop grande en td | Remplacer `\textwidth` par `\linewidth` |
| Overleaf ne se met pas à jour | Menu → GitHub → Pull from GitHub |
| Mauvais style de correction | Vérifier le skill dans CLAUDE.md local |
| Skill introuvable | Vérifier que le fichier est `.md` plat |
| index-concepts non mis à jour | Relancer `/generer` |
| log.md non mis à jour | Demander explicitement en fin de session |
| Pattern non appliqué | Mentionner `patterns/` dans la demande |
| CLAUDE.md local non chargé | Vérifier que `chapitres/chXX/CLAUDE.md` existe |
| Conflit git | Ne pas modifier le même chapitre dans Overleaf et Claude Code |
| Preamble modifié | `git checkout preamble/02_style.tex` |
| NotebookLM timeout | Demander section par section |
| `/repartir-duree` volume erroné | Corriger `Masse horaire` dans CLAUDE.md local (doit = Page1.tex) |
| Fichier image manquant après merge | `git log --diff-filter=D` puis `git checkout <hash>^ -- fichier` |
| Correction en masse → erreurs | Générer une par une + checklist Karpathy |
| Vim s'ouvre lors d'un merge | Taper `:wq` |
| SOLUTION_ACTIVITE sans phrase ▶ | Phrase `\blacktriangleright` obligatoire |
| SOLUTION_APPLICATION avec phrase ▶ | Supprimer : **interdite** en application |
| domaine-geometrie.md chargé | Fichier obsolète — utiliser le bon skill géométrie |
| Claude modifie blocs adjacents | karpathy-guidelines Principe 3 non chargé |
| Checklist ✓ absente | Rappeler : "Affiche la checklist karpathy-guidelines avant d'insérer" |
| Correction trop longue | karpathy-guidelines Principe 2 : simplifier |
| Claude génère sans confirmation | karpathy-guidelines Principe 1 : "Attend ma confirmation" |
| MEN LOGO 2.png manquant | `git checkout <hash>^ -- "chapitres/Images/MEN LOGO 2.png"` |
| Masse horaire CLAUDE.md ≠ Page1.tex | Corriger CLAUDE.md local → relancer `/repartir-duree` |
| Ancien numéro de chapitre utilisé | Consulter §22 — table de migration v7.4 → v7.5 |

---

## 21. HISTORIQUE DES VERSIONS

| Version | Changements majeurs |
|---------|-------------------|
| v7.0 | Architecture source.tex unique, balises %%, CLAUDE.md hiérarchique |
| v7.1 | /repartir-duree, règles durées cat. A/B, distinction SOLUTION_ACTIVITE/APPLICATION |
| v7.2 | 3 fichiers transversaux (log.md, index-concepts.md, patterns/), 9 domaines officiels TCS, 10 skills |
| v7.3 | Karpathy Guidelines intégrées (11e skill), checklist ✓ obligatoire, Étape 0 dans /generer, critères de succès dans /audit |
| v7.4 | Guide HTML interactif, alerte MEN LOGO 2.png, règle Masse horaire renforcée, génération incrémentale renforcée, dépannage étendu |
| v7.5 | **Nouvelle répartition officielle des 15 chapitres TCS**, renommage dossiers ch01→ch02 et ch11→ch12, mise à jour skills par domaine, table de migration §22 |

---

## 22. GUIDE DE MIGRATION v7.4 → v7.5

> ⭐ **À lire obligatoirement avant toute nouvelle session Claude Code.**

### Table de correspondance ancienne → nouvelle numérotation

| Ancien (v7.4) | Nouveau (v7.5) | Dossier à renommer | Action git |
|--------------|---------------|-------------------|-----------|
| ch01 — Arithmétique dans ℕ | **ch02** — Arithmétique dans ℕ | `ch01_arithmetique` → `ch02_arithmetique` | `git mv` |
| ch02 — Calcul vectoriel | **ch03** — Calcul vectoriel | `ch02_calcul_vectoriel` → `ch03_calcul_vectoriel` | `git mv` (si existait) |
| ch03 — La projection | **ch04** — La projection | `ch03_projection` → `ch04_projection` | `git mv` (si existait) |
| ch04 — Ensembles de nombres | **ch01** — Ensembles de nombres | n/a (non démarré) | Créer directement en ch01 |
| ch05 → ch08 | **ch05 → ch08** | inchangés | — |
| ch09 → ch10 | **ch09 → ch10** | inchangés | — |
| ch11 — Calcul trigono. (2) | **ch11** — Calcul trigono. (partie 2) | identique | — |
| ch11_fonctions | **ch12_fonctions** | `ch11_fonctions` → `ch12_fonctions` | `git mv` |
| ch12 → ch15 anciens | **ch12 → ch15 nouveaux** | voir tableau §3 | vérifier domaines |
| ch13 — Transformations | **ch14** — Transformations | `ch13_...` → `ch14_...` | `git mv` (si existait) |
| ch14 — Produit scalaire | **ch13** — Produit scalaire | `ch14_...` → `ch13_...` | `git mv` (si existait) |

### Commandes git de migration (chapitres actifs)

```bash
# Migration des deux dossiers actifs
git mv chapitres/ch01_arithmetique chapitres/ch02_arithmetique
git mv chapitres/ch11_fonctions chapitres/ch12_fonctions

# Mettre à jour CLAUDE.md local dans ch02_arithmetique
# (changer "Chapitre 01" → "Chapitre 02" dans l'en-tête)

# Mettre à jour CLAUDE.md local dans ch12_fonctions
# (changer "Chapitre 11" → "Chapitre 12" dans l'en-tête)

# Commit de migration
git add .
git commit -m "[migration] : répartition officielle v7.5 — renommage ch01→ch02, ch11→ch12"
git push
```

### Points de vigilance après migration

1. **MEN LOGO 2.png** → chemin global : `chapitres/Images/MEN LOGO 2.png` (ressource partagée par tous les chapitres)
2. **patterns/** → mettre à jour les références `ch01` → `ch02` et `ch11` → `ch12` dans les fichiers de patterns existants
3. **log.md** → les entrées passées restent inchangées (historique conservé) ; les nouvelles entrées utilisent la nouvelle numérotation
4. **index-concepts.md** → mettre à jour les références ch01/ch11 → ch02/ch12 lors du prochain `/generer`
5. **Overleaf** → après git push, faire Pull from GitHub pour synchroniser

---

*Pack Pédagogique v7.5 · Kaazouzi Ayyoub · Tronc Commun Maroc*
*Dernière mise à jour : mai 2026*
