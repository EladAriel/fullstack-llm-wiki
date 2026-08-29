---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MODEL_AUTHENTICATION.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:38:24.256603Z"
---
# Model_Authentication

---
title: MODEL_AUTHENTICATION
---

<Note>
    Currently only used in `langchainjs` (JavaScript/TypeScript).
</Note>

Your model provider is denying you access to their service.

This error typically occurs when there's an issue with your authentication credentials or API keys.

## Troubleshooting

* Confirm that your API key or authentication credentials are accurate and valid.
* If using environment-based authentication, verify:
    - The variable name is spelled correctly
    - The variable contains an assigned value
    - Third-party packages like `dotenv` haven't interfered with loading
* If using a proxy or non-standard endpoint, make sure that your custom provider does not expect an alternative authentication scheme.
* Bypass environment variable issues by passing credentials explicitly:

:::python
```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(api_key="YOUR_KEY_HERE")
```
:::
:::js
```typescript
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  apiKey: "YOUR_KEY_HERE",
});
```
:::


