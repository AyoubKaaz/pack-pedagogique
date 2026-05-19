---
name: fix-delimiteurs
description: Corriger les délimiteurs mathématiques dans source.tex d'un chapitre
---

# Commande /fix-delimiteurs

## Usage
/fix-delimiteurs chXX_nom

## Workflow
1. Lire source.tex du chapitre ciblé
2. Scanner tous les modes mathématiques $ ... $ et \[ ... \]
3. Appliquer les corrections :

   RÈGLE 1 — Accolades d'ensembles :
   \left\{ → \big\{
   \right\} → \big\}
   Exception : garder \left\{ si \frac à l'intérieur

   RÈGLE 2 — Crochets d'intervalles sans fraction :
   [ → \big[   (dans contexte intervalle)
   ] → \big]   (dans contexte intervalle)
   Exception : garder \left[ si \frac à l'intérieur

   RÈGLE 3 — Parenthèses sans fraction :
   \left( → \big(
   \right) → \big)
   Exception : garder \left( si \frac à l'intérieur

4. Afficher le rapport :
   - Nombre de corrections par règle
   - Liste des lignes modifiées
   - Liste des exceptions conservées (\frac détecté)

5. Attendre "OK" avant modification
6. git push avec message : [chXX] : fix délimiteurs mathématiques
