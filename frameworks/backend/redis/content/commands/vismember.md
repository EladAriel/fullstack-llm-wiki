---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/vismember.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
arguments:
- name: key
  type: key
- name: element
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
- READONLY
complexity: O(1)
description: Check if an element exists in a vector set.
function: vismemberCommand
group: vector_set
hidden: false
linkTitle: VISMEMBER
railroad_diagram: /images/railroad/vismember.svg
since: 8.0.0
summary: Check if an element exists in a vector set.
syntax_fmt: VISMEMBER key element
title: VISMEMBER
---

Check if an element exists in a vector set.

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element you want to check for membership.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="vismember-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element does not exist in the vector set, or the key does not exist. `1` if the element exists in the vector set.

-tab-sep-

[Boolean reply](../../develop/reference/protocol-spec#booleans): `false` if the element does not exist in the vector set, or the key does not exist. `true` if the element exists in the vector set.

{{< /multitabs >}}

## Related topics

- [Vector sets]({{< relref "/develop/data-types/vector-sets" >}})
