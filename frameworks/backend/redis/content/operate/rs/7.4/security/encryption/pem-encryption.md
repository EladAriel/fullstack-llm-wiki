---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/security/encryption/pem-encryption.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

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
