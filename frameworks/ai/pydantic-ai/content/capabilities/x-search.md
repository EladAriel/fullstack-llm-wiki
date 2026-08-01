---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/capabilities/x-search.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.863133Z"
---
# X Search

The [`XSearch`][pydantic_ai.capabilities.XSearch] [capability](overview.md) gives your agent search over X (Twitter) posts. It's a [provider-adaptive tool](overview.md#provider-adaptive-tools) backed by [`XSearchTool`][pydantic_ai.native_tools.XSearchTool] on the native side — see [X Search Tool](../native-tools.md#x-search-tool) for configuration options.

Unlike [Web Search](web-search.md) and [Web Fetch](web-fetch.md), there is no default non-xAI fallback: X search is only available natively on xAI models. If your agent is not running on an xAI model, set `fallback_model` explicitly to an xAI model that supports [`XSearchTool`][pydantic_ai.native_tools.XSearchTool], and search requests are delegated to that model as a subagent tool:

```python {title="x_search.py" test="skip" lint="skip"}
from pydantic_ai import Agent
from pydantic_ai.capabilities import XSearch

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    capabilities=[XSearch(fallback_model='xai:grok-4.3')],
)
```
