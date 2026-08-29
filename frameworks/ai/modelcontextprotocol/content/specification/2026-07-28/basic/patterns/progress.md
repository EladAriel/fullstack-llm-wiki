---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/specification/2026-07-28/basic/patterns/progress.mdx"
source_commit: "ca4ab3027f7c844cd3039c956438d72e8253f7f5"
source_commit_short: "ca4ab30"
source_commit_date: "2026-08-28T21:24:44-07:00"
generated_at: "2026-08-29T09:38:48.083251Z"
---
# Progress

---
title: Progress
---

<div id="enable-section-numbers" />

The Model Context Protocol (MCP) supports optional progress tracking for long-running
operations through notification messages. The server **MAY** send progress notifications
to report the status of requests the client has issued.

## Progress Flow

When a client wants to _receive_ progress updates for a request, it includes a
`progressToken` in the request metadata.

- Progress tokens **MUST** be a string or integer value
- Progress tokens can be chosen by the client using any means, but **MUST** be unique
  across all active requests.

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "some_method",
  "params": {
    "_meta": {
      "progressToken": "abc123"
    }
  }
}
```

The server **MAY** then send progress notifications containing:

- The original progress token
- The current progress value so far
- An optional "total" value
- An optional "message" value

```json
{
  "jsonrpc": "2.0",
  "method": "notifications/progress",
  "params": {
    "progressToken": "abc123",
    "progress": 50,
    "total": 100,
    "message": "Reticulating splines..."
  }
}
```

- The `progress` value **MUST** increase with each notification, even if the total is
  unknown.
- The `progress` and the `total` values **MAY** be floating point.
- The `message` field **SHOULD** provide relevant human readable progress information.

## Behavior Requirements

1. Progress notifications **MUST** only reference tokens that:
   - Were provided in an active request
   - Are associated with an in-progress operation

2. Servers receiving a request with a progress token **MAY**:
   - Choose not to send any progress notifications
   - Send notifications at whatever frequency they deem appropriate
   - Omit the total value if unknown

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Note over Client,Server: Request with progress token
    Client->>Server: Method request with progressToken

    Note over Client,Server: Progress updates
    Server-->>Client: Progress notification (0.2/1.0)
    Server-->>Client: Progress notification (0.6/1.0)
    Server-->>Client: Progress notification (1.0/1.0)

    Note over Client,Server: Operation complete
    Server->>Client: Method response
```

## Implementation Notes

- Clients and servers **SHOULD** track active progress tokens
- Both parties **SHOULD** implement rate limiting to prevent flooding
- Progress notifications **MUST** stop after completion
