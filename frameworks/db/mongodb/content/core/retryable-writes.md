---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/retryable-writes.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================

# Retryable Writes

Retryable writes let drivers retry specific write operations once after network errors or if they cannot find a healthy `primary` in the `replica set <replication>` or `sharded cluster <sharding-introduction>`.

## Compatibility

Retryable writes require:

Deployment Topologies A `replica set <replication>` or `sharded cluster <sharding-introduction>`. Not supported on `standalone instances <standalone>`.

Storage Engine A storage engine with document-level locking, such as `WiredTiger <storage-wiredtiger>` or `in-memory <storage-inmemory>`.

MongoDB Drivers Drivers compatible with MongoDB 3.6+.

.. include:: /includes/3.6-drivers.rst

MongoDB Version MongoDB 3.6+ and `featureCompatibilityVersion` 3.6+ on all nodes. See :dbcommand:`setFeatureCompatibilityVersion`.

Write Acknowledgment Writes with `/reference/write-concern` `0` are not retryable.

## Behaviors

### Retryable Writes and Multi-Document Transactions

`Transaction commit and abort operations <transactions-retry>` are retryable. Drivers retry these operations once on error, even if :urioption:`retryWrites` is `false`.

Writes inside a transaction are not individually retryable, regardless of value of :urioption:`retryWrites`.

For more information on transactions, see `/core/transactions`.

### Enabling Retryable Writes

MongoDB Drivers

.. include:: /includes/extracts/4.2-changes-drivers-retryWrites-default.rst

:binary:`~bin.mongosh` :binary:`~bin.mongosh` enables retryable writes by default. To disable, use :option:`--retryWrites=false <mongosh --retryWrites>`:

```bash
  mongosh --retryWrites=false
```

### Retryable Write Operations

MongoDB retries the following operations if they have acknowledged write concern (for example, `/reference/write-concern` cannot be :writeconcern:`{w: 0} <\<number\>>`):

> **Note:** Writes inside `transactions </core/transactions>` are not
individually retryable.

### Persistent Network Errors

By default, MongoDB retries writes **once**. One retry attempts to address transient network errors and `replica set elections <replica-set-elections>`, but not persistent network errors.

If you set `timeoutMS`, MongoDB may retry writes multiple times. Retries continue until one of the following conditions is true:

- The operation succeeds.
- The operation fails with a non-retryable error.
- The timeout expires.
### Failover Period

Drivers wait :urioption:`serverSelectionTimeoutMS` to find a new primary before retrying. Retryable writes fail if failover takes longer than this timeout.

> **Warning:** If a client is unresponsive for longer than
:parameter:`localLogicalSessionTimeoutMinutes`, the write might
retry and apply again when the client recovers.

### Diagnostics

:dbcommand:`serverStatus` includes retryable write statistics in the :serverstatus:`transactions` section.

### Retryable Writes Against `local` Database

Official drivers enable retryable writes by default. Writes to the `local` `database <replica-set-local-database>` fail unless you disable retryable writes.

To disable, set :urioption:`retryWrites=false <retryWrites>` in the `connection string <mongodb-uri>`.

### Error Handling

.. include:: /includes/6.1-retry-writes-error-handling.rst

## Learn More

`retryable-reads`
