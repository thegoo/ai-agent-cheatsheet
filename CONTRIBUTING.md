# Contributing to ai-agent-cheatsheet

Community reference maintained by [@thegoo](https://github.com/thegoo). PRs and issues welcome — the goal is accuracy and currency, not completeness for its own sake.

---

## What belongs here

This cheatsheet covers tools and files that developers actively use to configure and run AI coding agents. A good addition is:

- **Verifiable** — has a source link (docs page, changelog, GitHub repo, paper)
- **Scoped** — related to instruction files, agent tooling, or orchestration patterns
- **Current** — reflects how the tool actually works today, not how it worked at launch

What doesn't belong here:
- Agent frameworks for building agentic products (LangGraph, CrewAI, etc.) — that's a separate page
- Marketing claims without a source
- Tools with no meaningful instruction file or orchestration support

---

## How to contribute

### Fix something wrong

Open an issue with:
- What's incorrect
- What the correct information is
- A source link

Or raise a PR directly with the fix and a source link in the PR description.

### Add a tool or file type

Before adding, check:
1. Does the tool have documented support for instruction files or parallel agents?
2. Is there a public source (docs, changelog, GitHub) to link?
3. Is it distinct enough from existing entries to warrant its own card/row?

If yes to all three, raise a PR. Add the tool to the relevant section (Tool Landscape card, compatibility matrix row, or Projects card) and include at least one source link.

### Add a changelog entry

Changelog entries need:
- A date
- A type badge: `new`, `update`, `deprecated`, `standard`, `research`, `tool`, or `pattern`
- A source link

Use the existing entries as a template. Prepend new entries to the top of the changelog list.

### Add a tip

Tips should be things that aren't obvious from reading the docs — earned knowledge from real usage. Both the Basics and Pro Tips columns are open to additions. Keep tips concise: one strong point per tip, specific enough to act on.

---

## Style rules

**No speculation.** If you're not sure something is true, don't add it. An inaccurate cheatsheet is worse than an incomplete one.

**Source everything non-obvious.** If a fact could be questioned, link a source. Compatibility claims especially.

**Keep it scannable.** This is a reference, not a guide. Short descriptions, specific claims, no marketing language.

**Match the existing format.** The page is a single HTML file with no build system. Edit `index.html` directly. Match the existing card structure, CSS classes, and section conventions.

---

## What to tag @thegoo on

- Anything you're unsure about — compatibility claims, scoping decisions, whether something belongs
- New sections or structural changes (discuss in an issue before building)
- Deprecations — tool behavior changes fast and stale entries hurt more than missing ones

---

## Running locally

No build step. Open `index.html` in a browser.

```bash
# Clone
git clone https://github.com/thegoo/ai-agent-cheatsheet.git
cd ai-agent-cheatsheet

# Open (macOS)
open index.html

# Open (Linux)
xdg-open index.html
```

That's it.
