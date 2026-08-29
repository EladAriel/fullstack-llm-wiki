---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/smembers.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.030842Z"
---
# Smembers

---
acl_categories:
- '@read'
- '@set'
- '@slow'
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
complexity: O(N) where N is the set cardinality.
description: Returns all members of a set.
group: set
hidden: false
hints:
- nondeterministic_output_order
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
linkTitle: SMEMBERS
railroad_diagram: /images/railroad/smembers.svg
since: 1.0.0
summary: Returns all members of a set.
syntax_fmt: SMEMBERS key
title: SMEMBERS
---
Returns all the members of the set value stored at `key`.

This has the same effect as running [`SINTER`]({{< relref "/commands/sinter" >}}) with one argument `key`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the set.

</details>

## Examples

{{< clients-example set="cmds_set" step="smembers" description="Foundational: Retrieve all members of a set using SMEMBERS (returns unordered collection, useful for iterating all set members)" difficulty="beginner" >}}
redis> SADD myset "Hello"
(integer) 1
redis> SADD myset "World"
(integer) 1
redis> SMEMBERS myset
1) "Hello"
2) "World"
{{< /clients-example >}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="smembers-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Array reply](../../develop/reference/protocol-spec#arrays): an array with all the members of the set.

-tab-sep-

[Set reply](../../develop/reference/protocol-spec#sets): a set with all the members of the set.

{{< /multitabs >}}
