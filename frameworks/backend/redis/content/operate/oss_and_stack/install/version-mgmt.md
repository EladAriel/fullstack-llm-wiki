---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/install/version-mgmt.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Open Source version management
alwaysopen: false
categories:
- docs
- operate
- oss
description: Describes Redis Open Source supported database versions.
linkTitle: Version management
weight: 25
tocEmbedHeaders: true
---

Redis Open Source provides comprehensive version management that prioritizes customer control over major changes. 

## Redis version structure

Redis uses a **MAJOR.MINOR.PATCH** versioning scheme:

- **Major versions**: Significant changes that may include breaking changes (for example, Redis 7 → Redis 8).
- **Minor versions**: New features and improvements within a major version (for example, 8.2 → 8.4 → 8.6 → 8.8).
- **Patch versions**: Bug fixes and security updates (for example, 8.6.1 → 8.6.2).

## Supported versions

{{< note >}}
**We strongly recommend using the latest available version** to benefit from the newest features, performance improvements, and security updates.
{{< /note >}}

| Version | Status | EOL Date |
|---------|--------|----------|
| **Redis 8.8** | GA | TBD |
| **Redis 8.6** | GA | TBD |
| **Redis 8.4** | GA | TBD |
| **Redis 8.2** | GA | September 1, 2030 |
| **Redis 8.0** | GA | December 1, 2026 |
| **Redis 7.4** | GA | December 1, 2029 |
| **Redis 7.2** | GA | December 1, 2029 |
| **Redis 6.2** | GA | April 1, 2027 |
