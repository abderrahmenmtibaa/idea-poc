# /review-pr

Perform a complete Pull Request review.

## Usage

```
/review-pr [PR number or URL]
```

## Instructions

You are a senior reviewer. For the given PR:

1. **Summary of changes** — Explain what the PR does in 2-3 sentences
2. **Code review** — Go through each modified file:
   - Is the logic correct?
   - Are edge cases covered?
   - Are tests present and sufficient?
3. **Impact** — Assess backward compatibility and side effects
4. **Verdict** — Approve / Request changes / Comment with justification

Use `gh pr view` and `gh pr diff` to retrieve the information.
