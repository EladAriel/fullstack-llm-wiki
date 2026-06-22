---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/data-types/json/use_cases.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
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
description: JSON use cases
linkTitle: Use cases
title: Use cases
weight: 4
---

You can of course use Redis native data structures to store JSON objects, and that's a common practice. For example, you can serialize JSON and save it in a Redis String.

However, Redis JSON provides several benefits over this approach.

**Access and retrieval of subvalues**

With JSON, you can get nested values without having to transmit the entire object over the network. Being able to access sub-objects can lead to greater efficiencies when you're storing large JSON objects in Redis.

**Atomic partial updates**

JSON allows you to atomically run operations like incrementing a value, adding, or removing elements from an array, append strings, and so on. To do the same with a serialized object, you have to retrieve and then reserialize the entire object, which can be expensive and also lack atomicity.

**Indexing and querying**

When you store JSON objects as Redis strings, there's no good way to query those objects. On the other hand, storing these objects as JSON lets you index and query them. This capability is provided by Redis Search.

With the `FPHA` option to the [`JSON.SET`]({{< relref "/commands/json.set" >}}) command, Redis provides the user with a flexible way to store floating point vectors for vector search.
