---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/graphql/getting-started.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.203972Z"
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
