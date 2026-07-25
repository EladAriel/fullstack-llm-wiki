---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/settings/sandboxes/daytona.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.977832Z"
---
# Daytona

---
title: "Daytona"
description: "Run code evaluators in Daytona's managed development sandboxes."
---

<div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', marginTop: '1.5rem', marginBottom: '1.5rem' }}>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/daytona.svg" alt="Daytona" className="invert-on-dark" style={{ height: '112px', flexShrink: 0 }} />
<div>

[**Daytona**](https://www.daytona.io/) runs each evaluation in a managed development sandbox on its own cloud. Sandboxes start from snapshots, which keeps startup fast, and Daytona supports both Python and TypeScript evaluators.

</div>
</div>

## Setup

1. **Create a Daytona account** at [daytona.io](https://www.daytona.io/) if you don't already have one.
2. **Generate an API key** in the Daytona dashboard.
3. **Add the key to Phoenix.** Open [Settings → Sandboxes](/docs/phoenix/settings/sandboxes), find the **Daytona** row, click the gear icon, and paste the key as `DAYTONA_API_KEY`. You can also set it as an environment variable on the Phoenix server instead.
4. **Create a configuration.** In **Sandbox Configurations**, click **New Sandbox**, pick **Daytona**, choose the language (Python or TypeScript), set the timeout and any environment variables or dependencies, and save.
