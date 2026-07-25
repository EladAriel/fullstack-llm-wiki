---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/security/certificates/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Certificates and encryption
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: Manage TLS certificates, client certificates, and internode encryption for Redis Software on Kubernetes.
hideListLinks: true
linkTitle: Certificates and encryption
weight: 30
---

Certificates and encryption use Kubernetes Secrets and cert-manager integration to provision, distribute, and rotate the TLS certificates that Redis Software relies on. The operator distributes referenced certificates across every cluster node.

## How certificates work on Redis for Kubernetes

- **Cluster certificates** live in Kubernetes Secrets that the `RedisEnterpriseCluster` spec references. The operator distributes them to every cluster node.
- **cert-manager** can issue and rotate certificates automatically.
- **Client certificates** live in a Secret that the database references for mutual TLS authentication.
- **Internode encryption** is configured on the REC spec. The operator places the certificates on each node.

## What's the same as Redis Software

The underlying certificate roles, requirements, and TLS behavior are unchanged. For concepts and reference details, see the existing Redis Software docs:

- [Certificate roles and types]({{< relref "/operate/rs/security/certificates" >}}) — which certificate is used for what.
- [Create certificates]({{< relref "/operate/rs/security/certificates/create-certificates" >}}) — certificate requirements (SAN, CN, validity).
- [Update certificates]({{< relref "/operate/rs/security/certificates/updating-certificates" >}}) — rotation considerations on Redis Software.
- [Monitor certificates]({{< relref "/operate/rs/security/certificates/monitor-certificates" >}}) — certificate expiration alerts.
- [Client certificate authentication]({{< relref "/operate/rs/security/certificates/certificate-based-authentication" >}}) — how the cluster validates client certificates.
- [TLS protocols]({{< relref "/operate/rs/security/encryption/tls/tls-protocols" >}}) and [ciphers]({{< relref "/operate/rs/security/encryption/tls/ciphers" >}}) — protocol and cipher selection.
- [Enable TLS]({{< relref "/operate/rs/security/encryption/tls/enable-tls" >}}) — TLS for management, replication, and client connections.
- [Internode encryption]({{< relref "/operate/rs/security/encryption/internode-encryption" >}}) — purpose and scope.
- [PEM encryption]({{< relref "/operate/rs/security/encryption/pem-encryption" >}}) — encrypted private keys.

## What's different on Kubernetes

- **You capture certificates in Kubernetes Secrets and reference them declaratively in the REC spec.** The operator applies them to the cluster through the Redis Software REST API — the same way certificates are applied on Redis Software, cluster-wide rather than file-by-file on each node.
- **cert-manager can issue and rotate certificates automatically**, replacing manual rotation steps.

## In this section

- [Manage REC certificates]({{< relref "/operate/kubernetes/security/certificates/manage-rec-certificates" >}}) — configure cluster TLS certificates.
- [cert-manager integration]({{< relref "/operate/kubernetes/security/certificates/cert-manager" >}}) — automate certificate issuance and rotation with cert-manager.
- [Add client certificates]({{< relref "/operate/kubernetes/security/certificates/add-client-certificates" >}}) — enable client certificate authentication for databases.
- [Internode encryption]({{< relref "/operate/kubernetes/security/certificates/internode-encryption" >}}) — enable encryption between cluster nodes.
