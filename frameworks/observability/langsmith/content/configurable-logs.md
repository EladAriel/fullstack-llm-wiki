---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/configurable-logs.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.430042Z"
---
# Configurable Logs

---
title: Include HTTP headers in server logs
sidebarTitle: Logging Headers
---

By default, the [Agent Server](/langsmith/agent-server) omits HTTP headers from server logs for privacy reasons. However, logging request and correlation IDs can help you debug issues and trace requests across distributed systems. You can opt-in to logging headers for all API calls by modifying the `logging_headers` section in your [`langgraph.json`](/langsmith/application-structure#configuration-file) file.

```json
{
  "$schema": "https://langgra.ph/schema.json",
  "http": {
    "logging_headers": {
      "includes": ["request-id", "x-purchase-id", "*-trace-*"],
      "excludes": ["authorization", "x-api-key", "x-organization-id", "x-user-id"]
    }
  }
}
```

The `includes` and `excludes` lists accept exact header names or glob patterns using `*` as a wildcard to match any number of characters (case-insensitive). For your security, no other pattern types are supported.

Note that exclusions take precedence over inclusions. For example, if you include `*-id` but exclude `x-user-id`, the `x-user-id` header will not be logged.
