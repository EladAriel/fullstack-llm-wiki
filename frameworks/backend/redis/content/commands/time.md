---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/time.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.018720Z"
---
# Time

---
acl_categories:
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
- loading
- stale
- fast
complexity: O(1)
description: Returns the server time.
group: server
hidden: false
hints:
- nondeterministic_output
linkTitle: TIME
railroad_diagram: /images/railroad/time.svg
since: 2.6.0
summary: Returns the server time.
syntax_fmt: TIME
title: TIME
---
The `TIME` command returns the current server time as a two items lists: a Unix
timestamp and the amount of microseconds already elapsed in the current second.
Basically the interface is very similar to the one of the `gettimeofday` system
call.

## Examples

{{% redis-cli %}}
redis> TIME
1) "1784722081"
2) "827551"
redis> TIME
1) "1784722081"
2) "828843"
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="time-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, a two-element array consisting of the Unix timestamp in seconds and the microseconds' count.

-tab-sep-

[Array reply](../../develop/reference/protocol-spec#arrays): specifically, a two-element array consisting of the Unix timestamp in seconds and the microseconds' count.

{{< /multitabs >}}
