---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/fcall_ro.md"
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
- display_text: function
  name: function
  type: string
- display_text: numkeys
  name: numkeys
  type: integer
- display_text: key
  key_spec_index: 0
  multiple: true
  name: key
  optional: true
  type: key
- display_text: arg
  multiple: true
  name: arg
  optional: true
  type: string
arity: -3
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
- readonly
- noscript
- stale
- skip_monitor
- no_mandatory_keys
- movablekeys
complexity: Depends on the function that is executed.
description: Invokes a read-only function.
group: scripting
hidden: false
key_specs:
- RO: true
  access: true
  begin_search:
    spec:
      index: 2
    type: index
  find_keys:
    spec:
      firstkey: 1
      keynumidx: 0
      keystep: 1
    type: keynum
  notes: We cannot tell how the keys will be used so we assume the worst, RO and ACCESS
linkTitle: FCALL_RO
railroad_diagram: /images/railroad/fcall_ro.svg
since: 7.0.0
summary: Invokes a read-only function.
syntax_fmt: FCALL_RO function numkeys [key [key ...]] [arg [arg ...]]
title: FCALL_RO
---
This is a read-only variant of the [`FCALL`]({{< relref "/commands/fcall" >}}) command that cannot execute commands that modify data.

For more information about when to use this command vs [`FCALL`]({{< relref "/commands/fcall" >}}), please refer to [Read-only scripts]({{< relref "develop/programmability/#read-only_scripts" >}}).

For more information please refer to [Introduction to Redis Functions]({{< relref "/develop/programmability/functions-intro" >}}).

## Required arguments

<details open><summary><code>function</code></summary>

The name of the function to call. It must be a read-only function.

</details>

<details open><summary><code>numkeys</code></summary>

The number of key names that follow. Arguments after the keys are passed as regular arguments.

</details>

## Optional arguments

<details open><summary><code>key [key ...]</code></summary>

The key names the function accesses, provided to it via the Lua `KEYS` global variable. There must be exactly `numkeys` of them.

</details>

<details open><summary><code>arg [arg ...]</code></summary>

Additional arguments provided to the function via the Lua `ARGV` variable.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="fcall-ro-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

The return value depends on the function that was executed.

-tab-sep-

The return value depends on the function that was executed.

{{< /multitabs >}}
