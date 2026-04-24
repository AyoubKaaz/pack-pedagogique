---
name: figure
description: Générer et insérer une figure TikZ dans source.tex
---

# /figure — Insertion d'une figure TikZ

## Étape 0 — Collecter les informations
Poser ces questions si elles ne sont pas précisées :

1. "Dans quel chapitre et quelle position ?
   (ex: ch11_fonctions, après le bloc %% ACTIVITE 2)"

2. "Quel type de figure ?
   a) Courbe de fonction (pgfplots)
   b) Figure géométrique (tikzpicture classique)
   c) Droite numérique
   d) Repère avec points
   e) Autre — décris"

3. "Seule ou côte à côte avec une autre figure ?"

4. "Des éléments spécifiques à inclure ?
   (points nommés, zones colorées, asymptotes, tangentes...)"

## Étape 1 — Règles TikZ obligatoires pour ce projet

TOUJOURS respecter :
- Largeur : \linewidth (JAMAIS \textwidth)
- Couleurs : PrimaryColor, SecondaryColor, ou couleurs pgfplots standards
- Figures côte à côte : \begin{minipage}{0.45\linewidth} ... \end{minipage} \hfill
- Style des axes : axis lines=middle, -stealth, épaisseur thick
- Labels : font=\footnotesize\sffamily
- Compatibilité : doit compiler en 1 colonne (fiche) ET 2 colonnes (td)

## Étape 2 — Templates selon le type

### Type A — Courbe de fonction (pgfplots)
```latex
\begin{center}
\begin{tikzpicture}
    \begin{axis}[
        width=0.85\linewidth, height=0.7\linewidth,
        axis lines=middle,
        axis line style={thick, black, -stealth},
        xmin=XMIN, xmax=XMAX,
        ymin=YMIN, ymax=YMAX,
        xtick={VALEURS}, ytick={VALEURS},
        tick label style={font=\footnotesize\sffamily},
        xlabel={$x$}, ylabel={$y$},
        xlabel style={anchor=north west},
        ylabel style={anchor=south east},
        clip=false
    ]
    \addplot[thick, color=PrimaryColor, smooth,
             domain=DEBUT:FIN, samples=100] {EXPRESSION};
    \node[font=\footnotesize\sffamily\itshape, color=PrimaryColor]
        at (axis cs: X,Y) {$\mathcal{C}_f$};
    \end{axis}
\end{tikzpicture}
\end{center}
```

### Type B — Deux figures côte à côte
```latex
\begin{center}
\begin{minipage}{0.45\linewidth}
    \centering
    \begin{tikzpicture}
        \begin{axis}[width=\linewidth, height=\linewidth, ...]
        ...
        \end{axis}
    \end{tikzpicture}
\end{minipage}
\hfill
\begin{minipage}{0.45\linewidth}
    \centering
    \begin{tikzpicture}
        \begin{axis}[width=\linewidth, height=\linewidth, ...]
        ...
        \end{axis}
    \end{tikzpicture}
\end{minipage}
\end{center}
```

### Type C — Droite numérique
```latex
\begin{center}
\begin{tikzpicture}
    \draw[thick, -stealth] (DEBUT,0) -- (FIN,0) node[right] {$\R$};
    % Intervalle coloré
    \draw[thick, PrimaryColor] (A,0) -- (B,0);
    % Point fermé (crochet)
    \fill[PrimaryColor] (A,0) circle (2.5pt) node[below=4pt] {$a$};
    % Point ouvert (parenthèse)
    \draw[PrimaryColor, fill=white] (B,0) circle (2.5pt) node[below=4pt] {$b$};
    % Graduations
    \foreach \x in {LISTE}
        \draw (\x,-0.08) -- (\x,0.08);
\end{tikzpicture}
\end{center}
```

### Type D — Figure géométrique classique
```latex
\begin{center}
\begin{tikzpicture}[scale=ECHELLE, font=\footnotesize\sffamily]
    % Axes
    \draw[thick, -stealth] (-0.5,0) -- (XMAX,0) node[right] {$x$};
    \draw[thick, -stealth] (0,-0.5) -- (0,YMAX) node[above] {$y$};
    \node[below left] at (0,0) {$O$};
    % Points
    \fill[PrimaryColor] (X,Y) circle (2pt) node[above right] {$A(X;Y)$};
    % Lignes
    \draw[PrimaryColor, dashed] (X,0) node[below] {$X$} -- (X,Y) -- (0,Y)
        node[left] {$Y$};
\end{tikzpicture}
\end{center}
```

## Étape 3 — Afficher le code avant insertion
TOUJOURS montrer le code TikZ généré et attendre la validation :
"Voici la figure générée. Je l'insère dans source.tex ?"

## Étape 4 — Insérer dans source.tex
Insérer à la position exacte demandée.
Vérifier que le bloc %% correspondant est respecté.

## Étape 5 — Git push
```bash
git add chapitres/$CHAPITRE/source.tex
git commit -m "[$CHAPITRE] : figure TikZ ajoutée — [description courte]"
git push origin main
```
