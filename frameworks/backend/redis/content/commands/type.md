---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/type.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.068298Z"
---
# Type

---
acl_categories:
- '@keyspace'
- '@read'
- '@fast'
arguments:
- display_text: key
  key_spec_index: 0
  name: key
  type: key
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
- fast
complexity: O(1)
description: Determines the type of value stored at a key.
group: generic
hidden: false
key_specs:
- RO: true
  begin_search:
    spec:
      index: 1
    type: index
  find_keys:
    spec:
      keystep: 1
      lastkey: 0
      limit: 0
    type: range
linkTitle: TYPE
railroad_diagram: /images/railroad/type.svg
since: 1.0.0
summary: Determines the type of value stored at a key.
syntax_fmt: TYPE key
title: TYPE
---
Returns the string representation of the type of the value stored at `key`.
The different types that can be returned are: `string`, `list`, `set`, `zset`,
`hash`, `stream`, and `vectorset`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples

{{% redis-cli %}}
redis> SET key1 "value"
OK
redis> LPUSH key2 "value"
(integer) 1
redis> SADD key3 "value"
(integer) 1
redis> TYPE key1
string
redis> TYPE key2
list
redis> TYPE key3
set
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="type-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): the type of _key_, or `none` when _key_ doesn't exist.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): the type of _key_, or `none` when _key_ doesn't exist.

{{< /multitabs >}}
