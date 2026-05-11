# SKILL — Règles Communes à Tous les Chapitres
## `.claude/skills/correction-commune/SKILL.md`
**Pack Pédagogique · TCSF · Kaazouzi Ayyoub · 2025/2026**

> Ce fichier est chargé en PREMIER pour tout chapitre.
> Il est complété par `.claude/skills/correction-[chapitre]/SKILL.md`.
> En cas de conflit, le skill du chapitre prime.

---

## 1. CONNECTEURS LOGIQUES — UNIVERSELS

| Connecteur | Quand l'utiliser |
|-----------|-----------------|
| `On a :` | Démarrer tout calcul ou toute démonstration |
| `Donc` | Conclusion intermédiaire d'une étape |
| `Par conséquent,` | **Conclusion finale** d'une question (toujours en dernière ligne) |
| `D'où` | Conséquence directe et immédiate |
| `Or` | Rappeler une information connue ou une hypothèse |
| `Alors` | Implication directe dans un raisonnement |
| `D'après la question a),` | Renvoi explicite à un résultat déjà prouvé |
| `Montrons que` | Introduire ce qu'on veut démontrer |
| `En effet,` | Justifier une affirmation qui vient d'être posée |
| `On en déduit que` | Déduction depuis un résultat intermédiaire |

### Ordre obligatoire dans une correction

```
1. Phrase d'introduction  →  "On a :" / "Montrons que"
2. Calculs intermédiaires →  étapes numérotées ou align*
3. Conclusion partielle   →  "Donc ..."
4. Conclusion finale      →  "Par conséquent, ..."
```

---

## DISTINCTION FONDAMENTALE — SOLUTION_ACTIVITE vs SOLUTION_APPLICATION

### %% SOLUTION_ACTIVITE — Phase de construction
L'activité n'est PAS un exercice. C'est une phase d'éveil où l'élève
**découvre et construit** la notion par lui-même, à partir de ses acquis
du collège. La correction ne donne pas la réponse directement :
elle guide le raisonnement vers la définition/notion cible.

**Règles spécifiques :**
- Résolution étape par étape, en s'appuyant explicitement sur les
  acquis du collège (faire le pont).
- Ne jamais sauter une étape de calcul.
- À la fin de chaque question (si possible), ajouter une phrase
  d'institutionnalisation précédée de $\blacktriangleright$,
  entièrement en \textbf{...}, avec le terme technique en
  \textcolor{PrimaryColor}{...}.
- Ne jamais écrire le mot "Conclusion".
- Ne jamais donner la définition formelle avant que l'élève
  l'ait "découverte" via le raisonnement.

**Format de la phrase d'institutionnalisation :**
```latex
$\blacktriangleright$ \textbf{Ceci illustre la notion de
\textcolor{PrimaryColor}{taux de variation}.}
```

**Ton :** Vocabulaire très basique, adapté à un élève qui débute
le lycée. Rédaction directe, sans paragraphes superflus.

---

### %% SOLUTION_APPLICATION — Phase d'entraînement
L'application est un exercice d'entraînement. L'élève **mobilise**
une notion déjà construite et définie. La correction est rigoureuse,
directe et sert de modèle de rédaction.

**Règles spécifiques :**
- Appliquer le style du skill domaine concerné
  (domaine-algebre / domaine-analyse / domaine-geometrie).
- Appliquer les connecteurs logiques de correction-commune
  (`On a :` / `\Leftrightarrow` / `Donc` / `D'où`).
- Justifications obligatoires à chaque étape (voir tableau
  des justifications ci-dessous).
- Pas de phrase $\blacktriangleright$ — la notion est déjà acquise.
- Conclusion standard : `Donc $S = \{...\}$.`

**Ton :** Rigoureux, concis, sans commentaires pédagogiques.

---

## 2. FORMAT D'UNE ÉTAPE ALGÉBRIQUE

### Calcul développé (align*)

```latex
On a :
\begin{align*}
A &= \ldots          \\
  &= \ldots          \\
  &= \ldots
\end{align*}
Par conséquent, $A = valeur$.
```

### Équivalences (équations / inéquations)

```latex
On a :
\[expression_1\]
\[\Leftrightarrow expression_2 \qquad \text{(justification)}\]
\[\Leftrightarrow expression_3 \qquad \text{(justification)}\]
Donc $S = \{valeur\}$.
```

### Calcul en ligne (résultat simple)

```latex
On a : $A = \ldots = \ldots = valeur$.
Par conséquent, $A = valeur$.
```

---

## 3. JUSTIFICATIONS OBLIGATOIRES

| Opération | Justification à écrire |
|-----------|----------------------|
| Développer | `\text{(développement)}` ou `\text{(distributivité)}` |
| Factoriser | `\text{(factorisation)}` |
| Regrouper les termes | `\text{(on regroupe les termes semblables)}` |
| Diviser par c > 0 | `\text{(on divise par } c,\ c > 0\text{)}` |
| Diviser par c < 0 | `\text{(on divise par } c < 0\text{, le sens de l'inégalité s'inverse)}` |
| Multiplier par PPCM | `\text{(on multiplie par } n\text{, PPCM de } a \text{ et } b\text{)}` |
| Passer à la racine | `\text{(} \sqrt{\cdot} \text{ croissante sur } \mathbb{R}^+\text{)}` |
| Utiliser une identité | Écrire l'identité utilisée avant de l'appliquer |

---

## 4. FORMAT DE L'ENVIRONNEMENT SOLUTION

```latex
% Une question par Solution
\begin{Solution}[TYPE][N]
...
\end{Solution}

% Types disponibles :
% ACTIVITÉ / APPLICATION / EXERCICE DE SYNTHÈSE
```

### Règle d'or : montrer avant d'insérer
Toujours afficher le code généré avant de l'insérer dans source.tex.
Attendre la validation avant tout `git push`.

---

## 5. RÈGLES LaTeX ABSOLUES

| Règle | ✅ Correct | ❌ Interdit |
|-------|-----------|------------|
| Fractions | `\frac{a}{b}` | `\dfrac{a}{b}` |
| Largeur dans minipage | `\linewidth` | `\textwidth` |
| Espacement dans intervalles | `[a \; ; \; b]` | `[a;b]` ou `[a , b]` |
| Séparateur décimal | `,` | `.` |
| Guillemets | `\og \fg` ou `« »` | `"..."` |
| Vecteur | `\vect{AB}` | `\overrightarrow{AB}` |
| Valeur absolue | `\abs{x}` | `|x|` ou `\left|x\right|` |
| Ensembles | `\N \Z \R \C` | `\mathbb{N}` etc. |
| d droit (intégrale) | `\dd` | `d` ou `\mathrm{d}` |
| Points de suspension | `\ldots` | `...` |
| Infini dans intervalle | `+\infty` | `\infty` sans signe |

---

## 6. CONCLUSIONS TYPES — UNIVERSELLES

| Situation | Format |
|-----------|--------|
| Équation — solution unique | `Donc $S = \{valeur\}$.` |
| Équation — pas de solution | `Donc $S = \emptyset$.` |
| Équation — tout réel | `Donc $S = \R$.` |
| Inéquation | `Donc $S = [a \; ; \; +\infty[$.` |
| Valeur d'une expression | `Par conséquent, $A = valeur$.` |
| Démonstration terminée | `Par conséquent, [énoncé de ce qu'on voulait montrer].` |
| Résultat avec condition | `Par conséquent, pour tout $x \in D_f$, [conclusion].` |

---

## 7. STRUCTURE D'UNE DÉMONSTRATION

```latex
% Toujours suivre ce plan en 3 temps :

% 1. Hypothèses (ce qu'on sait)
Soit $n \in \mathbb{N}$ [tel que ...].

% 2. Corps de la démonstration
On a :
\begin{align*}
  ...
\end{align*}

% 3. Conclusion
Par conséquent, [ce qu'on voulait montrer].
```

### Renvoi à une question précédente

```latex
D'après la question \textbf{a)}, on sait que $[résultat]$.
```

---

## 8. LISTES ET ÉNUMÉRATIONS

```latex
% Toujours utiliser itemize pour les cas multiples
\begin{itemize}
    \item Premier cas : ...
    \item Deuxième cas : ...
\end{itemize}

% Pour les étapes numérotées dans une démonstration
\begin{enumerate}
    \item ...
    \item ...
\end{enumerate}
```

---

## 9. VOCABULAIRE OFFICIEL MAROCAIN — COMMUN

| ✅ Correct | ❌ Incorrect |
|-----------|-------------|
| `ensemble de définition` | `domaine de définition` |
| `ensemble solution` | `solution générale` |
| `sens de l'inégalité` | `signe de l'inégalité` |
| `membre gauche / droit` | `côté gauche / droit` |
| `strictement croissante` | `croissante strictement` |
| `entier naturel non nul` | `entier naturel positif` |
| `on pose` | `on définit` / `on note` (sauf notation officielle) |
| `Soit $x \in D_f$` | `Pour tout x dans Df` (sans formule) |
| `il faut et il suffit que` | `ssi` / `⟺` seul sans phrase |

---

## 10. CE QUI EST DANS LE SKILL DU CHAPITRE

Les règles suivantes sont **spécifiques** et ne sont jamais dans ce fichier :

| Chapitre | Règles spécifiques |
|----------|--------------------|
| Arithmétique | parité (Posons k ∈ N), PGCD/PPCM, tableau de divisions |
| Fonctions/Analyse | taux de variation, parité de f, tableaux de variations |
| Géométrie | Thalès, Pythagore, vecteurs, barycentre |
| Statistiques | moyenne, médiane, écart-type, tableaux statistiques |
| Équations/Inéquations | discriminant, tableaux de signes |

> Charger toujours les deux : ce fichier + le skill du chapitre en cours.
