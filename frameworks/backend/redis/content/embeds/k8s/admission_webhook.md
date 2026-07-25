---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/admission_webhook.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

```yaml
---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  labels:
    app: redis-enterprise
  name: redis-enterprise-admission
webhooks:
  - admissionReviewVersions:
      - v1beta1
    clientConfig:
      service:
        name: admission
        path: /admission
        namespace: OPERATOR_NAMESPACE
      caBundle: "" # Fill in with BASE64 encoded signed cert
    failurePolicy: Fail
    matchPolicy: Exact
    name: redisenterprise.admission.redislabs
    rules:
      - apiGroups:
          - app.redislabs.com
        apiVersions:
          - v1alpha1
        operations:
          - CREATE
          - UPDATE
        resources:
          - redisenterprisedatabases
          - redisenterpriseactiveactivedatabases
          - redisenterpriseremoteclusters
          - redisenterpriseacls
          - redisenterpriseclusterroles
          - redisenterpriseusers
          - redisenterpriseroles
    sideEffects: None
    timeoutSeconds: 30
```
