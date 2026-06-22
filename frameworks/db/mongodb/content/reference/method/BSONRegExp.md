---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/BSONRegExp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================

# BSONRegExp() (mongosh method)

## Definition

Creates a new `BSON type <bson-types>` for a regular expression.

## Syntax

`BSONRegExp` has the following syntax:

## Examples

### Insert a `BSONRegExp()` Object

Use the `BSONRegExp()` constructor to create the BSON regular expression.

```javascript
var bsonRegExp = BSONRegExp("(?-i)AA_", "i")
```

Insert the object into the `testbson` collection.

```javascript
db.testbson.insertOne( { foo: bsonRegExp } )
```

### Retrieve a `BSONRegExp()` Object

Query the `testbson` collection for the inserted document.

```javascript
db.testbson.find( {}, {}, { bsonRegExp: true } )
```

You can see the binary BSON regular expressions stored in the collection.

```javascript
[
  {
    _id: ObjectId('65e8ba8a4b3c33a76e6cacca'),
    foo: BSONRegExp('(?-i)AA_', 'i')
  }
]
```

If you set `bsonRegExp` to `false`, `mongosh` returns an error:
