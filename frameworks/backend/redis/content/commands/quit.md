---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/quit.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.072198Z"
---
# Quit

---
acl_categories:
- '@fast'
- '@connection'
arity: -1
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
- noscript
- loading
- stale
- fast
- no_auth
- allow_busy
complexity: O(1)
deprecated_since: 7.2.0
description: Closes the connection.
doc_flags:
- deprecated
group: connection
hidden: false
linkTitle: QUIT
railroad_diagram: /images/railroad/quit.svg
replaced_by: just closing the connection
since: 1.0.0
summary: Closes the connection.
syntax_fmt: QUIT
title: QUIT
---
Ask the server to close the connection.
The connection is closed as soon as all pending replies have been written to the
client.

**Note:** Clients should not use this command.
Instead, clients should simply close the connection when they're not used anymore.
Terminating a connection on the client side is preferable, as it eliminates `TIME_WAIT` lingering sockets on the server side.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v7.2.0. |

## Return information

{{< multitabs id="quit-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): OK.

-tab-sep-

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

{{< /multitabs >}}
