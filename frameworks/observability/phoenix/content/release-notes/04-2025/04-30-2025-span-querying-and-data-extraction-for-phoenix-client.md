---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-30-2025-span-querying-and-data-extraction-for-phoenix-client.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.900030Z"
---
# 04 30 2025 Span Querying And Data Extraction For Phoenix Client

---
title: "04.30.2025: Span querying & data extraction for Phoenix client"
description: Available in Phoenix 8.30+
---

<Update label="04.30.2025">

## Span Querying & Data Extraction For Phoenix Client

<Frame>
  <iframe 
    src="https://cdn.iframe.ly/SKzAJon" 
    width={1000} 
    height={400}
    allowFullScreen
  />
</Frame>

The Phoenix client now includes the **`SpanQuery` DSL**, enabling more advanced and flexible span querying for distributed tracing and telemetry data. This allows users to perform complex queries on span data, improving trace analysis and debugging.

In addition, the **`get_spans_dataframe`** method has been migrated, offering an easy-to-use way to extract span-related information as a Pandas DataFrame. This simplifies data processing and visualization, making it easier to analyze trace data within Python-based environments.

<Card title="feat: Add `SpanQuery` DSL to phoenix client and include `get_spans_dataframe` to client by anticorrelator · Pull Request #7071 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/7071" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Projects**](https://github.com/Arize-ai/phoenix/pull/7358): Add "Copy Name" button to project menu
* [**TLS**](https://github.com/Arize-ai/phoenix/pull/7370): Add independent flags for whether TLS is enabled for HTTP and gRPC servers
* [**Playground**](https://github.com/Arize-ai/phoenix/pull/7353): Log playground subscription errors
* [**API**](https://github.com/Arize-ai/phoenix/pull/7349): New RBAC primitives have been introduced for FastAPI and REST APIs
</Update>


