# GitHub Copilot — Instructions du projet

Ce fichier configure GitHub Copilot Chat pour ce projet.
Il est le miroir des commandes et agents définis dans `.claude/`.

---

## Commandes disponibles (à utiliser dans le chat)

### Analyser le code
> "Analyse ce fichier / ce projet : identifie l'architecture, les problèmes de qualité, de sécurité et de performance. Classe par sévérité (🔴 critique, 🟠 important, 🟡 mineur) avec le fichier et le numéro de ligne."

### Simplifier le code
> "Simplifie ce code sans changer son comportement : réduis la complexité, élimine la duplication, clarifie l'intention, supprime le code mort. Montre un diff commenté."

### Corriger un bug
> "Corrige ce bug : identifie la cause racine, applique le correctif minimal, explique pourquoi le bug existait. Ne refactorise pas le code environnant."

### Écrire des tests
> "Écris des tests pour ce code : couvre le happy path, les edge cases et les cas d'erreur. Utilise le framework déjà présent. Noms de tests au format `should_[comportement]_when_[condition]`."

### Revoir une PR
> "Fais la revue de cette PR : résumé des changements, problèmes identifiés par sévérité, impact sur la rétrocompatibilité, verdict (approve / request changes)."

### Concevoir une architecture
> "Conçois une solution pour [besoin] : analyse l'existant, propose une architecture simple et testable, liste les trade-offs, donne un plan d'implémentation étape par étape."

---

## Principes de développement

- **Minimalisme** — Ne modifie que ce qui est demandé
- **Tests** — Tout nouveau code doit être testé
- **Sécurité** — Aucun secret dans le code, valider les entrées utilisateur
- **Lisibilité** — Le code est lu plus souvent qu'il n'est écrit
- **YAGNI** — N'implémente pas ce dont tu n'as pas besoin maintenant
- **KISS** — Préfère la solution simple à l'élégante complexe

---

## Réponses attendues

- Toujours citer le fichier et le numéro de ligne
- Proposer du code corrigé, pas juste des conseils vagues
- Expliquer le **pourquoi**, pas seulement le **quoi**
- Respecter le style de code existant dans le projet
