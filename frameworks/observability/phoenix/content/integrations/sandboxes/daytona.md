---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/daytona.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.930719Z"
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
