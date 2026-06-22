---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/tools/insight/release-notes/v.2.48.0.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Redis Insight v2.48.0, April 2024
linkTitle: v2.48.0 (April 2024)
date: 2024-04-10 00:00:00 +0000
description: Redis Insight v2.48
weight: 1

---
## 2.48 (April 2024)
This is the General Availability (GA) release of Redis Insight 2.48.

### Highlights
- New look, equally fast.
- Learn Redis faster by uploading sample data and a concise tutorial for empty databases.
- Enhance the security and scalability when running Redis Insight on Docker behind a proxy by adding support for the static proxy subpath.


### Details

**Features and improvements**
- [#3233](https://github.com/RedisInsight/RedisInsight/pull/3233) New look, equally fast. We've refreshed our Redis Insight app to align with our new brand look.
- [#3224](https://github.com/RedisInsight/RedisInsight/pull/3224) Jumpstart your Redis journey by uploading sample data with JSON and basic data structures for empty databases. To upload the sample data, navigate to the Browser screen for your empty database and initiate the upload process with just a click.
- [#2711](https://github.com/RedisInsight/RedisInsight/pull/2711) Enhance the security and scalability by running Redis Insight on Docker [behind a proxy](https://github.com/RedisInsight/RedisInsight-reverse-proxy) using the newly added support for the static proxy subpath. Use the `RIPROXYPATH` environment variable to configure the subpath proxy path.
