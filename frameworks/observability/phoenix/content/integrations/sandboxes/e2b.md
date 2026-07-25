---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/e2b.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.838545Z"
---
# E2B

---
title: "E2B"
description: "Run Phoenix code evaluators in E2B's hosted micro-VM sandboxes."
---

<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/e2b.svg" alt="E2B" style={{ height: '64px' }} />

[**E2B**](https://e2b.dev/) provides hosted micro-VM sandboxes purpose-built for executing AI-generated code. Phoenix uses E2B as a hosted backend for Python [code evaluators](/docs/phoenix/evaluation/server-evals/code-evaluators), giving each invocation a fresh VM with kernel-level isolation, runtime dependency installation, and opt-in outbound network access — without exposing the rest of your deployment.

## Configure

1. Sign up at [e2b.dev](https://e2b.dev/) and create an API key.
2. Add it as `E2B_API_KEY` from **Settings → Sandboxes**.

See [Settings → Sandboxes → E2B](/docs/phoenix/settings/sandboxes/e2b) for full configuration details and [Sandbox Backends](/docs/phoenix/self-hosting/features/sandbox-runtimes) for self-hosting setup.
