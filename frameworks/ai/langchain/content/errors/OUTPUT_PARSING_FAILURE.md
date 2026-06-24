---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/OUTPUT_PARSING_FAILURE.mdx"
source_commit: "d037cd23f3f298721837c403b2ffd289e31d56d0"
source_commit_short: "d037cd23"
source_commit_date: "2026-06-23T11:18:55+02:00"
generated_at: "2026-06-23T13:53:33Z"
---

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
