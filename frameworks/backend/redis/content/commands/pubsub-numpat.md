---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/pubsub-numpat.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@pubsub'
- '@slow'
arity: 2
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
- loading
- stale
complexity: O(1)
description: Returns a count of unique pattern subscriptions.
group: pubsub
hidden: false
linkTitle: PUBSUB NUMPAT
railroad_diagram: /images/railroad/pubsub-numpat.svg
since: 2.8.0
summary: Returns a count of unique pattern subscriptions.
syntax_fmt: PUBSUB NUMPAT
title: PUBSUB NUMPAT
---
Returns the number of unique patterns that are subscribed to by clients (that are performed using the [`PSUBSCRIBE`]({{< relref "/commands/psubscribe" >}}) command).

Note that this isn't the count of clients subscribed to patterns, but the total number of unique patterns all the clients are subscribed to.

Cluster note: in a Redis Cluster clients can subscribe to every node, and can also publish to every other node. The cluster will make sure that published messages are forwarded as needed. That said, [`PUBSUB`]({{< relref "/commands/pubsub" >}})'s replies in a cluster only report information from the node's Pub/Sub context, rather than the entire cluster.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="pubsub-numpat-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the number of patterns all the clients are subscribed to.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the number of patterns all the clients are subscribed to.

{{< /multitabs >}}
