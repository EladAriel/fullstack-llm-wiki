---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getDBNames.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# Mongo.getDBNames() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Examples

### List Databases

List the available databases for the current MongoDB instance:

```javascript
db.getMongo().getDBNames()
```

The :method:`db.getMongo()` method creates a connection to the instance. :method:`Mongo.getDBNames()` returns:

```javascript
[ 'admin', 'config', 'local', 'test' ]
```

### Map Database List to Another Method

Use :method:`Mongo.getDBNames()` to get a list of collections:

```javascript
db.getMongo().getDBNames().map( 
   name => db.getSiblingDB( name ).getCollectionNames()
)
```

Example output:

```javascript
[
   [ 'system.users', 'system.keys', 'system.version' ],
   [
     'settings',
     'tenantMigrationRecipients',
     'system.sessions',
     'transactions',
     'external_validation_keys',
     'image_collection',
     'tenantMigrationDonors',
     'system.indexBuilds'
   ],
   [
     'replset.minvalid',
     'system.views',
     'oplog.rs',
     'replset.initialSyncId',
     'startup_log',
     'system.replset',
     'system.rollback.id',
     'replset.oplogTruncateAfterPoint',
     'replset.election',
     'system.tenantMigration.oplogView'
   ],
   [
     'feedback',
     'inventory',
     'engineers',
     'clothes'
   ]
]
```

- :method:`Mongo.getDBNames()` returns a list of databases.
- `map` defines a function that iterates over the list of databases.
Each iteration of `map`:

- assigns a database to the `name` variable,
- connects to the database currently stored in `name` using
:method:`db.getSiblingDB()`,

- returns the collections in the current database using
:method:`db.getCollectionNames()`.
