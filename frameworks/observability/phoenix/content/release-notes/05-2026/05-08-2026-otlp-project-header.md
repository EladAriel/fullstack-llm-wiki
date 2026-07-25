---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-08-2026-otlp-project-header.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.907666Z"
---
# 05 08 2026 Otlp Project Header

---
title: "05.08.2026: OTLP Project Routing via HTTP Header"
description: "Route OTLP traces to a named Phoenix project by setting the x-project-name HTTP header — no resource attribute required."
---

**Available in arize-phoenix 15.5.0+**

Phoenix now reads the `x-project-name` HTTP header on incoming OTLP trace exports and routes all spans in the request to that project. The header takes precedence over the `openinference.project.name` resource attribute, so tools like the OpenTelemetry Collector, Openclaw, and Daytona can route traces to the right project without modifying the instrumented application.

## Setting the header

**OpenTelemetry Collector**

```yaml
exporters:
  otlphttp:
    endpoint: http://localhost:6006
    headers:
      x-project-name: my-project
```

**Environment variable**

```bash
OTEL_EXPORTER_OTLP_HEADERS="x-project-name=my-project"
```

## Precedence rules

| Source | Priority |
|--------|----------|
| `x-project-name` HTTP header | Highest |
| `openinference.project.name` resource attribute | Second |
| Server default project | Fallback |

Every span in the request goes to the same project when the header is set, regardless of what individual spans report in their resource attributes.

## Bug fix: built-in evaluator preserved on dataset evaluator delete

**Available in arize-phoenix 15.5.1+**

Deleting a dataset evaluator link no longer removes the underlying evaluator — it stays available for other datasets.
