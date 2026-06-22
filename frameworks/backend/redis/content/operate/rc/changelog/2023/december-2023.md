---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/2023/december-2023.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Cloud changelog (December 2023)
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  December 2023.
highlights: Active-Active JSON support, mTLS enhancements
linktitle: December 2023
tags:
- changelog
weight: 72
aliases:
  - /operate/rc/changelog/december-2023
---

## New features

### Active-Active JSON support

[Active-Active databases]({{< relref "/operate/rc/databases/active-active" >}}) on Redis Cloud now support the [JSON]({{< relref "/operate/oss_and_stack/stack-with-enterprise/json" >}}) data type.

See [Create an Active-Active subscription]({{< relref "/operate/rc/databases/active-active/create-active-active-database" >}}) to learn how to create an Active-Active subscription.

### Mutual TLS enhancements

Databases that support [Transport layer security (TLS)]({{< relref "/operate/rc/security/database-security/tls-ssl" >}}) now support multiple client certificates for use with mutual TLS. This makes it easier to rotate client certificates outside of a maintenance window. In addition, you can now provide a client Certificate Authority chain to trust any leaf certificate it signed for more flexibility.

See [Transport layer security (TLS)]({{< relref "/operate/rc/security/database-security/tls-ssl" >}}) to learn how to enable TLS. 

