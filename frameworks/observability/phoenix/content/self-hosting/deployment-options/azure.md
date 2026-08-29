---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/deployment-options/azure.mdx"
source_commit: "c48e50e9906fcc56c1c103ebd93ef3c95ed6b6e7"
source_commit_short: "c48e50e"
source_commit_date: "2026-08-29T01:45:20-06:00"
generated_at: "2026-08-29T09:39:58.913904Z"
---
# Azure

---
title: "Azure"
description: Use this guide to deploy Arize Phoenix on Azure Container Instances via the prebuilt ARM template.
---

You can deploy Arize Phoenix on [Azure Container Instances](https://azure.microsoft.com/en-us/products/container-instances) via a prebuilt ARM template. The template runs the official Phoenix Docker image with an Azure Database for PostgreSQL flexible server and authentication enabled. It is defined by [`azuredeploy.json`](https://github.com/Arize-ai/phoenix/blob/main/azuredeploy.json) in the Phoenix repository, which is the source of truth for what gets provisioned.

## Deploy

Use the following button to deploy the Phoenix template to Azure:

<a href="https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FArize-ai%2Fphoenix%2Fmain%2Fazuredeploy.json" target="_blank">
  <img src="https://aka.ms/deploytoazurebutton" alt="Deploy to Azure" height="30" noZoom />
</a>

<Warning>
  Azure Container Instances does not terminate TLS, so the template serves plain HTTP. Front the deployment with a TLS proxy such as an [Application Gateway](https://azure.microsoft.com/en-us/products/application-gateway) before production use.
</Warning>

Once the container group is running, log in with the default admin account using the initial password you chose during deployment, as described in [Authentication](/docs/phoenix/self-hosting/features/authentication). To customize the instance, see [Environment Variables](/docs/phoenix/self-hosting/configuration#environment-variables).
