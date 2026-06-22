---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/kubernetes/7.22/security/_index.md"
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
url: '/operate/kubernetes/7.22/security/'
---

Configure security settings for your Redis Enterprise deployment on Kubernetes. Redis Enterprise for Kubernetes provides comprehensive security features including TLS encryption, authentication, access control, and certificate management.

## Credentials and authentication

Manage cluster credentials and authentication settings:

- [Manage REC credentials]({{< relref "/operate/kubernetes/7.22/security/manage-rec-credentials" >}}) - Configure and manage Redis Enterprise cluster credentials
- [LDAP authentication]({{< relref "/operate/kubernetes/7.22/security/ldap" >}}) - Integrate with LDAP for centralized authentication

## Certificates and encryption

Configure TLS certificates and encryption for secure communications:

- [Manage REC certificates]({{< relref "/operate/kubernetes/7.22/security/manage-rec-certificates" >}}) - Configure cluster certificates for TLS encryption
- [Add client certificates]({{< relref "/operate/kubernetes/7.22/security/add-client-certificates" >}}) - Set up client certificate authentication for databases
- [Internode encryption]({{< relref "/operate/kubernetes/7.22/security/internode-encryption" >}}) - Enable encryption between cluster nodes and configure custom certificates

## Resource management

Configure security-related resource settings:

- [Allow resource adjustment]({{< relref "/operate/kubernetes/7.22/security/allow-resource-adjustment" >}}) - Enable automatic adjustment of system resources for security compliance
