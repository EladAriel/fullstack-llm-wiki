---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/02-2026/02-12-2026-dataset-evaluators.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.887880Z"
---
# 02 12 2026 Dataset Evaluators

---
title: "Dataset Evaluators"
description: "Attach evaluators to datasets for automatic scoring during experiments."
---

**Requires Phoenix 13.x.**

**Dataset evaluators** let you attach evaluators directly to a dataset so they automatically run server-side whenever you execute experiments from the Phoenix UI (for example, from the Playground). This turns your dataset into a reusable evaluation suite and removes the need to reconfigure evaluators for every experiment.

**Key capabilities:**

- **Attach once, evaluate everywhere:** Add LLM or built-in code evaluators to a dataset and reuse them across Playground experiments.
- **Flexible input mapping:** Map evaluator inputs to dataset fields so each example is evaluated consistently.
- **Built-in visibility:** Each evaluator captures traces for debugging and refinement, with details available from the evaluator view.

To get started, open a dataset, navigate to the **Evaluators** tab, click **Add evaluator**, configure your input mapping, and run an experiment from the Playground to see server-side scores and traces.
