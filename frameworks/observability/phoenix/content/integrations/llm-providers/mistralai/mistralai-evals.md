---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/mistralai/mistralai-evals.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.941130Z"
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

