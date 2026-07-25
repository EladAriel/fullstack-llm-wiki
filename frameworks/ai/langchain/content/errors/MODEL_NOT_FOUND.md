---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MODEL_NOT_FOUND.mdx"
source_commit: "2aae1dfc98ee953a9a5185fb6fcdd9efb3f4d878"
source_commit_short: "2aae1dfc"
source_commit_date: "2026-07-25T00:27:23Z"
generated_at: "2026-07-25T11:51:05Z"
---

---
title: MODEL_NOT_FOUND
---

<Note>
    Currently only used in `langchainjs` (JavaScript/TypeScript).
</Note>

The model name you have specified is not acknowledged by your provider.

## Troubleshooting

To resolve this error:

1. **Verify the model identifier**: Double check the model string you are passing in. Ensure the spelling and format are correct
2. **Check proxy/wrapper configurations**: If you are using a proxy or other alternative host with a model wrapper, confirm that the permitted model names are not restricted or altered

The error typically stems from either a typo in the model name string itself or restrictions imposed by a proxy service or model wrapper between your code and the provider's API.
