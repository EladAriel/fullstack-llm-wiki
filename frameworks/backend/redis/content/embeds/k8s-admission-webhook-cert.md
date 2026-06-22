---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/embeds/k8s-admission-webhook-cert.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

1. Verify the `admission-tls` secret exists.

    ```sh
    kubectl get secret admission-tls
    ```
  
    The output should look similar to
  
    ```sh
    NAME            TYPE     DATA   AGE
    admission-tls   Opaque   2      2m43s
    ```

1. Save the certificate to a local environment variable.

    ```sh
    CERT=`kubectl get secret admission-tls -o jsonpath='{.data.cert}'`
    ```

1. Create a Kubernetes validating webhook, replacing `<namespace>` with the namespace where the REC was installed.

    The `webhook.yaml` template can be found in [redis-enterprise-k8s-docs/admission](https://github.com/RedisLabs/redis-enterprise-k8s-docs/tree/master/admission)

    ```sh
    sed 's/OPERATOR_NAMESPACE/<namespace>/g' webhook.yaml | kubectl create -f -
    ```

1. Create a patch file for the Kubernetes validating webhook.

    ```sh
    cat > modified-webhook.yaml <<EOF
    webhooks:
    - name: redisenterprise.admission.redislabs
      clientConfig:
       caBundle: $CERT
    EOF
    ```

1. Patch the webhook with the certificate.

    ```sh
    kubectl patch ValidatingWebhookConfiguration \
        redis-enterprise-admission --patch "$(cat modified-webhook.yaml)"
    ```
