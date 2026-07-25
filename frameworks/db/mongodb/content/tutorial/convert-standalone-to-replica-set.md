---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/convert-standalone-to-replica-set.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=========================================================

# Convert a Standalone Self-Managed mongod to a Replica Set

Use a `standalone` :binary:`mongod` instance for testing and development. A standalone instance isn't a good choice for a production deployment because it can be a single point of failure. A `replica set <replication>` provides redundancy and availability. Always use a replica set in production.

If you have a standalone server with data that you want to use in production, convert the standalone server to a replica set first.

> **Important:** If you convert a development server to a replica set for production
use, consult the `security checklist <security-checklist>` first.
Do this before you expose your cluster to the internet.

You can migrate from a standalone server to a [MongoDB Atlas](https://www.mongodb.com/docs/atlas)_ cluster. MongoDB Atlas is the fully managed service for MongoDB deployments in the cloud. To learn more, see [Migrate or Import Data](https://www.mongodb.com/docs/atlas/import/)_ in the {+atlas+} documentation.

## About This Task

### Server Architecture

The tutorial uses the following servers:

## Before You Begin

### Cluster Type

Before you convert your standalone instance, consider whether a `replica set <replication>` or a `sharded cluster <sharding-background>` is more appropriate for your workload.

A sharded cluster provides redundancy and availability by distributing data across `shards <shards-concepts>`, which are usually hosted on multiple servers to allow horizontal scaling.

### Authorization

To use authorization with a replica set, you must also configure replica set members to use X.509 certificates or keyfiles to perform internal authentication.

For more information, see:

- `x509-internal-authentication`
- `deploy-repl-set-with-keyfile`
## Procedure

## Learn More

- `Configuration options <configuration-options>`
- `Deploy a standalone instance <tutorials-installation>`
- `Deploy a new replica set <server-replica-set-deploy>`
