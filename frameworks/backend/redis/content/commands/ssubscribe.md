---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ssubscribe.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@pubsub'
- '@slow'
arguments:
- display_text: shardchannel
  multiple: true
  name: shardchannel
  type: string
arity: -2
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
command_flags:
- pubsub
- noscript
- loading
- stale
complexity: O(N) where N is the number of shard channels to subscribe to.
description: Listens for messages published to shard channels.
group: pubsub
hidden: false
key_specs:
- begin_search:
    spec:
      index: 1
    type: index
  find_keys:
    spec:
      keystep: 1
      lastkey: -1
      limit: 0
    type: range
  not_key: true
linkTitle: SSUBSCRIBE
railroad_diagram: /images/railroad/ssubscribe.svg
since: 7.0.0
summary: Listens for messages published to shard channels.
syntax_fmt: SSUBSCRIBE shardchannel [shardchannel ...]
title: SSUBSCRIBE
---
Subscribes the client to the specified shard channels.

In Redis Cluster, shard channels are assigned to slots with the same algorithm Redis uses to assign keys to slots. To receive messages published to a shard channel, subscribe to a node, either a primary or replica, that serves the channel’s slot.

All shard channels in a single SSUBSCRIBE call must belong to the same slot. To subscribe to shard channels across different slots, use separate SSUBSCRIBE calls.

For more information about sharded Pub/Sub, see [Sharded Pub/Sub]({{< relref "/develop/pubsub#sharded-pubsub" >}}).

## Required arguments

<details open><summary><code>shardchannel [shardchannel ...]</code></summary>

One or more shard channels to subscribe to.

</details>

## Examples

```
> ssubscribe orders
Reading messages... (press Ctrl-C to quit)
1) "ssubscribe"
2) "orders"
3) (integer) 1
1) "smessage"
2) "orders"
3) "hello"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="ssubscribe-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string `ssubscribe` is pushed as a confirmation that the command succeeded. Note that this command can also return a -MOVED redirect.

-tab-sep-

When successful, this command doesn't return anything. Instead, for each shard channel, one message with the first element being the string 'ssubscribe' is pushed as a confirmation that the command succeeded. Note that this command can also return a -MOVED redirect.

{{< /multitabs >}}
