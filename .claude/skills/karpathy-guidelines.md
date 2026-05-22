# Karpathy Guidelines — Pack Pédagogique v7.2

## Principe 1 — Réfléchir avant d'agir
Avant toute modification de source.tex :
- Lire le bloc %% concerné et les 2 blocs adjacents
- Vérifier patterns/ : existe-t-il un pattern applicable ?
- Énoncer explicitement : "Je vais modifier [bloc], pattern utilisé : [nom ou aucun]"
- Attendre la confirmation avant d'insérer quoi que ce soit

## Principe 2 — Simplicité stricte
Pour toute SOLUTION générée :
- Minimum de code qui satisfait correction-commune + skill domaine
- Zéro \textbf{} décoratif non prévu par le skill
- Zéro phrase supplémentaire au-delà des justifications obligatoires
- Si une formulation fait plus de 3 lignes pour une étape simple → réécrire

## Principe 3 — Modifications chirurgicales
Règle absolue lors de l'édition de source.tex :
- Seul le bloc %% SOLUTION demandé est modifié
- Les blocs %% voisins sont intouchables
- Les commentaires "% durée estimée : X min" ne sont jamais touchés
- Les espaces blancs entre environnements ne sont jamais modifiés
- Test de validation : diff = uniquement les lignes du bloc concerné

## Principe 4 — Objectif vérifiable
Pour chaque correction générée, afficher avant insertion :
✓ Bloc modifié : %% SOLUTION_[TYPE] [N]
✓ Pattern appliqué : [nom] ou [aucun]
✓ Style : SOLUTION_ACTIVITE ou SOLUTION_APPLICATION
✓ Phrase ▶ : présente / absente (selon le type)
✓ Conclusion "Donc S = ..." : présente / absente (selon le type)
✓ Blocs voisins : non modifiés
