---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/reaadb.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseActiveActiveDatabase
metadata:
  name: reaadb
  labels:
    app: redis-enterprise
spec:
  participatingClusters:
    # Participating cluster pointing to RERC named: 'new-york-1'.
    - name: new-york-1

    # Participating cluster pointing to RERC named: 'boston-1'.
    - name: boston-1
```
