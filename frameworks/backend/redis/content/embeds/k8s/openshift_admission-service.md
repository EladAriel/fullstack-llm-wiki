---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/openshift_admission-service.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

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
