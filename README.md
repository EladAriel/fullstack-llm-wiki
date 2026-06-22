# Fullstack LLM Wiki

Local Markdown documentation wikis for AI coding assistants.

Current wikis:

- `frameworks/ui/` - React, TanStack, Zod, shadcn/ui, and Next.js documentation
- `frameworks/backend/` - FastAPI, Pydantic, and Redis documentation
- `frameworks/db/` - Beanie, MongoDB, PostgreSQL, PyMongo, SQLAlchemy, and Alembic documentation
- `frameworks/test/` - Jest and pytest documentation

## Use With Any AI IDE

Your AI IDE should use this wiki automatically when your question is about a framework or library covered here. You should not need to paste long setup prompts or point the assistant at exact files.

Ask naturally, for example:

```text
How do FastAPI dependencies work?
What is the React pattern for server components?
How should I model SQLAlchemy relationships?
```

If you want to force a wiki lookup, say it directly:

```text
Search in the llm wiki about FastAPI dependency injection.
Look in the llm wiki for React server components.
Search the llm wiki for SQLAlchemy relationships.
```

When the IDE uses the wiki, it should follow this path:

```text
framework root index -> nearest directory index -> most specific content page
```

## Clone the wiki

Clone the wiki, open the repo root in your AI IDE, and ask questions normally:

```bash
git clone https://github.com/EladAriel/fullstack-llm-wiki.git
cd fullstack-llm-wiki
```

If you clone this repo inside another project, keep the folder name `fullstack-llm-wiki/` so the included rules can find it. If the wiki is the opened project root, paths start at `frameworks/`. If the wiki is nested inside another project, paths are prefixed with `fullstack-llm-wiki/`.

## Assign The Wiki To Your AI Tool

This repo includes native setup files so users do not have to create them manually.

To install the skill into another repo, copy the canonical skill folder into the tool-specific skill directory.

For Codex:

```bash
mkdir -p /path/to/user-repo/.agents/skills
cp -R skills/fullstack-llm-wiki-navigator /path/to/user-repo/.agents/skills/fullstack-llm-wiki-navigator
```

For Claude Code:

```bash
mkdir -p /path/to/user-repo/.claude/skills
cp -R skills/fullstack-llm-wiki-navigator /path/to/user-repo/.claude/skills/fullstack-llm-wiki-navigator
```

For Cursor:

```bash
mkdir -p /path/to/user-repo/.cursor/skills
cp -R skills/fullstack-llm-wiki-navigator /path/to/user-repo/.cursor/skills/fullstack-llm-wiki-navigator
```

For Antigravity CLI:

```bash
mkdir -p /path/to/user-repo/.antigravitycli/skills
cp -R skills/fullstack-llm-wiki-navigator /path/to/user-repo/.antigravitycli/skills/fullstack-llm-wiki-navigator
```

### Codex

Open Codex from the wiki repo root. Codex discovers the repo skill at:

```text
.agents/skills/fullstack-llm-wiki-navigator/SKILL.md
```

For another project, copy or symlink `.agents/skills/fullstack-llm-wiki-navigator/` into that project's `.agents/skills/`, or into your user skills folder. Keep this wiki repo accessible, preferably as `fullstack-llm-wiki/` inside the project.

### Claude Code

Open Claude Code from the wiki repo root. Claude can use:

```text
CLAUDE.md
.claude/skills/fullstack-llm-wiki-navigator/SKILL.md
```

For another project, copy or symlink `.claude/skills/fullstack-llm-wiki-navigator/` into that project's `.claude/skills/`, or into your user-level Claude skills folder. Keep this wiki repo accessible, preferably as `fullstack-llm-wiki/` inside the project.

### Cursor

Cursor supports skills, so this repo uses a Cursor skill instead of a Cursor rule. Rules are for always-on project guidance; this wiki is better as a skill because Cursor can invoke it for relevant framework/library questions without forcing the full instruction into every request.

Open the wiki repo in Cursor. Cursor discovers the project skill at:

```text
.cursor/skills/fullstack-llm-wiki-navigator/SKILL.md
```

For another project, copy `skills/fullstack-llm-wiki-navigator/` into that project's `.cursor/skills/`. Keep this wiki repo accessible, preferably as `fullstack-llm-wiki/` inside the project.

### Antigravity CLI

Gemini CLI is deprecated for this workflow. Use Antigravity CLI instead.

Open Antigravity CLI from the wiki repo root. Antigravity CLI discovers the project skill at:

```text
.antigravitycli/skills/fullstack-llm-wiki-navigator/SKILL.md
```

For another project, copy `skills/fullstack-llm-wiki-navigator/` into that project's `.antigravitycli/skills/`. Keep this wiki repo accessible, preferably as `fullstack-llm-wiki/` inside the project.

## Main Files

- `AGENTS.md` - shared repo instructions for tools that read agent guidance
- `CLAUDE.md` - Claude Code project memory
- `.agents/skills/fullstack-llm-wiki-navigator/SKILL.md` - Codex repo skill
- `.claude/skills/fullstack-llm-wiki-navigator/SKILL.md` - Claude Code repo skill
- `.cursor/skills/fullstack-llm-wiki-navigator/SKILL.md` - Cursor repo skill
- `.antigravitycli/skills/fullstack-llm-wiki-navigator/SKILL.md` - Antigravity CLI repo skill
- `skills/fullstack-llm-wiki-navigator/SKILL.md` - portable canonical skill instructions
- `frameworks/index.md` - global framework category index
- `frameworks/ui/index.md` - UI framework index
- `frameworks/backend/index.md` - backend framework index
- `frameworks/db/index.md` - database framework index
- `frameworks/test/index.md` - test framework index
