---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/security/certificates/add-client-certificates.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
categories:
- docs
- operate
- kubernetes
aliases: [/operate/kubernetes/security/add-client-certificates/]
description: Add client certificates to your REDB custom resource.
linkTitle: Add client certificates
title: Add client certificates
weight: 30
---

For each client certificate you want to use with your database, you need to create a Kubernetes secret to hold it. You can then reference that secret in your Redis Enterprise database (REDB) custom resource spec.

## Create a secret to hold the new certificate

1. [Create the secret config file](https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-config-file/) with the required fields shown below.

    ```yaml
    apiVersion: v1
    kind: Secret
    type: Opaque
    metadata:
      name: <client-cert-secret>
      namespace: <your-rec-namespace>
    data:
      cert: <client-certificate>
    ```
  
1. Apply the file to create the secret resource.

    ```bash
    kubectl apply -f <client-cert-secret>.yaml
    ```

## Edit the REDB resource

1. Add the secret name to the REDB custom resource (`redb.yaml`) with the `clientAuthenticationCertificates` property in the `spec` section.

  ```yaml
   spec:
      clientAuthenticationCertificates:
      - <client-cert-secret>
  ```