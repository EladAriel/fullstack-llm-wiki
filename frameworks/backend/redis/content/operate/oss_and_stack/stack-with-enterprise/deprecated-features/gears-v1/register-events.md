---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/register-events.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
Title: Register events
alwaysopen: false
categories:
- docs
- operate
- stack
description: Register RedisGears functions to run when certain events occur in a Redis
  database.
linkTitle: Register events
toc: 'true'
weight: 80
aliases:
- "/operate/oss_and_stack/stack-with-enterprise/gears-v1/register-events/"
bannerText: Redis Gears is a deprecated feature that is not recommended or supported
  for new users.
---

You can register RedisGears functions to run when certain events occur in a Redis database.

## Register on events

To register RedisGears functions to run on an event, your code needs to:

1. Pass `KeysReader` to a `GearsBuilder` object.

1. Call the `GearsBuilder.register()` function.

1. Pass the `eventTypes` parameter to either:

    - The `register` function for Python.
    
    - The `KeysReader` object for Java.

For more information and examples of event registration, see:

- Java references:

    - [`KeysReader`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/keysreader" >}})

    - [`GearsBuilder.register()`]({{< relref "/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/register" >}})

## Event types

For the list of event types you can register on, see the [Redis keyspace notification documentation]({{< relref "/develop/pubsub/keyspace-notifications" >}}#events-generated-by-different-commands).

## Active-Active event types

In addition to standard Redis [events]({{< relref "/develop/pubsub/keyspace-notifications" >}}#events-generated-by-different-commands), [Redis Software Active-Active databases]({{< relref "/operate/rs/databases/active-active" >}}) also support the registration of RedisGears functions for the following event types:

- `change`: This event occurs when a key changes on another replica of the Active-Active database.
