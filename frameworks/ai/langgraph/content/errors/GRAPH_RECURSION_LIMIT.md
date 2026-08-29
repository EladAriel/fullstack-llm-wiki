---
type: "Framework Learn Page"
framework: "LangGraph"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langgraph/errors/GRAPH_RECURSION_LIMIT.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:38:45.967019Z"
---
# Graph_Recursion_Limit

---
title: GRAPH_RECURSION_LIMIT
---

Your LangGraph @[`StateGraph`] reached the maximum number of steps before hitting a stop condition.
This is often due to an infinite loop caused by code like the example below:

:::python
```python
class State(TypedDict):
    some_key: str

builder = StateGraph(State)
builder.add_node("a", ...)
builder.add_node("b", ...)
builder.add_edge("a", "b")
builder.add_edge("b", "a")
...

graph = builder.compile()
```
:::

:::js
```typescript
import { StateGraph, StateSchema } from "@langchain/langgraph";
import { z } from "zod/v4";

const State = new StateSchema({
  someKey: z.string(),
});

const builder = new StateGraph(State)
  .addNode("a", ...)
  .addNode("b", ...)
  .addEdge("a", "b")
  .addEdge("b", "a")
  ...

const graph = builder.compile();
```
:::

However, complex graphs may hit the default limit naturally.

## Troubleshooting

* If you are not expecting your graph to go through many iterations, you likely have a cycle. Check your logic for infinite loops.

:::python
* If you have a complex graph, you can pass in a higher `recursion_limit` value into your `config` object when invoking your graph like this:

```python
graph.invoke({...}, {"recursion_limit": 1000})
```
:::

:::js
* If you have a complex graph, you can pass in a higher `recursionLimit` value into your `config` object when invoking your graph like this:

```typescript
await graph.invoke({...}, { recursionLimit: 1000 });
```
:::
