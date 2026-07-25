---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/mistralai/mistralai-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.853151Z"
---
---
title: "MistralAI evals"
sidebarTitle: "MistralAI Evals"
description: Configure and run MistralAI for evals
---

### Using MistralAI with Phoenix Evals

<Info>
Need to install extra dependency `mistralai`

</Info>

```python
from phoenix.evals import LLM

model = LLM(provider="litellm", model="mistral/mistral-large-latest")
```

## **Usage**

```python
# model = Instantiate your LLM here
model.generate_text(prompt="Hello there, how are you?")
# Output: "As an artificial intelligence, I don't have feelings, 
#          but I'm here and ready to assist you. How can I help you today?"
```

