# Framework Wiki Builder

Generate normalized Markdown for framework documentation into `frameworks/` using upstream official docs.

## Quick start

```bash
python3 scripts/wiki_builder/build_wiki.py --sources scripts/wiki_builder/sources.json
```

## Configure sources

Copy the example and edit:

```bash
cp scripts/wiki_builder/sources.example.json scripts/wiki_builder/sources.json
```

Each entry:

- `framework`: machine name (`fastapi`, `langchain`, `react`)
- `display_name`: human name
- `category`: one of `ai`, `ui`, `backend`, `db`, `test`, `observability`
- `source_repo`: git URL
- `source_branch`: branch name
- `source_docs_path`: path inside the repo where docs live
- `include_globs`: files to include (default: `**/*.md`, `**/*.mdx`)
- `exclude_globs`: files to skip
- `target_basename` (optional): override the output folder name

## What it writes

- `frameworks/<category>/<framework>/index.md`
- `frameworks/<category>/<framework>/metadata.json`
- `frameworks/<category>/<framework>/content/**` with per-page frontmatter:

```yaml
---
type: "Framework Learn Page"
framework: "<Display Name>"
source_repo: "<repo-url>"
source_branch: "<branch>"
source_path: "<relative/path/in/source>"
source_commit: "<full sha>"
source_commit_short: "<short sha>"
source_commit_date: "<ISO-8601>"
generated_at: "<ISO-8601>"
---
```

A simple `index.md` is created for each directory under `content/` with:

```yaml
---
type: "Framework Learn Directory Index"
framework: "<Display Name>"
generated_at: "<ISO-8601>"
---
```

## Cache and idempotency

The script clones sources into `.cache/wiki-sources/<framework>/` with `--depth=1` and hard-resets to the specified branch on subsequent runs.

## Notes

- `.mdx` files are copied as `.md` with the original body preserved.
- Images and non-Markdown assets are currently skipped.
- To limit scope, narrow `include_globs`.

