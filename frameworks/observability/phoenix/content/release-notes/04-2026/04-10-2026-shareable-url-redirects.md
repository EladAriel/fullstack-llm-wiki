---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2026/04-10-2026-shareable-url-redirects.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.852226Z"
---
# 04 10 2026 Shareable Url Redirects

---
title: "04.10.2026 Shareable Project URLs"
description: "Link to Phoenix projects by name without looking up internal IDs."
---

**Available in arize-phoenix 14.2.0+**

Phoenix now resolves human-readable identifiers to internal pages via redirect URLs. Navigate to `/redirects/projects/{project_name}` and Phoenix looks up the project by name and redirects to its page — no internal ID required. This makes it straightforward to construct stable, shareable links from identifiers you already use in code.

## Project URLs by Name

Use the same project name you set in `PHOENIX_PROJECT_NAME` or your `register()` call:

```
https://my-phoenix.example.com/redirects/projects/default
```

Useful for bookmarks, runbook links, dashboards, and CI/CD integrations where the project name is known but the internal Phoenix ID is not.

## All Supported Redirect Patterns

| Resource | URL Pattern | Identifier |
|---|---|---|
| Project | `/redirects/projects/{project_name}` | Project name (e.g. `default`) |
| Trace | `/redirects/traces/{trace_id}` | OpenTelemetry trace ID |
| Span | `/redirects/spans/{span_id}` | OpenTelemetry span ID |
| Session | `/redirects/sessions/{session_id}` | Session ID |
| Prompt tag | `/redirects/prompts/{prompt_id}/tags/{tag_name}` | Prompt global ID + tag name |

Names with special characters (spaces, etc.) should be URL-encoded: `/redirects/projects/my%20project`.

<CardGroup cols={2}>
  <Card title="Construct Shareable URLs" icon="link" href="/docs/phoenix/tracing/how-to-tracing/advanced/constructing-urls">
    Full reference for all Phoenix redirect URL patterns.
  </Card>
</CardGroup>
