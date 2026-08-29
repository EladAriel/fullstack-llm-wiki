---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/multi-ns_role.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.792565Z"
---
# Multi Ns_Role

```yaml
---
kind: Role
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: redb-role
  labels:
    app: redis-enterprise
rules:
  - apiGroups:
      - app.redislabs.com
    resources: ["redisenterprisedatabases",
                "redisenterprisedatabases/status",
                "redisenterprisedatabases/finalizers",
                "redisenterpriseactiveactivedatabases",
                "redisenterpriseactiveactivedatabases/status",
                "redisenterpriseactiveactivedatabases/finalizers"]
    verbs: ["delete", "get", "list", "patch", "create", "update", "watch"]
  - apiGroups: [""]
    resources: ["secrets"]
    verbs: ["update", "get", "watch", "create", "patch", "list"]
  - apiGroups: ["discovery.k8s.io"]
    resources: ["endpointslices"]
    verbs: ["get", "list", "watch"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["create", "patch"]
  - apiGroups: [""]
    resources: ["services"]
    verbs: ["get", "list", "update", "patch", "create", "delete", "watch"]
```
