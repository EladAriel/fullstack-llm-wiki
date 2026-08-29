---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/admission-service.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.792287Z"
---
# Admission Service

```yaml
---
apiVersion: v1
kind: Service
metadata:
  name: admission
  labels:
    app: redis-enterprise
spec:
  ports:
    - port: 443
      protocol: TCP
      targetPort: 8443
  selector:
    name: redis-enterprise-operator
```
