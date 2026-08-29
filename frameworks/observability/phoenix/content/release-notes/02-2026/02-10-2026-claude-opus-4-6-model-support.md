---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2026/02-10-2026-claude-opus-4-6-model-support.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.858212Z"
---
---
title: "Release Notes"
---

# Claude Opus 4.6 Model Support

February 9, 2026

Phoenix playground now supports Claude Opus 4.6, Anthropic's latest flagship model. Select `claude-opus-4-6` in the Anthropic provider or `anthropic.claude-opus-4-6-v1` in AWS Bedrock to start using the model with full extended thinking parameter support and accurate cost tracking.

**Key capabilities:**

- **Anthropic provider integration:** Access Claude Opus 4.6 directly through the playground with the `thinking` invocation parameter enabled for extended reasoning workflows
- **AWS Bedrock support:** Deploy Opus 4.6 through Bedrock with the region-specific model identifier
- **Automatic cost tracking:** Token costs are calculated using the latest pricing ($5 per million input tokens, $25 per million output tokens, plus cache read/write rates)

The model appears in playground dropdowns alongside other Claude models and inherits the same reasoning capabilities as other Claude 4.x models.