---
name: framework-wiki-builder
description: Build or refresh a local LLM-friendly frameworks wiki under frameworks/** from upstream official docs. Use when asked to generate, update, or add frameworks to this wiki. Input is a JSON config describing sources. Output is normalized Markdown with Framework Learn frontmatter, directory indexes, and metadata.json.
---

# Framework Wiki Builder

Builds this repository's `frameworks/` wiki from upstream official documentation. Produces consistent, LLM-friendly Markdown with stable frontmatter that matches this repo's existing wikis.

Use when:
- You need to recreate the wiki (first-time build)
- You want to refresh one or more frameworks to a newer source commit
- You want to add a new framework from its official docs

Do not use when:
- Answering questions from the wiki (use `fullstack-llm-wiki-navigator`)
- Editing content by hand (the builder will overwrite generated pages)

## Inputs

- `scripts/wiki_builder/sources.json` (you create it by copying `sources.example.json`)
  - An array of source definitions:
    - `framework` (string): machine name, e.g. `fastapi`, `langchain`, `react`
    - `display_name` (string): human name, e.g. `FastAPI`, `LangChain`
    - `category` (one of `ai`, `ui`, `backend`, `db`, `test`): determines target area under `frameworks/`
    - `source_repo` (string): git URL, e.g. `https://github.com/fastapi/fastapi.git`
    - `source_branch` (string): branch to read, e.g. `master` or `main`
    - `source_docs_path` (string): path within repo where docs live
    - `include_globs` (array<string>): file patterns to include (e.g. `**/*.md`, `**/*.mdx`)
    - `exclude_globs` (array<string>): file patterns to exclude (optional)
    - `target_basename` (string, optional): override folder name under `frameworks/<category>/`

## Outputs

- `frameworks/<category>/<framework>/index.md` — root Learn Wiki page with status metadata
- `frameworks/<category>/<framework>/metadata.json` — build metadata (source repo, commit, timestamps)
- `frameworks/<category>/<framework>/content/**` — normalized content pages:
  - Each page starts with frontmatter:
    - `type: "Framework Learn Page"` (or `"Framework Learn Directory Index"` for directory listings)
    - `framework`, `source_repo`, `source_branch`, `source_path`, `source_commit`, `source_commit_short`, `source_commit_date`, `generated_at`

The builder also creates directory-level `index.md` files with `type: "Framework Learn Directory Index"` that link child pages and subdirectories.

## How to run

1) Prepare config:
   - Copy `scripts/wiki_builder/sources.example.json` to `scripts/wiki_builder/sources.json`
   - Edit entries to match the frameworks you want to (re)build

2) Run the builder:

```bash
python3 scripts/wiki_builder/build_wiki.py --sources scripts/wiki_builder/sources.json
```

3) Review the diff and commit:

```bash
git add frameworks/**
git commit -m "wiki: rebuild frameworks from official docs"
```

## Notes and behavior

- Shallow clones: By default, the script performs a `--depth=1` clone of each source repo into `.cache/wiki-sources/<framework>/`.
- Idempotent: Running the builder again with the same source state re-writes the same normalized files.
- Frontmatter parity: The fields match those already present in this repo so consumers can rely on a stable schema.
- Format: `.mdx` sources are copied as `.md` with original body preserved; non-Markdown files are skipped.
- Safety: Only touches the target framework directory under `frameworks/<category>/<framework>/`.

## Common pitfalls

- Private or rate-limited sources: ensure the repo is public or your environment has credentials.
- Non-Markdown docs: the starter script processes `.md`/`.mdx`. Extend `include_globs` and add converters if needed.
- Large doc sets: narrow with `include_globs` and `exclude_globs` to keep the local wiki focused.

## Extending

- Add per-framework normalizers (e.g., header extraction, image handling)
- Convert `.mdx` components to plain Markdown
- Pull source last-modified dates per file instead of per-HEAD
- Generate richer directory maps (ordering, titles)

