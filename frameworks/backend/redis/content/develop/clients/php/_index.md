---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/clients/php/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
aliases:
- /develop/connect/clients/php
- /connect/clients/php/
- /clients/php/
- /develop/clients/predis
categories:
- docs
- develop
- stack
- oss
- rs
- rc
- oss
- kubernetes
- clients
description: Connect your PHP application to a Redis database
linkTitle: Predis (PHP)
title: Predis guide (PHP)
weight: 8
---

[`Predis`](https://github.com/predis/predis) is the recommended [PHP](https://php.net/)
client for Redis. 
The sections below explain how to install `Predis` and connect your application to a Redis database.

{{< note >}}Although we provide basic documentation for `Predis`, it is a third-party
client library and is not developed or supported directly by Redis.
{{< /note >}}

`Predis` requires a running Redis server. See [here]({{< relref "/operate/oss_and_stack/install/" >}}) for Redis Open Source installation instructions.

## Install

Use [Composer](https://getcomposer.org/) to install the `Predis` library
with the following command line:

```bash
composer require predis/predis
```

## Connect and test

Connect to a locally-running server on the standard port (6379)
with the following code:

{{< clients-example set="landing" step="connect" lang_filter="PHP" description="Foundational: Connect to a Redis server and establish a client connection" difficulty="beginner" >}}
{{< /clients-example >}}

Store and retrieve a simple string to test the connection:

{{< clients-example set="landing" step="set_get_string" lang_filter="PHP" description="Foundational: Set and retrieve string values using SET and GET commands" difficulty="beginner" >}}
{{< /clients-example >}}

Store and retrieve a [hash]({{< relref "/develop/data-types/hashes" >}})
object:

{{< clients-example set="landing" step="set_get_hash" lang_filter="PHP" description="Foundational: Store and retrieve hash data structures using HSET and HGETALL" difficulty="beginner" >}}
{{< /clients-example >}}

## More information

The [Predis wiki on Github](https://github.com/predis/predis/wiki) has
information about the different connection options you can use.

See also the pages in this section for more information and examples:
