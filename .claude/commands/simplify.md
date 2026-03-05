# /simplify

Simplifie le code sélectionné ou un fichier entier sans changer son comportement.

## Usage

```
/simplify [fichier ou extrait de code]
```

## Instructions

Tu es un expert en refactoring. Tu simplifie le code en appliquant ces principes :

### Objectifs

1. **Réduire la complexité** — Cyclomatic complexity, niveaux d'imbrication
2. **Éliminer la duplication** — DRY sans sur-abstraction
3. **Clarifier l'intention** — Noms expressifs, logique lisible à voix haute
4. **Supprimer le code mort** — Variables inutilisées, conditions jamais vraies
5. **Aplatir les structures** — Early returns, guard clauses

### Règles strictes

- **Zéro changement de comportement** — Les tests existants doivent continuer à passer
- **Pas de nouvelle dépendance**
- **Pas de sur-ingénierie** — Une simplification qui demande plus de code n'est pas une simplification
- **Préserver le style** du projet (indentation, conventions de nommage)

### Format de réponse

Présente les changements sous forme de diff commenté, avec pour chaque modification :
- Ce qui a changé
- Pourquoi c'est plus simple
- Confirmation que le comportement est identique
