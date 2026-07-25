---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/integrations/sandboxes/vercel.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.838724Z"
---
# Vercel

---
title: "Vercel Sandbox"
description: "Run Phoenix code evaluators in ephemeral compute on Vercel's infrastructure."
---

<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/vercel.svg" alt="Vercel Sandbox" style={{ height: '64px' }} />

[**Vercel Sandbox**](https://vercel.com/docs/vercel-sandbox) runs code in ephemeral compute on Vercel's infrastructure, scoped to a Vercel team and project. Phoenix uses it as a hosted backend for both Python and TypeScript [code evaluators](/docs/phoenix/evaluation/server-evals/code-evaluators). It's a good fit when your team is already on Vercel and you'd like sandbox usage to roll up under the same billing and access controls.

## Configure

1. Create a token in the [Vercel dashboard](https://vercel.com/account/tokens) and note your team and project IDs.
2. Add `VERCEL_TOKEN`, `VERCEL_PROJECT_ID`, and `VERCEL_TEAM_ID` from **Settings → Sandboxes**.

See [Settings → Sandboxes → Vercel Sandbox](/docs/phoenix/settings/sandboxes/vercel) for full configuration details and [Sandbox Backends](/docs/phoenix/self-hosting/features/sandbox-runtimes) for self-hosting setup.
