---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/unique-constraints-on-arbitrary-fields.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:orphan:

======================================

# Unique Constraints on Arbitrary Fields

If you cannot use a unique field as the shard key or if you need to enforce uniqueness over multiple fields, you must create another `collection` to act as a "proxy collection". This collection must contain both a reference to the original document (i.e. its `ObjectId`) and the unique key.

Consider a collection `records` that stores user information. The field `email` is not the shard key, but needs to be unique.

The `proxy` collection then would contain the following:

```javascript
{
  "_id" : ObjectId("...")
  "parent_id" : "<ID>"
  "email" : "<string>"
}
```

Use the following command to create a unique index on the `email` field:

```javascript
db.proxy.createIndex( { "email" : 1 }, { unique : true } )
```

The following example first attempts to insert a document containing the target field and a generated Unique ID into the `proxy` collection. If the operation is successful, then it inserts the full document into the `records` collection.

```javascript
records = db.getSiblingDB('records');
proxy = db.getSiblingDB('proxy');

var primary_id = ObjectId();

proxy.insertOne({
   "_id" : primary_id
   "email" : "example@example.net"
})

// if: the above operation returns successfully,
// then continue:

records.insertOne({
   "_id" : primary_id
   "email": "example@example.net"
   // additional information...
})
```

Note that this methodology requires creating a unique ID for the `primary_id` field rather than letting MongoDB automatically create it on document insertion.

If you need to enforce uniqueness on multiple fields, then each field would require its own proxy collection.

## Considerations

- Your application must catch errors when inserting documents into the
"proxy" collection and must enforce consistency between the two collections.

- If the proxy collection requires sharding, you must shard on the
single field on which you want to enforce uniqueness.

- To enforce uniqueness on more than one field using sharded proxy
collections, you must have one proxy collection for every field for which to enforce uniqueness. If you create multiple unique indexes on a single proxy collection, you cannot be able to shard proxy collections.
