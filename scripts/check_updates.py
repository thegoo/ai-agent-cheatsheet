"""
check_updates.py
Calls Claude with web search to check for AI agent instruction file
ecosystem changes, then patches index.html with any findings.
"""

import anthropic
import json
import re
from datetime import datetime, timedelta
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

REPO_ROOT   = Path(__file__).parent.parent
INDEX_HTML  = REPO_ROOT / "index.html"
LAST_RUN    = (datetime.utcnow() - timedelta(days=7)).strftime("%B %d, %Y")
TODAY       = datetime.utcnow().strftime("%B %d, %Y")

TRACKED_FILES = [
    "AGENTS.md", "CLAUDE.md", "SKILL.md",
    "copilot-instructions.md", "*.instructions.md",
    "GEMINI.md", ".claude/agents", ".claude/commands",
    ".cursor/rules",
]

TRACKED_TOOLS = [
    "GitHub Copilot", "Claude Code", "Cursor", "Windsurf",
    "OpenAI Codex", "Gemini CLI",
]

SYSTEM_PROMPT = """
You are a research agent maintaining a developer cheatsheet about AI agent
instruction files (AGENTS.md, CLAUDE.md, SKILL.md, copilot-instructions.md,
etc.). Your job is to find real, verified changes from the past week and
return structured JSON — nothing fabricated.

You will be given the current index.html. Return ONLY a JSON object with
this shape:

{
  "has_changes": true | false,
  "summary": "One sentence describing what changed.",
  "changelog_entries": [
    {
      "date": "Mar 2026",
      "type": "New | Update | Standard | Deprecated",
      "title": "Short title",
      "detail": "One or two sentence description.",
      "links": [
        {"label": "Announcement", "url": "https://..."},
        {"label": "Docs", "url": "https://..."}
      ]
    }
  ],
  "file_card_updates": [
    {
      "file": "AGENTS.md",
      "field": "desc | path | doc_links",
      "old": "exact string to find",
      "new": "replacement string"
    }
  ],
  "matrix_updates": [
    {
      "file": "AGENTS.md",
      "tool": "GitHub Copilot",
      "old_symbol": "—",
      "new_symbol": "✓"
    }
  ]
}

Rules:
- Only include entries you can verify with web search.
- If nothing changed, return has_changes: false and empty arrays.
- Dates should match the format already in the file (e.g. "Mar 2026").
- Do not include duplicate entries already in the changelog.
"""

USER_PROMPT = f"""
Today is {TODAY}. Check for changes to the AI agent instruction file
ecosystem since {LAST_RUN}. Focus on:

Tracked files: {", ".join(TRACKED_FILES)}
Tracked tools: {", ".join(TRACKED_TOOLS)}

Look for:
- New tool support for any tracked file type
- New file types introduced by any major tool
- Notable project releases (APM, Squad, copilot-sdk, anthropics/skills)
- Official doc updates or breaking changes
- Deprecations

Current index.html is provided below for context — avoid duplicating
anything already present in the changelog.

---

{INDEX_HTML.read_text(encoding="utf-8")}
"""

# ── Claude call ───────────────────────────────────────────────────────────────

def fetch_updates() -> dict:
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": USER_PROMPT}],
    )

    # Extract the final text block (after tool use)
    text = ""
    for block in response.content:
        if block.type == "text":
            text = block.text

    # Strip markdown fences if present
    text = re.sub(r"^```json\s*", "", text.strip())
    text = re.sub(r"\s*```$", "", text)

    return json.loads(text)

# ── Patch index.html ──────────────────────────────────────────────────────────

def inject_changelog(html: str, entries: list) -> str:
    """Prepend new changelog entries after the opening <div class="changelog-list"> tag."""
    if not entries:
        return html

    new_items = ""
    for e in entries:
        links_html = " ".join(
            f'<a href="{l["url"]}" target="_blank" rel="noopener" '
            f'class="doc-link" style="margin-top:6px;display:inline-block;">'
            f'{l["label"]} ↗</a>'
            for l in e.get("links", [])
        )
        new_items += f"""
      <div class="changelog-item">
        <div class="change-date">{e["date"]}</div>
        <div><span class="change-type type-{e["type"].lower()}">{e["type"]}</span></div>
        <div class="change-content">
          <strong>{e["title"]}</strong>
          <span>{e["detail"]}</span>
          {links_html}
        </div>
      </div>"""

    return html.replace(
        '<div class="changelog-list">',
        '<div class="changelog-list">' + new_items,
        1,
    )


def apply_file_card_updates(html: str, updates: list) -> str:
    for u in updates:
        if u["old"] in html:
            html = html.replace(u["old"], u["new"], 1)
        else:
            print(f"[WARN] Could not find string to replace for {u['file']} / {u['field']}")
    return html


def update_last_updated(html: str) -> str:
    month_year = datetime.utcnow().strftime("%b %Y")
    return re.sub(
        r'Last updated: \w+ \d{4}',
        f'Last updated: {month_year}',
        html,
    )

# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print(f"Checking for ecosystem updates since {LAST_RUN}...")

    result = fetch_updates()

    if not result.get("has_changes"):
        print("No changes found. index.html unchanged.")
        return

    print(f"Changes found: {result['summary']}")

    html = INDEX_HTML.read_text(encoding="utf-8")
    html = inject_changelog(html, result.get("changelog_entries", []))
    html = apply_file_card_updates(html, result.get("file_card_updates", []))
    html = update_last_updated(html)

    INDEX_HTML.write_text(html, encoding="utf-8")
    print("index.html updated.")


if __name__ == "__main__":
    main()
