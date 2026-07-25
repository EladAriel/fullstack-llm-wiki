---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2025/04-15-2025-display-tool-call-and-result-ids-in-span-details.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.899309Z"
---
# 04 15 2025 Display Tool Call And Result Ids In Span Details

---
title: "04.15.2025: Display tool call and result ids in span details"
description: Available in Phoenix 8.25+
---

<Update label="04.15.2025">

## Display Tool Call And Result IDs In Span Details

<Frame>
  <iframe
    src="https://cdn.iframe.ly/koXx6rf"
    width={1000}
    height={400}
    allowFullScreen
  />
</Frame>

Tool call and result IDs are now shown in the span details view. Each ID is placed within a collapsible header and can be easily copied. This update also supports spans with multiple tool calls. Get started with tracing your tool calls [here](/docs/phoenix/get-started/get-started-tracing).

<Card title="Release arize-phoenix: v8.25.0 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v8.25.0" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* **Performance**: Do not refetch tables when trace and span details closed
* **UI**: Redirect /v1/traces to root path
* **Playground**: Update GPT-4.1 models in Playground
</Update>
