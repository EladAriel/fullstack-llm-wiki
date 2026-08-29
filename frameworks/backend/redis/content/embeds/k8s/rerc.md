---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rerc.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.792140Z"
---
# Rerc

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
  dbFqdnSuffix: -example-new-york-1-ns1.redislabs.com

  # The name of the secret containing cluster credentials.
  # Needs to be formatted as: "redis-enterprise-<RERC name>"
  secretName: redis-enterprise-new-york-1
```
