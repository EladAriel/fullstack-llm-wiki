---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/server-evals/pre-built-metrics/levenshtein-distance.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.936375Z"
---
# Levenshtein Distance

---
title: "Levenshtein Distance"
description: "Measure the edit distance between two strings."
---

Calculates the [Levenshtein (edit) distance](https://en.wikipedia.org/wiki/Levenshtein_distance) between two strings — the minimum number of single-character insertions, deletions, or substitutions needed to transform one string into the other. A score of `0` means the strings are identical; higher scores indicate more differences.

## Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `expected` | string | Yes | — | The reference string |
| `actual` | string | Yes | — | The string to evaluate |
| `case_sensitive` | boolean | No | `true` | Whether the comparison is case-sensitive |

## Output

| Property | Value | Description |
|----------|-------|-------------|
| `score` | Integer ≥ 0 | Number of edits required; `0` = identical strings |
| Optimization | Minimize | Lower scores are better |

## Configuring Inputs

Each evaluator parameter can be set to either a **path** (a JSONPath expression that extracts a value from the evaluation parameters) or a **literal** (a fixed value typed directly). Use paths to pull from dataset inputs, task outputs, reference data, or metadata.

See [Input Mapping](/docs/phoenix/evaluation/server-evals/input-mapping) for full details on mapping modes, resolution order, and examples.

## Usage Examples

**Answer closeness** — A QA model where small paraphrasing is acceptable but significant divergence is not. **Actual** receives the model's text response; **Expected** receives the reference answer from your dataset, typically a path like `reference.answer`. Comparing average edit distance across experiment runs shows whether prompt changes are moving outputs closer to reference.

**Entity extraction quality** — A pipeline that extracts a specific named value (a product name, location, or identifier). **Actual** is the extracted value from the model's output — often a nested path like `output.entity` if the response is structured JSON. **Expected** is the ground-truth value per example in your dataset. Edit distance reveals whether extraction is improving as you iterate on prompts or model configuration.

**Comparative prompt evaluation** — Two prompt variants tested against the same dataset. **Actual** receives the response field from each run; **Expected** stays fixed, pointing to the same reference column. The variant with the lower average Levenshtein score is closer to the reference outputs.

## Notes

<Note>
The algorithm runs in O(n×m) time, where n and m are the lengths of the two strings. Performance degrades quadratically on very long inputs. Keep inputs under a few thousand characters for predictable evaluation times.
</Note>

## See Also

- [Pre-Built Metrics Overview](/docs/phoenix/evaluation/server-evals/pre-built-metrics)
- [Exact Match](/docs/phoenix/evaluation/server-evals/pre-built-metrics/exact-match) — for strict equality when approximate matching is not needed
- [JSON Distance](/docs/phoenix/evaluation/server-evals/pre-built-metrics/json-distance) — measure structural differences between two JSON values
