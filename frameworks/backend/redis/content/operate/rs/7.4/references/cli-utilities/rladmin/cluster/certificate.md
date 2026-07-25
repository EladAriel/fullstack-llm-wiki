---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/references/cli-utilities/rladmin/cluster/certificate.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: rladmin cluster certificate
alwaysopen: false
categories:
- docs
- operate
- rs
description: Sets the cluster certificate.
headerRange: '[1-2]'
linkTitle: certificate
tags:
- configured
toc: 'true'
weight: $weight
url: '/operate/rs/7.4/references/cli-utilities/rladmin/cluster/certificate/'
---

Sets a cluster certificate to a specified PEM file.

```sh
rladmin cluster certificate
        set <certificate name>
        certificate_file <certificate filepath>
        [ key_file <key filepath> ]
```

To set a certificate for a specific service, use the corresponding certificate name. See the [certificates table]({{< relref "/operate/rs/7.4/security/certificates" >}}) for the list of cluster certificates and their descriptions.

### Parameters

| Parameter | Type/Value | Description |
|-----------|------------|-------------|
| certificate name | 'cm'<br /> 'api'<br /> 'proxy'<br /> 'syncer'<br /> 'metrics_exporter' | Name of the certificate to update |
| certificate_file | filepath | Path to the certificate file |
| key_file | filepath | Path to the key file (optional) |

### Returns

Reports that the certificate was set to the specified file. Returns an error message if the certificate fails to update.

### Example

```sh
$ rladmin cluster certificate set proxy \
       certificate_file /tmp/proxy.pem
Set proxy certificate to contents of file /tmp/proxy.pem
```
