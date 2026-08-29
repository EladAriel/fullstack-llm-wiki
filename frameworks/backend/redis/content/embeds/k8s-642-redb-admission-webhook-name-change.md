---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s-642-redb-admission-webhook-name-change.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.102502Z"
---
# K8S 642 Redb Admission Webhook Name Change

 [Versions 6.4.2 and later]({{< relref "/operate/kubernetes/release-notes/previous-releases/" >}}) uses a new `ValidatingWebhookConfiguration` resource to replace `redb-admission`. To use newer releases, delete the old webhook resource and apply the new file.

1. Delete the existing `ValidatingWebhookConfiguration` on the Kubernetes cluster (named `redb-admission`).

        ```sh
        kubectl delete ValidatingWebhookConfiguration redb-admission
        ```

1. Apply the resource from the new file.

        ```sh
        kubectl apply -f deploy/admission/webhook.yaml
        ```
        