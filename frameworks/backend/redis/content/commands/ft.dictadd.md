---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ft.dictadd.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@search'
arguments:
- name: dict
  type: string
- multiple: true
  name: term
  type: string
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
complexity: O(1)
description: Adds terms to a dictionary
group: search
hidden: false
linkTitle: FT.DICTADD
module: Search
railroad_diagram: /images/railroad/ft.dictadd.svg
since: 1.4.0
stack_path: docs/interact/search-and-query
summary: Adds terms to a dictionary
syntax_fmt: FT.DICTADD dict term [term ...]
title: FT.DICTADD
---

Add terms to a dictionary

[Examples](#examples)

## Required arguments

<details open>
<summary><code>dict</code></summary>

is dictionary name.
</details>

<details open>
<summary><code>term</code></summary>

term to add to the dictionary.
</details>

## Examples

<details open>
<summary><b>Add terms to a dictionary</b></summary>

{{< highlight bash >}}
127.0.0.1:6379> FT.DICTADD dict foo bar "hello world"
(integer) 3
{{< / highlight >}}
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

{{< multitabs id="ft-dictadd-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of new terms added to the dictionary.

-tab-sep-

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of new terms added to the dictionary.

{{< /multitabs >}}

## See also

[`FT.DICTDEL`]({{< relref "commands/ft.dictdel/" >}}) | [`FT.DICTDUMP`]({{< relref "commands/ft.dictdump/" >}})

## Related topics

[RediSearch]({{< relref "/develop/ai/search-and-query/" >}})