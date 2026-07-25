---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2025/03-24-2025-tracing-configuration-tab.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.891407Z"
---
# 03 24 2025 Tracing Configuration Tab

---
title: "03.24.2025: Tracing configuration tab"
description: Available in Phoenix 8.19+
---

<Update label="03.24.2025">

## Tracing Configuration Tab

<Frame>
  <iframe
    src="https://cdn.iframe.ly/7hf3YeA"
    width={1000}
    height={400}
    allowFullScreen
  />
</Frame>

Within each project, there is now a **Config** tab to enhance customization. The default tab can now be set per project, ensuring the preferred view is displayed.

Learn more in [projects docs](/docs/phoenix/tracing/llm-traces/projects).

<Card title="feat(tracing): add a config tab by mikeldking · Pull Request #6857 · Arize-ai/phoenix" icon="github" href="https://github.com/Arize-ai/phoenix/issues/6857" horizontal>
  GitHub
</Card>

### Improvements and Bug Fixes 🐛

* [**Tracing**](https://github.com/Arize-ai/phoenix/pull/6904): Use correlated subquery for orphan spans
* [**Spans**](https://github.com/Arize-ai/phoenix/releases/tag/arize-phoenix-v8.19.1): Add toggle to treat orphan spans as root
* [**Performance**](https://github.com/Arize-ai/phoenix/pull/6896): Upgrade react-router, vite, vitest
* **Experiments**: Included delete experiment option to action menu
* **Feature:** Added support for specifying admin users via an environment variable at startup
* **Annotation:** Now displays metadata
* **Settings Page:** Now split across tabs for improved navigation and easier access
* **Feedback:** Added full metadata
* **Projects:** Improved performance
* **UI:** Added date format descriptions to explanations
</Update>
