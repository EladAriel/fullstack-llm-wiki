---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-high-availability.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# Replica Set High Availability

Replica sets use elections to support `high availability <high availability>`.

`/core/replica-set-elections` Elections occur when the primary becomes unavailable and the replica set members autonomously select a new primary.

`/core/replica-set-rollbacks` A rollback reverts write operations on a former primary when the member rejoins the replica set after a failover.

## Contents

- Elections </core/replica-set-elections>
- Failover Rollbacks </core/replica-set-rollbacks>
