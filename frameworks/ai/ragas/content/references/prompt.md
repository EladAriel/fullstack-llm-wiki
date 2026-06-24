---
type: "Framework Learn Page"
framework: "Ragas"
source_repo: "https://github.com/vibrantlabsai/ragas"
source_branch: "main"
source_path: "docs/references/prompt.md"
source_commit: "298b68274234c060deacab3cf5fb52aa3a20e885"
source_commit_short: "298b6827"
source_commit_date: "2026-02-24T13:17:18+05:30"
generated_at: "2026-06-23T13:55:50Z"
---

# Prompt API Reference

The prompt system in Ragas provides a flexible and type-safe way to define prompts for LLM-based metrics and other components. This page documents the core prompt classes and their usage.

## Overview

Ragas uses a modular prompt architecture based on the `BasePrompt` class. Prompts can be:

- **Input/Output Models**: Pydantic BaseModel classes that define the structure of prompt inputs and outputs
- **Prompt Classes**: Inherit from `BasePrompt` to define instructions, examples, and prompt generation logic
- **String Prompts**: Simple text-based prompts for backward compatibility

## Core Classes

::: ragas.prompt
    options:
        members:
            - BasePrompt
            - StringPrompt
            - InputModel
            - OutputModel
            - PydanticPrompt
            - BoolIO
            - StringIO
            - PromptMixin

## Metrics Collections Prompts

Modern metrics in Ragas use specialized prompt classes. Each metric module contains:

- **Input Model**: Defines what data the prompt needs (e.g., `FaithfulnessInput`)
- **Output Model**: Defines the expected LLM response structure (e.g., `FaithfulnessOutput`)
- **Prompt Class**: Inherits from `BasePrompt` to generate the prompt string with examples and instructions

### Example: Faithfulness Metric Prompts

```python
from ragas.metrics.collections.faithfulness.util import (
    FaithfulnessPrompt,
    FaithfulnessInput,
    FaithfulnessOutput,
)

# The prompt class combines input/output models with instructions and examples
prompt = FaithfulnessPrompt()

# Create input data
input_data = FaithfulnessInput(
    response="The capital of France is Paris.",
    context="Paris is the capital and most populous city of France."
)

# Generate the prompt string for the LLM
prompt_string = prompt.to_string(input_data)

# The output will be structured according to FaithfulnessOutput model
```

### Available Metric Prompts

See the individual metric documentation for details on their prompts:

- [Faithfulness](../concepts/metrics/available_metrics/faithfulness.md)
- [Context Recall](../concepts/metrics/available_metrics/context_recall.md)
- [Context Precision](../concepts/metrics/available_metrics/context_precision.md)
- [Answer Correctness](../concepts/metrics/available_metrics/answer_correctness.md)
- [Factual Correctness](../concepts/metrics/available_metrics/factual_correctness.md)
- [Noise Sensitivity](../concepts/metrics/available_metrics/noise_sensitivity.md)

## Customization

For detailed guidance on customizing prompts for metrics, see [Modifying prompts in metrics](../howtos/customizations/metrics/modifying-prompts-metrics.md).
