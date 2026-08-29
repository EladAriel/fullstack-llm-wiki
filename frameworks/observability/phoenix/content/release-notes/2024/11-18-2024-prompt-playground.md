---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/2024/11-18-2024-prompt-playground.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.843342Z"
---
# 11 18 2024 Prompt Playground

---
title: "11.18.2024: Prompt playground"
description: Available in Phoenix 6.0+
---

<Update label="11.18.2024">

## Prompt Playground

<Frame>
    <iframe src="https://cdn.iframe.ly/islLPi9" width={1000} height={400} allowFullScreen></iframe>
</Frame>

Sessions allow you to group multiple responses into a single thread. Each response is still captured as a single trace, but each trace is linked together and presented in a combined view.

Sessions make it easier to visual multi-turn exchanges with your chatbot or agent Sessions launches with Python and TS/JS support. For more on sessions, check out [a walkthrough video](https://www.youtube.com/watch?v=dzS6x0BE-EU) and the [docs](/docs/phoenix/tracing/how-to-tracing/setup-tracing/setup-sessions).

### Bug Fixes and Improvements 🐛

* Added support for FastAPI and GraphQL extensions
* Fixed a bug where Anthropic LLM as a Judge responses would be labeled as unparseable
* Fixed a bug causing 500 errors on client.get\_traces\_dataset() and client.get\_spans\_dataframe()
* Added the ability for authentication to work from behind a proxy
* Added an environment variable to set default admin passwords in auth
</Update>
