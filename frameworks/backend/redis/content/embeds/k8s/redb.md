---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/redb.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.794920Z"
---
# Redb

```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseDatabase
metadata:
  name: redb
  labels:
    app: redis-enterprise
spec:
  # Memory size of the database.
  memorySize: 256MB

  # Number of shards in the database.
  shardCount: 1

  # Determines whether replication will be enabled for the database.
  replication: false
```
