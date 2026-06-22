---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/vlinks.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
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
description: Return the neighbors of an element at each layer in the HNSW graph.
group: vector_set
hidden: false
linkTitle: VLINKS
railroad_diagram: /images/railroad/vlinks.svg
since: 8.0.0
summary: Return the neighbors of an element at each layer in the HNSW graph.
syntax_fmt: "VLINKS key element [WITHSCORES]"
title: VLINKS
---

Return the neighbors of a specified element in a vector set. The command shows the connections for each layer of the HNSW graph.

```shell
VLINKS key element
```

Use the `WITHSCORES` option to include similarity scores for each neighbor.

```shell
VLINKS key element WITHSCORES
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element whose HNSW neighbors you want to inspect.
</details>

## Optional arguments

<details open>
<summary><code>WITHSCORES</code></summary>

includes similarity scores for each neighbor.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="vlinks-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* An [array](../../develop/reference/protocol-spec#arrays) of [array replies](../../develop/reference/protocol-spec#arrays) containing the names of adjacent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings); interleaved with scores as [bulk strings](../../develop/reference/protocol-spec#bulk-strings) when used with the `WITHSCORES` option.
* [Simple error reply](../../develop/reference/protocol-spec/#simple-errors) for incorrect syntax.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) (null bulk string) for unknown keys and/or elements.

-tab-sep-

One of the following:
* An [array](../../develop/reference/protocol-spec#arrays) of [array replies](../../develop/reference/protocol-spec#arrays) containing the names of adjacent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings) when used without the `WITHSCORES` option.
* An [array](../../develop/reference/protocol-spec#arrays) of [map replies](../../develop/reference/protocol-spec#maps) containing the names of adjecent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings), together with their scores as [doubles](../../develop/reference/protocol-spec#doubles) when used with the `WITHSCORES` option.
* [Simple error reply](../../develop/reference/protocol-spec/#simple-errors) for incorrect syntax.
* [Null reply](../../develop/reference/protocol-spec#nulls) for unknown keys and/or elements.

{{< /multitabs >}}

## Related topics

- [Vector sets]({{< relref "/develop/data-types/vector-sets" >}})
