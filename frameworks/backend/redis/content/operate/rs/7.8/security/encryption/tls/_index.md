---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rs/7.8/security/encryption/tls/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Transport Layer Security (TLS)
alwaysopen: false
categories:
- docs
- operate
- rs
description: An overview of Transport Layer Security (TLS).
hideListLinks: true
linkTitle: TLS
weight: 10
url: '/operate/rs/7.8/security/encryption/tls/'
---
[Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security), a successor to SSL, ensures the privacy of data sent between applications and Redis databases. TLS also secures connections between Redis Enterprise Software nodes.

You can [use TLS authentication]({{< relref "/operate/rs/7.8/security/encryption/tls/enable-tls" >}}) for the following types of communication:

- Communication from clients (applications) to your database
- Communication from your database to other clusters for replication using [Replica Of]({{< relref "/operate/rs/7.8/databases/import-export/replica-of" >}})
- Communication to and from your database to other clusters for synchronization using [Active-Active]({{< relref "/operate/rs/7.8/databases/active-active/" >}})

## Protocols and ciphers

TLS protocols and ciphers define the overall suite of algorithms that clients are able to connect to the servers with.

You can change the [TLS protocols]({{< relref "/operate/rs/7.8/security/encryption/tls/tls-protocols" >}}) and [ciphers]({{< relref "/operate/rs/7.8/security/encryption/tls/ciphers" >}}) to improve the security of your Redis Enterprise cluster and databases. The default settings are in line with industry best practices, but you can customize them to match the security policy of your organization.
