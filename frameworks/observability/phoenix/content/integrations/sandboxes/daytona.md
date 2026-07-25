---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/daytona.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.838172Z"
---
# Daytona

---
title: "Daytona"
description: "Run Phoenix code evaluators in Daytona's managed development sandboxes."
---

<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/daytona.svg" alt="Daytona" style={{ height: '64px' }} />

[**Daytona**](https://www.daytona.io/) provides managed development sandboxes with fast, snapshot-based startup. Phoenix uses Daytona as a hosted backend for both Python and TypeScript [code evaluators](/docs/phoenix/evaluation/server-evals/code-evaluators) that need stronger isolation than the local sandboxes, longer maximum timeouts, or runtime dependency installation.

## Configure

1. Sign up at [daytona.io](https://www.daytona.io/) and generate an API key.
2. Add it as `DAYTONA_API_KEY` from **Settings → Sandboxes**.

See [Settings → Sandboxes → Daytona](/docs/phoenix/settings/sandboxes/daytona) for full configuration details and [Sandbox Backends](/docs/phoenix/self-hosting/features/sandbox-runtimes) for self-hosting setup.
