---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/rack_aware_cluster_role_binding.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.791571Z"
---
# Rack_Aware_Cluster_Role_Binding

```yaml
kind: ClusterRoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: redis-enterprise-operator
  labels:
    app: redis-enterprise
subjects:
- kind: ServiceAccount
  namespace: NAMESPACE_OF_SERVICE_ACCOUNT
  name: redis-enterprise-operator
roleRef:
  kind: ClusterRole
  name: redis-enterprise-operator
  apiGroup: rbac.authorization.k8s.io
```
