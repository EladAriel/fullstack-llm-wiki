---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rerc-ohare.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseRemoteCluster
metadata:
  name: rerc-ohare
spec:
  recName: rec-chicago
  recNamespace: ns-illinois
  apiFqdnUrl: api-rec-chicago-ns-illinois.example.com
  dbFqdnSuffix: .db-rec-chicago-ns-illinois.example.com
  secretName: redis-enterprise-rerc-ohare
```
