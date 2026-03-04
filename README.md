# AI Agent Instruction Files — The Developer Reference

A community-maintained reference for AI agent instruction files across all major tools.

**Live site:** `https://thegoo.github.io/ai-agent-cheatsheet`

## What's covered

- **Compatibility matrix** — which files each tool reads natively
- **Per-file reference** — what each file does, where it lives, starter templates
- **Changelog** — what's changed in the ecosystem and when
- **Best practices** — tips distilled from real-world usage

## Files covered

| File | Tools |
|------|-------|
| `AGENTS.md` | Universal (Copilot, Codex, Gemini CLI, Cursor, Windsurf, Zed...) |
| `CLAUDE.md` | Claude Code, GitHub Copilot |
| `.github/copilot-instructions.md` | GitHub Copilot |
| `*.instructions.md` | GitHub Copilot (path-scoped) |
| `*.agent.md` | GitHub Copilot (agent personas) |
| `*.prompt.md` | GitHub Copilot (reusable prompts) |
| `GEMINI.md` | Gemini CLI, GitHub Copilot (Gemini model) |
| `SKILL.md` | Claude Code, GitHub Copilot |
| `.claude/agents/*.md` | Claude Code |
| `.claude/commands/*.md` | Claude Code |
| `.cursor/rules/*.mdc` | Cursor |

## How to publish (GitHub Pages)

1. Create a new GitHub repo (e.g. `ai-agent-cheatsheet`)
2. Push this folder to the `main` branch
3. Go to **Settings → Pages → Source → Deploy from branch → main → / (root)**
4. Your site will be live at `https://[username].github.io/ai-agent-cheatsheet`

## Contributing

This field moves fast. If something is out of date or missing:

1. Fork the repo
2. Edit `index.html` — the changelog and matrix are straightforward to update
3. Open a PR with a source link

## Sources

- [agents.md](https://agents.md) — official AGENTS.md open standard
- [agentsmd/agents.md](https://github.com/agentsmd/agents.md) — spec repo
- [GitHub Copilot Docs](https://docs.github.com/copilot/customizing-copilot)
- [Claude Code Docs](https://code.claude.com/docs)
- [github/awesome-copilot](https://github.com/github/awesome-copilot)
- [GitHub Changelog](https://github.blog/changelog)

---

*Not affiliated with Anthropic, GitHub, Google, or OpenAI.*
