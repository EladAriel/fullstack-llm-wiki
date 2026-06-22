---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rerc.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

```yaml
apiVersion: app.redislabs.com/v1alpha1
kind: RedisEnterpriseRemoteCluster
metadata:
  name: new-york-1
  labels:
    app: redis-enterprise
spec:
  # The name of the REC that the RERC is pointing at.
  recName: rec

  # The namespace of the REC that the RERC is pointing at.
  recNamespace: ns1

  # The URL of the cluster, will be used for the active-active database URL.
  apiFqdnUrl: testapi-new-york-1-ns1.redislabs.com

  # The database URL suffix, will be used for the active-active
  # database replication endpoint and replication endpoint SNI.
  dbFqdnSuffix: .example-new-york-1-ns1.redislabs.com

  # The name of the secret containing cluster credentials.
  # Needs to be formatted as: "redis-enterprise-<RERC name>"
  secretName: redis-enterprise-new-york-1
```
