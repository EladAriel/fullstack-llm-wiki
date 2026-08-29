---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/settings/sandboxes/modal.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.950765Z"
---
# Modal

---
title: "Modal"
description: "Run code evaluators in Modal's serverless container platform."
---

<div style={{ display: 'flex', alignItems: 'center', gap: '1.5rem', marginTop: '1.5rem', marginBottom: '1.5rem' }}>
<img src="https://storage.googleapis.com/arize-phoenix-assets/assets/svgs/modal.svg" alt="Modal" style={{ height: '112px', flexShrink: 0 }} />
<div>

[**Modal**](https://modal.com/) runs each Python evaluation in a fresh, serverless container on its own cloud. Cold starts are typically under a second, and timeouts can be generous.

</div>
</div>

## Setup

1. **Create a Modal account** at [modal.com](https://modal.com/) if you don't already have one.
2. **Create a token pair** in the Modal dashboard. Modal authenticates with two values — a token ID and a token secret — and gives you both when you create the pair.
3. **Add the credentials to Phoenix.** Open [Settings → Sandboxes](/docs/phoenix/settings/sandboxes), find the **Modal** row, click the gear icon, and paste the values as `MODAL_TOKEN_ID` and `MODAL_TOKEN_SECRET`. You can also set them as environment variables on the Phoenix server instead.
4. **Create a configuration.** In **Sandbox Configurations**, click **New Sandbox**, pick **Modal**, set the timeout and any environment variables or dependencies, and save.
