---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/8.0.18/security/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
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
url: '/operate/kubernetes/8.0.18/security/'
---

Configure security settings for your Redis Enterprise deployment on Kubernetes. Redis Enterprise for Kubernetes provides comprehensive security features including TLS encryption, authentication, access control, and certificate management.

## Credentials and authentication

Manage cluster credentials and authentication settings:

- [Manage REC credentials]({{< relref "/operate/kubernetes/8.0.18/security/manage-rec-credentials" >}}) - Configure and manage Redis Enterprise cluster credentials
- [Configuration secrets]({{< relref "/operate/kubernetes/8.0.18/security/configuration-secrets" >}}) - Store Redis Enterprise configuration items in Kubernetes Secrets for automatic updates and secure management
- [LDAP authentication]({{< relref "/operate/kubernetes/8.0.18/security/ldap" >}}) - Integrate with LDAP for centralized authentication
- [SSO authentication]({{< relref "/operate/kubernetes/8.0.18/security/sso" >}}) - Enable SAML-based single sign-on for Cluster Manager UI access

## Certificates and encryption

Configure TLS certificates and encryption for secure communications:

- [Manage REC certificates]({{< relref "/operate/kubernetes/8.0.18/security/manage-rec-certificates" >}}) - Configure cluster certificates for TLS encryption
- [cert-manager integration]({{< relref "/operate/kubernetes/8.0.18/security/cert-manager" >}}) - Automate TLS certificate management with cert-manager
- [Add client certificates]({{< relref "/operate/kubernetes/8.0.18/security/add-client-certificates" >}}) - Set up client certificate authentication for databases
- [Internode encryption]({{< relref "/operate/kubernetes/8.0.18/security/internode-encryption" >}}) - Enable encryption between cluster nodes and configure custom certificates

## Secret management

Configure external secret management systems:

- [HashiCorp Vault integration]({{< relref "/operate/kubernetes/8.0.18/security/vault" >}}) - Configure HashiCorp Vault as the centralized secret management system for Redis Enterprise for Kubernetes

## Resource management

Configure security-related resource settings:

- [Allow resource adjustment]({{< relref "/operate/kubernetes/8.0.18/security/allow-resource-adjustment" >}}) - Enable automatic adjustment of system resources for security compliance
