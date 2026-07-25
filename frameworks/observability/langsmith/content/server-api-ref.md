---
type: "Framework Learn Page"
framework: "LangSmith"
source_repo: "https://github.com/langchain-ai/docs.git"
source_branch: "main"
source_path: "src/langsmith/server-api-ref.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1df"
source_commit_date: "2026-07-25T00:27:23+00:00"
generated_at: "2026-07-25T19:08:33.395531Z"
---
# Server Api Ref

---
title: Agent Server API reference for LangSmith Deployment
sidebarTitle: Overview
---

The Agent Server API reference is available within each [deployment](/langsmith/deployment) at the `/docs` endpoint (e.g. `http://localhost:8124/docs`).

Browse the full API reference in the **Agent Server API** section in the sidebar, or see the endpoint groups below:

- [Assistants](/langsmith/agent-server-api/assistants) - Configured instances of a graph
- [Threads](/langsmith/agent-server-api/threads) - Accumulated outputs of a group of runs
- [Thread Runs](/langsmith/agent-server-api/thread-runs) - Invocations of a graph/assistant on a thread
- [Stateless Runs](/langsmith/agent-server-api/stateless-runs) - Invocations with no state persistence
- [Crons](/langsmith/agent-server-api/crons) - Periodic runs on a schedule
- [Store](/langsmith/agent-server-api/store) - Persistent key-value store for long-term memory
- [A2A](/langsmith/agent-server-api/a2a) - Agent-to-Agent Protocol endpoints
- [MCP](/langsmith/agent-server-api/mcp) - Model Context Protocol endpoints
- [System](/langsmith/agent-server-api/system) - Health checks and server info

## Authentication

For deployments to LangSmith, authentication is required. Pass the `X-Api-Key` header with each request to the Agent Server. The value of the header should be set to a valid LangSmith API key for the organization where the Agent Server is deployed.

Example `curl` command:

```shell
curl --request POST \
  --url http://localhost:8124/assistants/search \
  --header 'Content-Type: application/json' \
  --header 'X-Api-Key: LANGSMITH_API_KEY' \
  --data '{
  "metadata": {},
  "limit": 10,
  "offset": 0
}'
```
