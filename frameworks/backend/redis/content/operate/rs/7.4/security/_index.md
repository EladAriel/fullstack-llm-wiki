---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.4/security/_index.md"
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
- rs
description: null
hideListLinks: true
weight: 60
aliases:
    - /operate/rs/administering/designing-production/security
url: '/operate/rs/7.4/security/'
---

Redis Enterprise Software provides various features to secure your Redis Enterprise Software deployment:

| Login and passwords | Users and roles | Encryption and TLS | Certificates and audit |
|---------------------|-----------------|--------------------|-----------------------|
| [Password attempts and session timeout]({{<relref "/operate/rs/7.4/security/access-control/manage-users/login-lockout">}}) | [Cluster and database access explained]({{<relref "/operate/rs/7.4/security/access-control">}}) | [Enable TLS]({{<relref "/operate/rs/7.4/security/encryption/tls/enable-tls">}}) | [Create certificates]({{<relref "/operate/rs/7.4/security/certificates/create-certificates">}}) |
| [Password complexity]({{<relref "/operate/rs/7.4/security/access-control/manage-passwords/password-complexity-rules">}}) | [Create users]({{<relref "/operate/rs/7.4/security/access-control/create-users">}}) | [Configure TLS protocols]({{<relref "/operate/rs/7.4/security/encryption/tls/tls-protocols">}}) | [Monitor certificates]({{<relref "/operate/rs/7.4/security/certificates/monitor-certificates">}}) |
| [Password expiration]({{<relref "/operate/rs/7.4/security/access-control/manage-passwords/password-expiration">}}) | [Create roles]({{<relref "/operate/rs/7.4/security/access-control/create-combined-roles">}}) | [Configure cipher suites]({{<relref "/operate/rs/7.4/security/encryption/tls/ciphers">}}) | [Update certificates]({{<relref "/operate/rs/7.4/security/certificates/updating-certificates">}}) |
| [Default database access]({{<relref "/operate/rs/7.4/security/access-control/manage-users/default-user">}}) | [Redis ACLs]({{<relref "/operate/rs/7.4/security/access-control/redis-acl-overview">}}) | [Encrypt private keys on disk]({{<relref "/operate/rs/7.4/security/encryption/pem-encryption">}}) | [Enable OCSP stapling]({{<relref "/operate/rs/7.4/security/certificates/ocsp-stapling">}}) |
| [Rotate user passwords]({{<relref "/operate/rs/7.4/security/access-control/manage-passwords/rotate-passwords">}}) | [Integrate with LDAP]({{<relref "/operate/rs/7.4/security/access-control/ldap">}}) | [Internode encryption]({{<relref "/operate/rs/7.4/security/encryption/internode-encryption">}}) | [Audit database connections]({{<relref "/operate/rs/7.4/security/audit-events">}}) |

## Recommended security practices

See [Recommended security practices]({{<relref "/operate/rs/7.4/security/recommended-security-practices">}}) to learn how to protect Redis Enterprise Software.

## Redis Trust Center

Visit our [Trust Center](https://trust.redis.io/) to learn more about Redis security policies. If you find a suspected security bug, you can [submit a report](https://hackerone.com/redis-vdp?type=team).
