---
type: "Framework Learn Page"
framework: "Ragas"
source_repo: "https://github.com/vibrantlabsai/ragas"
source_branch: "main"
source_path: "docs/references/aevaluate.md"
source_commit: "298b68274234c060deacab3cf5fb52aa3a20e885"
source_commit_short: "298b6827"
source_commit_date: "2026-02-24T13:17:18+05:30"
generated_at: "2026-06-23T13:55:50Z"
---

# Async Evaluation

## aevaluate()

::: ragas.evaluation.aevaluate

## Async Usage

Ragas provides both synchronous and asynchronous evaluation APIs to accommodate different use cases:

### Using aevaluate() (Recommended for Production)

For production async applications, use `aevaluate()` to avoid event loop conflicts:

```python
import asyncio
from ragas import aevaluate

async def evaluate_app():
    result = await aevaluate(dataset, metrics)
    return result

# In your async application
result = await evaluate_app()
```

### Using evaluate() with Async Control

For backward compatibility and Jupyter notebook usage, `evaluate()` provides optional control over `nest_asyncio`:

```python
# Default behavior (Jupyter-compatible)
result = evaluate(dataset, metrics)  # allow_nest_asyncio=True

# Production-safe (avoids event loop patching)
result = evaluate(dataset, metrics, allow_nest_asyncio=False)
```

### Migration from nest_asyncio Issues

If you're experiencing issues with `nest_asyncio` in production:

**Before (problematic):**
```python
# This may cause event loop conflicts
result = evaluate(dataset, metrics)
```

**After (fixed):**
```python
# Option 1: Use async API
result = await aevaluate(dataset, metrics)

# Option 2: Disable nest_asyncio
result = evaluate(dataset, metrics, allow_nest_asyncio=False)
```
