---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/render.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.915224Z"
---
# Render

---
title: "Render"
description: Use this guide to deploy Arize Phoenix on Render via the prebuilt blueprint.
---

You can deploy Arize Phoenix on [Render](https://render.com/) via a prebuilt blueprint. The blueprint runs the official Phoenix Docker image with a managed PostgreSQL database and authentication enabled. It is defined by [`render.yaml`](https://github.com/Arize-ai/phoenix/blob/main/render.yaml) in the Phoenix repository, which is the source of truth for what gets provisioned.

## Deploy

Use the following button to deploy the Phoenix blueprint on Render:

<a href="https://render.com/deploy?repo=https://github.com/Arize-ai/phoenix" target="_blank">
  <img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render" height="30" noZoom />
</a>

Once the service is live, log in with the default admin account as described in [Authentication](/docs/phoenix/self-hosting/features/authentication). To customize the instance, see [Environment Variables](/docs/phoenix/self-hosting/configuration#environment-variables).
