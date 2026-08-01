---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/capabilities/thread-executor.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.863673Z"
---
# Thread Executor

The [`UseThreadExecutor`][pydantic_ai.capabilities.UseThreadExecutor] [capability](overview.md) provides a custom [`Executor`][concurrent.futures.Executor] for running sync tool functions and other sync callbacks in threads. This is useful in long-running servers (e.g. FastAPI) where the default ephemeral threads from [`anyio.to_thread.run_sync`][anyio.to_thread.run_sync] can accumulate under sustained load:

```python {test="skip"}
from concurrent.futures import ThreadPoolExecutor

from pydantic_ai import Agent
from pydantic_ai.capabilities import UseThreadExecutor

executor = ThreadPoolExecutor(max_workers=16, thread_name_prefix='agent-worker')
agent = Agent('openai:gpt-5.2', capabilities=[UseThreadExecutor(executor)])
```

See [Thread executor for long-running servers](../tools-advanced.md#thread-executor-for-long-running-servers) for more details.
