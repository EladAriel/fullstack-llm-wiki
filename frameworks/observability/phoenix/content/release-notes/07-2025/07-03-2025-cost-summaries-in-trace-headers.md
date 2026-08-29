---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-03-2025-cost-summaries-in-trace-headers.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.849194Z"
---
# 07 03 2025 Cost Summaries In Trace Headers

---
title: "07.03.2025: Cost summaries in trace headers"
description: Available in Phoenix 11.4+
---

<Update label="07.03.2025">

## Cost Summaries In Trace Headers

<Frame>
    <iframe src="https://cdn.iframe.ly/v6DMYMvx" width={1000} height={400} allowFullScreen></iframe>
</Frame>

You can now **see total and segmented costs directly in your Phoenix trace headers** for faster debugging and spend visibility.

#### New Features:

* Extended `TraceDetails` GraphQL query to include `costSummary` fields (prompt, completion, total).
* Passes `costSummary` data into `TraceHeader` and displays formatted total cost.
* Adds a tooltip in `TraceHeader` showing **prompt vs. completion cost breakdown**.

<Card title="feat: add cost summary to trace header by RogerHYang · Pull Request #8406 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/pull/8406" horizontal>
  GitHub
</Card>
</Update>