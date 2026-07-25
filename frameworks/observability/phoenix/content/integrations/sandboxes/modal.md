---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/modal.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.838362Z"
---
# Modal

---
title: "Modal"
description: "Run Phoenix code evaluators in Modal's serverless container platform."
---

<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/modal.svg" alt="Modal" style={{ height: '64px' }} />

[**Modal**](https://modal.com/) is a serverless container platform with sub-second cold starts and Python-first ergonomics. Phoenix uses Modal as a hosted backend for Python [code evaluators](/docs/phoenix/evaluation/server-evals/code-evaluators) that benefit from Modal's fast container scheduling, generous timeouts, and pay-per-execution pricing.

## Configure

1. Sign up at [modal.com](https://modal.com/) and create a token pair.
2. Add `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET` from **Settings → Sandboxes**.

See [Settings → Sandboxes → Modal](/docs/phoenix/settings/sandboxes/modal) for full configuration details and [Sandbox Backends](/docs/phoenix/self-hosting/features/sandbox-runtimes) for self-hosting setup.
