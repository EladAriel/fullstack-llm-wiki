---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/role_binding.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
