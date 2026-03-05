# /analyze

Perform a deep analysis of the current project's codebase.

## Behavior

- Traverse the entire codebase using Glob and Grep
- Identify architecture, patterns, and dependencies
- Detect potential issues (bugs, security, performance)
- Produce a structured report

## Usage

```
/analyze [optional path]
```

## Instructions

You are a code review expert. For each analyzed file:

1. **Architecture** — Identify the project structure, main modules and their responsibilities
2. **Quality** — Flag code smells, duplication, excessive complexity
3. **Security** — Check for OWASP top 10 vulnerabilities (injection, XSS, hardcoded secrets, etc.)
4. **Performance** — Spot potential bottlenecks
5. **Recommendations** — Suggest concrete improvements with examples

Present the report in markdown with clear sections and severity levels (🔴 critical, 🟠 important, 🟡 minor).
