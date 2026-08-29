---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/post-v1prompt-2025-query.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.302851Z"
---
# Post V1Prompt 2025 Query

---
title: "Query Prompts"
api: "POST https://api.helicone.ai/v1/prompt-2025/query"
description: "Search and filter prompts with pagination"
---

Retrieves a paginated list of prompts based on search criteria and tag filters.

### Request Body

<ParamField body="search" type="string" required>
  Search term to filter prompts by name
</ParamField>

<ParamField body="tagsFilter" type="string[]" required>
  Array of tags to filter prompts (shows prompts with any of these tags)
</ParamField>

<ParamField body="page" type="number" required>
  Page number for pagination (0-based)
</ParamField>

<ParamField body="pageSize" type="number" required>
  Number of prompts to return per page
</ParamField>

### Response

Returns an array of prompt objects matching the search criteria.

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
curl -X POST "https://api.helicone.ai/v1/prompt-2025/query" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search": "support",
    "tagsFilter": ["chatbot", "customer"],
    "page": 0,
    "pageSize": 10
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    search: "support",
    tagsFilter: ["chatbot", "customer"],
    page: 0,
    pageSize: 10
  }),
});

const prompts = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
[
  {
    "id": "prompt_123",
    "name": "Customer Support Bot",
    "tags": ["support", "chatbot"],
    "created_at": "2024-01-15T10:30:00Z"
  },
  {
    "id": "prompt_456",
    "name": "Support Ticket Classifier",
    "tags": ["support", "classification"],
    "created_at": "2024-01-14T09:15:00Z"
  }
]
```

</ResponseExample> 