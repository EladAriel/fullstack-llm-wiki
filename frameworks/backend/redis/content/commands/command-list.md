---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/command-list.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@slow'
- '@connection'
arguments:
- arguments:
  - display_text: module-name
    name: module-name
    token: MODULE
    type: string
  - display_text: category
    name: category
    token: ACLCAT
    type: string
  - display_text: pattern
    name: pattern
    token: PATTERN
    type: pattern
  name: filterby
  optional: true
  token: FILTERBY
  type: oneof
arity: -2
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
- loading
- stale
complexity: O(N) where N is the total number of Redis commands
description: Returns a list of command names.
group: server
hidden: false
hints:
- nondeterministic_output_order
linkTitle: COMMAND LIST
railroad_diagram: /images/railroad/command-list.svg
since: 7.0.0
summary: Returns a list of command names.
syntax_fmt: "COMMAND LIST [FILTERBY\_<MODULE\_module-name | ACLCAT\_category |\n \
  \ PATTERN\_pattern>]"
title: COMMAND LIST
---
Return an array of the Redis server's command names.

## Optional arguments

<details open><summary><code>FILTERBY MODULE module-name | ACLCAT category | PATTERN pattern</code></summary>

Filter the listed commands by module (`MODULE`), [ACL category]({{< relref "operate/oss_and_stack/management/security/acl#command-categories" >}}) (`ACLCAT`), or a glob-style name pattern (`PATTERN`).

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="command-list-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Array reply](../../develop/reference/protocol-spec#arrays): a list of command names.

-tab-sep-

[Array reply](../../develop/reference/protocol-spec#arrays): a list of command names.

{{< /multitabs >}}
