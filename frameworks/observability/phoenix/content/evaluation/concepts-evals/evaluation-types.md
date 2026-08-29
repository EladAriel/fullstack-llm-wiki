---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/concepts-evals/evaluation-types.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.884952Z"
---
# Evaluation Types

---
title: "Eval Data Types"
description: "There are a multiple types of evaluations supported by the Phoenix Library. Each category of evaluation is categorized by its output type."
---

<Frame>
  <img src="https://storage.googleapis.com/arize-assets/phoenix/assets/images/eval_types.png" alt="" />
</Frame>

* **Categorical (binary) -** The evaluation results in a binary output, such as true/false or yes/no, which can be easily represented as 1/0. This simplicity makes it straightforward for decision-making processes but lacks the ability to capture nuanced judgements.
* **Categorical (Multi-class) -** The evaluation results in one of several predefined categories or classes, which could be text labels or distinct numbers representing different states or types.
* **Score -** The evaluation results is a numeric value within a set range (e.g. 1-10), offering a scale of measurement.&#x20;

Although score evals are an option in Phoenix, we recommend using categorical evaluations in production environments. LLMs often struggle with the subtleties of continuous scales, leading to inconsistent results even with slight prompt modifications or across different models. Repeated tests have shown that scores can fluctuate significantly, which is problematic when evaluating at scale.

Categorical evals, especially multi-class, strike a balance between simplicity and the ability to convey distinct evaluative outcomes, making them more suitable for applications where precise and consistent decision-making is important.

To explore the full analysis behind our recommendation and understand the limitations of score-based evaluations, check out [our research](https://arize.com/blog-course/numeric-evals-for-llm-as-a-judge/) on LLM eval data types.
