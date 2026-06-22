---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/json.clear.md"
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
  values, O(N) when path is evaluated to multiple values, where N is the size of the
  key
description: Clears all values from an array or an object and sets numeric values
  to `0`
group: json
hidden: false
linkTitle: JSON.CLEAR
module: JSON
railroad_diagram: /images/railroad/json.clear.svg
since: 2.0.0
stack_path: docs/data-types/json
summary: Clears all values from an array or an object and sets numeric values to `0`
syntax_fmt: JSON.CLEAR key [path]
title: JSON.CLEAR
---
Clear container values (arrays/objects) and set numeric values to `0`

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. Nonexisting paths are ignored.
</details>

{{% alert title="Note" color="warning" %}}
 
Already cleared values are ignored for empty containers and zero numbers.

{{% /alert %}}

## Examples

<details open>
<summary><b>Clear container values and set numeric values to <code>0</code></b></summary>

Create a JSON document.

{{< highlight bash >}}
redis> JSON.SET doc $ '{"obj":{"a":1, "b":2}, "arr":[1,2,3], "str": "foo", "bool": true, "int": 42, "float": 3.14}'
OK
{{< / highlight >}}

Clear all container values. This returns the number of objects with cleared values.

{{< highlight bash >}}
redis> JSON.CLEAR doc $.*
(integer) 4
{{< / highlight >}}

Get the updated document. Note that numeric values have been set to `0`.

{{< highlight bash >}}
redis> JSON.GET doc $
"[{\"obj\":{},\"arr\":[],\"str\":\"foo\",\"bool\":true,\"int\":0,\"float\":0}]"
{{< / highlight >}}
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

{{< multitabs id="json-clear-return-info"
    tab1="RESP2"
    tab2="RESP3" >}}

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of matching JSON arrays and objects cleared plus the number of matching JSON numerical values zeroed.

-tab-sep-

[Integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}): the number of matching JSON arrays and objects cleared plus the number of matching JSON numerical values zeroed.

{{< /multitabs >}}

## See also

[`JSON.ARRINDEX`]({{< relref "commands/json.arrindex/" >}}) | [`JSON.ARRINSERT`]({{< relref "commands/json.arrinsert/" >}}) 

## Related topics

* [RedisJSON]({{< relref "/develop/data-types/json/" >}})
* [Index and search JSON documents]({{< relref "/develop/ai/search-and-query/indexing/" >}})

