---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/retryable-reads.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Retryable Reads

Retryable reads allow MongoDB drivers to automatically retry certain read operations a single time if they encounter certain network or server errors.

## Prerequisites

Minimum Driver Version Official MongoDB drivers compatible with MongoDB Server 6.0 and later support retryable reads.

For more information on official MongoDB drivers, see :driver:`MongoDB Drivers </>`.

Minimum Server Version Drivers can only retry read operations if connected to MongoDB Server 6.0 or later.

## Enabling Retryable Reads

Official MongoDB drivers compatible with MongoDB Server 6.0 and later enable retryable reads by default. To explicitly disable retryable reads, specify :urioption:`retryReads=false <retryReads>` in the `connection string <mongodb-uri>` for the deployment.

:binary:`~bin.mongosh` does not support retryable reads.

## Retryable Read Operations

MongoDB drivers support retrying the following read operations. The list references a generic description of each method. For specific syntax and usage, defer to the driver documentation for that method.

MongoDB drivers may include retryable support for other operations, such as helper methods or methods that wrap a retryable read operation. Defer to the :driver:`driver documentation </>` to determine whether a method explicitly supports retryable reads.

> **Seealso:** Retryable Read Specification: [Supported Read Operations](https://github.com/mongodb/specifications/blob/master/source/retryable-reads/retryable-reads.rst#supported-read-operations)_

### Unsupported Read Operations

The following operations do not support retryable reads:

- :method:`db.collection.mapReduce()`
- :dbcommand:`getMore`
- Any read command passed to a generic `Database.runCommand` helper,
which is agnostic about read or write commands.

## Behavior

### Persistent Network Errors

MongoDB retryable reads make only **one** retry attempt. This helps address transient network errors or `replica set elections <replica-set-elections>`, but not persistent network errors.

### Failover Period

The driver performs `server selection <replica-set-read-preference-behavior>` using the read command's original `read preference <read-preference>` before retrying the read operation. If the driver cannot select a server for the retry attempt using the original read preference, the driver returns the original error.

The drivers wait :urioption:`serverSelectionTimeoutMS` milliseconds before performing server selection. Retryable reads do not address instances where no eligible servers exist after waiting :urioption:`serverSelectionTimeoutMS`.
