---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/sync.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.081780Z"
---
# Sync

---
acl_categories:
- '@admin'
- '@slow'
- '@dangerous'
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
- admin
- noscript
- no_async_loading
- no_multi
description: An internal command used in replication.
group: server
hidden: false
linkTitle: SYNC
railroad_diagram: /images/railroad/sync.svg
since: 1.0.0
summary: An internal command used in replication.
syntax_fmt: SYNC
title: SYNC
---
Initiates a replication stream from the master.

The `SYNC` command is called by Redis replicas for initiating a replication
stream from the master. It has been replaced in newer versions of Redis by
 [`PSYNC`]({{< relref "/commands/psync" >}}).

For more information about replication in Redis please check the
[replication page]({{< relref "/operate/oss_and_stack/management/replication" >}}).

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="sync-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

**Non-standard return value**, a bulk transfer of the data followed by `PING` and write requests from the master.

-tab-sep-

**Non-standard return value**, a bulk transfer of the data followed by `PING` and write requests from the master.

{{< /multitabs >}}
