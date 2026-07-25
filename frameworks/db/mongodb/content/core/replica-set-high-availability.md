---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-high-availability.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================

# Replica Set High Availability

Replica sets use elections to support `high availability <high availability>`.

`/core/replica-set-elections` Elections occur when the primary becomes unavailable and the replica set members autonomously select a new primary.

`/core/replica-set-rollbacks` A rollback reverts write operations on a former primary when the member rejoins the replica set after a failover.

## Contents

- Elections </core/replica-set-elections>
- Failover Rollbacks </core/replica-set-rollbacks>
