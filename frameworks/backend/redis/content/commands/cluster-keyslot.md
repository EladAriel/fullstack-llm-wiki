---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/cluster-keyslot.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
arguments:
- display_text: key
  name: key
  type: string
arity: 3
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
- stale
complexity: O(N) where N is the number of bytes in the key
description: Returns the hash slot for a key.
group: cluster
hidden: false
linkTitle: CLUSTER KEYSLOT
railroad_diagram: /images/railroad/cluster-keyslot.svg
since: 3.0.0
summary: Returns the hash slot for a key.
syntax_fmt: CLUSTER KEYSLOT key
title: CLUSTER KEYSLOT
---
Returns an integer identifying the hash slot the specified key hashes to.
This command is mainly useful for debugging and testing, since it exposes
via an API the underlying Redis implementation of the hashing algorithm.
Example use cases for this command:

1. Client libraries may use Redis in order to test their own hashing algorithm, generating random keys and hashing them with both their local implementation and using Redis `CLUSTER KEYSLOT` command, then checking if the result is the same.
2. Humans may use this command in order to check what is the hash slot, and then the associated Redis Cluster node, responsible for a given key.

The command uses the full [Redis Cluster hashing algorithm]({{< relref "/operate/oss_and_stack/reference/cluster-spec/#key-distribution-model" >}}), including support for hash tags. If a key contains a valid hash tag, Redis hashes only the part of the key between `{` and `}`. You can use hash tags to force multiple keys into the same hash slot so they are handled by the same node.

## Required arguments

<details open><summary><code>key</code></summary>

The key name to compute the hash slot for.

</details>

## Examples

```
> CLUSTER KEYSLOT somekey
(integer) 11058
> CLUSTER KEYSLOT foo{hash_tag}
(integer) 2515
> CLUSTER KEYSLOT bar{hash_tag}
(integer) 2515
```


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Only supported with the [OSS cluster API]({{< relref "/operate/rs/databases/configure/oss-cluster-api" >}}). |

## Return information

{{< multitabs id="cluster-keyslot-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): The hash slot number for the specified key

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): The hash slot number for the specified key

{{< /multitabs >}}
