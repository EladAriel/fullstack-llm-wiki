---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/post-v1prompt-2025-update-production-version.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.252087Z"
---
# Post V1Prompt 2025 Update Production Version

---
title: "Set Version Environment"
api: "POST https://api.helicone.ai/v1/prompt-2025/update/environment"
description: "Set the environment for a specific prompt version"
---

Updates the environment for a specific prompt version. Environments can be "production", "staging", "development", or any custom environment name.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt
</ParamField>

<ParamField body="promptVersionId" type="string" required>
  The unique identifier of the prompt version to update
</ParamField>

<ParamField body="environment" type="string" required>
  The environment to set for this version (e.g., "production", "staging", "development")
</ParamField>

### Response

Returns `null` on successful update.

<RequestExample>

```bash cURL
curl -X POST "https://api.helicone.ai/v1/prompt-2025/update/environment" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "promptId": "prompt_123",
    "promptVersionId": "version_789",
    "environment": "production"
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/update/environment', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    promptId: "prompt_123",
    promptVersionId: "version_789",
    environment: "production"
  }),
});
```

</RequestExample>

<ResponseExample>

```json Response
null
```

</ResponseExample> 