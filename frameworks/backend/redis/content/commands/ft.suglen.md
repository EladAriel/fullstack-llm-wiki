---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ft.suglen.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.001441Z"
---
# Ft.Suglen

---
acl_categories:
- '@search'
arguments:
- name: key
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
description: Gets the size of an auto-complete suggestion dictionary
group: suggestion
hidden: false
linkTitle: FT.SUGLEN
module: Search
railroad_diagram: /images/railroad/ft.suglen.svg
since: 1.0.0
stack_path: docs/interact/search-and-query
summary: Gets the size of an auto-complete suggestion dictionary
syntax_fmt: FT.SUGLEN key
title: FT.SUGLEN
---

Get the size of an auto-complete suggestion dictionary

[Examples](#examples)

## Required arguments

<details open>
<summary><code>key</code></summary>

is suggestion dictionary key.
</details>

## Examples

<details open>
<summary><b>Get the size of an auto-complete suggestion dictionary</b></summary>

{{< highlight bash >}}
127.0.0.1:6379> FT.SUGLEN sug
(integer) 2
{{< / highlight >}}
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Not supported on clustered databases. |

## Return information

{{< multitabs id="ft-suglen-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): number of suggestions in the dictionary.

-tab-sep-

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): number of suggestions in the dictionary.

{{< /multitabs >}}

## See also

[`FT.SUGADD`]({{< relref "commands/ft.sugadd/" >}}) | [`FT.SUGDEL`]({{< relref "commands/ft.sugdel/" >}}) | [`FT.SUGGET`]({{< relref "commands/ft.sugget/" >}}) 

## Related topics

[RediSearch]({{< relref "/develop/ai/search-and-query/" >}})