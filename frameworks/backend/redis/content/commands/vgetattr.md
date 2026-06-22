---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/vgetattr.md"
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
description: Retrieve the JSON attributes of elements.
group: vector_set
hidden: false
linkTitle: VGETATTR
railroad_diagram: /images/railroad/vgetattr.svg
since: 8.0.0
summary: Retrieve the JSON attributes of elements.
syntax_fmt: "VGETATTR key element"
title: VGETATTR
---

Return the JSON attributes associated with an element in a vector set.

```shell
VGETATTR key element
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element whose attributes you want to retrieve.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="vgetattr-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings) containing the JSON attribute(s).
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) (null bulk string) for unknown key or element, or when no attributes exist for the given key/element pair.

-tab-sep-

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings) containing the JSON attribute(s).
* [Null reply](../../develop/reference/protocol-spec#nulls) for unknown key or element, or when no attributes exist for the given key/element pair.

{{< /multitabs >}}

## Related topics

- [Vector sets]({{< relref "/develop/data-types/vector-sets" >}})
