---
name: correction-mathematique
description: Rédiger une correction mathématique dans le style
  exact de Kaazouzi Ayyoub pour le Tronc Commun Maroc —
  justification à chaque étape, connecteurs logiques précis,
  notation officielle marocaine
---

# Skill : Correction Mathématique

## Quand ce skill est activé
- Quand un bloc %% SOLUTION_* est manquant dans source.tex
- Quand /generer détecte une correction à produire
- Quand je demande explicitement "génère la correction de..."

---

## RÈGLE 1 — Connecteurs logiques

Utiliser UNIQUEMENT ces connecteurs dans cet ordre :

| Connecteur | Quand l'utiliser |
|---|---|
| `On a :` | Introduire la première ligne |
| `\Leftrightarrow` | Entre chaque étape équivalente |
| `\Rightarrow` | Implication non réversible |
| `Donc` | Conclusion / ensemble solution |
| `D'où` | Conséquence directe d'un calcul |
| `Or` | Introduire une information connue |
| `Ainsi` | Synthèse intermédiaire |

---

## RÈGLE 2 — Format d'une étape

Chaque étape = une ligne mathématique + une justification à droite.

```latex
On a :
\[
  expression_1
\]
\[
  \Leftrightarrow expression_2
  \qquad \text{(justification)}
\]
\[
  \Leftrightarrow expression_3
  \qquad \text{(justification)}
\]
Donc $S = \{valeur\}$.
```

---

## RÈGLE 3 — Justifications exactes à utiliser

| Opération | Justification à écrire |
|---|---|
| Développer | `(distributivité)` |
| Factoriser | `(factorisation)` |
| Regrouper termes en x | `(on regroupe les termes semblables)` |
| Ajouter c aux deux membres | `(on ajoute $c$ aux deux membres)` |
| Soustraire c des deux membres | `(on soustrait $c$ des deux membres)` |
| Multiplier par c > 0 | `(on multiplie par $c > 0$)` |
| Diviser par c > 0 | `(on divise par $c$, $c > 0$)` |
| Diviser par c < 0 | `(on divise par $c < 0$, le sens de l'inégalité s'inverse)` |
| Multiplier par le PPCM | `(on multiplie par $n$, PPCM de $a$ et $b$)` |
| Réduire au même dénominateur | `(réduction au même dénominateur)` |
| Simplifier | `(simplification)` |
| Condition de définition | `(condition : $Q(x) \neq 0$)` |

---

## RÈGLE 4 — Conclusions

| Type | Conclusion à écrire |
|---|---|
| Équation, solution unique | `Donc $S = \{valeur\}$.` |
| Équation, pas de solution | `Donc $S = \emptyset$.` |
| Équation, solution réelle | `Donc $S = \R$.` |
| Inéquation | `Donc $S = [a \; ; \; +\infty[$.` |
| Inéquation stricte | `Donc $S = ]a \; ; \; +\infty[$.` |
| Vérification | Terminer par `\checkmark` |

---

## RÈGLE 5 — Ce qu'il ne faut JAMAIS écrire

- Sauter une étape même évidente
- `Il suffit de...` / `Clairement...` / `On trouve facilement...`
- Reformuler l'énoncé avant la correction
- Ajouter des commentaires pédagogiques non demandés
- Utiliser `\dfrac` — utiliser `\frac` (redéfini automatiquement)
- Utiliser `\textwidth` dans les minipage

---

## EXEMPLES DE RÉFÉRENCE VALIDÉS

### Exemple 1 — Équation simple
```latex
%% SOLUTION_APPLICATION
\begin{Solution}[Correction — Application X]
\textbf{Résoudre dans $\R$ :} $3x - 7 = 2x + 5$

On a :
\[3x - 7 = 2x + 5\]
\[\Leftrightarrow 3x - 2x = 5 + 7
  \qquad \text{(on regroupe les termes semblables)}\]
\[\Leftrightarrow x = 12\]
Donc $S = \{12\}$.
\end{Solution}
```

### Exemple 2 — Équation avec développement
```latex
%% SOLUTION_APPLICATION
\begin{Solution}[Correction — Application X]
\textbf{Résoudre dans $\R$ :} $2(3x-1) = 4x + 6$

On a :
\[2(3x-1) = 4x + 6\]
\[\Leftrightarrow 6x - 2 = 4x + 6
  \qquad \text{(distributivité)}\]
\[\Leftrightarrow 6x - 4x = 6 + 2
  \qquad \text{(on regroupe les termes semblables)}\]
\[\Leftrightarrow 2x = 8\]
\[\Leftrightarrow x = 4
  \qquad \text{(on divise par $2$, $2 > 0$)}\]
Donc $S = \{4\}$.
\end{Solution}
```

### Exemple 3 — Inéquation avec division par négatif
```latex
%% SOLUTION_APPLICATION
\begin{Solution}[Correction — Application X]
\textbf{Résoudre dans $\R$ :} $-4x + 1 \leq 2x - 11$

On a :
\[-4x + 1 \leq 2x - 11\]
\[\Leftrightarrow -4x - 2x \leq -11 - 1
  \qquad \text{(on regroupe les termes semblables)}\]
\[\Leftrightarrow -6x \leq -12\]
\[\Leftrightarrow x \geq 2
  \qquad \text{(on divise par $-6 < 0$,
  le sens de l'inégalité s'inverse)}\]
Donc $S = [2 \; ; \; +\infty[$.
\end{Solution}
```

### Exemple 4 — Équation avec fractions
```latex
%% SOLUTION_APPLICATION
\begin{Solution}[Correction — Application X]
\textbf{Résoudre dans $\R$ :}
$\dfrac{x+1}{3} - \dfrac{x-2}{2} = 1$

On a :
\[\frac{x+1}{3} - \frac{x-2}{2} = 1\]
\[\Leftrightarrow 2(x+1) - 3(x-2) = 6
  \qquad \text{(on multiplie par $6$, PPCM de $3$ et $2$)}\]
\[\Leftrightarrow 2x + 2 - 3x + 6 = 6
  \qquad \text{(distributivité)}\]
\[\Leftrightarrow -x + 8 = 6
  \qquad \text{(on regroupe les termes semblables)}\]
\[\Leftrightarrow -x = -2
  \qquad \text{(on soustrait $8$ des deux membres)}\]
\[\Leftrightarrow x = 2
  \qquad \text{(on multiplie par $-1$)}\]
Donc $S = \{2\}$.
\end{Solution}
```

### Exemple 5 — Taux de variation
```latex
%% SOLUTION_APPLICATION
\begin{Solution}[Correction — Application X]
Soient $a$ et $b$ deux réels distincts de $\R$.

On a :
\[
T(a\,;\,b) = \frac{f(b)-f(a)}{b-a}
= \frac{(2b^2+3)-(2a^2+3)}{b-a}
= \frac{2(b^2-a^2)}{b-a}
\]
\[
= \frac{2(b-a)(b+a)}{b-a}
\qquad \text{(factorisation)}
\]
\[
= 2(a+b)
\qquad \text{(simplification, $b-a \neq 0$)}
\]
D'où $T(a\,;\,b) = 2(a+b)$.
\end{Solution}
```

---

## VOCABULAIRE OFFICIEL MAROCAIN

| ✅ Correct | ❌ Incorrect |
|---|---|
| ensemble de définition | domaine |
| ensemble solution | solution générale |
| sens de l'inégalité | signe de l'inégalité |
| taux de variation | taux d'accroissement |
| membre gauche / droit | côté gauche / droit |
| strictement croissante | croissante strictement |
| ensemble de définition $D_f$ | domaine $D$ |
