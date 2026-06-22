---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/acl-users.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@admin'
- '@slow'
- '@dangerous'
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
- admin
- noscript
- loading
- stale
complexity: O(N). Where N is the number of configured users.
description: Lists all ACL users.
group: server
hidden: false
linkTitle: ACL USERS
railroad_diagram: /images/railroad/acl-users.svg
since: 6.0.0
summary: Lists all ACL users.
syntax_fmt: ACL USERS
title: ACL USERS
---
The command shows a list of all the usernames of the currently configured
users in the Redis ACL system.

## Examples

```
> ACL USERS
1) "anna"
2) "antirez"
3) "default"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Not supported for [scripts]({{<relref "/develop/programmability">}}). |

## Return information

{{< multitabs id="acl-users-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Array reply](../../develop/reference/protocol-spec#arrays): list of existing ACL users.

-tab-sep-

[Array reply](../../develop/reference/protocol-spec#arrays): list of existing ACL users.

{{< /multitabs >}}
