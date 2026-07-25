---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/05-2026/05-13-2026-playground-thinking-controls.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.907270Z"
---
# 05 13 2026 Playground Thinking Controls

---
title: "05.13.2026: Playground Thinking Controls for Anthropic and Google"
description: "The Phoenix Playground now exposes first-class thinking controls for Anthropic extended thinking and Google thinking — token budgets, effort levels, and display toggles."
---

**Available in arize-phoenix 15.8.0+**

The Phoenix Playground now surfaces dedicated controls for extended thinking on Anthropic and Google models. Thinking parameters are persisted with saved prompts and restored correctly on reload or provider switch.

## Anthropic Extended Thinking

Three controls appear when an Anthropic model is selected:

- **Thinking** — choose between **Adaptive** (model decides when to think), **Enabled** (always think), or disabled. Adaptive mode is the default for new instances.
- **Thinking Budget** — token budget allocated for the thinking block. Minimum is 1,024 tokens; maximum is capped by the `max_tokens` setting. Defaults to 5,000.
- **Thinking Display** — toggle whether the thinking block is shown inline in the Playground response panel.

Anthropic also exposes an **Effort** control (low / medium / high) for models that support output-confidence effort levels independently of extended thinking.

## Google Thinking

For Google Gemini models:

- **Thinking Budget** — maximum tokens the model may spend on internal reasoning before emitting the response.
- **Thinking Level** — preset effort level (`LOW`, `MEDIUM`, `HIGH`). Overrides the budget when set.

Thinking parameters are saved as part of the prompt version and round-tripped through storage and the SDK export format. Switching to a provider that does not support thinking drops the thinking config automatically; switching back restores it.
