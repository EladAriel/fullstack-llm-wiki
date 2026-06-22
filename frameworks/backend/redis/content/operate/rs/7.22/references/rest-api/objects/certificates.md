---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.22/references/rest-api/objects/certificates.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Certificates object
alwaysopen: false
categories:
- docs
- operate
- rs
description: An object that represents a certificate
linkTitle: certificates
weight: $weight
url: '/operate/rs/7.22/references/rest-api/objects/certificates/'
---

An API object that represents a certificate used by a Redis Enterprise Software cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| name | `cm`<br />`api`<br />`mtls_trusted_ca`<br />`proxy`<br />`metrics_exporter`<br />`syncer`<br />`ldap_client`<br />`ccs_internode_encryption`<br />`data_internode_encryption` | Certificate type.<br />See the [certificates table]({{< relref "/operate/rs/7.22/security/certificates" >}}) for the list of cluster certificates and their descriptions. |
| certificate | string | The certificate in PEM format |
| key | string | The private key in PEM format |
