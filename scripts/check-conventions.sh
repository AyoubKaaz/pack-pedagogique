#!/bin/bash
# check-conventions.sh — Vérifie les conventions source.tex d'un chapitre

if [ -z "$1" ]; then
    echo "Usage: $0 <nom_chapitre>  (ex: ch02_arithmetique)"
    exit 1
fi

CHAPITRE="$1"
SOURCE="chapitres/$CHAPITRE/source.tex"
CLAUDE_MD="chapitres/$CHAPITRE/CLAUDE.md"
PAGE1="chapitres/$CHAPITRE/Page1.tex"
ERRORS=0

if [ ! -f "$SOURCE" ]; then
    echo "❌ Fichier introuvable : $SOURCE"
    exit 1
fi

echo "=== Vérification des conventions : $CHAPITRE ==="
echo ""

# 1. \textwidth interdit dans les minipage
if grep -q '\\textwidth' "$SOURCE"; then
    COUNT=$(grep -c '\\textwidth' "$SOURCE")
    echo "❌ \\textwidth trouvé ($COUNT occurrence(s)) — utiliser \\linewidth dans les minipage"
    ERRORS=$((ERRORS + 1))
fi

# 2. \mathbb{N} interdit (doit être \N)
if grep -q '\\mathbb{N}' "$SOURCE"; then
    COUNT=$(grep -c '\\mathbb{N}' "$SOURCE")
    echo "❌ \\mathbb{N} trouvé ($COUNT occurrence(s)) — utiliser \\N"
    ERRORS=$((ERRORS + 1))
fi

# 3. \operatorname{pgcd} interdit (doit être \pgcd)
if grep -q '\\operatorname{pgcd}' "$SOURCE"; then
    COUNT=$(grep -c '\\operatorname{pgcd}' "$SOURCE")
    echo "❌ \\operatorname{pgcd} trouvé ($COUNT occurrence(s)) — utiliser \\pgcd"
    ERRORS=$((ERRORS + 1))
fi

# 4. \dfrac interdit (doit être \frac)
if grep -q '\\dfrac' "$SOURCE"; then
    COUNT=$(grep -c '\\dfrac' "$SOURCE")
    echo "❌ \\dfrac trouvé ($COUNT occurrence(s)) — utiliser \\frac"
    ERRORS=$((ERRORS + 1))
fi

# 5. Cohérence Masse horaire entre CLAUDE.md et Page1.tex
if [ -f "$CLAUDE_MD" ] && [ -f "$PAGE1" ]; then
    MASSE_CLAUDE=$(grep -oE 'Masse horaire : [0-9]+h' "$CLAUDE_MD" | grep -oE '[0-9]+' | head -1)
    MASSE_PAGE1=$(grep -oE 'Masse Horaire[^:]*: [0-9]+ Heures' "$PAGE1" | grep -oE '[0-9]+' | head -1)

    if [ -n "$MASSE_CLAUDE" ] && [ -n "$MASSE_PAGE1" ]; then
        if [ "$MASSE_CLAUDE" != "$MASSE_PAGE1" ]; then
            echo "❌ Masse horaire incohérente : CLAUDE.md=${MASSE_CLAUDE}h  /  Page1.tex=${MASSE_PAGE1}h"
            ERRORS=$((ERRORS + 1))
        fi
    else
        [ -z "$MASSE_CLAUDE" ] && echo "⚠️  Masse horaire non trouvée dans CLAUDE.md"
        [ -z "$MASSE_PAGE1" ]  && echo "⚠️  Masse horaire non trouvée dans Page1.tex"
    fi
fi

echo ""
if [ "$ERRORS" -eq 0 ]; then
    echo "✅ Aucune erreur détectée dans $CHAPITRE"
else
    echo "❌ $ERRORS erreur(s) trouvée(s) dans $CHAPITRE"
    exit 1
fi
