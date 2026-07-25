---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/03-2026/03-05-2026-sdk-session-retrieval.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.889318Z"
---
---
title: "03.05.2026 SDK Session Retrieval"
description: "Get and list sessions programmatically from Python and TypeScript."
---

Session retrieval is now available in both the Python and TypeScript client SDKs. You can fetch individual sessions by ID or list all sessions for a project — with automatic pagination, async support, and DataFrame export built in.

## Python

The `client.sessions` resource adds three methods:

- **`get(session_id)`** — Fetch a single session with all its traces
- **`list(project_name, limit)`** — List sessions for a project with automatic pagination
- **`get_sessions_dataframe(project_name)`** — Return sessions as a pandas DataFrame

```python
from phoenix.client import Client

client = Client()

# Get a session
session = client.sessions.get(session_id="my-session-id")

# List recent sessions
sessions = client.sessions.list(project_name="my-chatbot", limit=10)

# Analyze in pandas
df = client.sessions.get_sessions_dataframe(project_name="my-chatbot")
```

Async variants are available on `AsyncClient` with the same interface.

## TypeScript

Two new functions are exported from `@arizeai/phoenix-client/sessions`:

- **`getSession({ sessionId })`** — Fetch a single session with all its traces
- **`listSessions({ projectName })`** — List all sessions for a project with automatic pagination

```javascript
import { getSession, listSessions } from "@arizeai/phoenix-client/sessions";

const session = await getSession({ sessionId: "my-session-id" });
const sessions = await listSessions({ projectName: "my-chatbot" });
```

## Return Types

Both SDKs return the same shape: each session includes `sessionId`, `projectId`, `startTime`, `endTime`, and a `traces` array. Each trace contains `traceId`, `startTime`, and `endTime`.

<CardGroup cols={2}>
  <Card title="Python SDK Reference" icon="python" href="/docs/phoenix/sdk-api-reference/python/arize-phoenix-client">
    Full Python client documentation
  </Card>
  <Card title="TypeScript SDK Reference" icon="js" href="/docs/phoenix/sdk-api-reference/typescript/arizeai-phoenix-client">
    Full TypeScript client documentation
  </Card>
</CardGroup>
