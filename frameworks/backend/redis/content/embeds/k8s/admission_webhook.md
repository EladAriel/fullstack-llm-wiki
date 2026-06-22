---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s/admission_webhook.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
    sideEffects: None
    timeoutSeconds: 30
```
