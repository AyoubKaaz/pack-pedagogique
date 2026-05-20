---
# Skill — Domaine Arithmétique
Chapitres couverts : ch01 (Arithmétique dans ℕ)
Toujours charger avec : correction-commune
---
## Notations officielles (jamais déroger)
- Divisibilité : a | b  (jamais a/b pour la relation)
- PGCD : PGCD(a,b)
- PPCM : PPCM(a,b)
- Division euclidienne : a = b×q + r,  avec 0 ≤ r < b
## Structure type — Algorithme d'Euclide
```latex
On a :
\begin{align*}
a &= b \times q_1 + r_1 \\
b &= r_1 \times q_2 + r_2 \\
r_1 &= r_2 \times q_3 + 0
\end{align*}
Donc $\text{PGCD}(a, b) = r_2$.
```
## Structure type — Justifier a | b
```latex
On a $a = b \times q$, donc $b \mid a$.
```
## Structure type — Calcul de PPCM
```latex
On a $\text{PGCD}(a,b) \times \text{PPCM}(a,b) = a \times b$,
donc $\text{PPCM}(a,b) = \dfrac{a \times b}{\text{PGCD}(a,b)} = \ldots$
```
## Justifications spécifiques au domaine
| Opération | Justification |
|-----------|---------------|
| Multiplier par PPCM | `(on multiplie par n, PPCM de a et b)` |
| Conclure divisibilité | `(le reste est nul)` |
| Appliquer Bézout | `(théorème de Bézout)` |
## À compléter lors de la rédaction de ch01
- Ajouter les règles de style spécifiques aux exercices de ch01
- Ajouter les types d'erreurs fréquentes observées
