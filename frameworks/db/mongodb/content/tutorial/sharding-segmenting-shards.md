---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/sharding-segmenting-shards.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================================

# Segmenting Data by Application or Customer

.. include:: /includes/intro-zone-sharding.rst

> **Tip:** .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

This tutorial shows you how to segment data using `zone-sharding`.

Consider the following scenarios where segmenting data by application or customer may be necessary:

- A database serving multiple applications
- A database serving multiple customers
- A database that requires isolating ranges or subsets of application
or customer data

- A database that requires resource allocation for ranges or subsets of
application or customer data

This diagram illustrates a sharded cluster using zones to segment data based on application or customer. This allows for data to be isolated to specific shards. Additionally, each shard can have specific hardware allocated to fit the performance requirement of the data stored on that shard.

.. include:: /images/sharding-segmenting-shards-overview.rst

## Scenario

An application tracks the score of a user along with a `client` field, storing scores in the `gamify` database under the `users` collection. Each possible value of `client` requires its own zone to allow for data segmentation. It also allows the administrator to optimize the hardware for each shard associated to a `client` for performance and cost.

The following documents represent a partial view of two users:

```javascript
{
  "_id" : ObjectId("56f08c447fe58b2e96f595fa"),
  "client" : "robot",
  "userid" : 123,
  "high_score" : 181,
  ...,
}
{
  "_id" : ObjectId("56f08c447fe58b2e96f595fb"),
  "client" : "fruitos",
  "userid" : 456,
  "high_score" : 210,
  ...,
}
```

### Shard Key

The `users` collection uses the `{ client : 1, userid : 1 }` compound index as the shard key.

The `client` field in each document allows creating a zone for each distinct client value.

The `userid` field provides a high `cardinality <shard-key-cardinality>` and low `frequency <shard-key-frequency>` component to the shard key relative to `country`.

See `Choosing a Shard Key <sharding-shard-key-requirements>` for more general instructions on selecting a shard key.

### Architecture

The application requires adding shard to a zone associated to a specific `client`.

The sharded cluster deployment currently consists of four `shards <shard>`.

.. include:: /images/sharding-segmenting-shards-architecture.rst

### Zones

For this application, there are two client zones.

.. include:: /images/sharding-segmenting-shards-tags.rst

Robot client ("robot") This zone represents all documents where `client : robot`.

FruitOS client ("fruitos") This zone represents all documents where `client : fruitos`.

### Write Operations

With zones, if an inserted or updated document matches a configured zone, it can only be written to a shard inside that zone.

MongoDB can write documents that do not match a configured zone to any shard in the cluster.

> **Note:** The behavior described above requires the cluster to be in a steady state
with no chunks violating a configured zone. See the following section
on the `balancer <sharding-tiered-hardware-balancing>` for more
information.

### Read Operations

MongoDB can route queries to a specific shard if the query includes at least the `client` field.

For example, MongoDB can attempt a `targeted read operation <sharding-mongos-targeted>` on the following query:

```javascript
chatDB = db.getSiblingDB("gamify")
chatDB.users.find( { "client" : "robot" , "userid" : "123" } )
```

Queries without the `client` field perform `broadcast operations <sharding-mongos-broadcast>`.

### Balancer

The `balancer <sharding-balancing>` `migrates <sharding-chunk-migration>` chunks to the appropriate shard respecting any configured zones. Until the migration, shards may contain chunks that violate configured zones. Once balancing completes, shards should only contain chunks whose ranges do not violate its assigned zones.

Adding or removing zones or zone ranges can result in chunk migrations. Depending on the size of your data set and the number of chunks a zone or zone range affects, these migrations may impact cluster performance. Consider running your `balancer <sharding-balancing>` during specific scheduled windows. See `sharding-schedule-balancing-window` for a tutorial on how to set a scheduling window.

### Security

For sharded clusters running with `authorization`, authenticate as a user with at least the :authrole:`clusterManager` role on the `admin` database.

## Procedure

You must be connected to a :binary:`~bin.mongos` associated to the target `sharded cluster` to proceed. You cannot create zones or zone ranges by connecting directly to a `shard`.

.. include:: /includes/steps/sharding-segmenting-shards.rst
