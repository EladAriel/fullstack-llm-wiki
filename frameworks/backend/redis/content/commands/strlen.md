---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/strlen.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@read'
- '@string'
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
description: Returns the length of a string value.
group: string
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
linkTitle: STRLEN
railroad_diagram: /images/railroad/strlen.svg
since: 2.2.0
summary: Returns the length of a string value.
syntax_fmt: STRLEN key
title: STRLEN
---
Returns the length of the string value stored at `key`.
An error is returned when `key` holds a non-string value.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key.

</details>

## Examples

{{% redis-cli %}}
SET mykey "Hello world"
STRLEN mykey
STRLEN nonexisting
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="strlen-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the string stored at key, or 0 when the key does not exist.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the string stored at key, or 0 when the key does not exist.

{{< /multitabs >}}
