---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/introduction.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================

# Introduction to MongoDB

You can create a MongoDB database in the following environments:

.. include:: /includes/fact-environments.rst

To learn more about creating a MongoDB database with the Atlas UI, see `Get Started with Atlas <unified-get-started>`.

## Document Database

A record in MongoDB is a document, which is a data structure composed of field and value pairs. MongoDB documents are similar to JSON objects. The values of fields may include other documents, arrays, and arrays of documents.

.. include:: /images/crud-annotated-document.rst

The advantages of using documents are:

- Documents correspond to native data types in many programming
languages.

- Embedded documents and arrays reduce need for expensive joins.
- Dynamic schema supports fluent polymorphism.
### Collections/Views/On-Demand Materialized Views

MongoDB stores documents in `collections <collections>`. Collections are analogous to tables in relational databases.

In addition to collections, MongoDB supports:

- Read-only `/core/views`
- `/core/materialized-views`
## Key Features

### High Performance

MongoDB provides high performance data persistence. In particular,

- Support for embedded data models reduces I/O activity on database
system.

- Indexes support faster queries and can include keys from embedded
documents and arrays.

### Query API

The MongoDB Query API supports `read and write operations (CRUD) <crud>` as well as:

- `Data Aggregation <aggregation-pipeline>`
- `Text Search <text-search>` and :doc:`Geospatial Queries
</tutorial/geospatial-tutorial>`.

> **Seealso:** - `/reference/sql-comparison`
- `/reference/sql-aggregation-comparison`

### High Availability

MongoDB's replication facility, called `replica set </replication>`, provides:

- automatic failover
- data redundancy.
A `replica set </replication>` is a group of MongoDB servers that maintain the same data set, providing redundancy and increasing data availability.

### Horizontal Scalability

MongoDB provides horizontal scalability as part of its core functionality:

- `Sharding <sharding-introduction>` distributes data across a
cluster of machines.

- Starting in 3.4, MongoDB supports creating :ref:`zones
<zone-sharding>` of data based on the `shard key`. In a balanced cluster, MongoDB directs reads and writes covered by a zone only to those shards inside the zone. See the `zone-sharding` manual page for more information.

### Support for Multiple Storage Engines

MongoDB supports `multiple storage engines </core/storage-engines>`:

- `/core/wiredtiger` (including support for
`/core/security-encryption-at-rest`)

- `/core/inmemory`.
In addition, MongoDB provides pluggable storage engine API that allows third parties to develop storage engines for MongoDB.

## Contents

- Get Started </tutorial/getting-started>
- Create an Atlas Free Tier Cluster <https://www.mongodb.com/docs/get-started/>
- MongoDB Shell (mongosh) <https://www.mongodb.com/docs/mongodb-shell/>
- Databases & Collections </core/databases-and-collections>
- Documents </core/document>
- Query API </query-api>
- BSON Types </reference/bson-types>
