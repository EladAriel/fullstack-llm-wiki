---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rerc-raegan.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseRemoteCluster
metadata:
  name: rerc-raegan
spec:
  recName: rec-arlington
  recNamespace: ns-virginia
  apiFqdnUrl: api-rec-arlington-ns-virginia.example.com
  dbFqdnSuffix: .db-rec-arlington-ns-virginia.example.com
  secretName: redis-enterprise-rerc-raegan
```
