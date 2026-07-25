---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/replica-configuration.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# Self-Managed Replica Set Configuration

You can access the configuration of a `replica set` using the :method:`rs.conf()` method or the :dbcommand:`replSetGetConfig` command.

To modify the configuration for a replica set, use the :method:`rs.reconfig()` method, passing a configuration document to the method.

> **Warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

## Replica Set Configuration Document Example

.. include:: /includes/replica-set-conf-document-output.rst

## Replica Set Configuration Fields

### `members`

### `settings`
