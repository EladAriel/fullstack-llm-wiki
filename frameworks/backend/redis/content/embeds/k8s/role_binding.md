---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/role_binding.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  labels:
    app: redis-enterprise
  name: redis-enterprise-operator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: redis-enterprise-operator
subjects:
  - kind: ServiceAccount
    name: redis-enterprise-operator
```
