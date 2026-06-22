---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/psubscribe.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@pubsub'
- '@slow'
arguments:
- display_text: pattern
  multiple: true
  name: pattern
  type: pattern
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
- pubsub
- noscript
- loading
- stale
complexity: O(N) where N is the number of patterns to subscribe to.
description: Listens for messages published to channels that match one or more patterns.
group: pubsub
hidden: false
history:
- - 6.2.0
  - RESET can be called to exit the subscribed state.
linkTitle: PSUBSCRIBE
railroad_diagram: /images/railroad/psubscribe.svg
since: 2.0.0
summary: Listens for messages published to channels that match one or more patterns.
syntax_fmt: PSUBSCRIBE pattern [pattern ...]
title: PSUBSCRIBE
---
Subscribes the client to the given patterns.


Once the client enters the subscribed state it is not supposed to issue any other commands, except for additional [`SUBSCRIBE`]({{< relref "/commands/subscribe" >}}), [`SSUBSCRIBE`]({{< relref "/commands/ssubscribe" >}}), `PSUBSCRIBE`, [`UNSUBSCRIBE`]({{< relref "/commands/unsubscribe" >}}), [`SUNSUBSCRIBE`]({{< relref "/commands/sunsubscribe" >}}), [`PUNSUBSCRIBE`]({{< relref "/commands/punsubscribe" >}}), [`PING`]({{< relref "/commands/ping" >}}), [`RESET`]({{< relref "/commands/reset" >}}) and [`QUIT`]({{< relref "/commands/quit" >}}) commands.
However, if RESP3 is used (see [`HELLO`]({{< relref "/commands/hello" >}})), it is possible for a client to issue any commands while in a subscribed state.

For more information, see [Pub/sub]({{< relref "/develop/pubsub" >}}).

## Required arguments

<details open><summary><code>pattern [pattern ...]</code></summary>

One or more glob-style patterns to subscribe to. Messages published to any channel whose name matches a pattern are delivered to the client.

Supported glob-style patterns:

* `h?llo` subscribes to `hello`, `hallo` and `hxllo`
* `h*llo` subscribes to `hllo` and `heeeello`
* `h[ae]llo` subscribes to `hello` and `hallo,` but not `hillo`

Use `\` to escape special characters if you want to match them verbatim.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

{{< multitabs id="psubscribe-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `psubscribe` is pushed as a confirmation that the command succeeded.

-tab-sep-

When successful, this command doesn't return anything. Instead, for each pattern, one message with the first element being the string `psubscribe` is pushed as a confirmation that the command succeeded.

{{< /multitabs >}}
