---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/prompt-engineering/overview-prompts/span-replay.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.976254Z"
---
# Span Replay

---
title: "Span Replay"
description: Replay LLM spans traced in your application directly in the playground
---

<Frame caption="Replay LLM spans traced in your application directly in the playground">
  <img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/span_replay.gif" />
</Frame>

Have you ever wanted to go back into a multi-step LLM chain and just replay one step to see if you could get a better outcome? Well you can with Phoenix's **Span Replay.** LLM spans that are stored within Phoenix can be loaded into the Prompt Playground and replayed. Replaying spans inside of Playground enables you to debug and improve the performance of your LLM systems by comparing LLM provider outputs, tweaking model parameters, changing prompt text, and more.

Chat completions generated inside of Playground are automatically instrumented, and the recorded spans are immediately available to be replayed inside of Playground.


