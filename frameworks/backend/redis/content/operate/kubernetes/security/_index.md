---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/security/_index.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.119387Z"
---
# _Index

---
Title: Security
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: Configure security settings for Redis Software clusters and databases on Kubernetes.
hideListLinks: true
linkTitle: Security
weight: 50
---

Configure security settings for Redis for Kubernetes. Security covers access control, cluster credentials, external identity providers, TLS certificates and encryption, and external secret management.

## Access control

- [Access control]({{< relref "/operate/kubernetes/security/access-control" >}}) — manage Redis Software users, roles, ACLs, and role bindings as Kubernetes custom resources.

## Authentication

- [Authentication]({{< relref "/operate/kubernetes/security/authentication" >}}) — manage cluster credentials, LDAP, SAML SSO, and configuration secrets.

## Certificates and encryption

- [Certificates and encryption]({{< relref "/operate/kubernetes/security/certificates" >}}) — provision TLS certificates, integrate cert-manager, add client certificates, and enable internode encryption.

## Secret management

- [HashiCorp Vault integration]({{< relref "/operate/kubernetes/security/vault" >}}) — use HashiCorp Vault as the centralized secret store for Redis for Kubernetes.

## Resource management

- [Allow resource adjustment]({{< relref "/operate/kubernetes/security/allow-resource-adjustment" >}}) — enable automatic adjustment of system resources for security compliance.

## Compliance

- [FIPS compliance]({{< relref "/operate/kubernetes/security/fips" >}}) — run your cluster in FIPS 140-3 compliance mode.
