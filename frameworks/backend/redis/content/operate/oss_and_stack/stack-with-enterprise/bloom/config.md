---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/bloom/config.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.251632Z"
---
# Config

---
Title: Probabilistic data structure configuration compatibility with Redis Software
alwaysopen: false
categories:
- docs
- operate
- stack
description: Probabilistic data structure configuration settings supported by Redis Software and Redis Cloud.
linkTitle: Configuration
toc: 'false'
weight: 30
---

## Configure probabilistic data structures in Redis Software

[Redis Software]({{< relref "/operate/rs" >}}) lets you manually change any [RedisBloom configuration setting]({{< relref "/develop/data-types/probabilistic/" >}}configuration/#redisbloom-configuration-parameters).

To change the RedisBloom configuration using the Redis Software Cluster Manager UI:

  1. From the **Databases** list, select the database, then click **Configuration**.

  1. Select the **Edit** button.

  1. In the **Capabilities** section, click **Parameters**.

  1. After you finish editing the module's configuration parameters, click **Done** to close the parameter editor.

  1. Click **Save**.

## Configure probabilistic data structures in Redis Cloud

[Redis Cloud]({{< relref "/operate/rc" >}}) does not let you configure RedisBloom manually. However, if you have a Flexible or Annual [subscription]({{< relref "/operate/rc/subscriptions" >}}), you can contact [support](https://redis.com/company/support/) to request a configuration change. You cannot change RedisBloom configuration for Free or Fixed subscriptions.

## Configuration settings

See [configuration parameters]({{< relref "/develop/data-types/probabilistic/configuration" >}}) in the Develop section for parameter details and compatibility with Redis Software and Redis Cloud.
