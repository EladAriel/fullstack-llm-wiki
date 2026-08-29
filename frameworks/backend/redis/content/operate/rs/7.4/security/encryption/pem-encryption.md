---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/security/encryption/pem-encryption.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.737134Z"
---
# Pem Encryption

---
alwaysopen: false
categories:
- docs
- operate
- rs
description: Enable PEM encryption to encrypt all private keys on disk.
linkTitle: Encrypt private keys
title: Encrypt private keys
toc: 'true'
weight: 50
url: '/operate/rs/7.4/security/encryption/pem-encryption/'
---

Enable PEM encryption to automatically encrypt all private keys on disk. Public keys (`.cert` files) are not encrypted.

When certificates are rotated, the encrypted private keys are also rotated.

## Enable PEM encryption

To enable PEM encryption and encrypt private keys on the disk, use [`rladmin`]({{< relref "/operate/rs/7.4/references/cli-utilities/rladmin" >}}) or the [REST API]({{< relref "/operate/rs/7.4/references/rest-api" >}}).


- [`rladmin cluster config`]({{< relref "/operate/rs/7.4/references/cli-utilities/rladmin/cluster/config" >}}):

    ```sh
    rladmin cluster config encrypt_pkeys enabled
    ```

- [Update cluster settings]({{< relref "/operate/rs/7.4/references/rest-api/requests/cluster#put-cluster" >}}) REST API request:

    ```sh
    PUT /v1/cluster
    { "encrypt_pkeys": true }
    ```

## Deactivate PEM encryption

To deactivate PEM encryption and decrypt private keys on the disk, use [`rladmin`]({{< relref "/operate/rs/7.4/references/cli-utilities/rladmin" >}}) or the [REST API]({{< relref "/operate/rs/7.4/references/rest-api" >}}).

- [`rladmin cluster config`]({{< relref "/operate/rs/7.4/references/cli-utilities/rladmin/cluster/config" >}}):

    ```sh
    rladmin cluster config encrypt_pkeys disabled
    ```

- [Update cluster settings]({{< relref "/operate/rs/7.4/references/rest-api/requests/cluster#put-cluster" >}}) REST API request:

    ```sh
    PUT /v1/cluster
    { "encrypt_pkeys": false }
    ```
