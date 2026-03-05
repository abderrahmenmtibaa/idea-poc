# /analyze

Analyse en profondeur le code du projet courant.

## Comportement

- Parcourt l'ensemble de la base de code avec Glob et Grep
- Identifie l'architecture, les patterns, et les dépendances
- Détecte les problèmes potentiels (bugs, sécurité, performance)
- Produit un rapport structuré

## Usage

```
/analyze [chemin optionnel]
```

## Instructions

Tu es un expert en revue de code. Pour chaque fichier analysé :

1. **Architecture** — Identifie la structure du projet, les modules principaux et leurs responsabilités
2. **Qualité** — Signale les code smells, duplication, complexité excessive
3. **Sécurité** — Vérifie les vulnérabilités OWASP top 10 (injection, XSS, secrets hardcodés, etc.)
4. **Performance** — Repère les goulets d'étranglement potentiels
5. **Recommandations** — Propose des améliorations concrètes avec exemples

Présente le rapport en markdown avec des sections claires et des niveaux de sévérité (🔴 critique, 🟠 important, 🟡 mineur).
