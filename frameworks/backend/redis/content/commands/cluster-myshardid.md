---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/cluster-myshardid.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
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
- stale
complexity: O(1)
description: Returns the shard ID of a node.
group: cluster
hidden: false
hints:
- nondeterministic_output
linkTitle: CLUSTER MYSHARDID
railroad_diagram: /images/railroad/cluster-myshardid.svg
since: 7.2.0
summary: Returns the shard ID of a node.
syntax_fmt: CLUSTER MYSHARDID
title: CLUSTER MYSHARDID
---
Returns the node's shard id.

The `CLUSTER MYSHARDID` command returns the unique, auto-generated identifier that is associated with the shard to which the connected cluster node belongs.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="cluster-myshardid-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the node's shard ID.

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the node's shard ID.

{{< /multitabs >}}
