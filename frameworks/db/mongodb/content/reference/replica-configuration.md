---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/replica-configuration.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================

# Self-Managed Replica Set Configuration

You can access the configuration of a `replica set` using the :method:`rs.conf()` method or the :dbcommand:`replSetGetConfig` command.

To modify the configuration for a replica set, use the :method:`rs.reconfig()` method, passing a configuration document to the method. See :method:`rs.reconfig()` for more information.

> **Warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

## Replica Set Configuration Document Example

.. include:: /includes/replica-set-conf-document-output.rst

## Replica Set Configuration Fields

### `members`

### `settings`
