---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/tracing/how-to-tracing/advanced/constructing-urls.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.918557Z"
---
# Constructing Urls

---
title: "Construct Shareable URLs"
description: Link directly to projects, traces, spans, and sessions by human-readable identifiers
---

Phoenix provides redirect URLs that let you link to resources using identifiers you already know — like a project name or an OpenTelemetry trace ID — without needing to look up Phoenix's internal IDs first. These URLs are stable, shareable, and useful for bookmarks, dashboards, runbooks, and CI/CD integrations.

## URL Patterns

All redirect URLs follow the pattern `{phoenix_host}/redirects/...` and resolve to the appropriate Phoenix page.

| Resource | URL Pattern | Identifier |
| --- | --- | --- |
| Project | `/redirects/projects/{project_name}` | Project name (e.g. `default`) |
| Trace | `/redirects/traces/{trace_id}` | OpenTelemetry trace ID |
| Span | `/redirects/spans/{span_id}` | OpenTelemetry span ID |
| Session | `/redirects/sessions/{session_id}` | Session ID |
| Prompt tag | `/redirects/prompts/{prompt_id}/tags/{tag_name}` | Prompt global ID + tag name |

## Examples

### Link to a project by name

```
https://my-phoenix.example.com/redirects/projects/default
```

This resolves the project named `default` and redirects to its project page. Useful when you know the project name from your `PHOENIX_PROJECT_NAME` environment variable or `register()` call.

### Link to a trace by OpenTelemetry trace ID

```
https://my-phoenix.example.com/redirects/traces/abc123def456
```

Redirects to the trace detail view. The trace ID is the same one you see in your OpenTelemetry SDK output or logs.

### Link to a span by OpenTelemetry span ID

```
https://my-phoenix.example.com/redirects/spans/789abc012def
```

Redirects to the trace view with the span selected.

### Link to a session by session ID

```
https://my-phoenix.example.com/redirects/sessions/user-session-42
```

Redirects to the session detail view within its parent project.

## Error Handling

If the identifier doesn't match any existing resource, Phoenix displays an error page. This can happen if the resource was deleted or the identifier is misspelled.

<Tip>
Names and IDs with special characters (e.g. spaces) should be URL-encoded: `/redirects/projects/my%20project`.
</Tip>
