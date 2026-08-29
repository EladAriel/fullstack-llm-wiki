---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/ai-gateway/get-v1models.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.295204Z"
---
# Get V1Models

---
title: "Get Models"
sidebarTitle: "Get Models (OpenAI Compatible)"
description: "Returns all available models supported by Helicone AI Gateway (OpenAI-compatible endpoint)"
openapi: get /v1/models
---

This endpoint returns a list of all AI models supported by the Helicone AI Gateway. This is an OpenAI-compatible endpoint that follows the same response format as OpenAI's `/v1/models` endpoint.

Use this endpoint to discover which models are available for routing through the AI Gateway.

## Endpoint URL

```
https://ai-gateway.helicone.ai/v1/models
```

## Example Request

```bash
curl https://ai-gateway.helicone.ai/v1/models
```

## Example Response

```json
{
  "object": "list",
  "data": [
    {
      "id": "claude-opus-4",
      "object": "model",
      "created": 1747180800,
      "owned_by": "anthropic"
    },
    {
      "id": "gpt-4o",
      "object": "model",
      "created": 1715558400,
      "owned_by": "openai"
    },
    ...
  ]
}
```

## Use Cases

- **OpenAI Compatibility**: Use this endpoint as a drop-in replacement for OpenAI's `/v1/models` endpoint
- **Model Discovery**: Discover which models are available through Helicone AI Gateway
- **Integration Testing**: Verify model availability for your applications
