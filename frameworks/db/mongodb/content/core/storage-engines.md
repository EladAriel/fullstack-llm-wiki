---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/storage-engines.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Storage Engines for Self-Managed Deployments

The `storage engine` is the component of the database that is responsible for managing how data is stored, both in memory and on disk. MongoDB supports multiple storage engines, as different engines perform better for specific workloads. Choosing the appropriate storage engine for your use case can significantly impact the performance of your applications.

|arrow| WiredTiger Storage Engine (Default) `WiredTiger <storage-wiredtiger>` is the default storage engine and is recommended for new deployments. WiredTiger provides a document-level concurrency model, checkpointing, and compression, among other features.

In MongoDB Enterprise, WiredTiger also supports `/core/security-encryption-at-rest`. See `encrypted-storage-engine`.

|arrow| In-Memory Storage Engine An `In-Memory storage engine <storage-inmemory>` is available in MongoDB Enterprise. Rather than storing documents on-disk, it retains them in-memory for more predictable data latencies.

## Contents

- WiredTiger </core/self-managed-wiredtiger>
- In-Memory </core/inmemory>
