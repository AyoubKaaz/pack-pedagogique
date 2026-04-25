import sys
import os

file_path = r"C:\Users\Ayyoub kaazouzi\pack-pedagogique-v5.0\pack-pedagogique\chapitres\ch11_fonctions\source.tex"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original = content  # sauvegarde

# ============================================================
# SOLUTION Application 13 — f(x) = x² - 6x + 7
# ============================================================
SOL13 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Vérifions que $f(x) \geq -2$ pour tout $x \in \mathbb{R}$ :}

    On a :
    \begin{align*}
        f(x) - (-2) &= x^2 - 6x + 7 + 2 \\
                    &= x^2 - 6x + 9 \\
                    &= (x - 3)^2
    \end{align*}
    Puisque $(x-3)^2 \geq 0$ pour tout $x \in \mathbb{R}$, on a $f(x) - (-2) \geq 0$.

    D'où : \quad $f(x) \geq -2$ pour tout $x \in \mathbb{R}$.

    \item \textbf{Calculons $f(3)$ :}

    \[ f(3) = 3^2 - 6 \times 3 + 7 = 9 - 18 + 7 = -2 \]

    \textbf{Conclusion :}
    Puisque $f(x) \geq -2$ pour tout $x \in \mathbb{R}$ et $f(3) = -2$, le nombre $-2$ est bien le \textbf{minimum} de $f$ sur $\mathbb{R}$.
\end{enumerate}
\end{Solution}

"""

ANCHOR13 = (
    "    \\item Calculer $f(3)$, puis en déduire que $-2$ est le minimum de $f$ sur $\\mathbb{R}$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW13 = ANCHOR13 + SOL13

if ANCHOR13 in content:
    content = content.replace(ANCHOR13, NEW13, 1)
    print("OK App 13")
else:
    print("ERREUR App 13 — ancre introuvable")

# ============================================================
# SOLUTION Application 14 — f(x) = -2x² + 4x + 3
# ============================================================
SOL14 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Montrons que $f(x) \leq 5$ pour tout $x \in \mathbb{R}$ :}

    On a :
    \begin{align*}
        5 - f(x) &= 5 - (-2x^2 + 4x + 3) \\
                 &= 5 + 2x^2 - 4x - 3 \\
                 &= 2x^2 - 4x + 2 \\
                 &= 2(x^2 - 2x + 1) \\
                 &= 2(x - 1)^2
    \end{align*}
    Puisque $2(x-1)^2 \geq 0$ pour tout $x \in \mathbb{R}$, on a $5 - f(x) \geq 0$.

    D'où : \quad $f(x) \leq 5$ pour tout $x \in \mathbb{R}$.

    \item \textbf{Calculons $f(1)$ :}

    \[ f(1) = -2(1)^2 + 4(1) + 3 = -2 + 4 + 3 = 5 \]

    \textbf{Conclusion :}
    Puisque $f(x) \leq 5$ pour tout $x \in \mathbb{R}$ et $f(1) = 5$, le nombre $5$ est bien le \textbf{maximum} de $f$ sur $\mathbb{R}$.
\end{enumerate}
\end{Solution}

"""

ANCHOR14 = (
    "    \\item Calculer $f(1)$, puis en déduire que $5$ est le maximum de $f$ sur $\\mathbb{R}$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW14 = ANCHOR14 + SOL14

if ANCHOR14 in content:
    content = content.replace(ANCHOR14, NEW14, 1)
    print("OK App 14")
else:
    print("ERREUR App 14 — ancre introuvable")

# ============================================================
# SOLUTION Application 15 — f(x) = x + 4/x
# ============================================================
SOL15 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Montrons que $4$ est le minimum de $f$ sur $]0 ; +\infty[$ :}

    Pour tout $x \in \left]0 ; +\infty\right[$, on a :
    \begin{align*}
        f(x) - 4 &= x + \dfrac{4}{x} - 4 \\[4pt]
                 &= \dfrac{x^2 - 4x + 4}{x} \\[4pt]
                 &= \dfrac{(x - 2)^2}{x}
    \end{align*}
    Puisque $(x-2)^2 \geq 0$ et $x > 0$, on a $f(x) - 4 \geq 0$, soit $f(x) \geq 4$.

    De plus : $f(2) = 2 + \dfrac{4}{2} = 4$.

    \textbf{Conclusion :} Le nombre $4$ est le \textbf{minimum} de $f$ sur $\left]0 ; +\infty\right[$.

    \item \textbf{Montrons que $-4$ est le maximum de $f$ sur $]-\infty ; 0[$ :}

    Pour tout $x \in \left]-\infty ; 0\right[$, on a :
    \begin{align*}
        f(x) - (-4) &= x + \dfrac{4}{x} + 4 \\[4pt]
                    &= \dfrac{x^2 + 4x + 4}{x} \\[4pt]
                    &= \dfrac{(x + 2)^2}{x}
    \end{align*}
    Puisque $(x+2)^2 \geq 0$ et $x < 0$, on a $\dfrac{(x+2)^2}{x} \leq 0$, soit $f(x) \leq -4$.

    De plus : $f(-2) = -2 + \dfrac{4}{-2} = -2 - 2 = -4$.

    \textbf{Conclusion :} Le nombre $-4$ est le \textbf{maximum} de $f$ sur $\left]-\infty ; 0\right[$.
\end{enumerate}
\end{Solution}

"""

ANCHOR15 = (
    "    \\item Montrer que $-4$ est le maximum de $f$ sur $]-\\infty ; 0[$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW15 = ANCHOR15 + SOL15

if ANCHOR15 in content:
    content = content.replace(ANCHOR15, NEW15, 1)
    print("OK App 15")
else:
    print("ERREUR App 15 — ancre introuvable")

# ============================================================
# SOLUTION Application 16 — f(x) = (x²-3)/(2x²+4)
# ============================================================
SOL16 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons $D_f$ :}

    Puisque $2x^2 + 4 = 2(x^2 + 2) > 0$ pour tout $x \in \mathbb{R}$, le dénominateur ne s'annule jamais.

    Donc : \quad $D_f = \mathbb{R}$

    \textbf{Étudions la parité de $f$ :}

    Soit $x \in \mathbb{R}$.
    \begin{align*}
        f(-x) &= \dfrac{(-x)^2 - 3}{2(-x)^2 + 4} = \dfrac{x^2 - 3}{2x^2 + 4} = f(x)
    \end{align*}
    La fonction $f$ est \textbf{paire}.

    \item \textbf{Calculons les images de $0$, $1$ et $-1$ :}

    \begin{align*}
        f(0) &= \dfrac{0 - 3}{0 + 4} = -\dfrac{3}{4} \\[6pt]
        f(1) &= \dfrac{1 - 3}{2 + 4} = \dfrac{-2}{6} = -\dfrac{1}{3} \\[6pt]
        f(-1) &= f(1) = -\dfrac{1}{3} \quad \text{(car la fonction $f$ est paire)}
    \end{align*}

    \item
    \begin{enumerate}
        \item \textbf{Résolvons $f(x) = \dfrac{1}{2}$ :}

        \begin{align*}
            \dfrac{x^2 - 3}{2x^2 + 4} = \dfrac{1}{2}
            &\text{ équivaut à } 2(x^2 - 3) = 2x^2 + 4 \\
            &\text{ équivaut à } 2x^2 - 6 = 2x^2 + 4 \\
            &\text{ équivaut à } -6 = 4
        \end{align*}
        Cette équation est impossible. L'équation $f(x) = \dfrac{1}{2}$ n'a \textbf{aucune solution} dans $\mathbb{R}$.

        \item \textbf{Montrons que $f(x) \leq \dfrac{1}{2}$ pour tout $x \in \mathbb{R}$ :}

        \begin{align*}
            \dfrac{1}{2} - f(x) &= \dfrac{1}{2} - \dfrac{x^2 - 3}{2x^2 + 4} \\[6pt]
                                &= \dfrac{(2x^2 + 4) - 2(x^2 - 3)}{2(2x^2 + 4)} \\[6pt]
                                &= \dfrac{2x^2 + 4 - 2x^2 + 6}{2(2x^2 + 4)} \\[6pt]
                                &= \dfrac{10}{2(2x^2 + 4)}
        \end{align*}
        Puisque $10 > 0$ et $2(2x^2+4) > 0$, on a $\dfrac{1}{2} - f(x) > 0$, donc $f(x) < \dfrac{1}{2}$.

        \item Puisque l'équation $f(x) = \dfrac{1}{2}$ n'admet aucune solution dans $\mathbb{R}$, le nombre $\dfrac{1}{2}$ \textbf{n'est pas un maximum} de $f$ sur $\mathbb{R}$.
    \end{enumerate}

    \item
    \begin{enumerate}
        \item \textbf{Montrons que $f(x) \geq -\dfrac{3}{4}$ pour tout $x \in \mathbb{R}$ :}

        \begin{align*}
            f(x) + \dfrac{3}{4} &= \dfrac{x^2 - 3}{2x^2 + 4} + \dfrac{3}{4} \\[6pt]
                                 &= \dfrac{4(x^2 - 3) + 3(2x^2 + 4)}{4(2x^2 + 4)} \\[6pt]
                                 &= \dfrac{4x^2 - 12 + 6x^2 + 12}{4(2x^2 + 4)} \\[6pt]
                                 &= \dfrac{10x^2}{4(2x^2 + 4)}
        \end{align*}
        Puisque $10x^2 \geq 0$ et $4(2x^2+4) > 0$, on a $f(x) + \dfrac{3}{4} \geq 0$, donc $f(x) \geq -\dfrac{3}{4}$.

        \item Puisque $f(x) \geq -\dfrac{3}{4}$ pour tout $x \in \mathbb{R}$ et $f(0) = -\dfrac{3}{4}$, le nombre $-\dfrac{3}{4}$ est bien le \textbf{minimum} de $f$ sur $\mathbb{R}$, atteint en $x = 0$.
    \end{enumerate}
\end{enumerate}
\end{Solution}

"""

ANCHOR16 = (
    "    \\item Le nombre $-\\frac{3}{4}$ est-il un minimum de $f$ sur $\\mathbb{R}$ ?\n"
    "  \\end{enumerate}\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW16 = ANCHOR16 + SOL16

if ANCHOR16 in content:
    content = content.replace(ANCHOR16, NEW16, 1)
    print("OK App 16")
else:
    print("ERREUR App 16 — ancre introuvable")

# ============================================================
# SOLUTION Application 17 — cos(x) et sin(x)
# ============================================================
SOL17 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Étudions la parité de $f$ et $g$ :}

    Soit $x \in \mathbb{R}$.
    \begin{align*}
        f(-x) &= \cos(-x) = \cos(x) = f(x)
    \end{align*}
    La fonction $f$ est \textbf{paire}.

    \begin{align*}
        g(-x) &= \sin(-x) = -\sin(x) = -g(x)
    \end{align*}
    Donc la fonction $g$ est \textbf{impaire}.

    \item \textbf{Calculons $f(x+2\pi)$ et $g(x+2\pi)$ :}

    \[ f(x + 2\pi) = \cos(x + 2\pi) = \cos(x) = f(x) \]
    \[ g(x + 2\pi) = \sin(x + 2\pi) = \sin(x) = g(x) \]

    \textbf{Conclusion :} Les fonctions $f$ et $g$ sont $2\pi$-\textbf{périodiques}.

    \item \textbf{Complétons les courbes :}

    Puisque $f$ est \textbf{paire}, sa courbe est symétrique par rapport à l'axe des ordonnées : on complète le tracé de $[0\,;\,\pi]$ par symétrie axiale, puis on reproduit par translation de $2k\pi$ ($k \in \mathbb{Z}$).

    Puisque $g$ est \textbf{impaire}, sa courbe est symétrique par rapport à l'origine : on complète le tracé de $[0\,;\,\pi]$ par symétrie centrale en $O$, puis on reproduit par translation de $2k\pi$.
\end{enumerate}
\end{Solution}

"""

ANCHOR17 = (
    "        \\draw[very thick, PrimaryColor, domain=0:pi, samples=100] plot (\\x, {sin(\\x r)});\n"
    "    \\end{tikzpicture}\n"
    "\\end{center}\n"
    "\n"
    "\\end{Application}\n"
)
NEW17 = ANCHOR17 + SOL17

if ANCHOR17 in content:
    content = content.replace(ANCHOR17, NEW17, 1)
    print("OK App 17")
else:
    print("ERREUR App 17 — ancre introuvable")

# ============================================================
# SOLUTION Exercice 1 — f(x) = 2x/(x²+1)
# ============================================================
SOL_EX1 = r"""
%% SOLUTION_EXERCICE
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons $D_f$ et étudions la parité de $f$ :}

    Puisque $x^2 + 1 > 0$ pour tout $x \in \mathbb{R}$, le dénominateur ne s'annule jamais.

    Donc : \quad $D_f = \mathbb{R}$

    Soit $x \in \mathbb{R}$.
    \begin{align*}
        f(-x) &= \dfrac{2(-x)}{(-x)^2 + 1} = \dfrac{-2x}{x^2 + 1} = -f(x)
    \end{align*}
    Donc la fonction $f$ est \textbf{impaire}.

    \item \textbf{Calculons $f(0)$, $f(1)$ et $f(2)$ :}

    \[ f(0) = \dfrac{0}{1} = 0 \qquad f(1) = \dfrac{2}{2} = 1 \qquad f(2) = \dfrac{4}{5} \]

    \item
    \begin{enumerate}
        \item \textbf{Calculons $T(a\,;\,b)$ :}

        \textbf{Étape 1 —} Définition du taux de variation :
        \[ T(a\,;\,b) = \dfrac{f(b) - f(a)}{b - a} \]

        \textbf{Étape 2 —} Calculons $f(b) - f(a)$ séparément :
        \begin{align*}
            f(b) - f(a) &= \dfrac{2b}{b^2 + 1} - \dfrac{2a}{a^2 + 1} \\[6pt]
                        &= \dfrac{2b(a^2 + 1) - 2a(b^2 + 1)}{(a^2 + 1)(b^2 + 1)} \\[6pt]
                        &= \dfrac{2a^2b + 2b - 2ab^2 - 2a}{(a^2 + 1)(b^2 + 1)} \\[6pt]
                        &= \dfrac{2ab(a - b) - 2(a - b)}{(a^2 + 1)(b^2 + 1)} \\[6pt]
                        &= \dfrac{2(a - b)(ab - 1)}{(a^2 + 1)(b^2 + 1)} \\[6pt]
                        &= \dfrac{-2(b - a)(1 - ab)}{(a^2 + 1)(b^2 + 1)}
        \end{align*}

        \textbf{Étape 3 —} Divisons par $(b - a)$ :
        \[ T(a\,;\,b) = \dfrac{f(b) - f(a)}{b - a} = \dfrac{-2(b-a)(1-ab)}{(a^2+1)(b^2+1)(b-a)} = \dfrac{2(1 - ab)}{(a^2 + 1)(b^2 + 1)} \quad \text{(car } a \neq b\text{)} \]

        \item \textbf{Étudions la monotonie de $f$ sur $[0\,;\,1]$ et sur $[1\,;\,+\infty[$ :}

        Soient $a$ et $b$ deux réels distincts de $[0\,;\,+\infty[$ avec $a < b$. On a $(a^2 + 1)(b^2 + 1) > 0$.

        \textbf{Sur $[0\,;\,1]$ :} Pour $0 \leq a < b \leq 1$, on a $ab \leq 1$, donc $1 - ab \geq 0$.

        D'où : $T(a\,;\,b) \geq 0$. Donc $f$ est \textbf{strictement croissante} sur $[0\,;\,1]$.

        \textbf{Sur $[1\,;\,+\infty[$ :} Pour $1 \leq a < b$, on a $ab \geq 1$, donc $1 - ab \leq 0$.

        D'où : $T(a\,;\,b) \leq 0$. Donc $f$ est \textbf{strictement décroissante} sur $[1\,;\,+\infty[$.

        \item \textbf{Déduisons la monotonie sur $[-1\,;\,0]$ et $]-\infty\,;\,-1]$ :}

        Puisque $f$ est \textbf{impaire}, $f$ est strictement croissante sur $[-1\,;\,0]$ et strictement décroissante sur $]-\infty\,;\,-1]$.

        \item \textbf{Tableau de variations de $f$ sur $\mathbb{R}$ :}

        \begin{center}
        \begin{tikzpicture}
            \tkzTabInit[lgt=1.5, espcl=2]{$x$ / 0.7, $f(x)$ / 2.5}{$-\infty$, $-1$, $0$, $1$, $+\infty$}
            \tkzTabVar{+/ , -/ $-1$ , -/ $0$ , +/ $1$ , -/ }
        \end{tikzpicture}
        \end{center}
    \end{enumerate}

    \item
    \begin{enumerate}
        \item \textbf{Montrons que $1 - f(x) = \dfrac{(x-1)^2}{x^2+1}$ :}

        \begin{align*}
            1 - f(x) &= 1 - \dfrac{2x}{x^2 + 1} = \dfrac{x^2 + 1 - 2x}{x^2 + 1} = \dfrac{(x-1)^2}{x^2+1}
        \end{align*}

        \item \textbf{Déduisons que $f(x) \leq 1$ :}

        Puisque $(x-1)^2 \geq 0$ et $x^2 + 1 > 0$, on a $\dfrac{(x-1)^2}{x^2+1} \geq 0$.

        Donc $1 - f(x) \geq 0$, d'où $f(x) \leq 1$.
    \end{enumerate}

    \item \textbf{Résolvons $f(x) = 1$ et concluons :}

    \[ f(x) = 1 \Leftrightarrow \dfrac{(x-1)^2}{x^2+1} = 0 \Leftrightarrow (x-1)^2 = 0 \Leftrightarrow x = 1 \]

    Puisque $f(x) \leq 1$ pour tout $x \in \mathbb{R}$ et $f(1) = 1$, le nombre $1$ est le \textbf{maximum} de $f$ sur $\mathbb{R}$.

    \item \textbf{Le minimum de $f$ sur $\mathbb{R}$ :}

    Puisque $f$ est \textbf{impaire} : pour tout $x \in \mathbb{R}$, $f(-x) = -f(x)$.

    Donc $f(x) = -f(-x) \geq -1$ (car $f(-x) \leq 1$).

    De plus $f(-1) = -f(1) = -1$.

    \textbf{Conclusion :} Le nombre $-1$ est le \textbf{minimum} de $f$ sur $\mathbb{R}$, atteint au point $(-1\,;\,-1)$.
\end{enumerate}
\end{Solution}

"""

ANCHOR_EX1 = (
    "    \\item En utilisant la parité de $f$, montrer que $-1$ est le minimum de $f$ sur $\\mathbb{R}$ et préciser en quel point il est atteint.\n"
    "\\end{enumerate}\n"
    "\\end{Exercice}\n"
)
NEW_EX1 = ANCHOR_EX1 + SOL_EX1

if ANCHOR_EX1 in content:
    content = content.replace(ANCHOR_EX1, NEW_EX1, 1)
    print("OK Exercice 1")
else:
    print("ERREUR Exercice 1 — ancre introuvable")

# ============================================================
# SOLUTION Application 18 — f(x) = 3x²
# ============================================================
SOL18 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Calculons $f(1)$ et $f(2)$ ; puis déduisons $f(-1)$ et $f(-2)$ :}

    \[ f(1) = 3 \times 1^2 = 3 \qquad f(2) = 3 \times 4 = 12 \]

    Puisque $f(x) = 3x^2$ est une fonction \textbf{paire} ($f(-x) = 3(-x)^2 = 3x^2 = f(x)$) :
    \[ f(-1) = f(1) = 3 \qquad f(-2) = f(2) = 12 \]

    \item \textbf{Tableau de variations de $f$ sur $\mathbb{R}$ :}

    Puisque $a = 3 > 0$, la parabole est dirigée vers le haut, avec minimum $f(0) = 0$ en $x = 0$.
    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $0$, $+\infty$}
        \tkzTabVar{+/ , -/ $0$ , +/ }
    \end{tikzpicture}
    \end{center}

    \item \textbf{Tracé de $(\mathcal{C}_f)$ :}

    $(\mathcal{C}_f)$ est une \textbf{parabole} de sommet $O(0\,;\,0)$, d'axe de symétrie l'axe des ordonnées, dirigée vers le \textbf{haut}.
\end{enumerate}
\end{Solution}

"""

ANCHOR18 = (
    "    \\item Tracer $(\\mathcal{C}_f)$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
    "\n"
    "%% APPLICATION\n"
    "\\begin{Application}[][10 min]\n"
    "Soit $g$ la fonction définie sur $\\mathbb{R}$ par : $g(x) = ax^2$"
)
NEW18 = ANCHOR18 + ""

# Need different anchor — use content before the second APPLICATION
ANCHOR18 = (
    "Soit $f$ la fonction définie sur $\\mathbb{R}$ par : $f(x) = 3x^2$\n"
    "\\begin{enumerate}\n"
    "    \\item Calculer $f(1)$ et $f(2)$ ; puis déduire $f(-1)$ et $f(-2)$.\n"
    "    \\item Dresser le tableau de variations de $f$ sur $\\mathbb{R}$.\n"
    "    \\item Tracer $(\\mathcal{C}_f)$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW18 = ANCHOR18 + SOL18

if ANCHOR18 in content:
    content = content.replace(ANCHOR18, NEW18, 1)
    print("OK App 18")
else:
    print("ERREUR App 18 — ancre introuvable")

# ============================================================
# SOLUTION Application 19 — g(x) = ax²
# ============================================================
SOL19 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons la valeur de $a$ :}

    On a : $g(2) = a \times 2^2 = 4a$.
    \begin{align*}
        g(2) = -3 &\text{ équivaut à } 4a = -3 \text{ équivaut à } a = -\dfrac{3}{4}
    \end{align*}
    Donc : \quad $a = -\dfrac{3}{4}$

    \item \textbf{Tableau de variations de $g$ sur $\mathbb{R}$ :}

    Puisque $a = -\dfrac{3}{4} < 0$, la parabole est dirigée vers le bas, avec maximum $g(0) = 0$ en $x = 0$.
    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1, espcl=2.5]{$x$ / 0.7, $g(x)$ / 2}{$-\infty$, $0$, $+\infty$}
        \tkzTabVar{-/ , +/ $0$ , -/ }
    \end{tikzpicture}
    \end{center}

    \item \textbf{Tracé de $(\mathcal{C}_g)$ :}

    $(\mathcal{C}_g)$ est une \textbf{parabole} de sommet $O(0\,;\,0)$, d'axe de symétrie l'axe des ordonnées, dirigée vers le \textbf{bas}.
\end{enumerate}
\end{Solution}

"""

ANCHOR19 = (
    "Soit $g$ la fonction définie sur $\\mathbb{R}$ par : $g(x) = ax^2$  ~ ($a \\in \\mathbb{R}^*$)\n"
    "\\begin{enumerate}\n"
    "    \\item Déterminer la valeur de $a$ tel que $g(2) = -3$.\n"
    "    \\item Dresser le tableau de variations de $g$ sur $\\mathbb{R}$.\n"
    "    \\item Tracer $(\\mathcal{C}_g)$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW19 = ANCHOR19 + SOL19

if ANCHOR19 in content:
    content = content.replace(ANCHOR19, NEW19, 1)
    print("OK App 19")
else:
    print("ERREUR App 19 — ancre introuvable")

# ============================================================
# SOLUTION Application 20 — Sommet et axe de symétrie
# ============================================================
SOL20 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item $f(x) = x^2 + 2x + 1$ : \quad $a = 1$, $b = 2$, $c = 1$.
    \[ -\dfrac{b}{2a} = -\dfrac{2}{2} = -1 \qquad f(-1) = 1 - 2 + 1 = 0 \]
    Le \textbf{sommet} est $S(-1\,;\,0)$ et l'axe de symétrie est la droite $x = -1$.

    \item $f(x) = -2x^2 + 6x + 1$ : \quad $a = -2$, $b = 6$, $c = 1$.
    \[ -\dfrac{b}{2a} = -\dfrac{6}{-4} = \dfrac{3}{2} \qquad f\!\left(\dfrac{3}{2}\right) = -2 \times \dfrac{9}{4} + 6 \times \dfrac{3}{2} + 1 = -\dfrac{9}{2} + 9 + 1 = \dfrac{11}{2} \]
    Le \textbf{sommet} est $S\!\left(\dfrac{3}{2}\,;\,\dfrac{11}{2}\right)$ et l'axe de symétrie est la droite $x = \dfrac{3}{2}$.

    \item $f(x) = x^2 - 1$ : \quad $a = 1$, $b = 0$, $c = -1$.
    \[ -\dfrac{b}{2a} = 0 \qquad f(0) = -1 \]
    Le \textbf{sommet} est $S(0\,;\,-1)$ et l'axe de symétrie est la droite $x = 0$ (axe des ordonnées).
\end{enumerate}
\end{Solution}

"""

ANCHOR20 = (
    "Déterminer le sommet et l'axe de symétrie de $f$ dans chacun des cas suivants : \\\\\n"
    "\\textbf{1.} $f(x) = x^2 + 2x + 1$ \\qquad\n"
    "\\textbf{2.} $f(x) = -2x^2 + 6x + 1$ \\qquad\n"
    "\\textbf{3.} $f(x) = x^2 - 1$\n"
    "\\end{Application}\n"
)
NEW20 = ANCHOR20 + SOL20

if ANCHOR20 in content:
    content = content.replace(ANCHOR20, NEW20, 1)
    print("OK App 20")
else:
    print("ERREUR App 20 — ancre introuvable")

# ============================================================
# SOLUTION Application 21 — Tableaux de variations (3 paraboles)
# ============================================================
SOL21 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item $f(x) = x^2 + 2x + 1$, $a = 1 > 0$, sommet $S(-1\,;\,0)$ :
    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $-1$, $+\infty$}
        \tkzTabVar{+/ , -/ $0$ , +/ }
    \end{tikzpicture}
    \end{center}

    \item $f(x) = -2x^2 + 6x + 1$, $a = -2 < 0$, sommet $S\!\left(\dfrac{3}{2}\,;\,\dfrac{11}{2}\right)$ :
    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $\frac{3}{2}$, $+\infty$}
        \tkzTabVar{-/ , +/ $\frac{11}{2}$ , -/ }
    \end{tikzpicture}
    \end{center}

    \item $f(x) = x^2 - 1$, $a = 1 > 0$, sommet $S(0\,;\,-1)$ :
    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $0$, $+\infty$}
        \tkzTabVar{+/ , -/ $-1$ , +/ }
    \end{tikzpicture}
    \end{center}
\end{enumerate}
\end{Solution}

"""

ANCHOR21 = (
    "Dresser le tableau de variations de $f$ dans chacun des cas suivants : \\\\\n"
    "\\textbf{1.} $f(x) = x^2 + 2x + 1$ \\qquad\n"
    "\\textbf{2.} $f(x) = -2x^2 + 6x + 1$ \\qquad\n"
    "\\textbf{3.} $f(x) = x^2 - 1$\n"
    "\\end{Application}\n"
)
NEW21 = ANCHOR21 + SOL21

if ANCHOR21 in content:
    content = content.replace(ANCHOR21, NEW21, 1)
    print("OK App 21")
else:
    print("ERREUR App 21 — ancre introuvable")

# ============================================================
# SOLUTION Application 22 — f(x) = 2x²-4x+3
# ============================================================
SOL22 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons la nature de $(C_f)$ :}

    On a $a = 2$, $b = -4$, $c = 3$.

    Puisque $a = 2 \neq 0$, la courbe $(C_f)$ est une \textbf{parabole}.
    \[ -\dfrac{b}{2a} = -\dfrac{-4}{4} = 1 \qquad f(1) = 2 - 4 + 3 = 1 \]
    Le \textbf{sommet} est $S(1\,;\,1)$ et l'axe de symétrie est la droite $x = 1$.

    Puisque $a = 2 > 0$, la parabole est dirigée vers le \textbf{haut}.

    Le discriminant est : $\Delta = (-4)^2 - 4 \times 2 \times 3 = 16 - 24 = -8 < 0$.

    Puisque $\Delta < 0$, la parabole ne coupe pas l'axe des abscisses.

    \item \textbf{Tableau de variations de $f$ :}

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $1$, $+\infty$}
        \tkzTabVar{+/ , -/ $1$ , +/ }
    \end{tikzpicture}
    \end{center}

    \item \textbf{Construction de $(C_f)$ :}

    $(C_f)$ est une parabole de sommet $S(1\,;\,1)$, d'axe $x = 1$, dirigée vers le haut.

    \item \textbf{Discussion de l'équation $f(x) = m$ :}

    L'équation $f(x) = m$ représente l'intersection de la parabole $(C_f)$ avec la droite $y = m$.

    Puisque le minimum de $f$ est $1$ (atteint en $x = 1$) :
    \begin{itemize}
        \item Si $m < 1$ : l'équation n'a \textbf{aucune solution}.
        \item Si $m = 1$ : l'équation a \textbf{une seule solution} : $x = 1$.
        \item Si $m > 1$ : l'équation a \textbf{deux solutions distinctes}.
    \end{itemize}
\end{enumerate}
\end{Solution}

"""

ANCHOR22 = (
    "    \\item Discuter suivant les valeurs de $m$ les solutions de l'équation $f(x) = m \\quad (m \\in \\mathbb{R})$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
    "\n"
    "%% REMARQUE"
)
NEW22 = ANCHOR22[:ANCHOR22.rfind("\n\n%% REMARQUE")] + "\n\\end{Application}\n" + SOL22 + "%% REMARQUE"

# Simpler: replace the anchor with itself + solution, but we need to keep %% REMARQUE
# Let's use a different strategy
ANCHOR22_FULL = (
    "    \\item Discuter suivant les valeurs de $m$ les solutions de l'équation $f(x) = m \\quad (m \\in \\mathbb{R})$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW22 = ANCHOR22_FULL + SOL22

if ANCHOR22_FULL in content:
    content = content.replace(ANCHOR22_FULL, NEW22, 1)
    print("OK App 22")
else:
    print("ERREUR App 22 — ancre introuvable")

# ============================================================
# SOLUTION Application 23 — f(x) = 3/x
# ============================================================
SOL23 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Tableau de variations de $f$ :}

    Puisque $a = 3 > 0$, la fonction $f(x) = \dfrac{3}{x}$ est \textbf{strictement décroissante} sur $]-\infty\,;\,0[$ et sur $]0\,;\,+\infty[$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $0$, $+\infty$}
        \tkzTabVar{+/ $0^-$ , -D+/ , -/ $0^+$ }
    \end{tikzpicture}
    \end{center}

    \item \textbf{Construction de $(\mathcal{C}_f)$ :}

    $(\mathcal{C}_f)$ est une \textbf{hyperbole} de centre $O(0\,;\,0)$, d'asymptotes les axes du repère.
\end{enumerate}
\end{Solution}

"""

ANCHOR23 = (
    "Soit $f$ la fonction définie par : $f(x) = \\frac{3}{x}$\n"
    "\n"
    "\\begin{enumerate}\n"
    "    \\item Donner le tableau de variations de $f$.\n"
    "    \\item Construire la courbe $(\\mathcal{C}_f)$ dans un repère orthonormal $(O; \\vec{i}, \\vec{j})$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW23 = ANCHOR23 + SOL23

if ANCHOR23 in content:
    content = content.replace(ANCHOR23, NEW23, 1)
    print("OK App 23")
else:
    print("ERREUR App 23 — ancre introuvable")

# ============================================================
# SOLUTION Application 24 — f(x) = -2/x
# ============================================================
SOL24 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Tableau de variations de $f$ :}

    Puisque $a = -2 < 0$, la fonction $f(x) = \dfrac{-2}{x}$ est \textbf{strictement croissante} sur $]-\infty\,;\,0[$ et sur $]0\,;\,+\infty[$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $0$, $+\infty$}
        \tkzTabVar{-/ $0^+$ , +D-/ , +/ $0^-$ }
    \end{tikzpicture}
    \end{center}

    \item \textbf{Construction de $(\mathcal{C}_f)$ :}

    $(\mathcal{C}_f)$ est une \textbf{hyperbole} de centre $O(0\,;\,0)$, d'asymptotes les axes du repère.
\end{enumerate}
\end{Solution}

"""

ANCHOR24 = (
    "Soit $f$ la fonction définie par : $f(x) = -\\frac{2}{x}$\n"
    "\n"
    "\\begin{enumerate}\n"
    "    \\item Donner le tableau de variations de $f$.\n"
    "    \\item Construire la courbe $(\\mathcal{C}_f)$ dans un repère orthonormal $(O; \\vec{i}, \\vec{j})$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW24 = ANCHOR24 + SOL24

if ANCHOR24 in content:
    content = content.replace(ANCHOR24, NEW24, 1)
    print("OK App 24")
else:
    print("ERREUR App 24 — ancre introuvable")

# ============================================================
# SOLUTION Application 25 — 3 fonctions homographiques
# ============================================================
SOL25 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{itemize}
    \item $f(x) = \dfrac{3x-1}{x+1}$ : \quad $a = 3$, $b = -1$, $c = 1$, $d = 1$.

    $\Delta = ad - bc = 3 \times 1 - (-1) \times 1 = 4 > 0$

    Puisque $\Delta > 0$, $f$ est \textbf{strictement croissante} sur $]-\infty\,;\,-1[$ et sur $]-1\,;\,+\infty[$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $-1$, $+\infty$}
        \tkzTabVar{-/ , +D-/ , +/ }
    \end{tikzpicture}
    \end{center}

    \item $g(x) = \dfrac{x}{2x+3}$ : \quad $a = 1$, $b = 0$, $c = 2$, $d = 3$.

    $\Delta = ad - bc = 1 \times 3 - 0 \times 2 = 3 > 0$

    Le pôle est $x = -\dfrac{d}{c} = -\dfrac{3}{2}$.

    Puisque $\Delta > 0$, $g$ est \textbf{strictement croissante} sur $\left]-\infty\,;\,-\dfrac{3}{2}\right[$ et sur $\left]-\dfrac{3}{2}\,;\,+\infty\right[$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $g(x)$ / 2}{$-\infty$, $-\frac{3}{2}$, $+\infty$}
        \tkzTabVar{-/ , +D-/ , +/ }
    \end{tikzpicture}
    \end{center}

    \item $h(x) = \dfrac{-3}{3x-1}$ : \quad $a = 0$, $b = -3$, $c = 3$, $d = -1$.

    $\Delta = ad - bc = 0 \times (-1) - (-3) \times 3 = 9 > 0$

    Le pôle est $x = -\dfrac{d}{c} = \dfrac{1}{3}$.

    Puisque $\Delta > 0$, $h$ est \textbf{strictement croissante} sur $\left]-\infty\,;\,\dfrac{1}{3}\right[$ et sur $\left]\dfrac{1}{3}\,;\,+\infty\right[$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $h(x)$ / 2}{$-\infty$, $\frac{1}{3}$, $+\infty$}
        \tkzTabVar{-/ , +D-/ , +/ }
    \end{tikzpicture}
    \end{center}
\end{itemize}
\end{Solution}

"""

ANCHOR25 = (
    "    \\item $f(x) = \\frac{3x-1}{x+1}$\n"
    "    \\item $g(x) = \\frac{x}{2x+3}$\n"
    "    \\item $h(x) = \\frac{-3}{3x-1}$\n"
    "\\end{itemize}\n"
    "\\end{Application}\n"
)
NEW25 = ANCHOR25 + SOL25

if ANCHOR25 in content:
    content = content.replace(ANCHOR25, NEW25, 1)
    print("OK App 25")
else:
    print("ERREUR App 25 — ancre introuvable")

# ============================================================
# SOLUTION Application 26 — f(x) = (2x+1)/(x-1)
# ============================================================
SOL26 = r"""
%% SOLUTION_APPLICATION
\begin{Solution}
\begin{enumerate}
    \item \textbf{Déterminons $D_f$ :}

    \begin{align*}
        D_f &= \left\{ x \in \mathbb{R} \mid x - 1 \neq 0 \right\} = \left\{ x \in \mathbb{R} \mid x \neq 1 \right\}
    \end{align*}
    Donc : \quad $D_f = \mathbb{R} \setminus \{1\} = \left]-\infty\,;\,1\right[ \cup \left]1\,;\,+\infty\right[$

    \item \textbf{Nature de $(C_f)$ et éléments caractéristiques :}

    On a $a = 2$, $b = 1$, $c = 1$, $d = -1$.

    $\Delta = ad - bc = 2 \times (-1) - 1 \times 1 = -3 < 0$

    La courbe $(C_f)$ est une \textbf{hyperbole} de centre :
    \[ \Omega\!\left(-\dfrac{d}{c}\,;\,\dfrac{a}{c}\right) = \Omega(1\,;\,2) \]

    Les asymptotes sont :
    \begin{itemize}
        \item Asymptote \textbf{verticale} : $x = 1$
        \item Asymptote \textbf{horizontale} : $y = 2$
    \end{itemize}

    Puisque $\Delta = -3 < 0$, $f$ est \textbf{strictement décroissante} sur $]-\infty\,;\,1[$ et sur $]1\,;\,+\infty[$.

    \item \textbf{Construction de $(C_f)$ :}

    $(C_f)$ est une hyperbole de centre $\Omega(1\,;\,2)$, d'asymptotes $x = 1$ et $y = 2$.
\end{enumerate}
\end{Solution}

"""

ANCHOR26 = (
    "Soit $f$ la fonction définie par $f(x) = \\frac{2x+1}{x-1}$\n"
    "\\begin{enumerate}\n"
    "    \\item Déterminer $D_f$.\n"
    "    \\item Déterminer la nature de $(C_f)$ en précisant ses éléments caractéristiques.\n"
    "    \\item Construire $(C_f)$.\n"
    "\\end{enumerate}\n"
    "\\end{Application}\n"
)
NEW26 = ANCHOR26 + SOL26

if ANCHOR26 in content:
    content = content.replace(ANCHOR26, NEW26, 1)
    print("OK App 26")
else:
    print("ERREUR App 26 — ancre introuvable")

# ============================================================
# SOLUTION Exercice 2 — f(x) = -x²+4x-3 et g(x) = (x-3)/(x-2)
# ============================================================
SOL_EX2 = r"""
%% SOLUTION_EXERCICE
\begin{Solution}
\begin{enumerate}
    \item
    \begin{enumerate}
        \item \textbf{Nature de $(C_f)$ :}

        On a $a = -1$, $b = 4$, $c = -3$.

        Puisque $a \neq 0$, $(C_f)$ est une \textbf{parabole}.
        \[ -\dfrac{b}{2a} = -\dfrac{4}{-2} = 2 \qquad f(2) = -4 + 8 - 3 = 1 \]
        Le \textbf{sommet} est $S(2\,;\,1)$, l'axe de symétrie est la droite $x = 2$.

        Puisque $a = -1 < 0$, la parabole est dirigée vers le \textbf{bas}.

        \item \textbf{Calculons $f(0)$, $f(1)$ et $f(3)$ :}

        \[ f(0) = -3 \qquad f(1) = -1 + 4 - 3 = 0 \qquad f(3) = -9 + 12 - 3 = 0 \]

        \item \textbf{Tableau de variations de $f$ :}

        \begin{center}
        \begin{tikzpicture}
            \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $f(x)$ / 2}{$-\infty$, $2$, $+\infty$}
            \tkzTabVar{-/ , +/ $1$ , -/ }
        \end{tikzpicture}
        \end{center}
    \end{enumerate}

    \item
    \begin{enumerate}
        \item \textbf{Déterminons $D_g$ :}

        \begin{align*}
            D_g = \left\{ x \in \mathbb{R} \mid x - 2 \neq 0 \right\} = \left\{ x \in \mathbb{R} \mid x \neq 2 \right\}
        \end{align*}
        Donc : \quad $D_g = \mathbb{R} \setminus \{2\} = \left]-\infty\,;\,2\right[ \cup \left]2\,;\,+\infty\right[$

        \item \textbf{Tableau de variations de $g$ :}

        On a $a = 1$, $b = -3$, $c = 1$, $d = -2$.

        $\Delta = ad - bc = 1 \times (-2) - (-3) \times 1 = -2 + 3 = 1 > 0$

        Puisque $\Delta > 0$, $g$ est \textbf{strictement croissante} sur $]-\infty\,;\,2[$ et sur $]2\,;\,+\infty[$.

        \begin{center}
        \begin{tikzpicture}
            \tkzTabInit[lgt=1.2, espcl=2.5]{$x$ / 0.7, $g(x)$ / 2}{$-\infty$, $2$, $+\infty$}
            \tkzTabVar{-/ , +D-/ , +/ }
        \end{tikzpicture}
        \end{center}

        \item \textbf{Nature de $(C_g)$ :}

        $(C_g)$ est une \textbf{hyperbole} de centre $\Omega(2\,;\,1)$, d'asymptotes : $x = 2$ (verticale) et $y = 1$ (horizontale).
    \end{enumerate}

    \item
    \begin{enumerate}
        \item \textbf{Montrons que $f(x) - g(x) = \dfrac{(x-3)(-x^2+3x-3)}{x-2}$ :}

        Pour $x \in D_g$, on a :
        \begin{align*}
            f(x) - g(x) &= (-x^2 + 4x - 3) - \dfrac{x-3}{x-2} \\[6pt]
                        &= \dfrac{(-x^2 + 4x - 3)(x-2) - (x-3)}{x-2}
        \end{align*}
        Calculons le numérateur :
        \begin{align*}
            (-x^2+4x-3)(x-2) - (x-3)
            &= -(x-1)(x-3)(x-2) - (x-3) \\
            &= (x-3)\big[-(x-1)(x-2) - 1\big] \\
            &= (x-3)\big[-(x^2-3x+2) - 1\big] \\
            &= (x-3)(-x^2+3x-3)
        \end{align*}
        D'où : \quad $f(x) - g(x) = \dfrac{(x-3)(-x^2+3x-3)}{x-2}$

        \item \textbf{Montrons que $-x^2+3x-3 < 0$ pour tout $x \in \mathbb{R}$ :}

        Le discriminant est $\Delta' = 3^2 - 4 \times (-1) \times (-3) = 9 - 12 = -3 < 0$.

        Puisque $\Delta' < 0$ et $a = -1 < 0$, on a $-x^2+3x-3 < 0$ pour tout réel $x$.

        \item \textbf{Point d'intersection de $(C_f)$ et $(C_g)$ :}

        $f(x) = g(x)$ équivaut à $\dfrac{(x-3)(-x^2+3x-3)}{x-2} = 0$.

        Puisque $-x^2+3x-3 < 0$ pour tout $x$ et $x \neq 2$ :
        \[ f(x) = g(x) \Leftrightarrow x - 3 = 0 \Leftrightarrow x = 3 \]

        On a $f(3) = 0$. Le point d'intersection est $\mathbf{A(3\,;\,0)}$.
    \end{enumerate}

    \item \textbf{Tracé des courbes :}

    Tracer les asymptotes $x = 2$ et $y = 1$, puis les courbes $(C_f)$ (parabole) et $(C_g)$ (hyperbole) dans le même repère, en marquant le point $A(3\,;\,0)$.

    \item \textbf{Résolution de $\dfrac{x-3}{x-2} \leq -x^2+4x-3$ :}

    L'inéquation équivaut à $g(x) \leq f(x)$, soit $f(x) - g(x) \geq 0$ :
    \[ \dfrac{(x-3)(-x^2+3x-3)}{x-2} \geq 0 \]

    Puisque $-x^2+3x-3 < 0$, cela équivaut à $\dfrac{x-3}{x-2} \leq 0$.

    \begin{center}
    \begin{tikzpicture}
        \tkzTabInit[lgt=1.5, espcl=2]{$x$ / 0.6, $x-3$ / 0.7, $x-2$ / 0.7, $\frac{x-3}{x-2}$ / 1}{$-\infty$, $2$, $3$, $+\infty$}
        \tkzTabLine{ , -, t, -, z, +, }
        \tkzTabLine{ , -, z, +, t, +, }
        \tkzTabLine{ , +, d, -, z, +, }
    \end{tikzpicture}
    \end{center}

    L'ensemble solution est : $\left]2\,;\,3\right]$

    \item \textbf{Discussion de $-x^2+4x-3-m = 0$ :}

    L'équation $f(x) = m$ représente l'intersection de $(C_f)$ avec la droite $y = m$.

    Le discriminant est $\Delta_m = b^2 - 4a(c-m) = 16 - 4(-1)(-3-m) = 16 - 4(3+m) = 4(1-m)$.
    \begin{itemize}
        \item Si $m > 1$ : $\Delta_m < 0$ : l'équation n'a \textbf{aucune solution}.
        \item Si $m = 1$ : $\Delta_m = 0$ : l'équation a \textbf{une seule solution} ($x = 2$).
        \item Si $m < 1$ : $\Delta_m > 0$ : l'équation a \textbf{deux solutions distinctes}.
    \end{itemize}
\end{enumerate}
\end{Solution}
"""

ANCHOR_EX2 = (
    "\\item  Discuter graphiquement, suivant les valeurs du paramètre réel $m$, le nombre de solutions de l'équation :$$-x^2 + 4x - 3 - m = 0$$\n"
    "\\end{enumerate}\n"
    "\\end{Exercice}\n"
)
NEW_EX2 = ANCHOR_EX2 + SOL_EX2

if ANCHOR_EX2 in content:
    content = content.replace(ANCHOR_EX2, NEW_EX2, 1)
    print("OK Exercice 2")
else:
    print("ERREUR Exercice 2 — ancre introuvable")

# ============================================================
# Sauvegarde
# ============================================================
if content == original:
    print("\nATTENTION : aucune modification effectuee !")
else:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("\nFichier sauvegarde avec succes.")
    print(f"Taille originale : {len(original)} chars")
    print(f"Taille nouvelle  : {len(content)} chars")
    print(f"Difference       : +{len(content) - len(original)} chars")
