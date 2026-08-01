---
type: "Framework Learn Page"
framework: "Pydantic AI"
source_repo: "https://github.com/pydantic/pydantic-ai.git"
source_branch: "main"
source_path: "docs/capabilities/handle-deferred-tool-calls.md"
source_commit: "bf2c7315ecc26d446b872c544bb501a01066b4e2"
source_commit_short: "bf2c731"
source_commit_date: "2026-08-01T09:04:12+00:00"
generated_at: "2026-08-01T12:41:00.866232Z"
---
# Handle Deferred Tool Calls

[`HandleDeferredToolCalls`][pydantic_ai.capabilities.HandleDeferredToolCalls] is a [capability](overview.md) that resolves [deferred tool calls](../deferred-tools.md) inline during an agent run. When tools require approval or external execution, the agent normally pauses and returns [`DeferredToolRequests`][pydantic_ai.tools.DeferredToolRequests] as output; this capability intercepts those calls, invokes your handler to resolve them, and continues the run automatically:

```python {title="handle_deferred_tool_calls.py"}
from pydantic_ai import Agent, RunContext
from pydantic_ai.capabilities import HandleDeferredToolCalls
from pydantic_ai.tools import DeferredToolRequests, DeferredToolResults


async def handle_deferred(ctx: RunContext, requests: DeferredToolRequests) -> DeferredToolResults:
    return requests.build_results(approve_all=True)  # (1)!


agent = Agent('openai:gpt-5.2', capabilities=[HandleDeferredToolCalls(handle_deferred)])
```

1. Auto-approve every call that's waiting on approval. Real handlers typically inspect `requests.approvals` and `requests.calls` and decide per call — prompt an operator, check a policy, or execute an external call.

The handler may be sync or async. It returns [`DeferredToolResults`][pydantic_ai.tools.DeferredToolResults] with results for some or all pending calls, or `None` to decline — in which case the next `HandleDeferredToolCalls` capability in the chain gets a chance, and unhandled calls bubble up as `DeferredToolRequests` output as usual.

See [Resolving deferred calls with a handler](../deferred-tools.md#resolving-deferred-calls-with-a-handler) for how this fits into the wider deferred-tools flow, including human-in-the-loop approval and external tool execution.
