---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/install.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.261062Z"
---
# Install

---
Title: Install RedisGears and the JVM plugin
alwaysopen: false
categories:
- docs
- operate
- stack
description: 
linkTitle: Install
toc: 'true'
weight: 20
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/install/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

Before you can use RedisGears with the JVM, you need to install the RedisGears module and JVM plugin on your Redis Software cluster and enable them for a database.

## Prerequisites

1. Redis Software v6.0.12 or later

1. [Created a Redis Software cluster]({{< relref "/operate/rs/clusters/new-cluster-setup" >}})

1. [Added nodes to the cluster]({{< relref "/operate/rs/clusters/add-node" >}})

1. [Installed RedisGears and the JVM plugin]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears" >}})

## Enable RedisGears for a database

1. From the Redis Software admin console's **databases** page, select the **Add** button to create a new database:

    {{<image filename="images/rs/icon_add.png" width="30px" alt="The Add icon">}}

1. Confirm that you want to create a new Redis database with the **Next** button.

1. On the **create database** page, give your database a name.

1. For **Redis Modules**, select the **Add** button and choose RedisGears from the **Module** dropdown list.

1. Select **Add Configuration**, enter `Plugin gears_jvm` in the box, then select the **OK** button:

    {{<image filename="images/rs/icon_save.png" width="30px" alt="The Save icon">}}

    {{<note>}}
You can configure additional JVM options in this box. For example:<br></br>
`Plugin gears_jvm JvmOptions `<nobr>`'-Dproperty1=value1`</nobr> <nobr>`-Dproperty2=value2'`</nobr>
    {{</note>}}

1. Select the **Activate** button.

## Verify the install

Run the `RG.JSTATS` command from a database shard to view statistics and verify that you set up RedisGears and the JVM plugin correctly:

```sh
$ shard-cli 3
172.16.0.1:12345> RG.JSTATS
```
