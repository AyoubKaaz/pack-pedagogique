---
# Pattern validé — Divisibilité, PGCD, PPCM
Validé dans : ch01
Skill appliqué : domaine-algebre + correction-commune
Type : SOLUTION_APPLICATION
---
## Notations officielles (jamais déroger)
- Divisibilité : a | b  (jamais a/b pour la relation de divisibilité)
- PGCD : PGCD(a,b)
- PPCM : PPCM(a,b)
- Division euclidienne : a = b×q + r,  avec 0 ≤ r < b
## Structure type — Calcul de PGCD par algorithme d'Euclide
```latex
On a :
\begin{align*}
120 &= 45 \times 2 + 30 \\
45  &= 30 \times 1 + 15 \\
30  &= 15 \times 2 + 0
\end{align*}
Donc $\text{PGCD}(120, 45) = 15$.
```
## Structure type — Justifier la divisibilité
```latex
On a $a = b \times q + r$ avec $r = 0$,
donc $b \mid a$.
```
## Règle clé
- Multiplier par PPCM dans une équation :
  justification : "(on multiplie par n, PPCM de a et b)"
