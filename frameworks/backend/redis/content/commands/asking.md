---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/asking.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@fast'
- '@connection'
arity: 1
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
- fast
complexity: O(1)
description: Signals that a cluster client is following an -ASK redirect.
group: cluster
hidden: false
linkTitle: ASKING
railroad_diagram: /images/railroad/asking.svg
since: 3.0.0
summary: Signals that a cluster client is following an -ASK redirect.
syntax_fmt: ASKING
title: ASKING
---
When a cluster client receives an `-ASK` redirect, the `ASKING` command is sent to the target node followed by the command which was redirected.
This is normally done automatically by cluster clients.

If an `-ASK` redirect is received during a transaction, only one ASKING command needs to be sent to the target node before sending the complete transaction to the target node.

See [ASK redirection in the Redis Cluster Specification]({{< relref "/operate/oss_and_stack/reference/cluster-spec#ask-redirection" >}}) for details.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="asking-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

{{< /multitabs >}}
