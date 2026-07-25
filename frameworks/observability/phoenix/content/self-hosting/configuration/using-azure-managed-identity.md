---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/self-hosting/configuration/using-azure-managed-identity.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.940481Z"
---
---
title: "Using Azure Database for PostgreSQL"
description: "Phoenix supports Microsoft Entra managed-identity authentication for Azure Database for PostgreSQL."
---

<Info>
Azure managed-identity authentication for PostgreSQL is available since Phoenix **14.8.0**. Use that version or newer before following this guide.
</Info>

First, ensure Phoenix runs in an environment where a managed identity is available (for example AKS, App Service, or an Azure VM). Azure PostgreSQL must have Microsoft Entra authentication enabled, and the managed identity must be created as a PostgreSQL principal.

Azure managed-identity auth in Phoenix requires `azure-identity` (for custom Python installs, install with `pip install 'arize-phoenix[azure]'`).

Then, configure Phoenix to use Azure managed identity for PostgreSQL:

```bash
# Enable Azure managed-identity auth
export PHOENIX_POSTGRES_USE_AZURE_MANAGED_IDENTITY=true

# Database connection
export PHOENIX_POSTGRES_HOST=mydb.postgres.database.azure.com
export PHOENIX_POSTGRES_USER=my-managed-identity-name
export PHOENIX_POSTGRES_DB=phoenix

# Optional: set this only for non-public Azure clouds.
# Public Azure default (used when unset):
#   https://ossrdbms-aad.database.windows.net/.default
# Example for Azure US Government:
# export PHOENIX_POSTGRES_AZURE_SCOPE=https://ossrdbms-aad.database.usgovcloudapi.net/.default
```

Notes:

- Do not set `PHOENIX_POSTGRES_PASSWORD` when `PHOENIX_POSTGRES_USE_AZURE_MANAGED_IDENTITY=true`.
- You do not need a token-lifetime tuning variable. Phoenix reuses `DefaultAzureCredential`, and `azure-identity` handles token cache and refresh behavior.
