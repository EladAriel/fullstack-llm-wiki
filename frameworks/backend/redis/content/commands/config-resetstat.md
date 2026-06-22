---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/config-resetstat.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@admin'
- '@slow'
- '@dangerous'
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
- admin
- noscript
- loading
- stale
complexity: O(1)
description: Resets the server's statistics.
group: server
hidden: false
hints:
- request_policy:all_nodes
- response_policy:all_succeeded
linkTitle: CONFIG RESETSTAT
railroad_diagram: /images/railroad/config-resetstat.svg
since: 2.0.0
summary: Resets the server's statistics.
syntax_fmt: CONFIG RESETSTAT
title: CONFIG RESETSTAT
---
Resets the statistics reported by Redis using the [`INFO`]({{< relref "/commands/info" >}}) and [`LATENCY HISTOGRAM`]({{< relref "/commands/latency-histogram" >}}) commands.

The following is a non-exhaustive list of values that are reset:

* Keyspace hits and misses
* Number of expired keys
* Command and error statistics
* Connections received, rejected and evicted
* Persistence statistics
* Active defragmentation statistics

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="config-resetstat-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

{{< /multitabs >}}
