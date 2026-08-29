---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/get-v1prompt-2025-environments.mdx"
source_commit: "607c855f787d6cc66e83692874bf90f880a08d62"
source_commit_short: "607c855"
source_commit_date: "2026-08-25T19:59:29-04:00"
generated_at: "2026-08-29T09:39:42.303412Z"
---
# Get V1Prompt 2025 Environments

---
title: "Get Environments"
api: "GET https://api.helicone.ai/v1/prompt-2025/environments"
description: "Get all available environments across your prompts"
---

Returns a list of all environment names that have been used across your prompt versions.

### Response

<ResponseField name="environments" type="string[]">
  Array of environment names (e.g., ["production", "staging", "development"])
</ResponseField>

<RequestExample>

```bash cURL
curl -X GET "https://api.helicone.ai/v1/prompt-2025/environments" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/environments', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
  },
});

const environments = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
[
  "production",
  "staging",
  "development"
]
```

</ResponseExample>
