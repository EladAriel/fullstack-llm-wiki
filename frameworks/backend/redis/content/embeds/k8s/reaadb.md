---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/reaadb.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
