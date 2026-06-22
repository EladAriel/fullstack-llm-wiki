---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/sharding-segmenting-data-by-location.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# Segmenting Data by Location

.. include:: /includes/intro-zone-sharding.rst

> **Tip:** .. include:: /includes/extracts/zoned-sharding-pre-define-zone.rst

This tutorial uses `zone-sharding` to segment data based on a geographic area.

The following are some example use cases for segmenting data by geographic area:

- An application that has to segment user data by country
- A database that has to allocate resources by country
The following diagram illustrates a sharded cluster that uses geographic zones to manage and satisfy data segmentation requirements.

.. include:: /images/sharding-segmenting-data-by-location-overview.rst

## Scenario

A financial chat application logs messages, tracking the country of the originating user. The application stores the logs in the `chat` database under the `messages` collection. The chats contain information that must be segmented by country to have servers local to the country serve read and write requests for the country's users. A group of countries can be assigned same zone in order to share resources.

The application currently has users in the US, UK, and Germany. The `country` field represents the user's country based on its [ISO 3166-1 Alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) two-character country codes.

The following documents represent a partial view of three chat messages:

```javascript
{
  "_id" : ObjectId("56f08c447fe58b2e96f595fa"),
  "country" : "US",
  "userid" : 123,
  "message" : "Hello there",
  ...,
}
{
  "_id" : ObjectId("56f08c447fe58b2e96f595fb"),
  "country" : "UK",
  "userid" : 456,
  "message" : "Good Morning"
  ...,
}
{
  "_id" : ObjectId("56f08c447fe58b2e96f595fc"),
  "country" : "DE",
  "userid" : 789,
  "message" : "Guten Tag"
  ...,
}
```

### Shard Key

The `messages` collection uses the `{ country : 1, userid : 1 }` compound index as the shard key.

The `country` field in each document allows for creating a zone for each distinct country value.

The `userid` field provides a high `cardinality <shard-key-cardinality>` and low `frequency <shard-key-frequency>` component to the shard key relative to `country`.

See `Choosing a Shard Key <sharding-shard-key-requirements>` for more general instructions on selecting a shard key.

### Architecture

The sharded cluster has shards in two data centers - one in Europe, and one in North America.

.. include:: /images/sharding-segmenting-data-by-location-architecture.rst

### Zones

This application requires one zone per data center.

`EU` - European data center Shards deployed on this data center are assigned to the `EU` zone.

For each country using the `EU` data center for local reads and writes, create a zone range for the `EU` zone with:

- a lower bound of `{ "country" : <country>, "userid" : MinKey }`
- an upper bound of `{ "country" : <next country>, "userid" : MinKey }`
`NA` - North American data center Shards deployed on this data center are assigned to the `NA` zone.

For each country using the `NA` data center for local reads and writes, create a zone range for the `NA` zone with:

- a lower bound of `{ "country" : <country>, "userid" : MinKey }`
- an upper bound of `{ "country" : <next country>, "userid" : MinKey }`
> **Note:** The :bsontype:`MinKey` and :bsontype:`MaxKey` values are reserved special
values for comparisons

### Write Operations

With zones, if an inserted or updated document matches a configured zone, it can only be written to a shard inside of that zone.

MongoDB can write documents that do not match a configured zone to any shard in the cluster.

> **Note:** The behavior described above requires the cluster to be in a steady state
with no chunks violating a configured zone. See the following section on
the `balancer <sharding-segmenting-data-by-location-balancer>` for
more information.

### Read Operations

MongoDB can route queries to a specific shard if the query includes at least the `country` field.

For example, MongoDB can attempt a `targeted read operation <sharding-mongos-targeted>` on the following query:

```javascript
chatDB = db.getSiblingDB("chat")
chatDB.messages.find( { "country" : "UK" , "userid" : "123" } )
```

Queries without the `country` field perform `broadcast operations <sharding-mongos-broadcast>`.

### Balancer

The `balancer <sharding-balancing>` `migrates <sharding-chunk-migration>` chunks to the appropriate shard respecting any configured zones. Until the migration, shards may contain chunks that violate configured zones. Once balancing completes, shards should only contain chunks whose ranges do not violate its assigned zones.

Adding or removing zones or zone ranges can result in chunk migrations. Depending on the size of your data set and the number of chunks a zone or zone range affects, these migrations may impact cluster performance. Consider running your `balancer <sharding-balancing>` during specific scheduled windows. See `sharding-schedule-balancing-window` for a tutorial on how to set a scheduling window.

### Security

For sharded clusters running with `authorization`, authenticate as a user with at least the :authrole:`clusterManager` role on the `admin` database.

## Procedure

You must be connected to a :binary:`~bin.mongos` to create zones and zone ranges. You cannot create zones or zone ranges by connecting directly to a `shard`.

.. include:: /includes/steps/sharding-segmenting-data-by-location.rst

### Updating Zones

The application requires the following updates:

- Documents with `country : UK` must now be associated to the new `UK`
data center. Any data in the `EU` data center must be migrated

- The chat application now supports users in Mexico. Documents with
`country : MX` must be routed to the `NA` data center.

Perform the following procedures to update the zone ranges.

.. include:: /includes/steps/sharding-segmenting-data-by-location-update.rst

> **Seealso:** `zone-sharding`
`sharding-balancing`
`/tutorial/deploy-shard-cluster`
