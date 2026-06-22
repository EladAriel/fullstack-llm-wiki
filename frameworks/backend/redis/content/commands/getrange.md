---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/getrange.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@read'
- '@string'
- '@slow'
arguments:
- display_text: key
  key_spec_index: 0
  name: key
  type: key
- display_text: start
  name: start
  type: integer
- display_text: end
  name: end
  type: integer
arity: 4
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
complexity: O(N) where N is the length of the returned string. The complexity is ultimately
  determined by the returned length, but because creating a substring from an existing
  string is very cheap, it can be considered O(1) for small strings.
description: Returns a substring of the string stored at a key.
group: string
hidden: false
key_specs:
- RO: true
  access: true
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
linkTitle: GETRANGE
railroad_diagram: /images/railroad/getrange.svg
since: 2.4.0
summary: Returns a substring of the string stored at a key.
syntax_fmt: GETRANGE key start end
title: GETRANGE
---
Returns the substring of the string value stored at key, as determined by the start and end offsets. Both offsets are inclusive.

You can use negative offsets to count backward from the end of the string. For example, -1 is the last character, -2 is the penultimate character, and so on.

The function handles out of range requests by limiting the resulting range to
the actual length of the string.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

<details open><summary><code>start</code></summary>

The start offset, zero-based. A negative value counts from the end of the string.

</details>

<details open><summary><code>end</code></summary>

The end offset, zero-based and inclusive. A negative value counts from the end of the string.

</details>

## Examples

{{% redis-cli %}}
SET mykey "This is a string"
GETRANGE mykey 0 3
GETRANGE mykey -3 -1
GETRANGE mykey 0 -1
GETRANGE mykey 10 100
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="getrange-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The substring of the string value stored at key, determined by the offsets start and end (both are inclusive).

-tab-sep-

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): The substring of the string value stored at key, determined by the offsets start and end (both are inclusive).

{{< /multitabs >}}
