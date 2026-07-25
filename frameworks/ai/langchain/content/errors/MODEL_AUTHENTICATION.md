---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MODEL_AUTHENTICATION.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1dfc"
source_commit_date: "2026-07-25T00:27:23Z"
generated_at: "2026-07-25T11:51:05Z"
---

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


