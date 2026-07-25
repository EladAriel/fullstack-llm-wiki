---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/certificates.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
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
---

An API object that represents a certificate used by a Redis Software cluster.

| Name | Type/Value | Description |
|------|------------|-------------|
| name | "cm"<br />"api"<br />"mtls_trusted_ca"<br />"proxy"<br />"metrics_exporter"<br />"syncer"<br />"ldap_client"<br />"ccs_internode_encryption"<br />"data_internode_encryption"<br />"sso_service"<br />"sso_issuer" | Certificate type.<br />See the [certificates table]({{< relref "/operate/rs/security/certificates" >}}) for the list of cluster certificates and their descriptions. |
| certificate | string | The certificate in PEM format |
| key | string | The private key in PEM format |
