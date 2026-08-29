---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/smith-api-ref.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:39:50.678581Z"
---
# Smith Api Ref

---
title: LangSmith API reference
sidebarTitle: Overview
---

The LangSmith REST API provides programmatic access to LangSmith platform features including tracing, datasets, experiments, annotations, and more.

Browse the full API reference in the **LangSmith REST API** section in the sidebar.

## Authentication

Pass the `X-Api-Key` header with each request. The value should be a valid [LangSmith API key](/langsmith/create-account-api-key).

```shell
curl --request GET \
  --url https://api.smith.langchain.com/api/v1/workspaces \
  --header 'X-Api-Key: LANGSMITH_API_KEY'
```
