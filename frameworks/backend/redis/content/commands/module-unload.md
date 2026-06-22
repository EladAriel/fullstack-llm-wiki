---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/module-unload.md"
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
arguments:
- display_text: name
  name: name
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
- admin
- noscript
- no_async_loading
complexity: O(1)
description: Unloads a module.
group: server
hidden: false
linkTitle: MODULE UNLOAD
railroad_diagram: /images/railroad/module-unload.svg
since: 4.0.0
summary: Unloads a module.
syntax_fmt: MODULE UNLOAD name
title: MODULE UNLOAD
---
Unloads a module.

This command unloads the module specified by `name`. Note that the module's name
is reported by the [`MODULE LIST`]({{< relref "/commands/module-list" >}}) command, and may differ from the dynamic
library's filename.

Known limitations:

*   Modules that register custom data types can not be unloaded.

## Required arguments

<details open><summary><code>name</code></summary>

The name of the module to unload, as reported by `MODULE LIST`.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="module-unload-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was unloaded.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the module was unloaded.

{{< /multitabs >}}
