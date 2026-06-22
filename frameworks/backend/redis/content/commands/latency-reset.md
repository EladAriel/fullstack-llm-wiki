---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/latency-reset.md"
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
- display_text: event
  multiple: true
  name: event
  optional: true
  type: string
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
- admin
- noscript
- loading
- stale
complexity: O(1)
description: Resets the latency data for one or more events.
group: server
hidden: false
hints:
- request_policy:all_nodes
- response_policy:agg_sum
linkTitle: LATENCY RESET
railroad_diagram: /images/railroad/latency-reset.svg
since: 2.8.13
summary: Resets the latency data for one or more events.
syntax_fmt: LATENCY RESET [event [event ...]]
title: LATENCY RESET
---
The `LATENCY RESET` command resets the latency spikes time series of all, or only some, events.

When the command is called without arguments, it resets all the
events, discarding the currently logged latency spike events, and resetting
the maximum event time register.

It is possible to reset only specific events by providing the `event` names
as arguments.

Valid values for `event` are:
* `active-defrag-cycle`
* `aof-fsync-always`
* `aof-stat`
* `aof-rewrite-diff-write`
* `aof-rename`
* `aof-write`
* `aof-write-active-child`
* `aof-write-alone`
* `aof-write-pending-fsync`
* `command`
* `expire-cycle`
* `eviction-cycle`
* `eviction-del`
* `fast-command`
* `fork`
* `rdb-unlink-temp-file`

For more information refer to the [Latency Monitoring Framework page][lm].

[lm]: /operate/oss_and_stack/management/optimization/latency-monitor.md

## Optional arguments

<details open><summary><code>event [event ...]</code></summary>

One or more latency events to reset. If omitted, all events are reset.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="latency-reset-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Integer reply](../../develop/reference/protocol-spec#integers): the number of event time series that were reset.

-tab-sep-

[Integer reply](../../develop/reference/protocol-spec#integers): the number of event time series that were reset.

{{< /multitabs >}}
