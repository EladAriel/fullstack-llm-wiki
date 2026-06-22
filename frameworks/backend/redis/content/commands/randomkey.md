---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/randomkey.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@keyspace'
- '@read'
- '@slow'
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
complexity: O(1)
description: Returns a random key name from the database.
group: generic
hidden: false
hints:
- request_policy:all_shards
- response_policy:special
- nondeterministic_output
linkTitle: RANDOMKEY
railroad_diagram: /images/railroad/randomkey.svg
since: 1.0.0
summary: Returns a random key name from the database.
syntax_fmt: RANDOMKEY
title: RANDOMKEY
---
Return a random key from the currently selected database.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="randomkey-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): when the database is empty.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a random key in database.

-tab-sep-

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): when the database is empty.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a random key in the database.

{{< /multitabs >}}
