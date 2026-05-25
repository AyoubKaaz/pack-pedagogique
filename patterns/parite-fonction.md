---
# Pattern validé — Parité d'une fonction
Validé dans : ch11
Skill appliqué : domaine-analyse + correction-commune
Type : SOLUTION_APPLICATION
---
## Structure type complète
```latex
\begin{itemize}
    \item On a : $D_f = \ldots$, donc $D_f$ est symétrique par rapport à $0$. \checkmark
    \item Soit $x \in D_f$. On a :
    \[f(-x) = \ldots = f(x)\]
    Donc pour tout $x \in D_f$,$-x \in D_f$ et $f(-x) = f(x)$.
    D'où $f$ est \textbf{paire}.
\end{itemize}
```
## Variantes conclusions
| Cas | Conclusion |
|-----|-----------|
| f(-x) = f(x) | D'où $f$ est \textbf{paire}. |
| f(-x) = -f(x) | D'où $f$ est \textbf{impaire}. |
| ni l'un ni l'autre | D'où $f$ n'est ni paire ni impaire. |
## Condition préalable obligatoire
Toujours vérifier en premier que D_f est symétrique par rapport à 0.
Si D_f n'est pas symétrique → la fonction n'est ni paire ni impaire
(inutile de calculer f(-x)).
