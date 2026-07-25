---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/role.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  labels:
    app: redis-enterprise
  name: redis-enterprise-operator
rules:
  - apiGroups:
      - rbac.authorization.k8s.io
    resources:
      - roles
      - rolebindings
    verbs:
      - create
      - get
      - list
      - watch
      - update
      - patch
      - delete
  - apiGroups:
      - ""
    resources:
      - serviceaccounts
    verbs:
      - create
      - get
      - update
      - patch
      - delete
  - apiGroups:
      - app.redislabs.com
    resources:
      - "*"
    verbs:
      - delete
      - get
      - list
      - patch
      - create
      - update
      - watch
  - apiGroups:
      - ""
    resources:
      - secrets
    verbs:
      - update
      - get
      - create
      - patch
      - delete
      - list
      - watch
  - apiGroups:
      - discovery.k8s.io
    resources:
      - endpointslices
    verbs:
      - get
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - events
    verbs:
      - create
      - patch
  - apiGroups:
      - apps
    resources:
      - deployments
      - statefulsets
      - replicasets
    verbs:
      - create
      - delete
      - get
      - patch
      - update
      - list
      - watch
  - apiGroups:
      - batch
    resources:
      - cronjobs
    verbs:
      - create
      - delete
      - get
      - patch
      - update
      - list
      - watch
  - apiGroups:
      - policy
    resources:
      - poddisruptionbudgets
    verbs:
      - create
      - delete
      - get
      - list
      - watch
      - update
  - apiGroups:
      - ""
    resources:
      - configmaps
    verbs:
      - create
      - delete
      - get
      - update
      - watch
      - list
  - apiGroups:
      - ""
    resources:
      - persistentvolumeclaims
    verbs:
      - create
      - delete
      - get
      - update
      - list
      - watch
  - apiGroups:
      - ""
    resources:
      - pods
    verbs:
      - get
      - list
      - update
      - patch
      - delete
      - watch
  - apiGroups:
      - ""
    resources:
      - services
    verbs:
      - get
      - list
      - update
      - patch
      - create
      - delete
      - watch
  - apiGroups:
      - networking.k8s.io
    resources:
      - ingresses
    verbs:
      - create
      - patch
      - delete
      - list
      - update
      - get
      - watch
  - apiGroups:
      - networking.istio.io
    resources:
      - gateways
      - virtualservices
    verbs:
      - get
      - list
      - update
      - patch
      - create
      - delete
      - watch
```
