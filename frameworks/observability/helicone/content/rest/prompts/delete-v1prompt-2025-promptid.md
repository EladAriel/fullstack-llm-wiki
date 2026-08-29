---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/delete-v1prompt-2025-promptid.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.301975Z"
---
# Delete V1Prompt 2025 Promptid

---
title: "Delete Prompt"
api: "DELETE https://api.helicone.ai/v1/prompt-2025/{promptId}"
description: "Delete an entire prompt and all its versions"
---

Permanently deletes a prompt and all associated versions.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt to delete
</ParamField>

### Response

Returns `null` on successful deletion.

<RequestExample>

```bash cURL
curl -X DELETE "https://api.helicone.ai/v1/prompt-2025/prompt_123" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/prompt_123', {
  method: 'DELETE',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
  },
});
```

</RequestExample>

<ResponseExample>

```json Response
null
```

</ResponseExample> 