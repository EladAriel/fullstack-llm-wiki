---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/ddl-operations.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============

# DDL Operations

DDL (Data Description Language) operations change the properties of a database or collection. MongoDB supports both `<explicit-ddl-operations>` and `<implicit-ddl-operations>`. Explicit DDL operations directly run an operation like creating or dropping a collection or index. Implicit DDL operations create collections by referencing a non-existent collection, like inserting data into a non-existent collection.

## Explicit DDL Operations

MongoDB supports the following explicit `DDL <DDL (Data Definition Language)>` operations:

- `cleanupStructuredEncryptionData`
- :dbcommand:`cloneCollectionAsCapped`
- :dbcommand:`collMod`
- :dbcommand:`compactStructuredEncryptionData`
- :dbcommand:`convertToCapped`
- :dbcommand:`create`
- :dbcommand:`createIndexes`
- :dbcommand:`drop`
- :dbcommand:`dropDatabase`
- :dbcommand:`dropIndexes`
- :dbcommand:`enableSharding`
- :dbcommand:`moveCollection`
- :dbcommand:`movePrimary`
- :dbcommand:`renameCollection`
- :dbcommand:`refineCollectionShardKey`
- :dbcommand:`reshardCollection`
- :dbcommand:`shardCollection`
- :dbcommand:`unshardCollection`
## Implicit DDL Operations

MongoDB also supports write operations such as :dbcommand:`insert` or :dbcommand:`update` with `upsert:true`. Any command that writes to a non-existing collection creates that collection.

### Examples

For example, this `insert` command creates the `users` collection if it does not already exist.

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [ { _id: 1, user: "abc123", status: "A" } ]
   }
)
```

This `update` command with `upsert: true` creates the `people` collection if it does not already exist.

```javascript
db.runCommand(
   {
      update: "people",
      updates: [
        { q: { name: "Andy" }, u: { $inc: { score: 1 } }, upsert: true }
      ]
   }
)
```
