# CLAUDE.md — idea-poc

This file configures Claude Code behavior for this project.

## Available Commands

| Command | Description |
|---|---|
| `/analyze` | Deep code analysis (architecture, quality, security) |
| `/review-pr` | Full Pull Request review |
| `/fix` | Automatic bug fix |
| `/test` | Test generation and execution |
| `/simplify` | Simplify code without changing behavior |
| `/deploy` | Deploy to a target environment |

## Available Agents

| Agent | Description |
|---|---|
| `code-reviewer` | Code review — quality, security, maintainability |
| `debugger` | Methodical debugging — root cause and minimal fix |
| `architect` | Technical design — architecture and implementation plan |
| `test-writer` | Test writing — full and meaningful coverage |

## Development Principles

- **Minimalism** — Only change what is asked
- **Tests** — All new code must be tested
- **Security** — No secrets in code, validate user inputs
- **Readability** — Code is read more often than it is written

## Compatibility

- **Claude Code** — Commands in `.claude/commands/`, agents in `.claude/agents/`
- **GitHub Copilot** — Instructions in `.github/copilot-instructions.md`

## Project Structure

```
.claude/
├── commands/          # Custom slash commands
│   ├── analyze.md
│   ├── review-pr.md
│   ├── fix.md
│   ├── test.md
│   ├── simplify.md
│   └── deploy.md
└── agents/            # Specialized agents
    ├── code-reviewer.md
    ├── debugger.md
    ├── architect.md
    └── test-writer.md
```
