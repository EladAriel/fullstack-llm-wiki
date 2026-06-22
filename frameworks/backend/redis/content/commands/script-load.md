---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/script-load.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@scripting'
arguments:
- display_text: script
  name: script
  type: string
arity: 3
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
- noscript
- stale
complexity: O(N) with N being the length in bytes of the script body.
description: Loads a server-side Lua script to the script cache.
group: scripting
hidden: false
hints:
- request_policy:all_nodes
- response_policy:all_succeeded
linkTitle: SCRIPT LOAD
railroad_diagram: /images/railroad/script-load.svg
since: 2.6.0
summary: Loads a server-side Lua script to the script cache.
syntax_fmt: SCRIPT LOAD script
title: SCRIPT LOAD
---
Load a script into the scripts cache, without executing it.
After the specified command is loaded into the script cache it will be callable
using [`EVALSHA`]({{< relref "/commands/evalsha" >}}) with the correct SHA1 digest of the script, exactly like after
the first successful invocation of [`EVAL`]({{< relref "/commands/eval" >}}).

The script is guaranteed to stay in the script cache forever (unless `SCRIPT
FLUSH` is called).

The command works in the same way even if the script was already present in the
script cache.

For more information about [`EVAL`]({{< relref "/commands/eval" >}}) scripts please see [Introduction to Eval Scripts]({{< relref "/develop/programmability/eval-intro" >}}).

## Required arguments

<details open><summary><code>script</code></summary>

The Lua script to load into the script cache. Its SHA1 digest is returned for use with `EVALSHA`.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="script-load-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the SHA1 digest of the script added into the script cache.

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the SHA1 digest of the script added into the script cache.

{{< /multitabs >}}
