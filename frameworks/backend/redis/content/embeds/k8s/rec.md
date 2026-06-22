---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rec.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
