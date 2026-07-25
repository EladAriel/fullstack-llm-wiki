---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0/security/_index.md"
source_commit: "9d30f68c3dad1a6b3b7d30fe604b911348ce8152"
source_commit_short: "9d30f68c"
source_commit_date: "2026-07-24T10:52:10-07:00"
generated_at: "2026-07-25T11:51:22Z"
---

---
Title: Security
alwaysopen: false
categories:
- docs
- operate
- kubernetes
description: Configure security settings for Redis Enterprise clusters and databases on Kubernetes.
hideListLinks: true
linkTitle: Security
weight: 50
url: '/operate/kubernetes/8.0/security/'
---

Configure security settings for your Redis Enterprise deployment on Kubernetes. Redis Enterprise for Kubernetes provides comprehensive security features including TLS encryption, authentication, access control, and certificate management.

## Credentials and authentication

Manage cluster credentials and authentication settings:

- [Manage REC credentials]({{< relref "/operate/kubernetes/8.0/security/manage-rec-credentials" >}}) - Configure and manage Redis Enterprise cluster credentials
- [Configuration secrets]({{< relref "/operate/kubernetes/8.0/security/configuration-secrets" >}}) - Store Redis Enterprise configuration items in Kubernetes Secrets for automatic updates and secure management
- [LDAP authentication]({{< relref "/operate/kubernetes/8.0/security/ldap" >}}) - Integrate with LDAP for centralized authentication
- [SSO authentication]({{< relref "/operate/kubernetes/8.0/security/sso" >}}) - Enable SAML-based single sign-on for Cluster Manager UI access

## Certificates and encryption

Configure TLS certificates and encryption for secure communications:

- [Manage REC certificates]({{< relref "/operate/kubernetes/8.0/security/manage-rec-certificates" >}}) - Configure cluster certificates for TLS encryption
- [Add client certificates]({{< relref "/operate/kubernetes/8.0/security/add-client-certificates" >}}) - Set up client certificate authentication for databases
- [Internode encryption]({{< relref "/operate/kubernetes/8.0/security/internode-encryption" >}}) - Enable encryption between cluster nodes and configure custom certificates

## Secret management

Configure external secret management systems:

- [HashiCorp Vault integration]({{< relref "/operate/kubernetes/8.0/security/vault" >}}) - Configure HashiCorp Vault as the centralized secret management system for Redis Enterprise for Kubernetes

## Resource management

Configure security-related resource settings:

- [Allow resource adjustment]({{< relref "/operate/kubernetes/8.0/security/allow-resource-adjustment" >}}) - Enable automatic adjustment of system resources for security compliance
