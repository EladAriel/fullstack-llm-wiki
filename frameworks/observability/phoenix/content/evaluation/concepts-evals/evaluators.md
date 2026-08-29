---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/concepts-evals/evaluators.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.885950Z"
---
# Evaluators

---
title: "Evaluators"
description: Definition and types of Evaluators. Score abstraction.
---

At the core, an Evaluator is anything that returns a Score. Evaluators can be split into two broad categories:

* LLM-based: evaluators that use an LLM to perform the judgement.
  * Examples: faithfulness, retrieval relevance
* Code: evaluators that use a deterministic process or heuristic calculation.
  * Examples: exact match, BLEU, precision

## Scores

* Every score has the following properties:
  * name: The human-readable name of the score/evaluator.
  * kind: The origin of the evaluation signal (llm, code, or human)
  * direction: The optimization direction; whether a high score is better or worse
* Scores may also have some of the following properties:
  * score: numeric score
  * label: The categorical outcome (e.g., "good", "bad", or other label).
  * explanation: A brief rationale or justification for the result.
  * metadata: Arbitrary extra context such as model details, intermediate scores, or run info.

## Properties of Evaluators

All phoenix-evals `Evaluators` have the following properties:&#x20;

* Sync and async evaluate methods for evaluating a single record or example&#x20;
* Single record evals return a list of `Score` objects. Oftentimes, this is a list of length 1 (e.g. `exact_match`), but some evaluators return multiple scores (e.g. precision-recall).
* A discoverable `input_schema` that describes what inputs it requires to run.
* Evaluators accept an arbitrary `eval_input` payload, and an optional `input_mapping` which map/transforms the input to the shape they require.&#x20;
