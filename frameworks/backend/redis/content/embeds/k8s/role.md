---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/role.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.793681Z"
---
# Role

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
