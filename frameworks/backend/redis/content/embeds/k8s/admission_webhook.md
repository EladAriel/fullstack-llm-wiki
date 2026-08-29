---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/admission_webhook.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.792987Z"
---
# Admission_Webhook

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
