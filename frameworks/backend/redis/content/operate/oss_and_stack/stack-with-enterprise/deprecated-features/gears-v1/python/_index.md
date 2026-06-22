---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: RedisGears Python plugin
alwaysopen: false
categories:
- docs
- operate
- stack
description: The RedisGears Python plugin allows you to run RedisGears functions with
  Python.
hideListLinks: true
linkTitle: Run with Python
weight: 71
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/python/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
bannerChildren: true
---

With the RedisGears Python plugin, you can write RedisGears functions in [Python](https://www.python.org/) and run them on a [Redis Software]({{< relref "/operate/rs/" >}}) cluster.

The Python plugin allows both batch processing and event-driven processing.

Before you can run RedisGears with Python, you will need to [install the RedisGears module and the Python plugin]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears" >}}) on your Redis Software cluster and [enable them for your database]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/install" >}}).

Once you have written your code, upload it to a node on your Redis Software cluster. Use the `RG.PYEXECUTE` command with the `redis-cli` command-line tool to run your code.

## More info

- [RedisGears Python quick start]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/quickstart" >}})
- [RedisGears recipes]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/recipes" >}})