---
# Skill — Domaine Géométrie Vectorielle
Chapitres couverts : ch02 (Calcul vectoriel), ch03 (Projection)
Toujours charger avec : correction-commune
---
## Notations officielles
- Vecteur : \vect{AB}  (macro disponible dans preamble/03_macros.tex)
- Norme : \|\vect{AB}\|  (jamais |AB|)
- Vecteur nul : \vect{0}
- Colinéarité : \vect{AB} = k\,\vect{CD}
## Structure type — Démontrer que deux vecteurs sont colinéaires
```latex
On a :
\[\vect{AB} = \begin{pmatrix} x_1 \\ y_1 \end{pmatrix}
\quad \text{et} \quad
\vect{CD} = \begin{pmatrix} x_2 \\ y_2 \end{pmatrix}\]
\[x_1 \times y_2 - x_2 \times y_1 = \ldots = 0\]
Donc $\vect{AB}$ et $\vect{CD}$ sont colinéaires.
```
## Structure type — Projection orthogonale
```latex
Soit $H$ le projeté orthogonal de $A$ sur $(BC)$.
On a $\vect{BH} = \dfrac{\vect{BA} \cdot \vect{BC}}
{\|\vect{BC}\|^2}\,\vect{BC}$.
```
## Justifications spécifiques au domaine
| Opération | Justification |
|-----------|---------------|
| Décomposer un vecteur | `(relation de Chasles)` |
| Conclure colinéarité | `(déterminant nul)` |
| Conclure orthogonalité | `(produit scalaire nul)` |
## À compléter lors de la rédaction de ch02 et ch03
