---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/multi-ns_role_binding.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: redb-role
  labels:
    app: redis-enterprise
subjects:
- kind: ServiceAccount
  name: redis-enterprise-operator
  namespace: NAMESPACE_OF_SERVICE_ACCOUNT
- kind: ServiceAccount
  name: NAME_OF_REC_SERVICE_ACCOUNT  # service account of the REC, usually the same as the name of the custom resource
  namespace: NAMESPACE_OF_SERVICE_ACCOUNT
roleRef:
  kind: Role
  name: redb-role
  apiGroup: rbac.authorization.k8s.io
```
