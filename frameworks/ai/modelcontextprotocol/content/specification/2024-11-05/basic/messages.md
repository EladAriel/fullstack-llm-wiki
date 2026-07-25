---
type: "Framework Learn Page"
framework: "Model Context Protocol"
source_repo: "https://github.com/modelcontextprotocol/modelcontextprotocol"
source_branch: "main"
source_path: "docs/specification/2024-11-05/basic/messages.mdx"
source_commit: "7634684382c3d14cf7e9f14073fe40a2d8ace3fa"
source_commit_short: "76346843"
source_commit_date: "2026-07-23T16:49:30-07:00"
generated_at: "2026-07-25T11:50:39Z"
---

---
title: Messages
type: docs
weight: 20
---

All messages in MCP **MUST** follow the
[JSON-RPC 2.0](https://www.jsonrpc.org/specification) specification. The protocol defines
three types of messages:

## Requests

Requests are sent from the client to the server or vice versa.

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

- Requests **MUST** include a string or integer ID.
- Unlike base JSON-RPC, the ID **MUST NOT** be `null`.
- The request ID **MUST NOT** have been previously used by the requestor within the same
  session.

## Responses

Responses are sent in reply to requests.

```typescript
{
  jsonrpc: "2.0";
  id: string | number;
  result?: {
    [key: string]: unknown;
  }
  error?: {
    code: number;
    message: string;
    data?: unknown;
  }
}
```

- Responses **MUST** include the same ID as the request they correspond to.
- Either a `result` or an `error` **MUST** be set. A response **MUST NOT** set both.
- Error codes **MUST** be integers.

## Notifications

Notifications are sent from the client to the server or vice versa. They do not expect a
response.

```typescript
{
  jsonrpc: "2.0";
  method: string;
  params?: {
    [key: string]: unknown;
  };
}
```

- Notifications **MUST NOT** include an ID.
