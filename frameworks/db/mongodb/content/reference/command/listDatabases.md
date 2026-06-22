---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/listDatabases.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# listDatabases (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

```javascript
db.adminCommand( 
   { 
     listDatabases: 1 
   } 
)
```

The value (for example, `1`) does not affect the output of the command.

## Command Fields

The command can take the following optional fields:

## Behavior

When `authentication <authentication>` is enabled, `listDatabases` returns different results based on the user's privileges and the `authorizedDatabases` option:

.. include:: /includes/extracts/listDatabases-auth-privileges-4.0.6.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Replica Set Member State Restriction

.. include:: /includes/extracts/4.4-changes-repl-state-restrictions-operation.rst

## Examples

### List Database Names and Sizes

Run `listDatabases` against the `admin` database:

```javascript
db.adminCommand( { listDatabases: 1 } )
```

Example output:

```json
{
   "databases" : [
      {
         "name" : "admin",
         "sizeOnDisk" : 83886080,
         "empty" : false
      },
      {
         "name" : "local",
         "sizeOnDisk" : 83886080,
         "empty" : false
      },
      {
         "name" : "test",
         "sizeOnDisk" : 83886080,
         "empty" : false
      }
   ],
   "totalSize" : 251658240,
   "totalSizeMb" : 251,
   "ok" : 1
}
```

### List Database Names Only

Run `listDatabases` against the `admin` database. Specify the `nameOnly: true` option:

```javascript
db.adminCommand( { listDatabases: 1, nameOnly: true} )
```

Example output:

```javascript
{
   "databases" : [
      {
         "name" : "admin"
      },
      {
         "name" : "local"
      },
      {
         "name" : "test"
      }
   ],
   "ok" : 1
}
```

### List Databases That Match the Filter

Run `listDatabases` against the `admin` database. Specify the `filter` option to list only databases that match the filter criteria.

For example, the following filter returns only databases whose name matches the specified :query:`regular expression <$regex>`:

```javascript
db.adminCommand( { listDatabases: 1, filter: { "name": /^rep/ } } )
```

### Sharded Clusters

When run against a :binary:`~bin.mongos` instance, `listDatabases`:

- adds a `shards` embedded document to each database's summary
document if `nameOnly: false`.

- excludes the `local` database.
Each field in the `shards` embedded document uses the shard name as the key and the database's size in bytes as the value.

The `sizeOnDisk` field represents the total size of all collections and indexes in the listed database.

For example:

```javascript
{
  "databases" : [
    {
      "name" : "admin",
      "sizeOnDisk" : 16384,
      "empty" : false,
      "shards" : {
        "config" : 16384
      }
    },
    {
      "name" : "config",
      "sizeOnDisk" : 176128,
      "empty" : false,
      "shards" : {
        "shard01" : 28672,
        "shard02" : 8192,
        "config" : 139264
      }
    },
    {
      "name" : "test",
      "sizeOnDisk" : 12288,
      "empty" : false,
      "shards" : {
        "shard01" : 12288
      }
    }
  ],
  "totalSize" : 204800,
  "totalSizeMb" : 0,
  "ok" : 1
}
```

> **Seealso:** `/tutorial/use-database-commands`.

## Output
