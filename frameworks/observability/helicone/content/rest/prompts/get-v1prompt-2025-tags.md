---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/get-v1prompt-2025-tags.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.302327Z"
---
# Get V1Prompt 2025 Tags

---
title: "Get Prompt Tags"
api: "GET https://api.helicone.ai/v1/prompt-2025/tags"
description: "Retrieve all available prompt tags"
---

Retrieves a list of all unique tags used across all prompts in the organization.

### Response

Returns an array of unique tag strings.

<RequestExample>

```bash cURL
curl -X GET "https://api.helicone.ai/v1/prompt-2025/tags" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/tags', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
  },
});

const tags = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
[
  "support",
  "chatbot",
  "classification",
  "customer",
  "analytics",
  "qa"
]
```

</ResponseExample> 