---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/settings/sandboxes/vercel.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.978793Z"
---
# Vercel

---
title: "Vercel Sandbox"
description: "Run code evaluators in ephemeral compute on Vercel's infrastructure."
---

<div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', marginTop: '1.5rem', marginBottom: '1.5rem' }}>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/vercel.svg" alt="Vercel Sandbox" className="invert-on-dark" style={{ height: '112px', flexShrink: 0 }} />
<div>

[**Vercel Sandbox**](https://vercel.com/docs/vercel-sandbox) runs each evaluation in ephemeral compute on Vercel's infrastructure, scoped to a specific Vercel team and project. It supports both Python and TypeScript evaluators.

</div>
</div>

## Setup

Vercel Sandbox needs three values:

| Value | What it is | Where to find it |
| :-- | :-- | :-- |
| `VERCEL_TOKEN` | A personal access token | [Account Settings → Tokens](https://vercel.com/account/tokens) |
| `VERCEL_PROJECT_ID` | The project's resource ID | Project Settings → General |
| `VERCEL_TEAM_ID` | The team's resource ID | `https://vercel.com/teams/<your-team>/settings#team-id` |

Then:

1. **Add the credentials to Phoenix.** Open [Settings → Sandboxes](/docs/phoenix/settings/sandboxes), find the **Vercel Sandbox** row, click the gear icon, and paste each value into the matching field. You can also set them as environment variables on the Phoenix server.
2. **Create a configuration.** In **Sandbox Configurations**, click **New Sandbox**, pick **Vercel Sandbox**, choose the language (Python or TypeScript), set the timeout and any environment variables or dependencies, and save.

For Vercel's full authentication walkthrough, see [Vercel Sandbox authentication](https://vercel.com/docs/vercel-sandbox/concepts/authentication).
