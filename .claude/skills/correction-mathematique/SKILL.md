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

| Connecteur | Quand l'utiliser |
|---|---|
| `Puisque` | Raisonnement basé sur un fait connu (type de fonction, signe de Δ...) |
| `On a :` / `On a donc :` | Lancer un calcul ou rappeler une formule |
| `Soit $x \in ...$` | Introduire la variable pour une étude (parité, monotonie) |
| `\text{ équivaut à }` | Transformation dans un `align*` (remplace `\Leftrightarrow`) |
| `Donc :` | Conclure une sous-étape — suivi de `\quad` + résultat |
| `D'où :` | Conséquence directe d'un calcul |
| `Nous constatons que` | Observation intermédiaire (ex : $D_f = D_g$) |
| `Cherchons` | Annoncer une recherche d'intersection ou de valeurs |
| `Par conséquent` | Conclusion logique d'un raisonnement (ni paire ni impaire) |
| `\textbf{Conclusion :}` | Conclusion finale d'un bloc complet |

---

## RÈGLE 2 — Format d'une étape

Chaque sous-question commence par un titre `\textbf{}` à l'**infinitif** + deux-points.
Le développement utilise `align*` pour les chaînes de calcul, `\[...\]` pour les résultats isolés.

```latex
\item \textbf{Déterminons $D_f$ :}

Puisque [raisonnement].
\begin{align*}
    D_f &= \left\{ x \in \mathbb{R} \mid ... \right\} \\
        &= \left\{ x \in \mathbb{R} \mid ... \right\}
\end{align*}
Donc : \quad $D_f = ...$
```

Format d'un système de conditions (intervalles) :
```latex
\[
\begin{cases}
    \text{condition 1} \\
    \text{condition 2}
\end{cases} \quad \text{alors} \quad
\begin{cases}
    \text{...} \\
    \text{...}
\end{cases} \quad \text{donc} \quad
\begin{cases}
    \text{...} \\
    \text{...}
\end{cases}
\]
Donc, $a < x < b$. L'intervalle est : $D = \left] a ; b \right[$
```

---

## RÈGLE 3 — Justifications exactes à utiliser

| Situation | Justification à écrire |
|---|---|
| Fonction polynôme | `Puisque $f$ est une fonction polynôme, elle est définie sur $\mathbb{R}$ tout entier.` |
| Condition dénominateur | `\left\{ x \in \mathbb{R} \mid Q(x) \neq 0 \right\}` |
| Condition racine carrée | `\left\{ x \in \mathbb{R} \mid P(x) \geq 0 \right\}` |
| Transformation équivalente | `\text{ équivaut à }` dans `align*` |
| Parité utilisée | `(car la fonction $f$ est paire)` ou `(car la fonction $f$ est impaire)` |
| Discriminant | `Puisque $\Delta = ... > 0$, le trinôme admet deux racines réelles distinctes :` |
| Intersection de conditions | `Cherchons l'intersection des deux conditions :` |
| Constat d'égalité | `Nous constatons que les deux ensembles sont identiques :` |
| $D_f$ non symétrique | `$D_f$ n'est pas symétrique par rapport à $0$.` |

## RÈGLE SPÉCIALE — Taux de variation T(a;b)

Pour tout calcul de taux de variation, suivre OBLIGATOIREMENT
cet ordre en 3 étapes :

Étape 1 : Écrire la définition
\[T(a\,;\,b) = \frac{f(b) - f(a)}{b - a}\]

Étape 2 : Calculer et simplifier f(b) - f(a) séparément
\[f(b) - f(a) = ...\]
\[= ... \qquad \text{(simplification)}\]

Étape 3 : Diviser par (b-a) à la toute fin
\[T(a\,;\,b) = \frac{f(b)-f(a)}{b-a} = \frac{...}{b-a} = ...\]

Ne jamais tout mettre dans une seule fraction dès le départ.
Ne jamais diviser avant d'avoir simplifié f(b) - f(a).

---

## RÈGLE SPÉCIALE — Étude de la parité d'une fonction

Suivre OBLIGATOIREMENT cette structure en 2 étapes :

### Structure de la réponse

```latex
\begin{itemize}
    \item On a : $D_f = ...$, donc $D_f$ est symétrique 
    par rapport à $0$.
    \item Soit $x \in D_f$. On a :
    \[f(-x) = ... = ... = f(x)\]
    Donc pour tout $x$ de $D_f$, $f(-x) = f(x)$
    
    D'où $f$ est \textbf{paire}.
\end{itemize}
```

### Variantes selon le résultat

**Si f est paire :**
```latex
\begin{itemize}
    \item On a : $D_f = ...$, donc $D_f$ est symétrique 
    par rapport à $0$.
    \item Soit $x \in D_f$. On a :
    \[f(-x) = ... = f(x)\]
    Donc pour tout $x$ de $D_f$, $f(-x) = f(x)$
    
    D'où $f$ est \textbf{paire}.
\end{itemize}
```

**Si f est impaire :**
```latex
\begin{itemize}
    \item On a : $D_f = ...$, donc $D_f$ est symétrique 
    par rapport à $0$.
    \item Soit $x \in D_f$. On a :
    \[f(-x) = ... = -f(x)\]
    Donc pour tout $x$ de $D_f$, $f(-x) = -f(x)$
    
    D'où $f$ est \textbf{impaire}.
\end{itemize}
```

**Si f est ni paire ni impaire :**
```latex
\begin{itemize}
    \item On a : $D_f = ...$, donc $D_f$ n'est pas 
    symétrique par rapport à $0$.
    
    Par conséquent, $f$ n'est \textbf{ni paire ni impaire}.
\end{itemize}
```

### Exemple de référence extrait de source.tex

```latex
\begin{itemize}
    \item On a : $D_f = \mathbb{R}$, donc $D_f$ est 
    symétrique par rapport à $0$.
    \item Soit $x \in \mathbb{R}$. On a :
    \[f(-x) = (-x)^2 - 3|-x| + 2 = x^2 - 3|x| + 2 = f(x)\]
    Donc pour tout $x$ de $\mathbb{R}$, $f(-x) = f(x)$
    
    D'où $f$ est \textbf{paire}.
\end{itemize}
```

### Règles absolues pour la parité
- TOUJOURS commencer par vérifier la symétrie de $D_f$
- TOUJOURS écrire `Soit $x \in D_f$` avant le calcul
- TOUJOURS développer $f(-x)$ étape par étape
- TOUJOURS conclure avec `D'où $f$ est \textbf{paire/impaire}`
- Si $D_f$ non symétrique → conclure immédiatement sans calculer $f(-x)$
- Ne jamais conclure sans avoir vérifié $D_f$ d'abord

---

## RÈGLE 4 — Conclusions

| Type | Conclusion à écrire |
|---|---|
| Ensemble de définition | `Donc : \quad $D_f = ...$` |
| Résultat de calcul | `D'où : \quad $...$` |
| Fonction paire | `La fonction $f$ est \textbf{paire}.` |
| Fonction impaire | `Donc la fonction $f$ est \textbf{impaire}.` |
| Ni paire ni impaire | `Par conséquent, la fonction $f$ n'est \textbf{ni paire ni impaire}.` |
| Égalité de fonctions | `\textbf{Conclusion :}` puis `$f = g$` sur la ligne suivante |
| Règle pédagogique | `\textbf{Règle d'or :}` + phrase explicative |
| Surface / valeur numérique | `La surface est de $25\text{ cm}^2$ lorsque $x = 5\text{ cm}$.` |

---

## RÈGLE 5 — Ce qu'il ne faut JAMAIS écrire

- Sauter une étape même évidente
- `Il suffit de...` / `Clairement...` / `On trouve facilement...`
- Reformuler l'énoncé avant la correction
- Ajouter des commentaires pédagogiques non demandés
- Utiliser `\[\Leftrightarrow expression\]` en série — utiliser `align*` avec `&=` et `\text{ équivaut à }`
- Écrire les titres de sous-questions sans `\textbf{}` et sans infinitif
- Utiliser `\textwidth` dans les minipage — utiliser `\linewidth`

---

## EXEMPLES DE RÉFÉRENCE EXTRAITS DE source.tex

### Exemple 1 — Ensemble de définition (fraction)
```latex
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item $f\left( x \right) = \dfrac{x+1}{2x-8}$
    \begin{align*}
         D_f = \left\{ x \in \mathbb{R} \mid 2x - 8 \neq 0 \right\}
             = \left\{ x \in \mathbb{R} \mid 2x  \neq 8 \right\}
             = \left\{ x \in \mathbb{R} \mid x  \neq 4 \right\}
    \end{align*}
    \[ D_f = \mathbb{R} \setminus \left\{ 4 \right\} = \left] -\infty ; 4 \right[ \cup \left] 4 ; +\infty \right[ \]
\end{enumerate}
\end{Solution}
```

### Exemple 2 — Ensemble de définition (fraction sous racine + tableau de signe)
```latex
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item $f\left( x \right) = \sqrt{\dfrac{x-3}{x+1}}$
    \[ D_f = \left\{ x \in \mathbb{R} \mid \dfrac{x-3}{x+1} \geq 0 \quad \text{et} \quad x + 1 \neq 0 \right\} \]
    \begin{itemize}
        \item $x - 3 = 0$ équivaut à $x = 3$
        \item $x + 1 = 0$ équivaut à $x = -1$
    \end{itemize}
    Dressons le tableau de signe de $\dfrac{x-3}{x+1}$ :
    \vspace{0.1cm}
\begin{center}
\begin{tikzpicture}
    \tkzTabInit[lgt=1.5, espcl=2]{$x$ / 0.6 , $x - 3$ / 0.7 , $x + 1$ / 0.7 , $\dfrac{x-3}{x+1}$ / 1}{$-\infty$, $-1$, $3$, $+\infty$}
    \tkzTabLine{ , -, t, -, z, +, }
    \tkzTabLine{ , -, z, +, t, +, }
    \tkzTabLine{ , +, d, -, z, +, }
\end{tikzpicture}
\end{center}
    \[ D_f = \left] -\infty ; -1 \right[ \cup \left[ 3 ; +\infty \right[ \]
    \textbf{Règle d'or :} Il faut toujours chercher l'ensemble de définition sur l'expression de départ, sans jamais la simplifier ni la transformer !
\end{enumerate}
\end{Solution}
```

### Exemple 3 — Égalité de deux fonctions
```latex
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{itemize}
    \item \textbf{Déterminons $D_f$ :}
     $f\left( x \right) = \dfrac{1}{\sqrt{x}-2}$
     \begin{align*}
        D_f &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad \sqrt{x} - 2 \neq 0  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad \sqrt{x}\neq 2  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x \neq 4  \right\}
    \end{align*}
     Donc : \quad $D_f = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[$

    \item \textbf{Déterminons $D_g$ :}
     $g\left( x \right) = \dfrac{\sqrt{x}+2}{x-4}$
    \begin{align*}
        D_g &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x - 4 \neq 0 \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x \neq 4 \right\}
    \end{align*}
  Donc : \quad $D_g = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[$

   Nous constatons que les deux ensembles sont identiques :
\[ D_f = D_g = \mathbb{R}^+ \setminus \left\{ 4 \right\} = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[ \]

\item Soit $x$ de $D_f$. Calculons $f\left( x \right)$ :
\begin{align*}
    f\left( x \right) &= \dfrac{1}{\sqrt{x}-2}
    = \dfrac{\left( \sqrt{x} + 2 \right)}{\left( \sqrt{x} - 2 \right)\left( \sqrt{x} + 2 \right)} = \dfrac{\sqrt{x} + 2}{x - 4} = g(x)
\end{align*}
\textbf{Conclusion :}
Puisque $D_f = D_g$ et pour tout $x$ de $D_f$, $f\left( x \right) = g\left( x \right)$, alors :
    $f = g$
\end{itemize}
\end{Solution}
```

### Exemple 4 — Parité (étude complète)
```latex
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Étude de la fonction $f\left( x \right) = 2x^3 - 5x$}

    On a : ~ $D_f = \mathbb{R}$ \quad (fonction polynôme)

    Soit $x \in \mathbb{R}$.
    \begin{align*}
        f\left( -x \right) = 2\left( -x \right)^3 - 5\left( -x \right)
         = -2x^3 + 5x
         &= -\left( 2x^3 - 5x \right) \\
        &= -f\left( x \right)
    \end{align*}

        Donc la fonction $f$ est \textbf{impaire}.

    \item \textbf{Étude de la fonction $f\left( x \right) = \sqrt{x - 1}$}

     On a : ~ $D_f = \left\{ x \in \mathbb{R} \mid x \geq 1 \right\}$

    L'ensemble de définition est donc : $D_f = \left[ 1 ; +\infty \right[$

    $D_f$ n'est pas symétrique par rapport à $0$. \\
    Par conséquent, la fonction $f$ n'est \textbf{ni paire ni impaire}.
\end{enumerate}
\end{Solution}
```

### Exemple 5 — Activité avec système de conditions
```latex
%% SOLUTION_ACTIVITE
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons l'intervalle $D$ auquel doit appartenir $x$ :}

    Pour que le rectangle existe, les longueurs $x$ et $y$ doivent être strictement positives :
    \[
\begin{cases}
    x > 0 \\
    y > 0
\end{cases} \quad \text{alors} \quad
\begin{cases}
    x > 0 \\
    10 - x > 0
\end{cases} \quad \text{donc} \quad
\begin{cases}
    x > 0 \\
    x < 10
\end{cases}
\]
    Donc, $0 < x < 10$. L'intervalle est : $D = \left] 0 ; 10 \right[$

    \item \textbf{Montrons que la surface $S(x) = 10x - x^2$ :}

    La surface d'un rectangle est donnée par la formule :
    $$S = \text{longueur} \times \text{largeur}$$
    On a donc :
    $S\left( x \right) = x \times \left( 10 - x \right) = 10x - x^2$
\end{enumerate}
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
