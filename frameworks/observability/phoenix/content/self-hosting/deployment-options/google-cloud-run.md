---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/google-cloud-run.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.913717Z"
---
# Google Cloud Run

---
title: "Google Cloud Run"
description: Use this guide to deploy Arize Phoenix on Google Cloud Run via the deploy button.
---

You can deploy Arize Phoenix on [Google Cloud Run](https://cloud.google.com/run) via a deploy button. The deployment runs Phoenix with authentication enabled and prompts you for configuration during setup. The prompts are defined by [`app.json`](https://github.com/Arize-ai/phoenix/blob/main/app.json) in the Phoenix repository, which is the source of truth for what gets provisioned.

## Deploy

Use the following button to deploy Phoenix to Cloud Run:

<a href="https://deploy.cloud.run/?git_repo=https://github.com/Arize-ai/phoenix" target="_blank">
  <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" height="30" noZoom />
</a>

<Note>
  The button clones the Phoenix repository into Cloud Shell and builds the image from source rather than deploying the prebuilt Docker Hub image.
</Note>

<Warning>
  Cloud Run's container filesystem is ephemeral — data is lost whenever a new revision is deployed or an instance restarts. For anything beyond a quick trial, set `PHOENIX_SQL_DATABASE_URL` to a PostgreSQL instance (for example, [Cloud SQL](https://cloud.google.com/sql)) so your traces persist.
</Warning>

Once the service is live, log in with the default admin account as described in [Authentication](/docs/phoenix/self-hosting/features/authentication). To customize the instance, see [Environment Variables](/docs/phoenix/self-hosting/configuration#environment-variables).
