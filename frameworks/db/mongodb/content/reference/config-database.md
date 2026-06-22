---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/config-database.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============

# Config Database

The collections in the `config` database support:

- `Sharded cluster operations <sharding-background>`
- `Causally consistent sessions <sessions>` for standalones,
replica sets, and sharded clusters and retryable writes for replica sets and sharded clusters.

> **Note:** Sharded clusters may show different collections in the
`config` database, depending on whether you connect to
:program:`mongos` or :program:`mongod`:
- On `mongos`, the `config` database shows collections
  located on the config servers, such as
  `config.collections` or `config.chunks`.
- On `mongod`, the `config` database shows
  collections specific to the given shard, such as
  `config.migrationCoordinators` or
  `config.rangeDeletions`.
When a config server and a shard are hosted on the same node,
:program:`mongos` may have access to some shard-local
collections in the `config` database.

## Restrictions

.. include:: /includes/fact-5.0-non-transactional-config-reads.rst

> **Important:** internal and may change between releases of MongoDB. The
`config` database is not a dependable API, and users should not
write data to the `config` database in the course of normal
operation or maintenance.

> **Note:** You cannot perform read/write operations to the collections in the
`config` database inside a :doc:`multi-document transaction
</core/transactions>`.

## Collections to Support Sharded Cluster Operations

list on the sharding-internals page.

To access the `config` database and view the list of collections that support sharding operations, connect :binary:`~bin.mongosh` to a :binary:`~bin.mongos` instance in a sharded cluster and issue the following:

```javascript
use config

show collections
```

> **Note:** If running with access control, ensure you have privileges that
grant :authaction:`listCollections` action on the database.

The config database is mainly for internal use, and during normal operations you should never manually insert or store data in it. However, if you need to verify the write availability of the config server for a sharded cluster, you can insert a document into a test collection (after making sure that no collection of that name already exists):

> **Warning:** system may lead to instability or inconsistent data sets. If you
must modify the `config` database, use :binary:`~bin.mongodump` to
create a full backup of the `config` database.

```javascript
db.testConfigServerWriteAvail.insertOne( { a : 1 } )
```

If the operation succeeds, the config server is available to process writes.

Future releases of the server may include different collections in the config database, so be careful when selecting a name for your test collection.

MongoDB uses the following collections in the `config` database to support sharding:

## Collections to Support Sessions

The `config` database contains the internal collections to support `causally consistent sessions <sessions>` for standalones, replica sets, and sharded clusters and retryable writes and `transactions <transactions>` for replica sets and sharded clusters.

> **Warning:** Do not manually modify or drop these collections.

To access these collections for a :binary:`~bin.mongod` or :binary:`~bin.mongos` instance, connect :binary:`~bin.mongosh` to the instance.
