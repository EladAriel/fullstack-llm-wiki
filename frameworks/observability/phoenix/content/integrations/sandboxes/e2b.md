---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/e2b.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.930901Z"
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
