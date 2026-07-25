---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2026/04-16-2026-azure-managed-identity-postgres.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.881723Z"
---
# 04 16 2026 Azure Managed Identity Postgres

---
title: "04.16.2026 Azure Managed Identity for PostgreSQL"
description: "Connect Phoenix to Azure Database for PostgreSQL using managed identity — no static passwords required."
---

**Available in arize-phoenix 14.8.0+**

Phoenix now supports Microsoft Entra managed-identity authentication when connecting to Azure Database for PostgreSQL (Flexible Server). Set two environment variables and install the `azure` extra — Phoenix handles token acquisition and refresh automatically on every new database connection.

## Setup

Install the `azure` extra to pull in `azure-identity` and `aiohttp`:

```bash
pip install 'arize-phoenix[azure]'
```

Set the required environment variables:

```bash
PHOENIX_POSTGRES_USE_AZURE_MANAGED_IDENTITY=true
PHOENIX_SQL_DATABASE_URL=postgresql+asyncpg://<user>@<host>/<db>
```

`PHOENIX_POSTGRES_AZURE_SCOPE` defaults to `https://ossrdbms-aad.database.windows.net/.default`. Override it only if you are running in a sovereign cloud such as Azure US Government:

```bash
PHOENIX_POSTGRES_AZURE_SCOPE=https://ossrdbms-aad.database.usgovcloudapi.net/.default
```

## Notes

- **Mutual exclusion** — `PHOENIX_POSTGRES_USE_AZURE_MANAGED_IDENTITY` and `PHOENIX_POSTGRES_USE_AWS_IAM_AUTH` cannot both be `true`; Phoenix raises a `ValueError` at startup if both are set.
- **`PHOENIX_POSTGRES_AWS_IAM_TOKEN_LIFETIME_SECONDS` is deprecated** — the env var is now silently ignored with a startup warning. Connection pool hygiene is managed internally.

<CardGroup cols={2}>
  <Card title="Using Azure Managed Identity" icon="microsoft" href="/docs/phoenix/self-hosting/configuration/using-azure-managed-identity">
    Full setup guide for Azure managed-identity PostgreSQL connections.
  </Card>
  <Card title="Amazon Aurora (AWS IAM)" icon="aws" href="/docs/phoenix/self-hosting/configuration/using-amazon-aurora">
    Configure AWS RDS IAM authentication for PostgreSQL.
  </Card>
</CardGroup>
