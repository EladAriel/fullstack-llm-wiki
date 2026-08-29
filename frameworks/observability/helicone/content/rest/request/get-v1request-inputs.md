---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/request/get-v1request-inputs.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.282872Z"
---
# Get V1Request Inputs

---
title: "Get Request Inputs"
sidebarTitle: "Get Request Inputs"
description: "Retrieve the prompt template inputs (variables) used for a specific request made through AI Gateway prompt management."
"twitter:title": "Get Request Inputs - Helicone OSS LLM Observability"
openapi: get /v1/request/{requestId}/inputs
---

import EUAPIWarning from "/snippets/eu-api-warning.mdx";

<EUAPIWarning />

## Overview

When you use [Prompt Management](/features/advanced-usage/prompts/overview) through the AI Gateway, template variables (inputs) are stored automatically. This endpoint lets you retrieve those inputs by request ID — useful for building testing pipelines that replay past requests against new prompt versions.

## Use Cases

- **Regression testing**: Pull a past request's inputs and replay them against a new prompt version to validate behavior.
- **Prompt comparison**: Compare outputs across prompt versions using the same inputs, without storing inputs separately on your end.
- **Debugging**: Inspect the exact variables that were injected into a prompt template at runtime.

<Note>Request data is retained for 90 days. Plan your testing workflows accordingly.</Note>

## Response

Returns `null` for `data` if the request has no associated inputs (e.g., the request was not made through prompt management, or the request ID doesn't exist).

### Example Response

```json
{
  "data": {
    "inputs": {
      "customer_name": "Sarah",
      "issue": "refund request"
    },
    "prompt_id": "customer-support",
    "version_id": "1c7a86c8-...",
    "environment": "production"
  },
  "error": null
}
```

### No Inputs Found

```json
{
  "data": null,
  "error": null
}
```
