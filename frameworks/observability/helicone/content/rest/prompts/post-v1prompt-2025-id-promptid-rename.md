---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/post-v1prompt-2025-id-promptid-rename.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.250119Z"
---
# Post V1Prompt 2025 Id Promptid Rename

---
title: "Rename Prompt"
api: "POST https://api.helicone.ai/v1/prompt-2025/id/{promptId}/rename"
description: "Rename an existing prompt"
---

Updates the name of an existing prompt.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt to rename
</ParamField>

### Request Body

<ParamField body="name" type="string" required>
  The new name for the prompt
</ParamField>

### Response

Returns `null` on successful rename.

<RequestExample>

```bash cURL
curl -X POST "https://api.helicone.ai/v1/prompt-2025/id/prompt_123/rename" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Updated Customer Support Bot"
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/id/prompt_123/rename', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: "Updated Customer Support Bot"
  }),
});
```

</RequestExample>

<ResponseExample>

```json Response
null
```

</ResponseExample> 