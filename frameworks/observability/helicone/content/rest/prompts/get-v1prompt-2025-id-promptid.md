---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/get-v1prompt-2025-id-promptid.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.250302Z"
---
# Get V1Prompt 2025 Id Promptid

---
title: "Get Prompt"
api: "GET https://api.helicone.ai/v1/prompt-2025/id/{promptId}"
description: "Retrieve a specific prompt by ID"
---

Retrieves detailed information about a specific prompt including its metadata.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt to retrieve
</ParamField>

### Response

<ResponseField name="id" type="string">
  Unique identifier of the prompt
</ResponseField>

<ResponseField name="name" type="string">
  Name of the prompt
</ResponseField>

<ResponseField name="tags" type="string[]">
  Array of tags associated with the prompt
</ResponseField>

<ResponseField name="created_at" type="string">
  ISO timestamp when the prompt was created
</ResponseField>

<RequestExample>

```bash cURL
curl -X GET "https://api.helicone.ai/v1/prompt-2025/id/prompt_123" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/id/prompt_123', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
  },
});

const prompt = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
{
  "id": "prompt_123",
  "name": "Customer Support Bot",
  "tags": ["support", "chatbot"],
  "created_at": "2024-01-15T10:30:00Z"
}
```

</ResponseExample> 