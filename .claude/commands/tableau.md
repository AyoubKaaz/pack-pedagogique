---
name: tableau
description: Générer et insérer un tableau LaTeX dans source.tex
---

# /tableau — Insertion d'un tableau

## Étape 0 — Collecter les informations
Poser ces questions si non précisées :

1. "Dans quel chapitre et quelle position ?
   (ex: ch11_fonctions, dans le bloc %% TECHNIQUES)"

2. "Quel type de tableau ?
   a) Tableau de variations (tkz-tab)
   b) Tableau de signes (tkz-tab)
   c) Tableau de données/techniques (tabular)
   d) Tableau de valeurs pour tracé de courbe"

3. "Colonnes et contenu — liste les données :
   ex: x | -∞ | -1 | 0 | 1 | +∞
       f(x) |    | -1 | 0 | 1 |"

## Étape 1 — Règles tableaux pour ce projet

TOUJOURS respecter :
- Booktabs : \toprule, \midrule, \bottomrule (jamais \hline seul)
- Centrage : \begin{center} ... \end{center}
- Largeur : s'adapter à \linewidth (compatible 2 colonnes)
- En-tête coloré : \rowcolor{PrimaryColor!15} pour la première ligne
- Police : \footnotesize\sffamily dans les cellules complexes
- Espacement : \renewcommand{\arraystretch}{1.4}

## Étape 2 — Templates selon le type

### Type A — Tableau de variations (tkz-tab)
```latex
\begin{center}
\begin{tikzpicture}
    \tkzTabInit[lgt=2, espcl=2.5]
        {$x$ / 1, $f(x)$ / 2}
        {$-\infty$, $VAL1$, $VAL2$, $+\infty$}
    \tkzTabVar{
        +/$+\infty$,
        -/$MIN$,
        +/$MAX$,
        -/$-\infty$
    }
\end{tikzpicture}
\end{center}
```

### Type B — Tableau de signes (tkz-tab)
```latex
\begin{center}
\begin{tikzpicture}
    \tkzTabInit[lgt=3, espcl=2]
        {$x$ / 1, $EXPRESSION$ / 1}
        {$-\infty$, $VAL$, $+\infty$}
    \tkzTabLine{, -, z, +, }
\end{tikzpicture}
\end{center}
```

### Type C — Tableau de données/techniques (tabular)
```latex
\begin{center}
\renewcommand{\arraystretch}{1.4}
\begin{tabular}{|>{\centering\arraybackslash}m{4cm}
                |>{\centering\arraybackslash}m{6cm}|}
\toprule
\rowcolor{PrimaryColor!15}
\textbf{Colonne 1} & \textbf{Colonne 2} \\
\midrule
Donnée 1 & Valeur 1 \\
Donnée 2 & Valeur 2 \\
\bottomrule
\end{tabular}
\end{center}
```

### Type D — Tableau de valeurs pour tracé
```latex
\begin{center}
\renewcommand{\arraystretch}{1.3}
\begin{tabular}{|c||*{N}{c|}}
\hline
\rowcolor{PrimaryColor!15}
$x$ & $VAL1$ & $VAL2$ & $VAL3$ & $VAL4$ & $VAL5$ \\
\hline
$f(x)$ & & & & & \\
\hline
\end{tabular}
\end{center}
```

### Type E — Tableau de variations + signe combiné
```latex
\begin{center}
\begin{tikzpicture}
    \tkzTabInit[lgt=3, espcl=2.5]
        {$x$ / 1, $f'(x)$ / 1, $f(x)$ / 2}
        {$-\infty$, $VAL$, $+\infty$}
    \tkzTabLine{, -, z, +, }
    \tkzTabVar{+/$+\infty$, -/$MIN$, +/$+\infty$}
\end{tikzpicture}
\end{center}
```

## Étape 3 — Cas spéciaux

### Tableau trop large pour 2 colonnes
Si le tableau dépasse la largeur d'une colonne dans td.tex :
Proposer d'utiliser \footnotesize ou réduire le nombre de colonnes.

### Tableau dans un environnement Techniques
Toujours envelopper dans :
```latex
\begin{Techniques}
[tableau ici]
\end{Techniques}
```

## Étape 4 — Afficher avant insertion
TOUJOURS montrer le code du tableau et attendre la validation :
"Voici le tableau généré. Je l'insère dans source.tex ?"

## Étape 5 — Git push
```bash
git add chapitres/$CHAPITRE/source.tex
git commit -m "[$CHAPITRE] : tableau ajouté — [description courte]"
git push origin main
```
