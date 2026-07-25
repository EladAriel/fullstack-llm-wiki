---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/delete-v1prompt-2025-promptid-versionid.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.251118Z"
---
# Delete V1Prompt 2025 Promptid Versionid

---
title: "Delete Prompt Version"
api: "DELETE https://api.helicone.ai/v1/prompt-2025/{promptId}/{versionId}"
description: "Delete a specific version of a prompt"
---

Permanently deletes a specific version of a prompt while keeping the prompt and other versions intact.

### Path Parameters

<ParamField path="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

<ParamField path="versionId" type="string" required>
  The unique identifier of the prompt version to delete
</ParamField>

### Response

Returns `null` on successful deletion.

<RequestExample>

```bash cURL
curl -X DELETE "https://api.helicone.ai/v1/prompt-2025/prompt_123/version_456" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/prompt_123/version_456', {
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