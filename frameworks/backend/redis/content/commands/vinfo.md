---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/vinfo.md"
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
description: Return information about a vector set.
group: vector_set
hidden: false
linkTitle: VINFO
railroad_diagram: /images/railroad/vinfo.svg
since: 8.0.0
summary: Return information about a vector set.
syntax_fmt: "VINFO key"
title: VINFO
---

Return metadata and internal details about a vector set, including size, dimensions, quantization type, and graph structure.

```shell
VINFO word_embeddings
1) quant-type
2) int8
3) vector-dim
4) (integer) 300
5) size
6) (integer) 3000000
7) max-level
8) (integer) 12
9) vset-uid
10) (integer) 1
11) hnsw-max-node-uid
12) (integer) 3000000
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="vinfo-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays) containing metadata and internal details about a vector set, including size, dimensions, quantization type, and graph structure.
* [Array reply](../../develop/reference/protocol-spec#arrays) (null array reply) for unknown key.

-tab-sep-

One of the following:
* [Array reply](../../develop/reference/protocol-spec#arrays) containing metadata and internal details about a vector set, including size, dimensions, quantization type, and graph structure.
* [Null reply](../../develop/reference/protocol-spec#nulls) for unknown key.

{{< /multitabs >}}

## Related topics

- [Vector sets]({{< relref "/develop/data-types/vector-sets" >}})
