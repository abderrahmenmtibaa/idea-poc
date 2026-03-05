# /test

Génère ou exécute les tests pour le code spécifié.

## Usage

```
/test [fichier ou fonction cible]
```

## Instructions

1. **Analyse** — Lis le code cible pour comprendre son comportement attendu
2. **Génération** — Crée des tests couvrant :
   - Cas nominaux (happy path)
   - Cas limites (valeurs nulles, vides, extrêmes)
   - Cas d'erreur (exceptions, états invalides)
3. **Exécution** — Lance les tests et vérifie qu'ils passent
4. **Rapport** — Indique la couverture atteinte

Utilise le framework de test déjà présent dans le projet (pytest, jest, vitest, etc.).
Ne crée pas de nouveau framework si un existe déjà.
