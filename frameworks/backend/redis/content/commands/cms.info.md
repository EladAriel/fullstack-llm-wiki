---
type: "Framework Learn Page"
framework: "Redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/cms.info.md"
source_commit: "f8693349287b0efbef3c865b6f6a2aceca88594d"
source_commit_short: "f869334"
source_commit_date: "2026-08-28T10:01:19-05:00"
generated_at: "2026-08-29T09:38:55.033029Z"
---
# Cms.Info

---
acl_categories:
- '@cms'
- '@read'
- '@fast'
arguments:
- name: key
  type: key
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
complexity: O(1)
description: Returns information about a sketch
group: cms
hidden: false
linkTitle: CMS.INFO
module: Bloom
railroad_diagram: /images/railroad/cms.info.svg
since: 2.0.0
stack_path: docs/data-types/probabilistic
summary: Returns information about a sketch
syntax_fmt: CMS.INFO key
title: CMS.INFO
---
Returns width, depth and total count of the sketch.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

## Examples

```
redis> CMS.INFO test
 1) width
 2) (integer) 2000
 3) depth
 4) (integer) 7
 5) count
 6) (integer) 0
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

{{< multitabs id="cms-info-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:

* [Array reply]({{< relref "/develop/reference/protocol-spec#arrays" >}}) of [simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}) and [integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}) pairs containing sketch information.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) in these cases: invalid arguments, missing key, or wrong key type.

-tab-sep-

One of the following:

* [Map reply]({{< relref "/develop/reference/protocol-spec#maps" >}}) of [simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}) and [integer reply]({{< relref "/develop/reference/protocol-spec#integers" >}}) pairs containing sketch information.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) in these cases: invalid arguments, missing key, or wrong key type.

{{< /multitabs >}}