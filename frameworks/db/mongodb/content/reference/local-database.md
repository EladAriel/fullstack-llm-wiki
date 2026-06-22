---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/local-database.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================

# The `local` Database

## Overview

Every :binary:`~bin.mongod` instance has its own `local` database, which stores data used in the replication process and other instance-specific data. Collections in the `local` database are not replicated.

## Collections on all `mongod` Instances

## Collections on Replica Set Members

## Restrictions

Multi-Document Transactions on `local` You cannot perform read/write operations to the collections in the `local` database inside a `multi-document transaction <transactions>`.

Retryable Writes against `local` You cannot perform write operations to collections in the `local` database with `retryable writes <retryable-writes>` enabled.

> **Important:**   The official MongoDB drivers enable retryable writes by
  default. Applications that write to the `local` database
  encounter write errors unless retryable writes are explicitly
  disabled.
  To disable retryable writes, specify
  :urioption:`retryWrites=false <retryWrites>` in the
  `connection string <mongodb-uri>` for the MongoDB cluster.
