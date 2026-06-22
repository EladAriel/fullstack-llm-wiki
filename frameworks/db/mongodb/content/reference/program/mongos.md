---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/program/mongos.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# `mongos` Instances

## Synopsis

For a `sharded cluster <sharding-sharded-cluster>`, the `mongos` instances provide the interface between the client applications and the sharded cluster. The `mongos` instances route queries and write operations to the shards. From the perspective of the application, a `mongos` instance behaves identically to any other MongoDB instance.

## Considerations

- Never change the name of the `mongos` binary.
- .. include:: /includes/fact-tls-1.0.rst
- .. include:: /includes/fact-mongos-fcv.rst
- .. include:: /includes/fact-mongod-mongos-ftdc-thread.rst
## Options

> **Seealso:** `conf-file-command-line-mapping`

> **Note:** - .. include:: /includes/extracts/4.2-changes-options-tls-ssl.rst
- .. include:: /includes/extracts/4.2-changes-options-tlsClusterCAFile.rst

> **Note:** - MongoDB 5.0 removes the `--serviceExecutor` command-line option and the
  corresponding `net.serviceExecutor` configuration option.

### Core Options

.. include:: /includes/parameter-listenbacklog.rst

### Sharded Cluster Options

### TLS Options

### Audit Options

### Profiler Options

### LDAP Authentication and Authorization Options

.. include:: /includes/LDAP-deprecated.rst

### Additional Options

SERVER-12889
