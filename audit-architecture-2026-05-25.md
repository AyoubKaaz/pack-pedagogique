# Audit Architectural — Pack Pédagogique TCS
**Date :** 2026-05-25  
**Auditeur :** Claude Code (mode lecture seule stricte)  
**Périmètre :** Repository complet — lecture de 41 fichiers, 0 modification  
**Version architecture de référence :** v7.3

---

## 1. Résumé Exécutif

**Score global : 60 / 100**

Le pack pédagogique dispose d'une **infrastructure conceptuellement solide** : séparation source/générés, système de skills plats, commandes documentées, préambule LaTeX protégé. La qualité des 2 chapitres rédigés est bonne sur le plan LaTeX (aucune violation critique détectée en échantillonnage).

Cependant, trois risques majeurs menacent la montée en charge vers les 13 chapitres manquants :

### 3 Forces
1. **Architecture LaTeX maîtrisée** — source.tex monolithique → 3 documents générés : concept robuste, balises `%% TYPE` bien appliquées sur les 2 chapitres existants
2. **Qualité du contenu LaTeX produit** — aucun `\textwidth` dans les minipage, vocabulaire officiel marocain respecté, délimiteurs mathématiques conformes, `$\blacktriangleright$` correctement distribué (ACTIVITE ✓ / APPLICATION ✗)
3. **Système de skills plats bien structuré** — `correction-commune.md` de référence, `karpathy-guidelines.md` adapté au contexte LaTeX, skills domaines spécialisés cohérents

### 3 Risques Critiques
1. **`log.md` quasi vide** — 1 seule entrée pour l'ensemble du projet (Session 0, 2026-05-20). Impossible de reconstituer les décisions prises sur ch01 et ch11. Risque de réincidence sur les mêmes problèmes
2. **Mapping domaines incohérent entre sources de vérité** — `CLAUDE.md` global et `nouveau-chapitre.md` se contredisent sur les skills à charger (ex : ch06-ch10 → `domaine-geometrie` OBSOLÈTE dans nouveau-chapitre.md). Erreur garantie à la création des 13 prochains chapitres
3. **Discipline git insuffisante** — 7/20 commits (35%) non conformes au format `[chXX] : description`, working tree actuellement sale, `git add .` dans les instructions CLAUDE.md

---

## 2. Scoring par Axe

| Axe | Note | Justification |
|-----|------|---------------|
| **Architecture & modularité** | 7/10 | Structure de dossiers claire, skills/commandes bien organisés. Pénalités : CLAUDE.md racine 87 lignes (limite 80), fichier obsolète `domaine-geometrie.md` non supprimé, commande `fix-delimiteurs` non déclarée |
| **Cohérence inter-fichiers** | 5/10 | Incohérence critique entre CLAUDE.md global et nouveau-chapitre.md sur le mapping domaines. Skill ch11 `domaine-trigonometrie` vs `domaine-analyse` selon nouveau-chapitre.md. Section dupliquée dans ch01/CLAUDE.md. ch01 sans bloc EXERCICE |
| **Qualité LaTeX** | 8/10 | Aucune violation `\textwidth`, vocabulaire officiel respecté, délimiteurs conformes 10pt, durées multiples de 5. Pénalité : ch01 sans exercice de synthèse (0 bloc `%% EXERCICE`) |
| **Hygiène git / sync** | 5/10 | .gitignore couvre bien les artefacts LaTeX, remote GitHub configuré. Pénalités : 7/20 commits non conformes, dirty tree actuel, `git add .` risqué dans CLAUDE.md |
| **Traçabilité (log, index, patterns)** | 4/10 | Patterns bien alimentés (4 fichiers, 2/chapitre). Mais log.md avec 1 seule entrée = traçabilité quasi nulle. Index-concepts.md cohérent avec les 2 chapitres rédigés |
| **Conformité Karpathy v7.3** | 7/10 | `/generer` a bien l'Étape 0 Karpathy, `/audit` a les critères de succès. Pénalités : CLAUDE.md local des chapitres ne mentionne pas karpathy-guidelines, template nouveau-chapitre non mis à jour |

---

## 3. Inventaire

### 3.1 Fichiers racine

| Fichier | Présent | Conforme | Anomalie |
|---------|---------|----------|----------|
| `CLAUDE.md` | ✅ | ⚠️ | **87 lignes** (limite 80) |
| `STATUS.md` | ✅ | ⚠️ | Titres ch02-ch10, ch12-ch15 vides ("—") |
| `log.md` | ✅ | 🔴 | 1 seule entrée sur toute la durée du projet |
| `index-concepts.md` | ✅ | ✅ | Cohérent avec l'état actuel (2 chapitres) |
| `README.md` | ✅ | ⚠️ | Contenu obsolète (instructions de copie manuelle) |
| `.gitignore` | ✅ | ✅ | Couvre .aux, .log, .out, .synctex.gz, .toc, .fls, .fdb_latexmk, .pdf |

### 3.2 Commandes (`.claude/commands/`)

| Commande | Attendue (CLAUDE.md) | Présente | Conforme |
|----------|---------------------|----------|----------|
| `generer` | ✅ | ✅ | ✅ — Étape 0 Karpathy présente |
| `nouveau-chapitre` | ✅ | ✅ | ⚠️ — Mapping domaines incohérent (voir Ph.2) |
| `figure` | ✅ | ✅ | ✅ |
| `tableau` | ✅ | ✅ | ✅ |
| `audit` | ✅ | ✅ | ✅ — Critères Karpathy présents |
| `audit-global` | ✅ | ✅ | ✅ |
| `repartir-duree` | ✅ | ✅ | ✅ |
| `verificateur-graphes` | ✅ | ✅ | ✅ |
| `fix-delimiteurs` | ❌ (non déclarée) | ✅ | 🟡 — Commande fonctionnelle mais fantôme dans CLAUDE.md |

### 3.3 Skills (`.claude/skills/`)

| Skill | Déclaré CLAUDE.md | Présent | Conforme |
|-------|------------------|---------|----------|
| `karpathy-guidelines` | ✅ | ✅ | ✅ |
| `correction-commune` | ✅ | ✅ | ✅ |
| `domaine-arithmetique` | ✅ | ✅ | ✅ |
| `domaine-geometrie-vectorielle` | ✅ | ✅ | ✅ |
| `domaine-algebre` | ✅ | ✅ | ✅ |
| `domaine-geometrie-analytique` | ✅ | ✅ | ✅ |
| `domaine-trigonometrie` | ✅ | ✅ | ✅ |
| `domaine-statistiques` | ✅ | ✅ | ✅ |
| `domaine-analyse` | ✅ | ✅ | ✅ |
| `domaine-geometrie-plane` | ✅ | ✅ | ✅ |
| `domaine-geometrie-espace` | ✅ | ✅ | ✅ |
| `domaine-geometrie` | ❌ (non déclaré) | ✅ | 🟡 — Marqué OBSOLÈTE dans le fichier lui-même |

### 3.4 Patterns (`patterns/`)

| Fichier | Chapitre source | Présent | Listé README |
|---------|----------------|---------|--------------|
| `divisibilite-pgcd-ppcm.md` | ch01 | ✅ | ✅ |
| `resolution-equation-1er-degre.md` | ch01 | ✅ | ✅ |
| `taux-de-variation.md` | ch11 | ✅ | ✅ |
| `parite-fonction.md` | ch11 | ✅ (modifié non commité) | ✅ |

### 3.5 Chapitres présents vs attendus

| Chapitre | Titre officiel TCS | source.tex | fiche_prof | td | td_correction | CLAUDE.md local |
|----------|-------------------|:----------:|:----------:|:--:|:-------------:|:---------------:|
| ch01 | Arithmétique | ✅ | ✅ | ✅ | ✅ | ✅ |
| ch02 | Vecteurs | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch03 | Barycentre | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch04 | Équations/Inéquations 1er degré | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch05 | Systèmes d'équations | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch06 | Repérage dans le plan | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch07 | Développement / Factorisation | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch08 | Équations du 2nd degré | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch09 | Trigonométrie | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch10 | Statistiques | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch11 | Fonctions Numériques | ✅ | ✅ | ✅ | ✅ | ✅ |
| ch12 | Limites et Dérivées | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch13 | Géométrie plane | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch14 | Géométrie analytique | ❌ | ❌ | ❌ | ❌ | ❌ |
| ch15 | Géométrie dans l'espace | ❌ | ❌ | ❌ | ❌ | ❌ |

**Complétion : 2/15 chapitres (13%)**

### 3.6 Balises source.tex — couverture par chapitre

| Balise | ch01 | ch11 | Attendu |
|--------|:----:|:----:|---------|
| `%% SECTION` | 6 | 14 | ≥1 |
| `%% ACTIVITE` | 5 | 5 | ≥1 |
| `%% SOLUTION_ACTIVITE` | 5 | 5 | = ACTIVITE |
| `%% DEFINITION` | 7 | 12 | ≥1 |
| `%% PROPRIETE` | 9 | 6 | ≥1 |
| `%% TECHNIQUES` | 0 | 1 | — |
| `%% EXEMPLE` | 7 | 9 | ≥1 |
| `%% REMARQUE` | 4 | 3 | — |
| `%% APPLICATION` | 12 | 26 | ≥1 |
| `%% SOLUTION_APPLICATION` | 12 | 26 | = APPLICATION |
| `%% EXERCICE` | **0** | 2 | ≥1 |
| `%% SOLUTION_EXERCICE` | **0** | 2 | = EXERCICE |

---

## 4. Anomalies Détectées

### 🔴 BLOQUANT

| # | Fichier (ligne) | Règle violée | Correction suggérée |
|---|----------------|-------------|---------------------|
| A1 | `nouveau-chapitre.md` L23-24 : mapping `06–10 → domaine-geometrie` | `domaine-geometrie.md` est marqué OBSOLÈTE depuis 2026-05-21. Tout `/nouveau-chapitre` pour ch06-ch10 chargera un skill vide | Remplacer la table par : `06 → domaine-geometrie-analytique` · `07-08 → domaine-algebre` · `09 → domaine-trigonometrie` · `10 → domaine-statistiques` · `11-15 → domaine-analyse` |

### 🟠 MAJEUR

| # | Fichier (ligne) | Règle violée | Correction suggérée |
|---|----------------|-------------|---------------------|
| A2 | `CLAUDE.md` racine (L87) | Limite 80 lignes dépassée : 87 lignes — risque de troncature contexte Claude Code | Fusionner ou condenser les sections "Règle log.md" (L76-81) et "Règle patterns/" (L83-87) en 4 lignes |
| A3 | `ch11_fonctions/CLAUDE.md` L5 : `domaine-trigonometrie` | Incohérence : CLAUDE.md global (L64) mappe ch11 → `domaine-trigonometrie`, mais `nouveau-chapitre.md` (L22) mappe 11-15 → `domaine-analyse`. "Fonctions Numériques" est du domaine analyse | Choisir une source de vérité et aligner les deux : soit CLAUDE.md global, soit nouveau-chapitre.md |
| A4 | `ch01_arithmetique/CLAUDE.md` L31-61 | Section "Distinction SOLUTION_ACTIVITE / SOLUTION_APPLICATION" dupliquée à l'identique (lignes 31-43 = lignes 47-60) | Supprimer le second bloc (L47-61) |
| A5 | `ch01_arithmetique/CLAUDE.md` L42, L57 | Référence morte : `correction-commune/SKILL.md` (ancien chemin dossier v6) — devrait être `.claude/skills/correction-commune.md` | Remplacer par le chemin actuel dans les deux occurrences |
| A6 | `chapitres/ch01_arithmetique/source.tex` | 0 bloc `%% EXERCICE` — l'exercice de synthèse est absent du chapitre | Rédiger 1 exercice de synthèse avec son `%% SOLUTION_EXERCICE` |
| A7 | `log.md` (entrée unique, L12-19) | 1 seule entrée pour tout le projet. Toutes les sessions ch01 (mai 2026) et ch11 (2025) sont non tracées. Règle CLAUDE.md L76 non respectée | Ajouter les entrées manquantes rétrospectivement pour ch11 et les 4+ sessions ch01 |
| A8 | Git — commits `858d209`, `ad59d74`, `4bdffd3`, `cbd3033`, `041c0f6`, `34ef038` | Format `[chXX] : description` non respecté — 7/20 commits (35%) avec messages aléatoires ou auto-générés Overleaf | Adopter un pre-commit hook ou un alias git pour imposer le format. Pour les commits Overleaf, accepter `[overleaf] : pull` comme format |
| A9 | `.claude/settings.local.json` + `patterns/parite-fonction.md` | Working tree sale — 2 fichiers modifiés non commités (git status) | Commiter ou reverter avant toute nouvelle session |

### 🟡 MINEUR

| # | Fichier (ligne) | Règle violée | Correction suggérée |
|---|----------------|-------------|---------------------|
| B1 | `.claude/skills/domaine-geometrie.md` | Fichier marqué "NE PLUS UTILISER" depuis 2026-05-21 mais présent dans le repo — risque de confusion | Supprimer le fichier (ou le déplacer dans `.claude/skills/archive/`) |
| B2 | `CLAUDE.md` racine L5-8 | `git add .` dans la règle git universelle — risque d'inclure des artefacts non gitignorés ou des fichiers sensibles | Remplacer par `git add chapitres/$CHAPITRE/ [fichier concerné]` |
| B3 | `README.md` L38-40 | Instructions de copie manuelle obsolètes ("Copier dans `chapitres/ch11_fonctions/` : Page1.tex, Images/MEN LOGO 2.png") | Supprimer ces lignes — elles décrivent un état initial dépassé |
| B4 | `chapitres/Images/` (racine de chapitres/) | `MEN LOGO 2.png` présent à `chapitres/Images/` et suivi par git. Devrait être uniquement dans chaque `chapitres/chXX/Images/` | Vérifier si ce fichier est utile à la racine ; si non, supprimer et mettre à jour les `.gitignore` de chapitres/ si besoin |
| B5 | `STATUS.md` L11-25 | Titres ch02-ch10 et ch12-ch15 vides ("—") | Remplir les titres officiels du programme TCS (cf. tableau Phase 0) |
| B6 | `.claude/commands/nouveau-chapitre.md` L133-157 | Template CLAUDE.md local généré par `/nouveau-chapitre` ne mentionne pas `karpathy-guidelines` — exigence v7.3 | Ajouter `karpathy-guidelines` dans la section "Skills à charger" du template Étape 2b |
| B7 | `CLAUDE.md` racine L58-69 | Section "Skills disponibles" ne mentionne pas `fix-delimiteurs` parmi les commandes | Ajouter `fix-delimiteurs` dans la liste ou dans une section "Commandes utiles" |
| B8 | `.antigravitycli/` (répertoire racine) | Répertoire d'outil tiers non documenté, non gitignored. Présence imprévue dans le repo | Vérifier son contenu et ajouter à `.gitignore` si ce sont des données locales |

---

## 5. Quick Wins (< 1h chacun, impact élevé)

| Priorité | Action | Impact | Durée estimée |
|----------|--------|--------|---------------|
| **QW1** | Corriger le mapping domaines dans `nouveau-chapitre.md` (tableau L19-24) | 🔴 Évite erreurs de skill sur 13 chapitres futurs | 15 min |
| **QW2** | Ajouter les entrées manquantes dans `log.md` (sessions ch01 + ch11 2025-2026) | 🟠 Restaure la traçabilité du projet | 30 min |
| **QW3** | Supprimer la section dupliquée dans `ch01_arithmetique/CLAUDE.md` (L47-61) | 🟠 Évite confusion lors des corrections | 5 min |
| **QW4** | Commiter les 2 fichiers en attente (`.claude/settings.local.json`, `patterns/parite-fonction.md`) avec un message conforme | 🟠 Nettoie le working tree | 5 min |
| **QW5** | Réduire `CLAUDE.md` racine à ≤80 lignes (condenser sections log et patterns) | 🟠 Respect de la limite absolue | 20 min |

---

## 6. Chantiers Structurels (> 1 jour, impact stratégique)

| Priorité | Chantier | Justification | Effort |
|----------|----------|---------------|--------|
| **CS1** | **Rédiger les 13 chapitres manquants** (ch02-ch10, ch12-ch15) | Complétion du programme TCS — le vrai objectif du projet | Long terme |
| **CS2** | **Aligner toutes les sources de vérité sur le mapping domaines** | CLAUDE.md global vs nouveau-chapitre.md vs CLAUDE.md locaux — 3 sources divergentes | 1 journée |
| **CS3** | **Ajouter un exercice de synthèse à ch01** | ch01 est le seul chapitre sans `%% EXERCICE` — incomplet pédagogiquement | 2-3h |
| **CS4** | **Mettre en place une discipline git systématique** | 35% de commits non conformes. Solution : alias git, pre-commit hook léger, ou règle explicite dans CLAUDE.md | 2-4h |
| **CS5** | **Alimenter le log.md de manière systématique** | 1 entrée pour ~10 sessions de travail = traçabilité nulle. Ajouter une alerte en début de session (hook Claude Code) | 2-4h |

---

## 7. Roadmap 3 Mois

### Sprint 1 — Juin 2026 : Fondations propres
**Objectif mesurable : 0 anomalie 🔴 ou 🟠 ouverte**

- [ ] Corriger `nouveau-chapitre.md` mapping domaines (QW1) — avant 2026-06-01
- [ ] Nettoyer working tree + commiter (QW4) — avant 2026-06-01
- [ ] Réduire CLAUDE.md ≤80 lignes (QW5) — avant 2026-06-01
- [ ] Supprimer `ch01/CLAUDE.md` section dupliquée (QW3) — avant 2026-06-01
- [ ] Ajouter exercice de synthèse à ch01 (CS3) — avant 2026-06-15
- [ ] Retrouver et logger les sessions passées dans log.md (QW2) — avant 2026-06-15
- [ ] Aligner sources de vérité domaines (CS2) — avant 2026-06-30

### Sprint 2 — Juillet 2026 : Expansion ch02-ch06
**Objectif mesurable : 5 nouveaux chapitres créés et rédigés**

- [ ] `/nouveau-chapitre` ch02 (Vecteurs) → domaine-geometrie-vectorielle
- [ ] `/nouveau-chapitre` ch03 (Barycentre) → domaine-geometrie-vectorielle
- [ ] `/nouveau-chapitre` ch04 (Équations 1er degré) → domaine-algebre
- [ ] `/nouveau-chapitre` ch05 (Systèmes) → domaine-algebre
- [ ] `/nouveau-chapitre` ch06 (Repérage) → domaine-geometrie-analytique
- [ ] Pour chaque chapitre : log.md renseigné, patterns versés si applicable

### Sprint 3 — Août 2026 : Expansion ch07-ch15
**Objectif mesurable : 100% chapitres créés, ≥8 rédigés (>50%)**

- [ ] Chapitres ch07-ch10 (algèbre, statistiques)
- [ ] Chapitres ch12-ch15 (analyse, géométries)
- [ ] git hook pre-commit pour valider le format `[chXX]` — avant 2026-08-01
- [ ] `STATUS.md` titres complets pour tous les 15 chapitres — avant 2026-08-01
- [ ] Audit architectural de mi-parcours — 2026-08-25

---

## 8. Annexe — Commandes git utiles pour appliquer les corrections

```bash
# QW4 — Commiter les fichiers en attente
git add .claude/settings.local.json patterns/parite-fonction.md
git commit -m "[projet] : mise à jour settings + pattern parite-fonction"
git push origin main

# B1 — Supprimer domaine-geometrie.md obsolète
git rm .claude/skills/domaine-geometrie.md
git commit -m "[skills] : suppression domaine-geometrie.md obsolète (remplacé depuis 2026-05-21)"
git push origin main

# B4 — Supprimer le logo orphelin à la racine de chapitres/
git rm "chapitres/Images/MEN LOGO 2.png"
git commit -m "[projet] : suppression logo orphelin chapitres/Images/"
git push origin main

# Vérifier l'état de synchronisation avec origin
git fetch origin
git status

# Voir les commits non conformes (pour référence)
git log --oneline -20 | grep -v "^\w\+ \[" 

# Alias utile à ajouter (~/.gitconfig) pour imposer le format
# git config --global alias.ch-commit '!f() { git commit -m "[ch$1] : $2"; }; f'
# Usage : git ch-commit 04 "rédaction section 1 équations"
```

---

## Checklist Karpathy — Fin d'audit

- ✓ **6 phases exécutées** (Ph.0 Plan → Ph.5 Traçabilité → Ph.6 Synthèse)
- ✓ **Aucun fichier modifié hors du rapport** (lecture seule stricte respectée)
- ✓ **Toutes les anomalies tracées** (fichier + ligne quand disponible)
- ✓ **Roadmap chiffrée et datée** (3 sprints mensuels, objectifs mesurables)
- ✓ **Rapport sauvegardé** à `audit-architecture-2026-05-25.md` — en attente de validation pour commit

---

*Audit réalisé en lecture seule le 2026-05-25. Aucune modification effectuée sur le repository.*
