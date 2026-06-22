---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/references/cli-utilities/rladmin/cluster/certificate.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/rs/7.8/references/cli-utilities/rladmin/cluster/certificate/'
---

Sets a cluster certificate to a specified PEM file.

```sh
rladmin cluster certificate
        set <certificate name>
        certificate_file <certificate filepath>
        [ key_file <key filepath> ]
```

To set a certificate for a specific service, use the corresponding certificate name. See the [certificates table]({{< relref "/operate/rs/7.8/security/certificates" >}}) for the list of cluster certificates and their descriptions.

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
