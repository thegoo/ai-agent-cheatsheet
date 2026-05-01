# AI Agent Developer Reference

A community-maintained reference for developers navigating the AI coding agent ecosystem. Tools, instruction files, orchestration patterns, and what actually changed this week — all in one place.

**Live site:** https://thegoo.github.io/ai-agent-cheatsheet

---

## What's covered

| Section | What you'll find |
| --- | --- |
| **Compatibility Matrix** | Which instruction files each tool reads natively |
| **File Reference** | What each file does, where it lives, starter templates |
| **Tool Landscape** | Category map of CLI agents, IDEs, cloud agents, orchestration layers — plus parallel sub-agent comparison table |
| **Orchestration Patterns** | Three patterns (Fire and Forget, Coordinated Team, Async Background) with tool mapping and config file references |
| **Projects** | Notable tools and collections that extend or orchestrate instruction files |
| **Tips & Pro Tips** | Basics for everyone + advanced patterns for teams running real agentic workflows |
| **Changelog** | What's changed in the ecosystem and when |

---

## Instruction files covered

| File | Tools |
| --- | --- |
| `AGENTS.md` | Universal — Copilot, Codex, Gemini CLI, Cursor, Windsurf, Zed, Cline... |
| `CLAUDE.md` | Claude Code, GitHub Copilot |
| `.github/copilot-instructions.md` | GitHub Copilot (repo-wide) |
| `*.instructions.md` | GitHub Copilot (path-scoped, `.github/instructions/`) |
| `*.agent.md` | GitHub Copilot (custom agent personas, `.github/agents/`) |
| `*.prompt.md` | GitHub Copilot (reusable prompts, `.github/prompts/`) |
| `GEMINI.md` | Gemini CLI, GitHub Copilot (Gemini model) |
| `SKILL.md` | Claude Code, GitHub Copilot, Windsurf |
| `.claude/agents/*.md` | Claude Code (custom sub-agents) |
| `.claude/commands/*.md` | Claude Code (slash commands) |
| `.cursor/rules/*.mdc` | Cursor (4 loading modes) |
| `openai-codex/setup.sh` | OpenAI Codex |
| `.github/agents/*.agent.md` | GitHub Copilot (GA April 2026, replaces `.chatmode.md`) |

---

## Tools covered

**CLI Agents:** Claude Code, OpenAI Codex, Gemini CLI, OpenCode, Cline

**AI-Native IDEs:** Cursor, Windsurf, VS Code + Copilot, Zed

**Cloud / Async Agents:** Copilot Cloud Agent, Codex Automations, Cursor Background Agents

**Orchestration Layers:** Squad, SuperSet, APM

---

## Repo structure

```
ai-agent-cheatsheet/
├── index.html          # Main page — single file, no build system
├── README.md           # This file
├── CONTRIBUTING.md     # How to contribute
├── LICENSE             # MIT
├── _config.yml         # GitHub Pages config
├── .github/workflows/  # Automated ecosystem update agent
└── scripts/            # Update agent scripts
```

**Planned pages** (not yet live):
- `frameworks.html` — Agent frameworks for building agentic products (LangGraph, CrewAI, Azure AI Foundry, etc.)
- `mcp.html` — MCP servers reference: notable servers, how MCP relates to instruction files, pro tips

---

## How to deploy your own copy

1. Fork the repo
2. Go to **Settings → Pages → Source → Deploy from branch → main → / (root)**
3. Live at `https://[username].github.io/ai-agent-cheatsheet`

---

## Contributing

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide — what belongs, how to add a tool or file type, changelog entry format, and style rules.

Short version:
- Everything must be verifiable — include a source link
- No speculation, no marketing claims
- Match the existing card/row format in `index.html`
- Open an issue first for structural changes; PRs welcome for fixes and additions

---

## Sources

- [agents.md](https://agents.md) — official AGENTS.md open standard
- [agentsmd/agents.md](https://github.com/agentsmd/agents.md) — spec repo (Linux Foundation AAIF)
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code/overview)
- [github/awesome-copilot](https://github.com/github/awesome-copilot)
- [GitHub Changelog](https://github.blog/changelog)
- [Windsurf Changelog](https://windsurf.com/changelog)
- [Cursor Docs](https://docs.cursor.com)
- [OpenAI Codex Docs](https://developers.openai.com/codex)
- [Gemini CLI Docs](https://github.com/google-gemini/gemini-cli)

---

*Not affiliated with Anthropic, GitHub, Google, or OpenAI. Community reference by [@thegoo](https://github.com/thegoo).*
