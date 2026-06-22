---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/analyzeShardKey-examples.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### { _id: 1 } keyCharacteristics

This example uses the |analyzeShardKey| to provide metrics on the `{ _id: 1 }` shard key on the `social.post` collection.

The following code block uses :method:`db.collection.configureQueryAnalyzer()` to turn on query sampling:

```javascript
use social
db.post.configureQueryAnalyzer( 
   {
      mode: "full",
      samplesPerSecond: 5
   } 
)
```

After `db.collection.configureQueryAnalyzer()` collects query samples, the following code block uses the |analyzeShardKey| to sample 10,000 documents and calculate results:

```javascript
use social
db.post.analyzeShardKey(
   { _id: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false,
      sampleSize: 10000
   }
)
```

### { lastName: 1 } keyCharacteristics

This |analyzeShardKey| provides metrics on the `{ lastName: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { lastName: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false
   }
)
```

The output for this example resembles the following:

.. include:: /includes/analyzeShardKey-example1-output.rst

### { userId: 1 } keyCharacteristics

This |analyzeShardKey| provides metrics on the `{ userId: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { userId: 1 },
   {
      keyCharacteristics: true,
      readWriteDistribution: false
   }
)
```

The output for this example resembles the following:

.. include:: /includes/analyzeShardKey-example2-output.rst

### { userId: 1 } readWriteDistribution

This |analyzeShardKey| provides metrics on the `{ userId: 1 }` shard key on the `social.post` collection:

```javascript
use social
db.post.analyzeShardKey(
   { userId: 1 },
   {
      keyCharacteristics: false,
      readWriteDistribution: true
   }
)
```

The output for this example resembles the following:

.. include:: /includes/analyzeShardKey-example3-output.rst
