---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/evaluation/llm-evals/executors.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.933900Z"
---
# Executors

---
title: "Executors"
description: "Phoenix Evals leverages executors that make the execution of evaluations many times faster."
---

<Frame>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/images/eval_executor.png"/>
</Frame>

When performing evaluations, speed is paramount so that you can focus on improving your system. Phoenix Evals executors run evaluations faster and more reliably by automatically handling rate limits, errors, and concurrency.

## What Executors Do

* **Handle Rate Limits**: Automatically retry when LLM providers throttle requests
* **Manage Errors**: Distinguish between temporary failures and permanent errors
* **Optimize Speed**: Dynamically adjust concurrency based on provider performance

## Why Use Executors

Running thousands of evaluations manually is slow and error-prone. Executors automatically handle the complexity so you can focus on your evaluation logic instead of infrastructure.

## Retries and Timeouts

Both `evaluate_dataframe` and `async_evaluate_dataframe` accept a `max_retries` argument (default `10`) that bounds how many times a failing evaluation task is retried before it is marked failed.

When you use the asynchronous executor (`async_evaluate_dataframe`), each task also has a `timeout` (default 60 seconds). **A timed-out task counts against `max_retries`.** A timeout is logged and the task requeued, and once the retry budget is exhausted the task is marked `FAILED` — honoring `exit_on_error` — rather than being retried forever. If you have long-running eval tasks that legitimately need more time, raise the timeout or increase `max_retries`; if tasks are hanging, lowering `max_retries` makes them fail faster.

<Note>
This applies to the async executor's per-task timeout. The synchronous executor retries on exceptions only and has no per-task timeout.
</Note>
