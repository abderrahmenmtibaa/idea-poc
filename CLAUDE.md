# CLAUDE.md — Configuration du projet idea-poc

Ce fichier configure le comportement de Claude Code pour ce projet.

## Commandes disponibles

| Commande | Description |
|---|---|
| `/analyze` | Analyse approfondie du code (architecture, qualité, sécurité) |
| `/review-pr` | Revue complète d'une Pull Request |
| `/fix` | Correction automatique d'un bug |
| `/test` | Génération et exécution de tests |
| `/deploy` | Déploiement vers un environnement cible |

## Agents disponibles

| Agent | Description |
|---|---|
| `code-reviewer` | Revue de code — qualité, sécurité, maintenabilité |
| `debugger` | Débogage méthodique — cause racine et correction minimale |
| `architect` | Conception technique — architecture et plan d'implémentation |
| `test-writer` | Écriture de tests — couverture complète et pertinente |

## Principes de développement

- **Minimalisme** — Ne modifie que ce qui est demandé
- **Tests** — Tout nouveau code doit être testé
- **Sécurité** — Aucun secret dans le code, valider les entrées
- **Lisibilité** — Le code est lu plus souvent qu'il n'est écrit

## Structure du projet

```
.claude/
├── commands/          # Commandes slash personnalisées
│   ├── analyze.md
│   ├── review-pr.md
│   ├── fix.md
│   ├── test.md
│   └── deploy.md
└── agents/            # Agents spécialisés
    ├── code-reviewer.md
    ├── debugger.md
    ├── architect.md
    └── test-writer.md
```
