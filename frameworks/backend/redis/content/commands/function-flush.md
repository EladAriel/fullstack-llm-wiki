---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/function-flush.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@write'
- '@slow'
- '@scripting'
arguments:
- arguments:
  - display_text: async
    name: async
    token: ASYNC
    type: pure-token
  - display_text: sync
    name: sync
    token: SYNC
    type: pure-token
  name: flush-type
  optional: true
  type: oneof
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
- write
- noscript
complexity: O(N) where N is the number of functions deleted
description: Deletes all libraries and functions.
group: scripting
hidden: false
hints:
- request_policy:all_shards
- response_policy:all_succeeded
linkTitle: FUNCTION FLUSH
railroad_diagram: /images/railroad/function-flush.svg
since: 7.0.0
summary: Deletes all libraries and functions.
syntax_fmt: FUNCTION FLUSH [ASYNC | SYNC]
title: FUNCTION FLUSH
---
Deletes all the libraries.

Unless called with the optional mode argument, the `lazyfree-lazy-user-flush` configuration directive sets the effective behavior.

For more information please refer to [Introduction to Redis Functions]({{< relref "/develop/programmability/functions-intro" >}}).

## Optional arguments

<details open><summary><code>ASYNC | SYNC</code></summary>

Flush the function libraries asynchronously (`ASYNC`) or synchronously (`SYNC`). The default is set by the `lazyfree-lazy-user-flush` configuration directive.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="function-flush-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

{{< /multitabs >}}
