---
type: "Framework Learn Page"
framework: "Arize Phoenix"
source_repo: "https://github.com/Arize-ai/phoenix.git"
source_branch: "main"
source_path: "docs/phoenix/release-notes/04-2026/04-07-2026-postgresql-read-replica.mdx"
source_commit: "69b3ab92c37ff65812feaa2dbf0b1c0ad5ae55fe"
source_commit_short: "69b3ab9"
source_commit_date: "2026-07-25T11:48:12-06:00"
generated_at: "2026-07-25T19:08:24.882850Z"
---
# 04 07 2026 Postgresql Read Replica

---
title: "04.07.2026 PostgreSQL Read Replica Routing"
description: "Route read-only queries to a PostgreSQL read replica to reduce load on the primary under high ingestion."
---

**Available in arize-phoenix 14.0.0+**

Phoenix now routes read-only queries to an optional PostgreSQL read replica when `PHOENIX_SQL_DATABASE_READ_REPLICA_URL` is set. This reduces CPU, I/O, and connection pool pressure on the primary database under high span ingestion load.

## Configuration

Set both environment variables before starting the server:

```bash
export PHOENIX_SQL_DATABASE_URL="postgresql://user:pass@primary-host:5432/phoenix"
export PHOENIX_SQL_DATABASE_READ_REPLICA_URL="postgresql://user:pass@replica-host:5432/phoenix"

phoenix serve
```

When `PHOENIX_SQL_DATABASE_READ_REPLICA_URL` is not set, Phoenix falls back to the primary for all queries — no configuration change is required for existing deployments.

## What Routes to the Replica

The following are routed to the read replica when configured:

- **Dataloaders** — span and trace attribute lookups
- **GraphQL query resolvers** — all read-only queries
- **REST read endpoints** — spans, traces, and sessions
- **Generative model store daemon** — periodic model list refresh

Writes (span ingestion, mutations, migrations) always go to the primary.

## Notes

- `PHOENIX_SQL_DATABASE_READ_REPLICA_URL` is only supported for PostgreSQL. Setting it with a SQLite database logs a warning and is ignored.
- The replica connection uses the same `asyncpg` driver as the primary.
- Replication lag is not managed by Phoenix — reads may reflect slightly stale data depending on your PostgreSQL replication setup.
