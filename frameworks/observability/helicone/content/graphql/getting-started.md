---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/graphql/getting-started.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.278363Z"
---
# Getting Started

---
title: "Getting Started"
---

## Setting Up Your API Key

First, grab your Helicone-API-key or head to our portal at https://www.helicone.ai/keys and generate a new key.

### Interactive Playground: Experiment with Queries

[https://www.helicone.ai/api/graphql](https://www.helicone.ai/api/graphql)

In the HTTP Headers section, insert the following block, replacing `HELICONE_API_KEY` with your own:

```json
{
  "authorization": "Bearer HELICONE_API_KEY"
}
```

After you've added your key, here's a sample request to get you started:

```graphql
{
  heliconeRequest(limit: 1, offset: 0) {
    prompt
    properties {
      name
    }
    responseBody
    response
  }
}
```

Our playground is equipped with IntelliSense, a handy tool that makes it easier to understand what types of fields you can query. Just press (ctrl + space)!

### Accessing the Schema Documentation

You can find the Schema Documentation on the right side of the playground interface. This is your go-to resource for understanding the structure of the data you can query. Visit our playground at [https://www.helicone.ai/api/graphql](https://www.helicone.ai/api/graphql) to explore more!
