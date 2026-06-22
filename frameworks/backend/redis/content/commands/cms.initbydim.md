---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/commands/cms.initbydim.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
acl_categories:
- '@cms'
- '@write'
- '@fast'
arguments:
- name: key
  type: key
- name: width
  type: integer
- name: depth
  type: integer
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
description: Initializes a Count-Min Sketch to dimensions specified by user
group: cms
hidden: false
linkTitle: CMS.INITBYDIM
module: Bloom
railroad_diagram: /images/railroad/cms.initbydim.svg
since: 2.0.0
stack_path: docs/data-types/probabilistic
summary: Initializes a Count-Min Sketch to dimensions specified by user
syntax_fmt: CMS.INITBYDIM key width depth
title: CMS.INITBYDIM
---
Initializes a Count-Min Sketch to dimensions specified by user.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the sketch.

</details>

<details open><summary><code>width</code></summary>

Number of counters in each array. Reduces the error size.

</details>

<details open><summary><code>depth</code></summary>

Number of counter-arrays. Reduces the probability for an error of a certain size (percentage of total count).

</details>

## Examples

```
redis> CMS.INITBYDIM test 2000 5
OK
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

{{< multitabs id="cms-initbydim-return-info" 
    tab1="RESP2" 
    tab2="RESP3" >}}

One of the following:

* [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}) `OK` if executed correctly.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) if the given key already exists.

-tab-sep-

One of the following:

* [Simple string reply]({{< relref "/develop/reference/protocol-spec#simple-strings" >}}) `OK` if executed correctly.
* [Simple error reply]({{< relref "/develop/reference/protocol-spec#simple-errors" >}}) if the given key already exists.

{{< /multitabs >}}