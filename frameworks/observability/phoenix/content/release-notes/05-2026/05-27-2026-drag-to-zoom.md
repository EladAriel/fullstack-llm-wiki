---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-27-2026-drag-to-zoom.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.865087Z"
---
# 05 27 2026 Drag To Zoom

---
title: "05.27.2026: Drag-to-Zoom on Project Metric Charts"
description: "Click and drag across any project metric chart or the spans sparkline to zoom into a selected time window."
---

**Available in arize-phoenix 16.3.0+**

Project metric charts and the spans-tab sparkline now support click-and-drag to zoom into a time window. Drag across any region of the chart to set a custom time range — the selection applies to all metric panels simultaneously via the shared time-range context.

- **All metric charts covered**: latency, error rate, token usage, and the trace-count sparkline all respond to brush selection.
- **Shared time range**: dragging on any chart updates the page-level time range, keeping all panels in sync.
- **Adaptive tick density**: x-axis labels scale with the chart's rendered pixel width rather than bin count, so labels stay readable at any zoom level.
