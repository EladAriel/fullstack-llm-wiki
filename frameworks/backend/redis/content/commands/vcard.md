---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/vcard.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.086703Z"
---
# Vcard

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
description: Return the number of elements in a vector set.
group: vector_set
hidden: false
linkTitle: VCARD
railroad_diagram: /images/railroad/vcard.svg
since: 8.0.0
summary: Return the number of elements in a vector set.
syntax_fmt: "VCARD key"
title: VCARD
---

Return the number of elements in the specified vector set.

```shell
VCARD word_embeddings
(integer) 3000000
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

{{< multitabs id="vcard-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if the key doesn't exist or the number of elements contained in the vector set.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if the key doesn't exist or the number of elements contained in the vector set.

{{< /multitabs >}}

## Related topics

- [Vector sets]({{< relref "/develop/data-types/vector-sets" >}})
