---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/request/post-v1requestquery.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.257390Z"
---
# Post V1Requestquery

---
title: "Get Requests (Point Queries)"
sidebarTitle: "Get Requests (Point Queries)"
description: "Retrieve all requests visible in the request table at Helicone."
"twitter:title": "Get Requests (Point Queries) - Helicone OSS LLM Observability"
openapi: post /v1/request/query
---

import EUAPIWarning from "/snippets/eu-api-warning.mdx";

<EUAPIWarning />

<Warning>
  This API is optimized for point queries. For bulk queries, use the [Get
  Requests (faster)](/rest/request/post-v1requestquery-clickhouse) API.
</Warning>

The following API lets you get all of the requests
that would be visible in the request table at
[helicone.ai/requests](https://helicone.ai/requests).

### Premade examples 👇

| Filter                                                         | Description                         |
| -------------------------------------------------------------- | ----------------------------------- |
| [Get Request by User](/guides/cookbooks/getting-user-requests) | Get all the requests made by a user |

### Filter

A filter is either a FilterLeaf or a FilterBranch, and can be composed of multiple filters generating an [AST](https://en.wikipedia.org/wiki/Abstract_syntax_tree) of ANDs/ORs.

Here is how it is represented in typescript:

```ts
export interface FilterBranch {
  left: FilterNode;
  operator: "or" | "and"; // Can add more later
  right: FilterNode;
}

export type FilterNode = FilterLeaf | FilterBranch | "all";
```

This allows us to build complex filters like this:

```json
{
  "filter": {
    "operator": "and",
    "right": {
      "request": {
        "model": {
          "contains": "gpt-4"
        }
      }
    },
    "left": {
      "request": {
        "user_id": {
          "equals": "abc@email.com"
        }
      }
    }
  }
}
```
