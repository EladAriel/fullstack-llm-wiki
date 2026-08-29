---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/12-2025/12-04-2025-evaluator-message-formats.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.866234Z"
---
# 12 04 2025 Evaluator Message Formats

---
title: "12.04.2025: Evaluator Message Formats"
description: Available in phoenix-evals 0.22+ (Python) and @arizeai/phoenix-evals 2.0+ (TypeScript)
---

## Evaluator Message Formats

Phoenix evaluators now support flexible prompt formats in both Python and TypeScript, giving you full control over how you structure prompts for LLM-based evaluations.

### Supported Formats

**String Templates** - Simple templates with variable placeholders:

<Tabs>
  <Tab title="Python" icon="python">
    ```python
    from phoenix.evals import ClassificationEvaluator, LLM

    evaluator = ClassificationEvaluator(
        name="sentiment",
        llm=LLM(provider="openai", model="gpt-4o-mini"),
        prompt_template="Classify the sentiment: {text}",
        choices=["positive", "negative", "neutral"]
    )
    ```
  </Tab>
  <Tab title="TypeScript" icon="js">
    ```typescript
    import { createClassificationEvaluator } from "@arizeai/phoenix-evals";
    import { openai } from "@ai-sdk/openai";

    const evaluator = createClassificationEvaluator({
      name: "sentiment",
      model: openai("gpt-4o-mini"),
      promptTemplate: "Classify the sentiment: {{text}}",
      choices: { positive: 1, negative: 0, neutral: 0.5 },
    });
    ```
  </Tab>
</Tabs>

**Message Lists** - OpenAI-style arrays with `role` and `content` fields for multi-turn prompts:

<Tabs>
  <Tab title="Python" icon="python">
    ```python
    evaluator = ClassificationEvaluator(
        name="helpfulness",
        llm=llm,
        prompt_template=[
            {"role": "system", "content": "You evaluate response helpfulness."},
            {"role": "user", "content": "Question: {question}\nAnswer: {answer}"}
        ],
        choices=["helpful", "somewhat_helpful", "not_helpful"]
    )
    ```
  </Tab>
  <Tab title="TypeScript" icon="js">
    ```typescript
    const evaluator = createClassificationEvaluator({
      name: "helpfulness",
      model,
      promptTemplate: [
        { role: "system", content: "You evaluate response helpfulness." },
        { role: "user", content: "Question: {{question}}\nAnswer: {{answer}}" },
      ],
      choices: { helpful: 1, somewhat_helpful: 0.5, not_helpful: 0 },
    });
    ```
  </Tab>
</Tabs>

### Template Variable Syntax

- **Python**: Supports both f-string (`{variable}`) and mustache (`{{variable}}`) syntax with auto-detection
- **TypeScript**: Uses mustache syntax (`{{variable}}`)

### Provider Compatibility

Adapters handle provider-specific message transformations automatically:

| Provider | Transformation |
|----------|----------------|
| OpenAI | System role converted to developer role for reasoning models |
| Anthropic | System messages extracted to `system` parameter |
| Google GenAI | System messages passed via `system_instruction` |
| LiteLLM | Messages passed in OpenAI format (LiteLLM handles conversion) |
| LangChain | Converted to LangChain message objects |

#### More Information:

<Card title="Eval Prompt Templates" icon="book" href="/docs/phoenix/evaluation/how-to-evals/prompt-formats" horizontal description="Evaluator prompt formats"/>

