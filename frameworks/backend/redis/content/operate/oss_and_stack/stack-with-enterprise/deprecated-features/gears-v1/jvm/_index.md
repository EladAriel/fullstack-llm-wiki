---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisGears JVM plugin
alwaysopen: false
categories:
- docs
- operate
- stack
description: The RedisGears JVM plugin allows you to run RedisGears functions in the
  Java virtual machine.
hideListLinks: true
linkTitle: Run with JVM
weight: 75
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/jvm/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

With the [RedisGears JVM plugin](https://github.com/RedisGears/JVMPlugin), you can write RedisGears functions in [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) and run them on a [Redis Software]({{< relref "/operate/rs/" >}}) cluster. It currently supports [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) version 11.

Similar to the Python plugin, the JVM plugin allows both batch processing and event-driven processing.

Before you can run RedisGears with Java, you will need to [install the RedisGears module and the JVM plugin]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears" >}}) on your Redis Software cluster and [enable them for your database]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/install" >}}).

Once you have written your code, compile and package it into a [JAR](https://en.wikipedia.org/wiki/JAR_(file_format)) file and upload it to a node on your Redis Software cluster. Use the `RG.JEXECUTE` command with the `redis-cli` command-line tool to run your code.

## More info

- [RedisGears JVM quick start]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/quickstart" >}})
- [RedisGears Java classes and functions]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes" >}})
- [RedisGears recipes]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/recipes" >}})