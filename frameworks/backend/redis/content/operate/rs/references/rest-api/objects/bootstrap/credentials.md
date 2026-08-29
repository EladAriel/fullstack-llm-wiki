---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/references/rest-api/objects/bootstrap/credentials.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.613940Z"
---
# Credentials

---
Title: Credentials object
alwaysopen: false
categories:
- docs
- operate
- rs
description: Documents the credentials object used with Redis Software
  REST API calls.
linkTitle: credentials
weight: $weight
---

| Name | Type/Value | Description |
|------|------------|-------------|
| client_cert | string      | Client certificate as a PEM string. Use certificate credentials instead of a username and password to join a node to a cluster. Required with `client_key`. See [Certificate-based authentication for cluster management]({{<relref "/operate/rs/security/certificates/certificate-based-authentication#certificate-based-authentication-for-cluster-management">}}). |
| client_key | string       | The client certificate's private key as a PEM string. Required with `client_cert`. |
| password   | string       | Admin password. Required unless you use certificate credentials. |
| trusted_ca | string       | CA that validates the API certificate the cluster presents, as a PEM string. If you omit it, the cluster uses the certificates in its `mtls_trusted_ca.pem` file. |
| username   | string       | Admin username (pattern does not allow special characters &,\<,>,"). Required unless you use certificate credentials. |
