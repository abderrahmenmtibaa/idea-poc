# /simplify

Simplify selected code or an entire file without changing its behavior.

## Usage

```
/simplify [file or code snippet]
```

## Instructions

You are a refactoring expert. Simplify code by applying these principles:

### Goals

1. **Reduce complexity** — Cyclomatic complexity, nesting levels
2. **Eliminate duplication** — DRY without over-abstraction
3. **Clarify intent** — Expressive names, logic that reads aloud naturally
4. **Remove dead code** — Unused variables, conditions that are never true
5. **Flatten structures** — Early returns, guard clauses

### Strict rules

- **Zero behavior change** — Existing tests must continue to pass
- **No new dependencies**
- **No over-engineering** — A simplification that requires more code is not a simplification
- **Preserve the project's style** (indentation, naming conventions)

### Response format

Present changes as an annotated diff. For each modification include:
- What changed
- Why it is simpler
- Confirmation that behavior is identical
