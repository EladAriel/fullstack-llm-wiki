---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2025/05-09-2025-annotations-data-retention-policies-hotkeys.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.850572Z"
---
# 05 09 2025 Annotations Data Retention Policies Hotkeys

---
title: "05.09.2025: Annotations, data retention policies, hotkeys"
description: Available in Phoenix 9.0.0+
---

<Update label="05.09.2025">

## Annotations, Data Retention Policies, Hotkeys

<Frame caption="Annotation Improvements">
  <iframe src="https://cdn.iframe.ly/Gfnn20w" width={1000} height={400} allowFullScreen allow="encrypted-media *;"></iframe>
</Frame>

Phoenix v9.0.0 release brings major updates to annotation support, and a whole host of other improvements.

## [Annotations](/docs/phoenix/tracing/llm-traces/how-to-annotate-traces) 🏷️

Up until now, Phoenix has only supported one annotation of a given type on each trace. We've now unlocked that limit, allowing you to capture multiple values of an annotation label on each span.

In addition, we've added:

* API support for annotations - create, query, and update annotations through the REST API
* Additional support for code evaluations as annotations
* Support for arbitrary metadata on annotations
* Annotation configurations to structure your annotations within and across projects

<Frame caption="Annotation Configs">
  <iframe src="https://cdn.iframe.ly/MTvrorg" width={1000} height={400} allowFullScreen allow="encrypted-media *;"></iframe>
</Frame>

## [Data Retention](/docs/phoenix/settings/data-retention) 💿

Now you can create custom global and per-project data retention polices to remove traces after a certain window of time, or based on number of traces. Additionally, you can now view your disk usage in the Settings page of Phoenix.

<Frame>
  <iframe src="https://cdn.iframe.ly/Glgk78D" width={1000} height={400} allowFullScreen allow="encrypted-media *;"></iframe>
</Frame>

## Hotkeys 🔥

We've added hotkeys to Phoenix!

You can now use `j` and `k` to quickly page through your traces, and `e` and `n` to add annotations and notes - you never have to lift your hands off the keyboard again!

<Frame>
  <iframe src="https://cdn.iframe.ly/9AJ9xdm" width={1000} height={400} allowFullScreen allow="encrypted-media *;"></iframe>
</Frame>

## Full v9.0.0 Release

<Card title="Release arize-phoenix: v9.0.0 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v9.0.0" horizontal>
  GitHub
</Card>
</Update>
