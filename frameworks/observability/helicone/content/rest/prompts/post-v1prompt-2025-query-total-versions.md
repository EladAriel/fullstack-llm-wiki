---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/post-v1prompt-2025-query-total-versions.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.302676Z"
---
# Post V1Prompt 2025 Query Total Versions

---
title: "Get Prompt Version Counts"
api: "POST https://api.helicone.ai/v1/prompt-2025/query/total-versions"
description: "Get version count statistics for a specific prompt"
---

Retrieves statistics about the total number of versions and major versions for a specific prompt.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

### Response

<ResponseField name="totalVersions" type="number">
  Total number of versions (major and minor) for this prompt
</ResponseField>

<ResponseField name="majorVersions" type="number">
  Total number of major versions for this prompt
</ResponseField>

<RequestExample>

```bash cURL
curl -X POST "https://api.helicone.ai/v1/prompt-2025/query/total-versions" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "promptId": "prompt_123"
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/query/total-versions', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    promptId: "prompt_123"
  }),
});

const versionCounts = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
{
  "totalVersions": 8,
  "majorVersions": 3
}
```

</ResponseExample> 