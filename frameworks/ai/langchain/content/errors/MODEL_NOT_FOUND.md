---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MODEL_NOT_FOUND.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:38:24.256452Z"
---
# Model_Not_Found

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
