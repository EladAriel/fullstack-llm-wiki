---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ft.aliaslist.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.013891Z"
---
# Ft.Aliaslist

---
acl_categories:
- '@search'
arguments:
- display_text: index
  name: index
  summary: Specifies the name of the index. The index must be created using `FT.CREATE`.
  type: string
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
- readonly
- module
complexity: O(N) where N is the number of aliases
description: Lists all aliases for the index
group: search
hidden: false
linkTitle: FT.ALIASLIST
module: search
railroad_diagram: /images/railroad/ft.aliaslist.svg
since: 8.10.0
summary: Lists all aliases for the index
syntax_fmt: FT.ALIASLIST index
title: FT.ALIASLIST
---
Lists all aliases for the given `index`.

## Required arguments

<details open><summary><code>index</code></summary>

is the name of the index for which to list aliases.

</details>

## Examples

<details open>
<summary><b>Add an alias to an index</b></summary>

Add an alias to an index.

```
> FT.ALIASADD alias idx:bicycle
OK
```

List the aliases for `idx:bicycle`

```
> FT.ALIASLIST idx:bicycle
1) "alias"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</nobr></span> |  |

## Return information

{{< multitabs id="return-info"
    tab1="RESP2"
    tab2="RESP3" >}}

One of the following:

* An [array]({{< relref "/develop/reference/protocol-spec#array" >}}) of [bulk strings]({{< relref "/develop/reference/protocol-spec#bulk-strings" >}}), the names of existing index aliases, or an empty array if no aliases exist.
* A [simple error]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) when the provided index doesn't exist.

-tab-sep-

One of the following:

* A [set]({{< relref "/develop/reference/protocol-spec#sets" >}}) of [bulk strings]({{< relref "/develop/reference/protocol-spec#bulk-strings" >}}), the names of index aliases, or an empty set if no aliases exist.
* A [simple error]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) when the provided index doesn't exist.

{{< /multitabs >}}
