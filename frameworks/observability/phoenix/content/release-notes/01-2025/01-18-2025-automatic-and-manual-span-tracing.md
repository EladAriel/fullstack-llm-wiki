---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/01-2025/01-18-2025-automatic-and-manual-span-tracing.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.903738Z"
---
# 01 18 2025 Automatic And Manual Span Tracing

---
title: "01.18.2025: Automatic & manual span tracing"
description: Available in Phoenix 7.9+
---

<Update label="01.18.2025" description="">

## Automatic & Manual Span Tracing

<Frame>
  <iframe
    src="https://cdn.iframe.ly/eYTN9GP"
    width={1000}
    height={400}
    allowFullScreen
  />
</Frame>

In addition to using our automatic instrumentors and tracing directly using OTEL, we've now added our own layer to let you have the granularity of manual instrumentation without as much boilerplate code.

You can now access a tracer object with streamlined options to trace functions and code blocks. The main two options are:

* Using the **decorator** `@tracer.chain` traces the entire function automatically as a Span in Phoenix. The input, output, and status attributes are set based on the function's parameters and return value.
* Using the tracer in a `with` clause allows you to trace specific code blocks within a function. You manually define the Span name, input, output, and status.

Check out the [docs](/docs/phoenix/tracing/how-to-tracing/setup-tracing/instrument#using-helpers) for more on how to use tracer objects.
</Update>
