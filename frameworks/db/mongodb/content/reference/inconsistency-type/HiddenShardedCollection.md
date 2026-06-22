---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/inconsistency-type/HiddenShardedCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

######################## HiddenShardedCollection ########################

# Description

# Format

```json
{
   type: "HiddenShardedCollection",
   description: "<string>",
   details: {
      namespace: "<string>",
      collection: "<object>",
   }
}
```

|incon-type| inconsistency documents contain the following fields:

# Example

.. include:: /includes/inconsistency-type/example

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "HiddenShardedCollection",
            description: "Found sharded collection but relative database does not exist",
            details: {
               namespace: "test.authors",
               collection: {
                   _id: "test.authors",
                   lastmodEpoch: ObjectId("64ddd78de906038182671674"),
                   lastmod: ISODate("2023-08-17T08:17:17.944Z"),
                   timestamp: Timestamp(1692260237, 58),
                   uuid: new UUID("69317741-7bc5-4eca-8877-7858cecf67d6"),
                   key: {
                      "skey" : 1
                   },
                   unique: false,
                   noBalance: false
                }
            }
         }
      ],
   },
   ok: 1
}
```
