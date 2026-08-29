---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/ping.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:54.995947Z"
---
# Ping

---
acl_categories:
- '@fast'
- '@connection'
arguments:
- display_text: message
  name: message
  optional: true
  type: string
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
- fast
complexity: O(1)
description: Returns the server's liveliness response.
group: connection
hidden: false
hints:
- request_policy:all_shards
- response_policy:all_succeeded
linkTitle: PING
railroad_diagram: /images/railroad/ping.svg
since: 1.0.0
summary: Returns the server's liveliness response.
syntax_fmt: PING [message]
title: PING
---

This command returns the bulk string `PONG` if no argument is provided, otherwise it returns a copy of the
provided `message` as a bulk string.

This command is useful for:
1. Testing whether a connection is still alive.
1. Verifying the server's ability to serve data - an error is returned when this isn't the case (for example, during load from persistence data or accessing a stale replica).
1. Measuring latency.

If the client is subscribed to a channel or a pattern, it will instead return a
multi-bulk string with `PONG` in the first position and an empty bulk string in the second
position, unless an argument is provided, in which case it returns a copy
of the argument.

## Optional arguments

<details open><summary><code>message</code></summary>

A message to return instead of `PONG`.

</details>

## Examples

{{% redis-cli %}}
redis> PING
PONG
redis> PING "hello world"
"hello world"
{{% /redis-cli %}}

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="ping-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `PONG` when no argument is provided.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the provided argument.

-tab-sep-

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `PONG` when no argument is provided.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the provided argument.

{{< /multitabs >}}
