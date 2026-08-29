---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/fleet/auth-format.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.694476Z"
---
# Auth Format

---
title: Auth-aware tool responses
description: Format tool responses to trigger OAuth flows and resume execution automatically.
sidebarTitle: Auth responses
mode: wide
---

Some [tools](/langsmith/fleet/tools) require user authorization (for example, Google, Slack, GitHub). LangSmith Fleet includes middleware to detect when a tool needs authorization and to pause the run with a clear prompt to the user. After the user completes auth, the same tool call is retried automatically.

## Return shape to request auth

If a tool detects missing authorization, return a JSON string containing the following fields:

```json
{
  "auth_required": true,
  "auth_url": "https://auth.example.com/start",
  "auth_id": "opaque-tracking-id"
}
```

- `auth_required`: set to `true` to signal an interrupt is needed.
- `auth_url`: where the user should be redirected to authorize.
- `auth_id`: optional correlation ID to track the auth session.

When Fleet detects this response, it interrupts the run, displays the authentication UI to the user, and automatically retries the tool call once authorization completes.

If you want your custom tools to reuse the same authentication required interrupt + UI, ensure your tools return the same shape of JSON.

<Note>
Return only this JSON as the tool's output. Avoid including additional text or content. Fleet parses the response to trigger the authentication flow.
</Note>
