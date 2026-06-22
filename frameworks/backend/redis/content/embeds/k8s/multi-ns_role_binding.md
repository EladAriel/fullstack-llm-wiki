---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/multi-ns_role_binding.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
