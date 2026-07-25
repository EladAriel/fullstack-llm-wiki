---
type: "Framework Learn Page"
framework: "Helicone"
source_repo: "https://github.com/Helicone/helicone.git"
source_branch: "main"
source_path: "docs/references/latency-affect.mdx"
source_commit: "67df07b8d807a960f2e53d9ec2a9c49513ca2379"
source_commit_short: "67df07b"
source_commit_date: "2026-07-21T05:35:38-07:00"
generated_at: "2026-07-25T19:08:22.194340Z"
---
# Latency Affect

---
title: "Latency Impact"
sidebarTitle: "Latency"
description: "Helicone minimizes latency for your LLM applications using Cloudflare's global network. Detailed benchmarking results and performance metrics included."
"twitter:title": "Latency Impact - Helicone OSS LLM Observability"
---

import QuestionsSection from "/snippets/questions-section.mdx";
import FaqHeader from "/snippets/faq-header.mdx";

Helicone leverages [Cloudflare Workers](https://developers.cloudflare.com/workers), which run code instantly across the globe on [Cloudflare's global network](https://workers.cloudflare.com/), to provide a fast and reliable proxy for your LLM requests. By utilizing this extensive network of servers, Helicone minimizes latency by ensuring that requests are handled by the servers closest to your users.

### How Cloudflare Workers Minimize Latency

Cloudflare Workers operate on a serverless architecture running on [Cloudflare's global edge network](https://developers.cloudflare.com/workers/reference/how-workers-works/). This means your requests are processed at the edge, reducing the distance data has to travel and significantly lowering latency. Workers are powered by V8 isolates, which are lightweight and have extremely fast startup times. This eliminates cold starts and ensures quick response times for your applications.

### Benchmarking Helicone's Proxy Service

To demonstrate the negligible latency introduced by Helicone's proxy, we conducted the following experiment:

- We interleaved 500 requests with unique prompts to both OpenAI and Helicone.
- Both received the same requests within the same 1-second window, varying which endpoint was called first for each request.
- We maximized the prompt context window to make these requests as large as possible.
- We used the `text-ada-001` model.
- We logged the roundtrip latency for both sets of requests.

#### Results

| Statistic          | OpenAI (s) | Helicone (s) |
| ------------------ | ---------- | ------------ |
| Mean               | 2.21       | 2.21         |
| Median             | 2.87       | 2.90         |
| Standard Deviation | 1.12       | 1.12         |
| Min                | 0.14       | 0.14         |
| Max                | 3.56       | 3.76         |
| p10                | 0.52       | 0.52         |
| p90                | 3.27       | 3.29         |

The metrics show that Helicone's latency **closely matches that of direct requests to OpenAI**. The slight differences at the right tail indicate a minimal overhead introduced by Helicone, which is negligible in most practical applications. This demonstrates that using Helicone's proxy does not significantly impact the performance of your LLM requests.

<Frame>
  ![Comparison of latency between OpenAI and Helicone proxies for LLM
  requests](/images/getting-started/openai-helicone.png)
</Frame>

<FaqHeader />

- [Concerns about reliability?](/references/availability)

<QuestionsSection />
