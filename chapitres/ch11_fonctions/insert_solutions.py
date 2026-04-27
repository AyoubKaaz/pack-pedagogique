#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insert 9 solution blocks into source.tex at the correct positions."""

import sys

SRC = r'C:\Users\Ayyoub kaazouzi\pack-pedagogique-v5.0\pack-pedagogique\chapitres\ch11_fonctions\source.tex'

with open(SRC, 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# ─────────────────────────────────────────────
# BLOCK 1 — Solution Activité 1 (fil de fer)
# inserted after \end{Activite} of section 1
# ─────────────────────────────────────────────
SOL1 = r"""%% SOLUTION_ACTIVITE
\begin{Solution}
\begin{enumerate}
    \item \textbf{Exprimons la largeur $y$ en fonction de $x$ :}

    Le périmètre du rectangle est égal à la longueur totale du fil, soit $20\text{ cm}$.
    Le périmètre est : $2x + 2y = 20$.

    Donc : $x + y = 10$

    D'où :   $y = 10 - x$


    \item \textbf{Déterminons l'intervalle $D$ auquel doit appartenir $x$ :}

    Pour que le rectangle existe, les longueurs $x$  et $y$ doivent être strictement positives :
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
    Donc,  $0<x<10$ . L'intervalle est : $D = \left] 0 ; 10 \right[$


    \item \textbf{Montrons que la surface $S(x) = 10x - x^2$ :}

    La surface d'un rectangle est donnée par la formule :
    $$S = \text{longueur} \times \text{largeur}$$
    On a donc :
    $ S\left( x \right) = x \times \left( 10 - x \right) = 10x - x^2$

    \item \textbf{Calculons la surface pour $x = 2$ et $x = 8$ :}

    \begin{itemize}
        \item Pour $x = 2$ :
         $S\left( 2 \right) = 10 \times 2 - 2^2 = 20 - 4 = 16\text{ cm}^2 $
        \item Pour $x = 8$ :
        $S\left( 8 \right) = 10 \times 8 - 8^2 = 80 - 64 = 16\text{ cm}^2$
    \end{itemize}
    On remarque que deux longueurs différentes peuvent donner la même surface.

    \item \textbf{Déterminons $x$ pour que la surface soit égale à $25\text{ cm}^2$ :}

    Résolvons l'équation $S\left( x \right) = 25$ :
   \begin{align*}
    S\left( x \right) = 25 \quad \text{ équivaut à } \qquad 10x - x^2 &= 25 \\
     x^2 - 10x + 25 &= 0 \\
     \left( x - 5 \right)^2 &= 0 \\
     x - 5 &= 0 \\
     x &= 5
    \end{align*}
        La surface est de $25\text{ cm}^2$ lorsque $x = 5\text{ cm}$.
\end{enumerate}
\end{Solution}

"""

OLD1 = r"""\end{Activite}

%% DEFINITION
\begin{Definition}[Fonction numérique][]"""

NEW1 = r"""\end{Activite}

""" + SOL1 + r"""%% DEFINITION
\begin{Definition}[Fonction numérique][]"""

assert OLD1 in content, "ANCHOR 1 NOT FOUND"
content = content.replace(OLD1, NEW1, 1)

# ─────────────────────────────────────────────
# BLOCK 2 — Solution Application 1 (8 ensembles)
# inserted after \end{Application} before %% TECHNIQUES
# ─────────────────────────────────────────────
SOL2 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}

    \item $f\left( x \right) = x^2 - 2x + 1$

    Puisque $f$ est une fonction polynôme, elle est définie sur $\mathbb{R}$ tout entier.
    \[ D_f = \mathbb{R} = \left] -\infty ; +\infty \right[ \]

    \item  $f\left( x \right) = \dfrac{x+1}{2x-8}$
    \begin{align*}
         D_f = \left\{ x \in \mathbb{R} \mid 2x - 8 \neq 0 \right\}
             = \left\{ x \in \mathbb{R} \mid 2x  \neq 8 \right\}
             = \left\{ x \in \mathbb{R} \mid x  \neq 4 \right\}
    \end{align*}
    \[ D_f = \mathbb{R} \setminus \left\{ 4 \right\} = \left] -\infty ; 4 \right[ \cup \left] 4 ; +\infty \right[ \]

    \item  $f\left( x \right) = \sqrt{2-x}$
    \begin{align*}
        D_f = \left\{ x \in \mathbb{R} \mid 2 - x \geq 0 \right\}
         = \left\{ x \in \mathbb{R} \mid  - x \geq -2 \right\}
         = \left\{ x \in \mathbb{R} \mid x \leq 2 \right\}
    \end{align*}
    \[ D_f = \left] -\infty ; 2 \right] \]

    \item $f\left( x \right) = \sqrt{x^2 - 5x + 6}$
    \[ D_f = \left\{ x \in \mathbb{R} \mid x^2 - 5x + 6 \geq 0 \right\} \]
    Étudions le signe du trinôme $x^2 - 5x + 6$

    Puisque $\Delta = 1 > 0$, le trinôme admet deux racines réelles distinctes :
    \begin{align*}
        x_1 &= \dfrac{-\left( -5 \right) - \sqrt{1}}{2 \times 1} = \dfrac{5 - 1}{2} = 2 \\
        x_2 &= \dfrac{-\left( -5 \right) + \sqrt{1}}{2 \times 1} = \dfrac{5 + 1}{2} = 3
    \end{align*}

\begin{center}
    \begin{tikzpicture}
    \tkzTabInit[lgt=2, espcl=1.6]{$x$ / 0.5 , $x^2 - 5x + 6$ / 1}{$-\infty$, $2$, $3$, $+\infty$}
    \tkzTabLine{ , +, z, -, z, +, }
\end{tikzpicture}
\end{center}

    \[ D_f = \left] -\infty ; 2 \right] \cup \left[ 3 ; +\infty \right[ \]

    \item  $f\left( x \right) = \dfrac{\sqrt{x}}{x^2 - 2x + 1}$
    \begin{align*}
        D_f &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x^2 - 2x + 1 \neq 0  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad (x-1)^2 \neq 0  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x-1 \neq 0  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x \neq 1  \right\}
    \end{align*}
    L'ensemble de définition est donc :
    $D_f = \left[ 0 ; 1 \right[ \cup \left] 1 ; +\infty \right[$

    \item $f\left( x \right) = \dfrac{x+4}{|x| - 3}$
    \[ D_f = \left\{ x \in \mathbb{R} \mid |x| - 3 \neq 0 \right\} \]
    \begin{align*}
        |x| - 3 = 0 &\text{ équivaut à } |x| = 3 \\
        &\text{ équivaut à } x = 3 \text{ ou } x = -3
    \end{align*}
    \[ D_f = \mathbb{R} \setminus \left\{ -3 ; 3 \right\} = \left] -\infty ; -3 \right[ \cup \left] -3 ; 3 \right[ \cup \left] 3 ; +\infty \right[ \]

    \item $f\left( x \right) = \dfrac{\sqrt{x-3}}{\sqrt{x+1}}$


    \[ D_f = \left\{ x \in \mathbb{R} \mid  x - 3 \geq 0 \quad \text{et} \quad x + 1 > 0 \right\} \]
    Cherchons l'intersection des deux conditions :
    \begin{align*}
        \begin{cases} x - 3 \geq 0 \\ x + 1 > 0 \end{cases} &\text{ équivaut à } \begin{cases} x \geq 3 \\ x > -1 \end{cases} ~~
        \text{ équivaut à } ~~ x \geq 3
    \end{align*}
    Donc : \qquad
     $D_f = \left[ 3 ; +\infty \right[$

    \item  $f\left( x \right) = \sqrt{\dfrac{x-3}{x+1}}$
    \[ D_f = \left\{ x \in \mathbb{R} \mid \dfrac{x-3}{x+1} \geq 0 \quad \text{et} \quad x + 1 \neq 0  \right\} \]
    \begin{itemize}
        \item $x - 3 = 0$ équivaut à $x = 3$
        \item $x + 1 = 0$ équivaut à $x = -1$
    \end{itemize}
    Dressons le tableau de signe de $\dfrac{x-3}{x+1}$:
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

"""

OLD2 = r"""\end{Application}

%% TECHNIQUES"""

NEW2 = r"""\end{Application}

""" + SOL2 + r"""%% TECHNIQUES"""

assert OLD2 in content, "ANCHOR 2 NOT FOUND"
content = content.replace(OLD2, NEW2, 1)

# ─────────────────────────────────────────────
# BLOCK 3 — Solution Application 2 (f=g)
# inserted after \end{Application} before %% SECTION Représentation
# ─────────────────────────────────────────────
SOL3 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\begin{itemize}
    \item \textbf{Déterminons $D_f$ :}
     $f\left( x \right) = \dfrac{1}{\sqrt{x}-2}$
     \begin{align*}
        D_f &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad \sqrt{x} - 2 \neq 0  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad \sqrt{x}\neq 2  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad \left( \sqrt{x} \right)^2 \neq 2^2  \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x \neq 4  \right\}
    \end{align*}
     Donc : \quad $D_f = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[$

    \item \textbf{Déterminons $D_g$ :}
     $g\left( x \right) = \dfrac{\sqrt{x}+2}{x-4}$
    \begin{align*}
        D_g &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x - 4 \neq 0 \right\} \\
         &= \left\{ x \in \mathbb{R} \mid  x \geq 0 \quad \text{et} \quad x \neq 4 \right\}
    \end{align*}
  Donc : \quad   $D_g = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[ $

   Nous constatons que les deux ensembles sont identiques :
\[ D_f = D_g = \mathbb{R}^+ \setminus \left\{ 4 \right\} = \left[ 0 ; 4 \right[ \cup \left] 4 ; +\infty \right[ \]

\item Soit $x$ de $D_f$. Calculons $f\left( x \right)$ :
\begin{align*}
    f\left( x \right) &= \dfrac{1}{\sqrt{x}-2}
    = \dfrac{\left( \sqrt{x} + 2 \right)}{\left( \sqrt{x} - 2 \right)\left( \sqrt{x} + 2 \right)} = \dfrac{\sqrt{x} + 2}{x - 4} =g(x)
\end{align*}
\textbf{Conclusion :}
Puisque $D_f = D_g$ et pour tout $x$ de $D_f$, $f\left( x \right) = g\left( x \right)$, Alors  :
    $f = g$
\end{itemize}
\end{Solution}

"""

OLD3 = r"""\end{Application}


%% SECTION
\section{Représentation graphique"""

NEW3 = r"""\end{Application}

""" + SOL3 + r"""%% SECTION
\section{Représentation graphique"""

assert OLD3 in content, "ANCHOR 3 NOT FOUND"
content = content.replace(OLD3, NEW3, 1)

# ─────────────────────────────────────────────
# BLOCK 4 — Solution Application 3 (points sur Cf)
# inserted after \end{Application} before %% SECTION Parité
# ─────────────────────────────────────────────
SOL4 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
On a: \quad $f\left( x \right) = \dfrac{x^2}{x+1}$ avec $D_f = \mathbb{R} \setminus \left\{ -1 \right\}$

\begin{itemize}
    \item On a $f\left( 0 \right) = 0$ donc le point $A\left( 0 ; 0 \right) \in \left( \mathcal{C}_f \right)$
    \item On a $-1 \notin D_f$ donc le point $B\left( -1 ; 1 \right) \notin \left( \mathcal{C}_f \right)$
    \item On a $f\left( 3 \right) = \dfrac{9}{4}$ donc le point $C\left( 3 ; \dfrac{9}{4} \right) \in \left( \mathcal{C}_f \right)$
    \item On a $f\left( 2 \right) = \dfrac{4}{3} \neq 4$ donc le point $D\left( 2 ; 4 \right) \notin \left( \mathcal{C}_f \right)$
\end{itemize}
\end{Solution}

"""

OLD4 = r"""\end{Application}


%% SECTION
\section{Parité"""

NEW4 = r"""\end{Application}

""" + SOL4 + r"""%% SECTION
\section{Parité"""

assert OLD4 in content, "ANCHOR 4 NOT FOUND"
content = content.replace(OLD4, NEW4, 1)

# ─────────────────────────────────────────────
# BLOCK 5 — Solution Activité 2 (parité f=3x², g=x³)
# inserted after \end{Activite} before %% DEFINITION (parité)
# ─────────────────────────────────────────────
SOL5 = r"""%% SOLUTION_ACTIVITE
\begin{Solution}
\begin{enumerate}
    \item \textbf{a) Vérifions que pour tout $x \in D_f$, $f\left( -x \right) = f\left( x \right)$ :}
    \begin{align*}
        f\left( -x \right) &= 3 \times \left( -x \right)^2
        = 3 \times x^2 =f(x)
    \end{align*}
    \item \textbf{b) Propriété géométrique vérifiée par $\mathscr{C}_f$ :}

    La propriété géométrique est que l'axe des ordonnées est un \textbf{axe de symétrie} pour la courbe $\mathscr{C}_f$.
\end{enumerate}

\begin{enumerate}
    \item \textbf{a) Vérifions que pour tout $x \in D_g$, $g\left( -x \right) = -g\left( x \right)$ :}
    \begin{align*}
        g\left( -x \right) &= \left( -x \right)^3
        = -x^3 = -g(x)
    \end{align*}
    \item \textbf{b) Propriété géométrique vérifiée par $\mathscr{C}_g$ :}

        La propriété géométrique est que l'origine du repère (le point $O$) est un \textbf{centre de symétrie} pour la courbe $\mathscr{C}_g$.
\end{enumerate}
\end{Solution}

"""

OLD5 = r"""\end{Activite}

%% DEFINITION
\begin{Definition}[][]
Soit $f$ une fonction et $D_f$ son ensemble de définition."""

NEW5 = r"""\end{Activite}

""" + SOL5 + r"""%% DEFINITION
\begin{Definition}[][]
Soit $f$ une fonction et $D_f$ son ensemble de définition."""

assert OLD5 in content, "ANCHOR 5 NOT FOUND"
content = content.replace(OLD5, NEW5, 1)

# ─────────────────────────────────────────────
# BLOCK 6 — Solution Application 4 (parité 3 cas)
# inserted after \end{Application} before Application x²+x
# ─────────────────────────────────────────────
SOL6 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Étude de la fonction $f\left( x \right) = x^2 - 3|x| + 2$}

    On a :  $D_f = \mathbb{R}$

    L'ensemble $\mathbb{R}$ est symétrique par rapport à $0$.

    Soit $x \in \mathbb{R}$.
    \begin{align*}
         f\left( -x \right) = \left( -x \right)^2 - 3|-x| + 2
                            = x^2 - 3|x| + 2
    \end{align*}

         La fonction $f$ est \textbf{paire}.

    \vspace{0.5cm}

    \item \textbf{Étude de la fonction $f\left( x \right) = 2x^3 - 5x$}

    \textbf{Étape 1 : Ensemble de définition}

    On a : ~ $D_f = \mathbb{R}$ \quad (fonction polynôme)


    Soit $x \in \mathbb{R}$.
    \begin{align*}
        f\left( -x \right) = 2\left( -x \right)^3 - 5\left( -x \right)
         = -2x^3 + 5x
         &= -\left( 2x^3 - 5x \right) \\
        &= -f\left( x \right)
    \end{align*}

        Donc la fonction $f$ est \textbf{impaire}.

    \vspace{0.5cm}

    \item \textbf{Étude de la fonction $f\left( x \right) = \sqrt{x - 1}$}

     On a : ~ $D_f = \left\{ x \in \mathbb{R} \mid x - 1 \geq 0 \right\}=
     \left\{ x \in \mathbb{R} \mid x  \geq 1 \right\}$

    L'ensemble de définition est donc : $D_f = \left[ 1 ; +\infty \right[$

    $D_f$ n'est pas symétrique par rapport à $0$. \\
    Par conséquent, la fonction $f$ n'est \textbf{ni paire ni impaire}.

\end{enumerate}
\end{Solution}

"""

OLD6 = r"""\end{Application}

%% APPLICATION
\begin{Application}[][10 min]
Soit $f$ la fonction définie par : $f(x) = x^2 + x$"""

NEW6 = r"""\end{Application}

""" + SOL6 + r"""%% APPLICATION
\begin{Application}[][10 min]
Soit $f$ la fonction définie par : $f(x) = x^2 + x$"""

assert OLD6 in content, "ANCHOR 6 NOT FOUND"
content = content.replace(OLD6, NEW6, 1)

# ─────────────────────────────────────────────
# BLOCK 7 — Solution Application 5 (x²+x ni paire ni impaire)
# inserted after \end{Application} before %% PROPRIETE
# ─────────────────────────────────────────────
SOL7 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}

    % Question 1
    \item \textbf{Calculons $f\left(1\right)$ et $f\left(-1\right)$}
    \begin{itemize}
        \item $f\left(1\right) = \left(1\right)^2 + \left(1\right)
     = 1 + 1 \
     = 2$
        \item $f\left(-1\right) = \left(-1\right)^2 + \left(-1\right)
     = 1 - 1
     = 0$
    \end{itemize}

    % Question 2
    \item \textbf{Déduisons que $f$ n'est ni paire, ni impaire}

    \begin{itemize}
        \item on a trouvé $f\left(-1\right) = 0$ et $f\left(1\right) = 2$.
        Puisque $0 \neq 2$,

        nous remarquons que :
        $f\left(-1\right) \neq f\left(1\right)$

        La fonction n'est donc pas paire.

        \item  nous remarquons que :
        $f\left(-1\right) \neq -f\left(1\right)$

        La fonction n'est donc pas impaire.
    \end{itemize}

    Conclusion : La fonction $f$ n'est ni paire, ni impaire.

\end{enumerate}
\end{Solution}

"""

OLD7 = r"""\end{Application}

%% PROPRIETE
\begin{Propriete}"""

NEW7 = r"""\end{Application}

""" + SOL7 + r"""%% PROPRIETE
\begin{Propriete}"""

assert OLD7 in content, "ANCHOR 7 NOT FOUND"
content = content.replace(OLD7, NEW7, 1)

# ─────────────────────────────────────────────
# BLOCK 8 — Solution Application 6 (fonction paire, courbe)
# inserted after \end{Application} before Application impaire
# ─────────────────────────────────────────────
SOL8 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\noindent
\begin{enumerate}

    % Question 1
    \item \textbf{Complétons la construction de la courbe $\left(C_f\right)$}

Pour compléter le tracé sur tout l'intervalle $\left[-6 ; 6\right]$, nous allons utiliser la symétrie par rapport à l'axe des ordonnées.


    Voici la courbe complétée (les tracés ajoutés sont en bleu pour bien les repérer) :

    \begin{center}
    \begin{tikzpicture}[x=0.72cm, y=0.72cm]
        % Grille de fond
        \draw[black!12, step=1, solid] (-6.5,-2.5) grid (6.5,3.5);

        % Axes principaux
        \draw[->, >=stealth, thick, black] (-6.5,0) -- (6.5,0) node[below right, font=\small\sffamily] {$x$};
        \draw[->, >=stealth, thick, black] (0,-2.5) -- (0,3.5) node[left, font=\small\sffamily] {$y$};

        % Graduations axe X
        \foreach \x in {-6,-5,-4,-3,-2,-1,1,2,3,4,5,6} {
            \draw[black] (\x, 0.08) -- (\x, -0.08);
        }
        \node[below, font=\small\sffamily] at (-6, -0.15) {$-6$};
        \node[below, font=\small\sffamily] at (-5, -0.15) {$-5$};
        \node[above left, font=\small\sffamily] at (-2,  0.1) {$-2$};
        \node[above right, font=\small\sffamily] at ( 2,  0.1) {$2$};
        \node[below, font=\small\sffamily] at ( 6, -0.15) {$6$};
        \node[below left, font=\small\sffamily] at (0, 0) {$O$};

        % Graduations axe Y
        \foreach \y in {-1,1,2,3} {
            \draw[black] (0.08, \y) -- (-0.08, \y);
        }
        \node[right, font=\small\sffamily] at (0.12, -1) {$-1$};
        \node[right, font=\small\sffamily] at (0.12,  1) {$1$};
        \node[right, font=\small\sffamily] at (0.12,  2) {$2$};
        \node[right, font=\small\sffamily] at (0.12,  3) {$3$};

        % Tracés donnés par l'énoncé (en noir épais)
        \draw[very thick, black] (-6, 3) -- (-2, -1);
        \draw[very thick, black] (0, 2) -- (2, -1);

        % Tracés complétés par symétrie (en bleu)
        \draw[very thick, blue] (0, 2) -- (-2, -1);
        \draw[very thick, blue] (6, 3) -- (2, -1);

        % Points remarquables
        \filldraw[black] (-6,  3) circle (2pt);
        \filldraw[black] (-2, -1) circle (2pt);
        \filldraw[black] ( 0,  2) circle (2pt);
        \filldraw[black] ( 2, -1) circle (2pt);
        \filldraw[blue]  ( 6,  3) circle (2pt);

        % Label courbe
        \node[right, font=\small\sffamily\itshape, color=blue] at (4.2, 2.2) {$\left(C_f\right)$};
    \end{tikzpicture}
    \end{center}

    \vspace{0.3cm}

    % Question 2
    \item \textbf{Déterminons $f\left(6\right)$}

     Puisque  $f$ est paire, donc : $f\left(6\right) = f\left(-6\right)$
    et $f\left(-6\right) = 3$

    D'où : $f\left(6\right)=0$

    % Question 3
    \item \textbf{Calculons $f\left(-3\right)$ et $f\left(3\right)$}

    Utilisons la parité de $f$ pour trouver $f\left(3\right)$.

    On a :  $f\left(3\right) = f\left(-3\right)$.

    Donc : $f\left(-3\right) = 0 \quad \text{et} \quad f\left(3\right) = 0$

\end{enumerate}
\end{Solution}

"""

OLD8 = r"""\end{Application}

%% APPLICATION
\begin{Application}[][10 min]
\noindent
\begin{minipage}[t]{0.55\linewidth}
\vspace{0pt}
Soit $f$ une fonction impaire"""

NEW8 = r"""\end{Application}

""" + SOL8 + r"""%% APPLICATION
\begin{Application}[][10 min]
\noindent
\begin{minipage}[t]{0.55\linewidth}
\vspace{0pt}
Soit $f$ une fonction impaire"""

assert OLD8 in content, "ANCHOR 8 NOT FOUND"
content = content.replace(OLD8, NEW8, 1)

# ─────────────────────────────────────────────
# BLOCK 9 — Solution Application 7 (fonction impaire, courbe)
# inserted after \end{Application} before %% SECTION Variations
# ─────────────────────────────────────────────
SOL9 = r"""%% SOLUTION_APPLICATION
\begin{Solution}
\noindent

\begin{enumerate}

    % Question 1
    \item \textbf{Complétons le tracé de $\left(C_f\right)$}

     La fonction $f$ est impaire, donc sa courbe est symétrique par rapport à l'origine $O$. Pour tracer la partie manquante sur l'intervalle $\left[1 ; 4\right]$, nous allons utiliser la symétrie centrale.
    \begin{itemize}
        \item Le point $\left(-4 ; 0\right)$ a pour symétrique $\left(4 ; 0\right)$.
        \item Le point $\left(-2 ; 3\right)$ a pour symétrique $\left(2 ; -3\right)$.
        \item Le point $\left(-1 ; 1\right)$ a pour symétrique $\left(1 ; -1\right)$.
    \end{itemize}
    \begin{center}
    \begin{tikzpicture}[x=0.72cm, y=0.72cm]
        % Grille étendue pour inclure la partie négative
        \draw[black!12, step=1, solid] (-4.8,-3.8) grid (4.8,4.5);

        % Axes principaux
        \draw[->, >=stealth, thick, black] (-5,0) -- (5,0) node[below right, font=\small\sffamily] {$x$};
        \draw[->, >=stealth, thick, black] (0,-4) -- (0,4.5) node[right, font=\small\sffamily] {$y$};

        % Graduations X
        \foreach \x in {-4,-3,-2,-1,1,2,3,4} {
            \draw[black] (\x, 0.08) -- (\x, -0.08);
        }
        \node[above left,  font=\small\sffamily] at (-4, 0) {$-4$};
        \node[above right, font=\small\sffamily] at (-2, 0) {$-2$};
        \node[above right, font=\small\sffamily] at (-1, 0) {$-1$};
        \node[above right, font=\small\sffamily] at ( 1, 0) {$1$};
        \node[above right, font=\small\sffamily] at ( 2, 0) {$2$};
        \node[below right, font=\small\sffamily] at ( 4, 0) {$4$};
        \node[below left,  font=\small\sffamily] at ( 0, 0) {$O$};

        % Graduations Y
        \foreach \y in {-3,-2,-1,1,2,3,4} {
            \draw[black] (0.08, \y) -- (-0.08, \y);
        }
        \node[left, font=\small\sffamily] at (0,  4) {$4$};
        \node[left, font=\small\sffamily] at (0,  3) {$3$};
        \node[left, font=\small\sffamily] at (0,  1) {$1$};
        \node[left, font=\small\sffamily] at (0, -1) {$-1$};
        \node[left, font=\small\sffamily] at (0, -3) {$-3$};

        % Courbe donnée (en noir épais)
        \draw[very thick, black] (-4, 0) -- (-2, 3) -- (-1, 1);

        % Points donnés
        \filldraw[black] (-4, 0) circle (2pt);
        \filldraw[black] (-2,  3) circle (2pt);
        \filldraw[black] (-1,  1) circle (2pt);

        % Partie complétée par symétrie (en bleu)
        \draw[very thick, blue] (1, -1) -- (2, -3) -- (4, 0);

        % Points complétés
        \filldraw[blue] (1, -1) circle (2pt);
        \filldraw[blue] (2, -3) circle (2pt);
        \filldraw[blue] (4,  0) circle (2pt);

        % Labels
        \node[right, font=\small\sffamily\itshape, color=black] at (-3.8, 1.5) {$\left(C_f\right)$};
        \node[right, font=\small\sffamily\itshape, color=blue] at (2.2, -1.5) {$\left(C_f\right)$};
    \end{tikzpicture}
    \end{center}

    \vspace{0.3cm}

    % Question 2
    \item \textbf{Déterminons $f\left(4\right)$ et $f\left(2\right)$}

    On a :
    $f\left(4\right) = -f\left(-4\right) \qquad \text{(car la fonction $f$ est impaire)}$

    et $f\left(-4\right) = 0$ \qquad
    Donc : $f\left(4\right) = -0 = 0$

    On a :
    $f\left(2\right) = -f\left(-2\right) \qquad \text{(car la fonction $f$ est impaire)}$

   et $f\left(-2\right) = 3$
    Donc :   $f\left(2\right) = -3$

\end{enumerate}
\end{Solution}

"""

OLD9 = r"""\end{Application}


%% SECTION
\section{Variations d'une fonction"""

NEW9 = r"""\end{Application}

""" + SOL9 + r"""%% SECTION
\section{Variations d'une fonction"""

assert OLD9 in content, "ANCHOR 9 NOT FOUND"
content = content.replace(OLD9, NEW9, 1)

# ─────────────────────────────────────────────
# Write result
# ─────────────────────────────────────────────
with open(SRC, 'w', encoding='utf-8') as f:
    f.write(content)

new_len = len(content)
print(f"Done. File size: {original_len} → {new_len} chars (+{new_len - original_len})")
