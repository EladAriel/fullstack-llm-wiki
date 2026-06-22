---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/acl-deluser.md"
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
arguments:
- display_text: username
  multiple: true
  name: username
  type: string
arity: -3
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
complexity: O(1) amortized time considering the typical user.
description: Deletes ACL users, and terminates their connections.
group: server
hidden: false
hints:
- request_policy:all_nodes
- response_policy:all_succeeded
linkTitle: ACL DELUSER
railroad_diagram: /images/railroad/acl-deluser.svg
since: 6.0.0
summary: Deletes ACL users, and terminates their connections.
syntax_fmt: ACL DELUSER username [username ...]
title: ACL DELUSER
---
Delete all the specified ACL users and terminate all the connections that are
authenticated with such users. Note: the special `default` user cannot be
removed from the system, this is the default user that every new connection
is authenticated with. The list of users may include usernames that do not
exist, in such case no operation is performed for the non existing users.

## Required arguments

<details open><summary><code>username [username ...]</code></summary>

One or more usernames to delete.

</details>

## Examples

```
> ACL DELUSER antirez
1
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="acl-deluser-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the number of users that were deleted. This number will not always match the number of arguments since certain users may not exist.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the number of users that were deleted. This number will not always match the number of arguments since certain users may not exist.

{{< /multitabs >}}
