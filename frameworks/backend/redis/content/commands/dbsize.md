---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/dbsize.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.016496Z"
---
# Dbsize

---
acl_categories:
- '@keyspace'
- '@read'
- '@fast'
arity: 1
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
description: Returns the number of keys in the database.
group: server
hidden: false
hints:
- request_policy:all_shards
- response_policy:agg_sum
linkTitle: DBSIZE
railroad_diagram: /images/railroad/dbsize.svg
since: 1.0.0
summary: Returns the number of keys in the database.
syntax_fmt: DBSIZE
title: DBSIZE
---
{{< note >}}
This command's behavior varies in clustered Redis environments. See the [multi-key operations]({{< relref "/develop/using-commands/multi-key-operations" >}}) page for more information.
{{< /note >}}


Return the number of keys in the currently-selected database.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="dbsize-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys in the currently-selected database.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the number of keys in the currently-selected database.

{{< /multitabs >}}
