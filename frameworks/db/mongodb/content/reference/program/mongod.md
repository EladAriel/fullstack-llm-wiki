---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/program/mongod.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================

# `mongod` Instances

## Synopsis

`mongod` is the primary daemon process for the MongoDB system. It handles data requests, manages data access, and performs background management operations.

This document provides a complete overview of all command line options for `mongod`. These command line options are primarily useful for testing: In common operation, use the `configuration file options </reference/configuration-options>` to control the behavior of your database.

> **Seealso:** `conf-file-command-line-mapping`

> **Note:** .. include:: /includes/fact-tls-1.0.rst

## Compatibility

Deployments hosted in the following environments use `mongod`:

.. include:: /includes/fact-environments-atlas-only.rst

> **Note:** {+atlas+} manages the `mongod` for all {+atlas+} deployments.

.. include:: /includes/fact-environments-onprem-only.rst

## Considerations

- .. include:: /includes/fact-mongod-mongos-ftdc-thread.rst
## Options

.. versionchanged:: 6.1

.. versionchanged:: 5.2

.. versionchanged:: 5.0

### Core Options

.. include:: /includes/parameter-listenbacklog.rst

### LDAP Authentication or Authorization Options

.. include:: /includes/LDAP-deprecated.rst

.. include:: /includes/query-password.rst

### Storage Options

### WiredTiger Options

### Replication Options

### Sharded Cluster Options

### TLS Options

### Profiler Options

### Audit Options

### inMemory Options

### Encryption Key Management Options
