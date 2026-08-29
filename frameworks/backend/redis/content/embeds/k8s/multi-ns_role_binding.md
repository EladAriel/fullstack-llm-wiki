---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/multi-ns_role_binding.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.792706Z"
---
# Multi Ns_Role_Binding

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
