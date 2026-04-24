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
