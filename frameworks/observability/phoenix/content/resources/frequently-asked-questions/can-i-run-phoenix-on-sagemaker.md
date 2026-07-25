---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/resources/frequently-asked-questions/can-i-run-phoenix-on-sagemaker.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.877861Z"
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
