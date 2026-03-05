# /test

Generate or run tests for the specified code.

## Usage

```
/test [target file or function]
```

## Instructions

1. **Analyze** — Read the target code to understand its expected behavior
2. **Generate** — Create tests covering:
   - Happy path (normal operation)
   - Edge cases (null values, empty, extremes)
   - Error cases (exceptions, invalid states)
3. **Run** — Execute the tests and verify they pass
4. **Report** — Indicate the coverage achieved

Use the test framework already present in the project (pytest, jest, vitest, etc.).
Do not introduce a new framework if one already exists.
