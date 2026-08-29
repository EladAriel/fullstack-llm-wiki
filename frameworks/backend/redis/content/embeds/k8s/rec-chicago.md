---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rec-chicago.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.791105Z"
---
# Rec Chicago

```yaml
apiVersion: app.redislabs.com/v1
kind: RedisEnterpriseCluster
metadata:
  name: rec-chicago
  namespace: ns-illinois
spec:
  nodes: 3
  persistentSpec:
    enabled: true
    volumeSize: 20Gi
  redisEnterpriseNodeResources:
    requests:
      cpu: 2
      memory: 4Gi
    limits:
      cpu: 2
      memory: 4Gi
```
