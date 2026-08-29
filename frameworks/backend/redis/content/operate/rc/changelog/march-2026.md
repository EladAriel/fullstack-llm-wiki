---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/rc/changelog/march-2026.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.291955Z"
---
# March 2026

---
Title: Redis Cloud changelog (March 2026)
alwaysopen: false
categories:
- docs
- operate
- rc
description: New features, enhancements, and other changes added to Redis Cloud during
  March 2026.
highlights: Passwordless authentication for Redis Cloud Pro, Redis 8.4 on Redis Cloud Pro, Automatic database upgrades
linktitle: March 2026
weight: 53
tags:
- changelog
---

## New features

### Passwordless authentication for Redis Cloud Pro

Passwordless authentication is now available for Redis Cloud Pro databases on subscriptions that have [blocked the public endpoint]({{< relref "/operate/rc/security/database-security/block-public-endpoints" >}}). For more information, see [Turn on passwordless authentication for the default user]({{< relref "/operate/rc/security/database-security/block-public-endpoints#turn-on-passwordless-authentication-for-the-default-user" >}}).

### Redis 8.4 on Redis Cloud Pro

Redis 8.4 is now available for [Redis Cloud Pro databases]({{< relref "/operate/rc/databases/create-database/create-essentials-database" >}}) in select regions.

Redis 8.4 builds on the foundation of Redis 8.2 with significant enhancements to cluster operations, string manipulation, and stream processing capabilities. For more information on the changes in Redis 8.4, see [What's new in Redis 8.4]({{<relref "/develop/whats-new/8-4" >}}) and review the Redis Open Source [8.4 release notes]({{<relref "/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.4-release-notes" >}}).

### Automatic database upgrades

All Redis Cloud databases running Redis 8.4 and later will be automatically upgraded to the next minor version upon release. For example, all Redis 8.4 databases will be upgraded to Redis 8.6 when it is available on Redis Cloud.

Redis Cloud Pro users can opt out of minor version auto-upgrades. See [Version management]({{< relref "/operate/rc/databases/version-management" >}}) for more details.

