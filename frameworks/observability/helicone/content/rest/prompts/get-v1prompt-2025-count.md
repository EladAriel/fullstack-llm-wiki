---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/rest/prompts/get-v1prompt-2025-count.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.252270Z"
---
# Get V1Prompt 2025 Count

---
title: "Get Prompt Count"
api: "GET https://api.helicone.ai/v1/prompt-2025/count"
description: "Get the total number of prompts"
---

Retrieves the total count of prompts in the organization.

### Response

Returns the total number of prompts as an integer.

<RequestExample>

```bash cURL
curl -X GET "https://api.helicone.ai/v1/prompt-2025/count" \
  -H "Authorization: Bearer $HELICONE_API_KEY"
```

```typescript TypeScript
const response = await fetch('https://api.helicone.ai/v1/prompt-2025/count', {
  method: 'GET',
  headers: {
    'Authorization': `Bearer ${HELICONE_API_KEY}`,
  },
});

const count = await response.json();
```

</RequestExample>

<ResponseExample>

```json Response
42
```

</ResponseExample> 