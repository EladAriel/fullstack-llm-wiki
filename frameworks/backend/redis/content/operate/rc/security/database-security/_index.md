---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/security/database-security/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Cloud database security
alwaysopen: false
categories:
- docs
- operate
- rc
description: null
hideListLinks: true
weight: 20
---

Redis Cloud provides several features to help you secure your databases. These include
[password-based authentication]({{< relref "/operate/rc/security/access-control/data-access-control/default-user" >}}) and [role-based access control]({{< relref "/operate/rc/security/access-control/data-access-control/role-based-access-control.md" >}}),
[network security]({{< relref "/operate/rc/security/database-security/network-security.md" >}}), [TLS]({{< relref "/operate/rc/security/database-security/tls-ssl.md" >}}), and [encryption-at-rest]({{< relref "/operate/rc/security/encryption-at-rest.md" >}}).

## Passwords, users, and roles

All Redis Cloud databases [require a password]({{< relref "/operate/rc/security/access-control/data-access-control/default-user" >}}) to connect. However, we recommend enabling [role-based access control]({{< relref "/operate/rc/security/access-control/data-access-control/role-based-access-control.md" >}}) (RBAC) for additional security. With RBAC, you can define
all the roles you need, with the appropriate permissions, and assign those roles
to your users.

## Network security

Redis Cloud supports two types of network security: [IP Restrictions]({{< relref "/operate/rc/security/database-security/network-security.md" >}}#ip) and [VPCs]({{< relref "/operate/rc/security/database-security/network-security.md" >}}#virtual-private-clouds). We recommend that you employ at least one of these network security options to constrain access to your databases.

## Transport Layer Security (TLS)

Redis Cloud supports [Transport Layer Security]({{< relref "/operate/rc/security/database-security/tls-ssl.md" >}}) (TLS) for database access. TLS, often called "SSL", ensures the privacy of the TCP connection between your application and database. When client
authentication is activated, TLS ensures that only clients with an authorized key can access to your Redis databases.

We strongly recommend enabling TLS for any application transmitting sensitive data across the wire.

## Disk encryption

Redis Cloud provides encryption for all data stored on disk in Redis databases. See our [encryption at rest documentation]({{< relref "/operate/rc/security/encryption-at-rest.md" >}}) for specific details.

## Continue learning with Redis University

{{< university-links >}}
