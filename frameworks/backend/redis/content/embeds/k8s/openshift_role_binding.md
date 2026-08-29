---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/openshift_role_binding.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.795224Z"
---
# Openshift_Role_Binding

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
