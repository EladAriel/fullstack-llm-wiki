---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/patch-v1prompt-2025-id-promptid-tags.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.300739Z"
---
# Patch V1Prompt 2025 Id Promptid Tags

---
title: "Update Prompt Tags"
api: "PATCH https://api.helicone.ai/v1/prompt-2025/id/{promptId}/tags"
description: "Update the tags for a prompt"
---

Updates the tags associated with a prompt. This replaces all existing tags with the new set provided.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

### Request Body

<ParamField body="tags" type="string[]" required>
  Array of tag strings to set for the prompt
</ParamField>

### Response

<ResponseField name="tags" type="string[]">
  The updated array of tags
</ResponseField>

<RequestExample>

```bash cURL
curl -X PATCH "https://api.helicone.ai/v1/prompt-2025/id/prompt_123/tags" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "tags": ["customer-support", "v2", "production"]
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/id/prompt_123/tags', {
  method: 'PATCH',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    tags: ["customer-support", "v2", "production"]
  }),
});

const result = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
[
  "customer-support",
  "v2",
  "production"
]
```

</ResponseExample>
