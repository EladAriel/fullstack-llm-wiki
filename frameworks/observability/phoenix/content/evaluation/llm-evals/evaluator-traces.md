---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/llm-evals/evaluator-traces.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.934092Z"
---
# Evaluator Traces

---
title: "Evaluator Traces"
---

<Frame>
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/evaluator_traces.png" alt="" />
</Frame>

<Frame caption="Evaluator traces list view">
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/evaluator_traces_page.png" alt="Evaluator traces page" />
</Frame>

<Frame caption="Evaluator trace detail view">
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/evaluator_trace.png" alt="Evaluator trace detail" />
</Frame>

Phoenix Evals automatically traces all evaluation executions, providing complete transparency into how your evaluators make decisions. This visibility is essential for achieving human alignment and building trust in your evaluation results.

## Why Tracing Matters for Human Alignment

LLM evaluations are only as good as their alignment with human judgment. To achieve this alignment, you need to:

- **Inspect Evaluator Reasoning**: See exactly how the evaluator LLM interpreted your prompt and reached its decision
- **Debug Evaluation Logic**: Identify when evaluators misunderstand instructions or make inconsistent judgments
- **Validate Prompt Engineering**: Verify that your evaluation prompts are working as intended across different examples
- **Build Confidence**: Provide stakeholders with transparent evidence of evaluation quality

## What Gets Traced

Every evaluation execution captures:

- **Input Data**: The original content being evaluated
- **Evaluation Prompts**: The exact prompts sent to evaluator LLMs
- **Model Responses**: Full reasoning and decision-making process
- **Final Scores**: Structured evaluation results and metadata
- **Execution Details**: Timing, retries, and performance metrics

## Transparency by Design

Phoenix Evals follows the **Transparency** pillar - nothing is abstracted away. You can inspect every aspect of the evaluation process, from the raw prompts to the model's step-by-step reasoning. This transparency enables you to:

- Tune evaluation prompts for better human alignment
- Identify systematic biases or errors in evaluation logic
- Provide evidence-based justification for evaluation results
- Continuously improve evaluator performance through data-driven insights

Use Phoenix's trace viewer to explore evaluation traces and ensure your evaluators are making decisions that align with human judgment.
