---
name: audit
description: Vérifier les corrections manquantes et l'état du chapitre
---

# /audit — Audit complet d'un chapitre

## Étape 0 — Identifier le chapitre
Si non précisé, demander :
"Quel chapitre auditer ? (ex: ch11_fonctions, ou 'tous' pour tous les chapitres)"

## Étape 1 — Lire source.tex
Lire chapitres/$CHAPITRE/source.tex et produire le rapport suivant :

### Rapport d'audit

**Blocs présents :**
- ACTIVITE        : N blocs
- SOLUTION_ACTIVITE : N blocs
- DEFINITION      : N blocs
- PROPRIETE       : N blocs
- TECHNIQUES      : N blocs
- EXEMPLE         : N blocs
- REMARQUE        : N blocs
- APPLICATION     : N blocs
- SOLUTION_APPLICATION : N blocs
- EXERCICE        : N blocs
- SOLUTION_EXERCICE : N blocs

**Corrections manquantes :**
- [ ] ACTIVITE X n'a pas de SOLUTION_ACTIVITE
- [ ] APPLICATION Y n'a pas de SOLUTION_APPLICATION
- [ ] EXERCICE Z n'a pas de SOLUTION_EXERCICE

**Vérifications LaTeX :**
- [ ] Présence de \textwidth dans les minipage (INTERDIT)
- [ ] Blocs \begin{...} sans \end{...} correspondant
- [ ] Balises %% non reconnues

**Documents générés :**
- [ ] fiche_prof.tex existe
- [ ] td.tex existe
- [ ] td_correction.tex existe
- [ ] Les 3 fichiers sont à jour (date de modification)

## Étape 2 — Proposer les actions
Selon le rapport, proposer :
"Il manque X corrections. Veux-tu que je les génère maintenant ?"
"Il y a Y problèmes LaTeX. Veux-tu que je les corrige ?"
"Les documents ne sont pas à jour. Lance /generer pour les régénérer."

## Étape 3 — Pas de modification automatique
/audit ne modifie RIEN. Il observe et rapporte seulement.
Toute action doit être confirmée explicitement.
