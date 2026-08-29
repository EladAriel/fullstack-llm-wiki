---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/OUTPUT_PARSING_FAILURE.mdx"
source_commit: "a174f9cf7c91ee5eb14ee2382eb48bfe6e4956e9"
source_commit_short: "a174f9c"
source_commit_date: "2026-08-28T17:04:12-07:00"
generated_at: "2026-08-29T09:38:24.255992Z"
---
# Output_Parsing_Failure

---
title: OUTPUT_PARSING_FAILURE
---

An [output parser](https://reference.langchain.com/python/langchain_core/output_parsers/) was unable to handle model output as expected.

<Note>
    Some prebuilt constructs like legacy LangChain agents and chains may use output parsers internally, so you may see this error even if you're not visibly instantiating and using an output parser.
</Note>

## Troubleshooting

- Consider using tool calling or other structured output techniques if possible without an output parser to reliably output parseable values.
- Add more precise formatting instructions to your prompt.
- If you are using a smaller or less capable model, try using a more capable one.
