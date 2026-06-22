---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/json.forget.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@json'
- '@write'
- '@slow'
arguments:
- name: key
  type: key
- name: path
  optional: true
  type: string
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
complexity: O(N) when path is evaluated to a single value where N is the size of the
  deleted value, O(N) when path is evaluated to multiple values, where N is the size
  of the key
description: Deletes a value
group: json
hidden: false
linkTitle: JSON.FORGET
module: JSON
railroad_diagram: /images/railroad/json.forget.svg
since: 1.0.0
stack_path: docs/data-types/json
summary: Deletes a value
syntax_fmt: JSON.FORGET key [path]
title: JSON.FORGET
---
See [`JSON.DEL`]({{< relref "commands/json.del/" >}}).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

{{< multitabs id="json-forget-return-info"
    tab1="RESP2"
    tab2="RESP3" >}}

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of paths deleted (0 or more).

-tab-sep-

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of paths deleted (0 or more).

{{< /multitabs >}}
