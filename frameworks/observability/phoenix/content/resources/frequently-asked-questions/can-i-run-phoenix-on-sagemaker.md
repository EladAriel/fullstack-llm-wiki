---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/can-i-run-phoenix-on-sagemaker.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.950115Z"
---
# Can I Run Phoenix On Sagemaker

---
title: "Can I run Phoenix on Sagemaker?"
description: "With SageMaker notebooks, phoenix leverages the jupyter-server-proy to host the server under `proxy/6006.`Note, that phoenix will automatically try to detect that you are running in SageMaker but you can declare the notebook runtime via a parameter to `launch_app` or an environment variable"
---

```python
import os

os.environ["PHOENIX_NOTEBOOK_ENV"] = "sagemaker"
```
