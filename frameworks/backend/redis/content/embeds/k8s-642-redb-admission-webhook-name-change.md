---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s-642-redb-admission-webhook-name-change.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

 [Versions 6.4.2 and later]({{< relref "/operate/kubernetes/release-notes/previous-releases/" >}}) uses a new `ValidatingWebhookConfiguration` resource to replace `redb-admission`. To use newer releases, delete the old webhook resource and apply the new file.

1. Delete the existing `ValidatingWebhookConfiguration` on the Kubernetes cluster (named `redb-admission`).

        ```sh
        kubectl delete ValidatingWebhookConfiguration redb-admission
        ```

1. Apply the resource from the new file.

        ```sh
        kubectl apply -f deploy/admission/webhook.yaml
        ```
        