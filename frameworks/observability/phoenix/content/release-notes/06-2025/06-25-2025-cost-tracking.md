---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/06-2025/06-25-2025-cost-tracking.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.855224Z"
---
# 06 25 2025 Cost Tracking

---
title: "06.25.2025: Cost tracking"
description: Available in Phoenix 11.0+
---

<Update label="06.25.2025">

## Cost Tracking

<Frame>
    <iframe src="https://cdn.iframe.ly/rIqN5QUj" width={1000} height={400} allowFullScreen allow="encrypted-media *;"></iframe>
</Frame>

Phoenix now allows you to track token-based costs for LLM runs automatically, calculating costs from token counts and model pricing data and rolling them up to trace and project levels for comprehensive analysis.

**New Features:**

* Automatic calculation of token-based costs using Phoenix's built-in model pricing table.
* Support for custom pricing configurations in **Settings > Models** when needed.
* Token counts and model information are captured automatically when using OpenInference auto-instrumentation with OpenAI, Anthropic, and other supported SDKs.
* For manual instrumentation, token count attributes can be included in spans to enable cost tracking.
* OpenTelemetry users can leverage OpenInference semantic conventions to include token counts in LLM spans.

#### More Information in our documentation:

<Card title="Cost Tracking | Phoenix" icon="book" href="/docs/phoenix/tracing/how-to-tracing/cost-tracking" horizontal description="Cost tracking guide"/>
</Update>

