---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/07-2025/07-03-2025-cost-summaries-in-trace-headers.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.901804Z"
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