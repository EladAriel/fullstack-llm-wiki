---
type: "Framework Learn Page"
framework: "redis"
source_repo: "https://github.com/redis/docs.git"
source_branch: "main"
source_path: "content/develop/ai/search-and-query/query/_index.md"
source_commit: "bc92ea237bbfc2117c870c904f1a3ca619073ef1"
source_commit_short: "bc92ea23"
source_commit_date: "2026-06-18T14:53:00-05:00"
generated_at: "2026-06-21T11:25:32Z"
---

---
aliases:
- /develop/interact/search-and-query/query
- /develop/interact/search-and-query/query/
- /interact/search-and-query/query/
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
description: Understand how to query, search, and aggregate Redis data
hideListLinks: true
linkTitle: Querying
title: Querying data
weight: 5
---

Redis Open Source distinguishes between the [FT.SEARCH]({{< relref "/commands/ft.search" >}}) and [FT.AGGREGATE]({{< relref "/commands/ft.aggregate" >}}) query commands. You should use [FT.SEARCH]({{< relref "/commands/ft.search" >}}) if you want to perform selections and projections only. If you also need to apply mapping functions, group, or aggregate data, use the [FT.AGGREGATE]({{< relref "/commands/ft.aggregate" >}}) command. 

* **Selection**: A selection allows you to return all documents that fulfill specific criteria.
* **Projection**: Projections are used to return specific fields of the result set. You can also map/project to calculated field values.
* **Aggregation**: Aggregations collect and summarize data across several fields.

Here is a short SQL comparison using the [bicycle dataset](./data/bicycles.txt):

|Type| SQL | Redis |
|----------| --- | ----------- |
| Selection | `SELECT * FROM bicycles WHERE price >= 1000` | `FT.SEARCH idx:bicycle "@price:[1000 +inf]"` |
| Simple projection | `SELECT id, price FROM bicycles` | `FT.SEARCH idx:bicycle "*" RETURN 2 __key, price` |
| Calculated projection| `SELECT id, price-price*0.1 AS discounted FROM bicycles`| `FT.AGGREGATE idx:bicycle "*" LOAD 2 __key price APPLY "@price-@price*0.1" AS discounted`| 
| Aggregation | `SELECT condition, AVG(price) AS avg_price FROM bicycles GROUP BY condition` | `FT.AGGREGATE idx:bicycle "*" GROUPBY 1 @condition REDUCE AVG 1 @price AS avg_price` |

The following articles provide an overview of how to query data with the [FT.SEARCH]({{< relref "commands/ft.search" >}}) command:

* [Exact match queries]({{< relref "/develop/ai/search-and-query/query/exact-match" >}})
* [Range queries]({{< relref "/develop/ai/search-and-query/query/range" >}})
* [Full-text search ]({{< relref "/develop/ai/search-and-query/query/full-text" >}})
* [Geospatial queries]({{< relref "/develop/ai/search-and-query/query/geo-spatial" >}})
* [Vector search]({{< relref "/develop/ai/search-and-query/query/vector-search" >}})
* [Combined queries]({{< relref "/develop/ai/search-and-query/query/combined" >}})

You can find further details about aggregation queries with [FT.AGGREGATE]({{< relref "commands/ft.aggregate" >}}) in the following article:

* [Aggregation queries]({{< relref "/develop/ai/search-and-query/query/aggregation" >}})