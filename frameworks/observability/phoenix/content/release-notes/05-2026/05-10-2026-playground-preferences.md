---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-10-2026-playground-preferences.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.907487Z"
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
