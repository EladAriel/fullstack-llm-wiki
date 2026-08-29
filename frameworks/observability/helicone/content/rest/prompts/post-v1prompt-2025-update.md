---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/post-v1prompt-2025-update.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.303228Z"
---
# Post V1Prompt 2025 Update

---
title: "Update Prompt"
api: "POST https://api.helicone.ai/v1/prompt-2025/update"
description: "Create a new version of an existing prompt"
---

Creates a new version of an existing prompt with updated content. Can create either a major or minor version.

### Request Body

<ParamField body="promptId" type="string" required>
  The unique identifier of the prompt to update
</ParamField>

<ParamField body="promptVersionId" type="string" required>
  The unique identifier of the current prompt version to base the update on
</ParamField>

<ParamField body="newMajorVersion" type="boolean" required>
  Whether to create a new major version (true) or minor version (false)
</ParamField>

<ParamField body="environment" type="string">
  Optional environment to set for this new version (e.g., "production", "staging", "development")
</ParamField>

<ParamField body="commitMessage" type="string" required>
  A description of the changes made in this version
</ParamField>

<ParamField body="promptBody" type="OpenAIChatRequest" required>
  The updated prompt body following OpenAI chat completion format
</ParamField>

### Response

<ResponseField name="id" type="string">
  Unique identifier of the new prompt version
</ResponseField>

<RequestExample>

```bash cURL
curl -X POST "https://api.helicone.ai/v1/prompt-2025/update" \
  -H "Authorization: Bearer $HELICONE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "promptId": "prompt_123",
    "promptVersionId": "version_456",
    "newMajorVersion": true,
    "environment": "production",
    "commitMessage": "Updated system prompt for better customer interactions",
    "promptBody": {
      "model": "gpt-4",
      "messages": [
        {
          "role": "system",
          "content": "You are an expert customer support assistant with deep knowledge of our products."
        }
      ],
      "temperature": 0.7
    }
  }'
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/update', {
  method: 'POST',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    promptId: "prompt_123",
    promptVersionId: "version_456",
    newMajorVersion: true,
    environment: "production",
    commitMessage: "Updated system prompt for better customer interactions",
    promptBody: {
      model: "gpt-4",
      messages: [
        {
          role: "system",
          content: "You are an expert customer support assistant with deep knowledge of our products."
        }
      ],
      temperature: 0.7
    }
  }),
});

const result = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
{
  "id": "version_789"
}
```

</ResponseExample> 