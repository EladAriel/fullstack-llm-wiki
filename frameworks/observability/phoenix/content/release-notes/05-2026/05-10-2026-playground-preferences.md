---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-10-2026-playground-preferences.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.864318Z"
---
---
title: "05.10.2026: Playground Preferences"
description: "Save a default provider and model for the Playground, and the metrics aside is now always visible on the project page."
---

# Default Playground Provider and Model

**Available in arize-phoenix 15.6.0+**

You can now save a personal default provider and model for the Playground from the **AI Providers** settings page. Phoenix stores the preference in your browser and uses it whenever you open a new Playground session. When no preference is set, Playground falls back to the existing default (OpenAI / gpt-4o).

If you've previously configured per-provider invocation parameters (model, temperature, max tokens), those saved settings still take precedence for your preferred provider — the preference acts as a starting point, not an override.

# Span Metrics Always Visible

**Available in arize-phoenix 15.6.0+**

The metrics aside — showing latency percentiles, token counts, and error rates — is now always visible on the right side of the spans table on the project page.
