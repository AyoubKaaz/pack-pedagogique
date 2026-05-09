# SKILL — Style de Correction : Arithmétique des entiers naturels
## `.claude/skills/correction-arithmetique/SKILL.md`
**Chapitre 1 · TCSF · Kaazouzi Ayyoub · 2025/2026**

---

## 1. CONNECTEURS LOGIQUES

| Connecteur | Quand l'utiliser |
|-----------|-----------------|
| `On a :` | Démarrer tout calcul ou toute démonstration |
| `Posons` | Définir un entier auxiliaire (k, k', k'', a, b…) |
| `Donc` | Conclusion intermédiaire d'une étape |
| `Par conséquent,` | **Conclusion finale** d'une question (toujours en dernière ligne) |
| `D'après la question a),` | Renvoi explicite à un résultat déjà prouvé |
| `Montrons que` | Introduire ce qu'on veut démontrer |
| `Déduisons que` | Introduire une déduction depuis un résultat précédent |
| `Il existe donc` | Affirmer l'existence d'un entier auxiliaire |
| `Alors` | Implication directe dans un raisonnement |
| `On sait que` | Rappeler une hypothèse ou contrainte (ex: n ≥ 2) |
| `On ne retient que` | Filtrer les cas selon les contraintes du problème |
| `On examine ces deux cas :` | Avant une énumération de cas |

---

## 2. RÈGLE ABSOLUE — PARITÉ

### Format standard (à appliquer à chaque nombre)

```latex
On a : $expression = développement = \ldots = 2(\ldots)$

Posons $k = \ldots \in \mathbb{N}$

Donc : $expression = 2k$

Par conséquent, $expression$ est un nombre \textbf{pair}.
```

```latex
On a : $expression = développement = \ldots = 2(\ldots)+1$

Posons $k = \ldots \in \mathbb{N}$

Donc : $expression = 2k+1$

Par conséquent, $expression$ est un nombre \textbf{impair}.
```

### Règle spéciale — Poser k avec ∈ N obligatoire
```latex
% CORRECT
Posons $k = 2n+6 \in \mathbb{N}$
Donc : $a = 2k+1$

% INTERDIT — ne jamais écrire directement sans poser k
Donc : $a = 2(2n+6)+1$ ← Ne pas conclure sans poser k
```

### Règle spéciale — Parité par conservation de la puissance
```latex
Le nombre $15$ est impair.
Et puisque la puissance conserve la parité.
Par conséquent, $15^{n+1}$ est un nombre \textbf{impair}.
```

### Règle spéciale — Parité d'un produit de consécutifs
```latex
% Montrer que k(k+1) est pair → il existe a ∈ N tel que k(k+1) = 2a
Le produit $k(k+1)$ est un nombre pair.
Il existe donc un entier $a \in \mathbb{N}$ tel que $k(k+1) = 2a$.
On peut alors écrire : $m^2 = 4(2a)+1 = 8a+1$.
```

---

## 3. RÈGLE ABSOLUE — DIVISIBILITÉ / MULTIPLES

### Format — Montrer qu'une expression est un multiple de d

```latex
% Étape 1 : Factoriser pour faire apparaître d
On a :
\begin{align*}
A &= \ldots \\
  &= \ldots \\
  &= d \times (\ldots)
\end{align*}

% Étape 2 : Poser K si nécessaire
Posons $K = \ldots \in \mathbb{N}$

% Étape 3 : Conclusion
On a : $A = d \times K$, avec $K \in \mathbb{N}$.

Par conséquent, $A$ est \textbf{divisible par $d$} (ou : est un \textbf{multiple de $d$}).
```

### Format — Démonstration en deux temps (montrer puis déduire)

```latex
% PARTIE 1 : Montrer la forme factorisée
Montrons que $A = 9(15^{n+1}-1)$. On a :
\begin{align*}
A &= 3^{n+3} \times 5^{n+1} - 9 \\
  &= 3^{(n+1)+2} \times 5^{n+1} - 9 \\
  &= (3^{n+1} \times 3^2) \times 5^{n+1} - 9 \\
  &= (3^{n+1} \times 5^{n+1}) \times 9 - 9 \\
  &= (3 \times 5)^{n+1} \times 9 - 9 \\
  &= 9(15^{n+1}-1)
\end{align*}
Donc $A = 9(15^{n+1}-1)$.

% PARTIE 2 : Déduire la divisibilité
Déduisons que $A$ est un multiple de $18$.

D'après la question a), $15^{n+1}$ est un nombre impair.
Il existe donc un entier $k \in \mathbb{N}$ tel que $15^{n+1} = 2k+1$.
Alors $15^{n+1} - 1 = (2k+1)-1 = 2k$.
Par conséquent, $15^{n+1}-1$ est un nombre pair.
On a donc : $A = 9(15^{n+1}-1) = 9(2k) = 18k$.

Par conséquent, $A$ est un \textbf{multiple de $18$}.
```

### Justifications obligatoires en arithmétique

| Opération | Justification à écrire |
|-----------|----------------------|
| Développer une puissance | pas de mention, montrer les étapes |
| Factoriser un exposant | écrire l'étape intermédiaire explicitement |
| Utiliser un résultat précédent | `D'après la question a),` |
| Poser l'existence d'un entier | `Il existe donc un entier $k \in \mathbb{N}$ tel que` |
| Filtrer par contrainte | `On sait que $n \geq 2$, donc $2n \geq 4$. Alors $\min(2,2n) = 2$.` |

---

## 4. RÈGLE ABSOLUE — DÉCOMPOSITION EN FACTEURS PREMIERS

### Format — Tableau de divisions successives

```latex
On effectue les divisions successives par les nombres premiers :

\[
\begin{array}{r|l}
450 & 2 \\
225 & 3 \\
75  & 3 \\
25  & 5 \\
5   & 5 \\
1   &
\end{array}
\]

Par conséquent, $X = 2 \times 3^2 \times 5^2$.
```

### Format — Vérification d'une décomposition

```latex
% Toujours partir du membre de gauche et développer algébriquement
Vérification de la décomposition de $Y$. On a :
\begin{align*}
Y &= 5^{2n+2} - 5^{2n} \\
  &= 5^{2n} \times 5^2 - 5^{2n} \times 1 \\
  &= 5^{2n}(5^2 - 1) \\
  &= 5^{2n}(24) \\
  &= 5^{2n} \times (2^3 \times 3) \\
  &= 2^3 \times 3 \times 5^{2n}
\end{align*}
Par conséquent, la décomposition $Y = 2^3 \times 3 \times 5^{2n}$ \textbf{est vérifiée}.
```

---

## 5. RÈGLE ABSOLUE — PGCD ET PPCM

### Format standard

```latex
On a les décompositions :
\[X = 2^1 \times 3^2 \times 5^2 \quad \text{et} \quad Y = 2^3 \times 3^1 \times 5^{2n}\]

% PGCD
\textbf{Calcul du PGCD$(X\,;\,Y)$} : On prend les facteurs premiers communs
avec le plus petit exposant.

On sait que $n \geq 2$, donc $2n \geq 4$. Alors $\min(2,2n) = 2$.

\[\text{PGCD}(X\,;\,Y) = 2^1 \times 3^1 \times 5^2 = 2 \times 3 \times 25 = 150\]

Par conséquent, $\text{PGCD}(X\,;\,Y) = 150$.

% PPCM
\textbf{Calcul du PPCM$(X\,;\,Y)$} : On prend tous les facteurs premiers
(communs ou non) avec le plus grand exposant.

On sait que $n \geq 2$, donc $2n \geq 4$. Alors $\max(2,2n) = 2n$.

\[\text{PPCM}(X\,;\,Y) = 2^3 \times 3^2 \times 5^{2n} = 8 \times 9 \times 5^{2n} = 72 \times 5^{2n}\]

Par conséquent, $\text{PPCM}(X\,;\,Y) = 72 \times 5^{2n}$.
```

### Format — Algorithme d'Euclide

```latex
On effectue les divisions euclidiennes successives :
\begin{align*}
255 &= 1 \times 141 + 114 \\
141 &= 1 \times 114 + 27  \\
114 &= 4 \times 27  + 6   \\
27  &= 4 \times 6   + 3   \\
6   &= 2 \times 3   + 0
\end{align*}
\textit{Le reste est nul, on s'arrête.}

Par conséquent, $\text{pgcd}(255\,;\,141) = 3$.
```

---

## 6. RÈGLE ABSOLUE — NOMBRES PREMIERS

### Format — Test de primalité

```latex
Pour montrer que $163$ est premier, on vérifie que $\sqrt{163} < 13$.
Il suffit de tester les diviseurs premiers $p \leq 12$ : $2, 3, 5, 7, 11$.

\begin{itemize}
    \item $163$ n'est pas pair, donc $2 \nmid 163$.
    \item $1+6+3 = 10$ n'est pas divisible par $3$, donc $3 \nmid 163$.
    \item $163$ ne se termine pas par $0$ ou $5$, donc $5 \nmid 163$.
    \item $163 = 23 \times 7 + 2$, donc $7 \nmid 163$.
    \item $163 = 14 \times 11 + 9$, donc $11 \nmid 163$.
\end{itemize}

Par conséquent, $163$ est un nombre \textbf{premier}.
```

---

## 7. RÈGLE ABSOLUE — ENTIER X = fraction ∈ N (type "diviseurs")

### Format standard

```latex
% Étape 1 : Réécrire sous forme a + r/(n+c)
Vérifions que : $X = 2 + \dfrac{15}{n+3}$

On part de l'expression $2 + \dfrac{15}{n+3}$ et on la met au même dénominateur :
\[2 + \frac{15}{n+3} = \frac{2(n+3)}{n+3} + \frac{15}{n+3} = \frac{2n+6+15}{n+3} = \frac{2n+21}{n+3}\]

Par conséquent, $X = 2 + \dfrac{15}{n+3}$.

% Étape 2 : Condition pour X ∈ N
On utilise la forme : $X = 2 + \dfrac{15}{n+3}$

Pour que $X \in \mathbb{N}$, il faut et il suffit que $\dfrac{15}{n+3} \in \mathbb{N}$
(puisque $2 \in \mathbb{N}$).

$\dfrac{15}{n+3} \in \mathbb{N}$ signifie que $(n+3)$ est un diviseur de $15$.

Les diviseurs de $15$ sont $D_{15} = \{1\,;\,3\,;\,5\,;\,15\}$.

De plus, $n \geq 1$, alors $n+3 \geq 4$.
On ne retient que les diviseurs supérieurs ou égaux à $4$ :
Les cas possibles pour $(n+3)$ sont $5$ et $15$.

% Étape 3 : Examiner les cas
On examine ces deux cas :
\begin{itemize}
    \item Si $n+3 = 5$, alors $n = 5-3 = 2$.
    \item Si $n+3 = 15$, alors $n = 15-3 = 12$.
\end{itemize}

% Étape 4 : Appliquer la contrainte supplémentaire si elle existe
Puisque $n$ est non premier, la seule valeur de $n$ pour laquelle $X \in \mathbb{N}$
est $\boxed{n = 12}$.
```

---

## 8. CONCLUSIONS TYPES

| Situation | Format de conclusion |
|-----------|---------------------|
| Parité paire | `Par conséquent, $a$ est un nombre \textbf{pair}.` |
| Parité impaire | `Par conséquent, $a$ est un nombre \textbf{impair}.` |
| Multiple de d | `Par conséquent, $A$ est un \textbf{multiple de $d$}.` |
| Divisible par d | `Par conséquent, le nombre $A$ \textbf{est divisible par $d$}.` |
| PGCD trouvé | `Par conséquent, $\text{PGCD}(X\,;\,Y) = valeur$.` |
| PPCM trouvé | `Par conséquent, $\text{PPCM}(X\,;\,Y) = valeur$.` |
| Décomposition vérifiée | `Par conséquent, la décomposition $Y = \ldots$ \textbf{est vérifiée}.` |
| Nombre premier | `Par conséquent, $n$ est un nombre \textbf{premier}.` |
| Valeur de n | `La seule valeur de $n$ pour laquelle $X \in \mathbb{N}$ est $n = valeur$.` |

---

## 9. VOCABULAIRE OFFICIEL ARITHMÉTIQUE (TCSF Maroc)

| ✅ Correct | ❌ Incorrect |
|-----------|-------------|
| `ensemble des entiers naturels` | `les naturels` |
| `entier naturel non nul` | `entier naturel positif` |
| `nombres premiers entre eux` | `copremiers` / `coprimes` |
| `décomposition en produit de facteurs premiers` | `factorisation première` |
| `PGCD` ou `pgcd` | `GCD` / `PGDC` |
| `PPCM` ou `ppcm` | `LCM` / `PPCM` en minuscules dans les énoncés |
| `diviseurs positifs de n` | `diviseurs de n` (sans préciser positifs) |
| `carré parfait` | `carré entier` |
| `multiple de` | `divisible exactement par` |
| `algorithme d'Euclide` | `méthode d'Euclide` |
| `le reste est nul, on s'arrête` | toujours écrire cette phrase à la fin de l'algo |

---

## 10. ERREURS À NE JAMAIS COMMETTRE

1. **Ne jamais conclure sans poser k** : si on trouve `2(2n+6)+1`, toujours écrire `Posons k = 2n+6 ∈ N` avant de conclure.
2. **Ne jamais écrire `pair/impair` sans justification** : toujours passer par la forme `2k` ou `2k+1`.
3. **Ne jamais oublier `∈ N`** après chaque `Posons k = ...`.
4. **Ne jamais sauter l'étape de filtrage des diviseurs** : toujours écrire "De plus, n ≥ ..., alors n+c ≥ ...".
5. **Ne jamais utiliser `min`/`max` sans justifier** : toujours écrire "On sait que n ≥ 2, donc 2n ≥ 4. Alors min(2,2n) = 2."
6. **PGCD : toujours écrire les deux décompositions** avant de calculer.
7. **Tableau de divisions** : ne jamais sauter de ligne, écrire chaque quotient.
