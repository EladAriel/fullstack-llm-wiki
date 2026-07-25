---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/llm-providers/google-gen-ai/gemini-evals.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.847814Z"
---
---
title: "Gemini Evals"
description: Configure and run Gemini for evals
---

### Google Gemini via Vertex AI

Use the `LLM` wrapper with the `"vertex"` provider to run evals with Gemini models. Authenticate by setting your project and location, or by passing credentials directly.

```bash
pip install "arize-phoenix-evals>=3" google-cloud-aiplatform
```

```python
import os
from phoenix.evals import LLM

os.environ["CLOUD_ML_PROJECT_ID"] = "my-project-id"
os.environ["CLOUD_ML_REGION"] = "us-central1"

llm = LLM(provider="vertex", model="gemini-2.5-flash")
llm.generate_text(prompt="Hello there, how are you?")
# Output: "Hello! I'm doing well, thank you for asking!"
```

### Google Gemini via Google AI Studio

Alternatively, use the `"google"` provider with a Google AI Studio API key:

```bash
pip install "arize-phoenix-evals>=3" google-generativeai
```

```python
import os
from phoenix.evals import LLM

os.environ["GOOGLE_API_KEY"] = "<your-api-key>"

llm = LLM(provider="google", model="gemini-2.5-flash")
llm.generate_text(prompt="Hello there, how are you?")
# Output: "Hello! I'm doing well, thank you for asking!"
```
