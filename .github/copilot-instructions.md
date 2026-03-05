# GitHub Copilot — Project Instructions

This file configures GitHub Copilot Chat for this project.
It mirrors the commands and agents defined in `.claude/`.

---

## Available prompts (use in chat)

### Analyze code
> "Analyze this file / project: identify the architecture, quality issues, security vulnerabilities, and performance bottlenecks. Rank by severity (🔴 critical, 🟠 important, 🟡 minor) with file name and line number."

### Simplify code
> "Simplify this code without changing its behavior: reduce complexity, eliminate duplication, clarify intent, remove dead code. Show an annotated diff."

### Fix a bug
> "Fix this bug: identify the root cause, apply the minimal patch, explain why the bug existed. Do not refactor surrounding code."

### Write tests
> "Write tests for this code: cover the happy path, edge cases, and error cases. Use the existing framework. Name tests as `should_[behavior]_when_[condition]`."

### Review a PR
> "Review this PR: summarize the changes, list issues by severity, assess backward compatibility impact, give a verdict (approve / request changes)."

### Design an architecture
> "Design a solution for [need]: analyze the existing code, propose a simple and testable architecture, list trade-offs, provide a step-by-step implementation plan."

---

## Development principles

- **Minimalism** — Only change what is asked
- **Tests** — All new code must be tested
- **Security** — No secrets in code, validate user inputs
- **Readability** — Code is read more often than it is written
- **YAGNI** — Don't implement what you don't need right now
- **KISS** — Prefer the simple solution over the elegant complex one

---

## Expected responses

- Always cite the file and line number
- Provide corrected code, not just vague advice
- Explain the **why**, not just the **what**
- Respect the existing code style of the project
