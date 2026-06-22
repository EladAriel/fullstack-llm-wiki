---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/binarySize.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# $binarySize (expression operator)

## Definition

## Behavior

The argument for :expression:`$binarySize` must resolve to either:

- A string,
- A binary data value, or
- null.
If the argument is a string or binary data value, the expression returns the size of the argument in bytes.

If the argument is `null`, the expression returns `null`.

If the argument resolves to any other data type, :expression:`$binarySize` errors.

### String Size Calculation

If the argument for :expression:`$binarySize` is a string, the operator counts the number of UTF-8 encoded bytes in a string where each character may use between one and four bytes.

.. include:: /includes/fact-utf8-char-byte-sizes.rst

Consider the following examples:

## Example

In :binary:`~bin.mongosh`, create a sample collection named `images` with the following documents:

```javascript
db.images.insertMany([
  { _id: 1, name: "cat.jpg", binary: new BinData(0, "OEJTfmD8twzaj/LPKLIVkA==")},
  { _id: 2, name: "big_ben.jpg", binary: new BinData(0, "aGVsZmRqYWZqYmxhaGJsYXJnYWZkYXJlcTU1NDE1Z2FmZCBmZGFmZGE=")},
  { _id: 3, name: "tea_set.jpg", binary: new BinData(0, "MyIRAFVEd2aImaq7zN3u/w==")},
  { _id: 4, name: "concert.jpg", binary: new BinData(0, "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=")},
  { _id: 5, name: "empty.jpg", binary: new BinData(0, "") }
])
```

The following aggregation :pipeline:`projects <$project>`:

- The `name` field
- The `imageSize` field, which uses :expression:`$binarySize` to
return the size of the document's `binary` field in bytes.

```javascript
db.images.aggregate([
  {
    $project: {
      "name": "$name",
      "imageSize": { $binarySize: "$binary" }
    }
  }
])
```

The operation returns the following result:

```javascript
{ "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
{ "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
{ "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
{ "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
{ "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
```

### Find Largest Binary Data

The following pipeline returns the image with the largest binary data size:

```javascript
db.images.aggregate([
   // First Stage
   { $project: { name: "$name", imageSize: { $binarySize: "$binary" } }  },
   // Second Stage
   { $sort: { "imageSize" : -1 } },
   // Third Stage
   { $limit: 1 }
])
```

First Stage The first stage of the pipeline :pipeline:`projects <$project>`:

- The `name` field
- The `imageSize` field, which uses :expression:`$binarySize` to
return the size of the document's `binary` field in bytes.

This stage outputs the following documents to the next stage:

```javascript
  { "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
  { "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
  { "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
  { "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
```

Second Stage The second stage :pipeline:`sorts <$sort>` the documents by `imageSize` in descending order.

This stage outputs the following documents to the next stage:

```javascript
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
  { "_id" : 2, "name" : "big_ben.jpg", "imageSize" : 41 }
  { "_id" : 1, "name" : "cat.jpg", "imageSize" : 16 }
  { "_id" : 3, "name" : "teaset.jpg", "imageSize" : 16 }
  { "_id" : 5, "name" : "empty.jpg", "imageSize" : 0 }
```

Third Stage The third stage :pipeline:`limits <$limit>` the output documents to only return the document appearing first in the sort order:

```javascript
  { "_id" : 4, "name" : "concert.jpg", "imageSize" : 269 }
```

> **Seealso:** - :pipeline:`$project`
- :pipeline:`$sort`
- :pipeline:`$limit`
- :expression:`$strLenBytes`
- :expression:`$bsonSize`
