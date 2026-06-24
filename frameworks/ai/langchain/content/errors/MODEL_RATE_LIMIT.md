---
type: "Framework Learn Page"
framework: "LangChain"
source_repo: "https://github.com/langchain-ai/docs"
source_branch: "main"
source_path: "src/oss/langchain/errors/MODEL_RATE_LIMIT.mdx"
source_commit: "d037cd23f3f298721837c403b2ffd289e31d56d0"
source_commit_short: "d037cd23"
source_commit_date: "2026-06-23T11:18:55+02:00"
generated_at: "2026-06-23T13:53:33Z"
---

---
title: MODEL_RATE_LIMIT
---

<Note>
    Currently only used in `langchainjs` (JavaScript/TypeScript).
</Note>

You have hit the maximum number of requests that a model provider allows over a given time period and are being temporarily blocked.

This error occurs when you exceed the maximum number of requests permitted by your model provider within a specific timeframe, resulting in temporary blocking. The restriction is generally temporary and lifts after the limit resets.

## Troubleshooting

To resolve this error, you can:

1. **Implement Rate Limiting**: Deploy a rate limiter to regulate the frequency of requests sent to the model.
    :::python
    See [rate limiting](/oss/langchain/models#rate-limiting) docs.
    :::
2. **Implement Response Caching**: Use model response caching to reduce redundant requests when incoming queries are repetitive.
3. **Use Multiple Providers**: Distribute requests across multiple providers if your application architecture supports this approach
4. **Contact Your Provider**: Reach out to your model provider requesting an increase to your rate limits
