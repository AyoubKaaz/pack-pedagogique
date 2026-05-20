# Pack Pédagogique Mathématiques — Tronc Commun Maroc
**Auteur :** Kaazouzi Ayyoub  
**Version :** 5.0

## Structure
- `CLAUDE.md` — Instructions pour Claude Code
- `.claude/commands/` — Commandes rapides (`/generer`, `/figure`, etc.)
- `.claude/skills/` — Style de correction mathématique
- `preamble/` — Fichiers LaTeX partagés (**copier tes vrais fichiers ici**)
- `chapitres/` — Un dossier par chapitre

## Fichiers à ajouter manuellement
Copier dans `preamble/` :
- `01_packages.tex`
- `02_style.tex`  
- `03_macros.tex`

## Fichiers transversaux (v7.2)

Ces fichiers assurent la cohérence entre les 15 chapitres.
Ils sont mis à jour automatiquement par les commandes Claude Code.

| Fichier | Rôle | Mis à jour par |
|---------|------|----------------|
| `log.md` | Journal de bord session par session | Fin de chaque session |
| `index-concepts.md` | Index de toutes les notions du programme TCS | `/generer`, `/nouveau-chapitre` |
| `patterns/` | Bibliothèque de corrections validées | Manuel + Claude Code |

### Ajouter un pattern manuellement
Après avoir validé une correction dans Claude Code :
  "Verse ce pattern dans patterns/nom-du-fichier.md"

### Consulter l'état global
  /audit-global
→ affiche maintenant l'état transversal (log, index, patterns)
  avant l'état chapitre par chapitre.

Copier dans `chapitres/ch11_fonctions/` :
- `Page1.tex`
- `Images/MEN LOGO 2.png`

## Commandes disponibles dans Claude Code
| Commande | Action |
|---|---|
| `/generer` | Génère les 3 documents depuis source.tex |
| `/nouveau-chapitre` | Crée un nouveau chapitre |
| `/figure` | Insère une figure TikZ |
| `/tableau` | Insère un tableau LaTeX |
| `/audit` | Vérifie les corrections manquantes |



## Workflow
```
1. Rédiger dans source.tex
2. /generer ch11_fonctions
3. git push → Overleaf pull → compiler
```
