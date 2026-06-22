---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/oidc/workforce/configure-oidc.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================================

# Configure MongoDB with Workforce Identity Federation

Configure MongoDB with Workforce Identity Federation to authenticate users across different platforms using a single set of credentials. This enhances security and simplifies user management.

> **Important:** .. include:: includes/fact-OIDC-linux-only.rst

## Before you Begin

- Ensure that you are on MongoDB Enterprise.
.. include:: /includes/fact-confirm-enterprise-binaries.rst

- Configure your external |idp-abbr|. For more details, see
`workforce-external-provider`.

## Steps

## oidcIdentityProviders for Sharded Clusters

In a sharded cluster, configure :parameter:`oidcIdentityProviders` on every |mongos| instance. Clients authenticate through `mongos`, which requires this configuration to verify |idp| tokens. If clients connect directly to config servers or shard :binary:`~bin.mongod` instances, you must also configure `oidcIdentityProviders` on those instances.

Apply the steps in this tutorial to each `mongos` instance in your deployment. To configure database users for Workforce Identity Federation, see `database-user-workforce`.
