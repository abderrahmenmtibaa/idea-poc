# /review-pr

Effectue une revue complète d'une Pull Request.

## Usage

```
/review-pr [numéro PR ou URL]
```

## Instructions

Tu es un reviewer senior. Pour la PR fournie :

1. **Résumé des changements** — Explique ce que fait la PR en 2-3 phrases
2. **Revue du code** — Ligne par ligne sur les fichiers modifiés :
   - Logique correcte ?
   - Cas limites couverts ?
   - Tests présents et suffisants ?
3. **Impact** — Évalue la rétrocompatibilité et les effets de bord
4. **Verdict** — Approve / Request changes / Comment avec justification

Utilise `gh pr view` et `gh pr diff` pour récupérer les informations.
