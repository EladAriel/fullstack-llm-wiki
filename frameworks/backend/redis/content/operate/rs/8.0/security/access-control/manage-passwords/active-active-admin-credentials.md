---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/8.0/security/access-control/manage-passwords/active-active-admin-credentials.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Update admin credentials for Active-Active databases
alwaysopen: false
categories:
- docs
- operate
- rs
description: Update admin credentials for Active-Active databases.
linkTitle: Update Active-Active admin credentials
weight: 90
url: '/operate/rs/8.0/security/access-control/manage-passwords/active-active-admin-credentials/'
---

Active-Active databases use administrator credentials to manage operations. When you change the administrator password on clusters with Active-Active databases, you must update the Active-Active database configuration to prevent authentication failures during Active-Active management operations.

{{<warning>}}
Do not perform any management operations on the databases until these steps are complete.
{{</warning>}}

To update the administrator password on a cluster with Active-Active databases:

1. From the user management page, update the administrator user password on the clusters you want to update.

1. Run [`crdb-cli crdb list`]({{<relref "/operate/rs/8.0/references/cli-utilities/crdb-cli/crdb/list">}}) to find the `CRDB-GUID` that uniquely identifies each Active-Active database and the fully qualified domain names (`FQDN`) of each participating cluster:

    ```sh
    crdb-cli crdb list
    ```

    Example output:

    ```sh
    CRDB-GUID                             NAME        REPL-ID  FQDN
    4053a0dd-a4a5-4f38-b135-75b7a2dc7331  my-aa-db    1        fqdn1.example.com
    4053a0dd-a4a5-4f38-b135-75b7a2dc7331  my-aa-db    2        fqdn2.example.com
    ```

1. Update the Active-Active database credentials using the [`crdb-cli crdb update`]({{< relref "/operate/rs/8.0/references/cli-utilities/crdb-cli/crdb/update" >}}) command:

    ```sh
    crdb-cli crdb update \
      --crdb-guid <CRDB-GUID> \
      --credentials id=<REPL-ID-1>,username=<admin-username>,password=<FQDN-1-password> \
      --credentials id=<REPL-ID-2>,username=<admin-username>,password=<FQDN-2-password> \
      --force
    ```

    Replace the following values:

    - `<CRDB-GUID>`: The `CRDB-GUID` from the `crdb-cli crdb list` output

    - `<admin-username>`: The administrator username for the clusters

    - `<REPL-ID-1>` and `<REPL-ID-2>`: The `REPL-ID` for the corresponding FQDNs

    - `<FQDN-1-password>` and `<FQDN-2-password>`: The current administrator passwords for each cluster
