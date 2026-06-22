---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/security/certificates/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Certificates
alwaysopen: false
categories:
- docs
- operate
- rs
description: An overview of certificates in Redis Enterprise Software.
hideListLinks: true
linkTitle: Certificates
weight: 60
url: '/operate/rs/7.4/security/certificates/'
---

Redis Enterprise Software uses self-signed certificates by default to ensure that the product is secure. If using a self-signed certificate is not the right solution for you, you can import a certificate signed by a certificate authority of your choice.

Here's the list of self-signed certificates that create secure, encrypted connections to your Redis Enterprise cluster:

| Certificate name | Description |
|------------------|-------------|
| `api` | Encrypts [REST API]({{< relref "/operate/rs/7.4/references/rest-api/" >}}) requests and responses. |
| `cm` | Secures connections to the Redis Enterprise Cluster Manager UI. |
| `ldap_client` | Secures connections between LDAP clients and LDAP servers. |
| `metrics_exporter` | Sends Redis Enterprise metrics to external [monitoring tools]({{< relref "/operate/rs/7.4/clusters/monitoring/" >}}) over a secure connection. |
| `proxy` | Creates secure, encrypted connections between clients and databases. |
| `syncer` | For [Active-Active]({{< relref "/operate/rs/7.4/databases/active-active/" >}}) or [Replica Of]({{< relref "/operate/rs/7.4/databases/import-export/replica-of/" >}}) databases, encrypts data during the synchronization of participating clusters. |

These self-signed certificates are generated on the first node of each Redis Enterprise Software installation and are copied to all other nodes added to the cluster.

When you use the default self-signed certificates and you connect to the Cluster Manager UI over a web browser, you'll see an untrusted connection notification.

Depending on your browser, you can allow the connection for each session or add an exception to trust the certificate for all future sessions.
