---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rec.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
apiVersion: app.redislabs.com/v1
kind: RedisEnterpriseCluster
metadata:
  name: rec
  labels:
    app: redis-enterprise
spec:
  # The number of Redis Enterprise nodes in the clusters.
  nodes: 3

  persistentSpec:
    # Whether to enable persistent storage for the Redis Enterprise nodes.
    enabled: true

    # The size of the persistent volume for each Redis Enterprise node.
    volumeSize: 20Gi

  # The resources allocated to each Redis Enterprise node.
  redisEnterpriseNodeResources:
    requests:
      cpu: 2
      memory: 4Gi
    limits:
      cpu: 2
      memory: 4Gi
```
