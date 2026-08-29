---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ft.aliasupdate.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.073719Z"
---
# Ft.Aliasupdate

---
acl_categories:
- '@search'
arguments:
- name: alias
  type: string
- name: index
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
description: Adds or updates an alias to the index
group: search
hidden: false
linkTitle: FT.ALIASUPDATE
module: Search
railroad_diagram: /images/railroad/ft.aliasupdate.svg
since: 1.0.0
stack_path: docs/interact/search-and-query
summary: Adds or updates an alias to the index
syntax_fmt: FT.ALIASUPDATE alias index
title: FT.ALIASUPDATE
---

Add an alias to an index. If the alias is already associated with another
index, FT.ALIASUPDATE removes the alias association with the previous index.

[Examples](#examples)

## Required arguments

<details open>
<summary><code>alias index</code></summary>

is alias to be added to an index.
</details>

## Examples

<details open>
<summary><b>Update an index alias</b></summary>

Update the alias of an index.

{{< highlight bash >}}
127.0.0.1:6379> FT.ALIASUPDATE alias idx
OK
{{< / highlight >}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> |  |

## Return information

{{< multitabs id="ft-aliasupdate-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}): `OK` if executed correctly.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) in these cases: index does not exist.

-tab-sep-

One of the following:
* [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}): `OK` if executed correctly.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) in these cases: index does not exist.

{{< /multitabs >}}

## See also

[`FT.ALIASADD`]({{< relref "commands/ft.aliasadd/" >}}) | [`FT.ALIASDEL`]({{< relref "commands/ft.aliasdel/" >}}) 

## Related topics

[RediSearch]({{< relref "/develop/ai/search-and-query/" >}})