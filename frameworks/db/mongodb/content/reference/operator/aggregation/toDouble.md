---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/toDouble.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# $toDouble (expression operator)

## Definition

## Behavior

The following table lists the input types that can be converted to a double:

.. include:: /includes/strings-to-non-decimal.rst

The following table lists some conversion to double examples:

### Subnormal Numbers

.. include:: /includes/fact-float-parse-behavior-8.3.rst

## Example

Create a collection `weather` with the following documents:

```javascript
db.weather.insertMany( [
   { _id: 1, date: new Date("2018-06-01"), temp: "26.1C" },
   { _id: 2,  date: new Date("2018-06-02"), temp: "25.1C" },
   { _id: 3,  date: new Date("2018-06-03"), temp: "25.4C" },
] )
```

The following aggregation operation on the `weather` collection parses the `temp` value and converts to a double:

```javascript
// Define stage to add degrees field with converted value

tempConversionStage = { 
   $addFields: { 
      degrees: { $toDouble: { $substrBytes: [ "$temp", 0, 4 ] } } 
   }
};

db.weather.aggregate( [
   tempConversionStage,
] )
```

The operation returns the following documents:

```javascript
{ "_id" : 1, "date" : ISODate("2018-06-01T00:00:00Z"), "temp" : "26.1C", "degrees" : 26.1 }
{ "_id" : 2, "date" : ISODate("2018-06-02T00:00:00Z"), "temp" : "25.1C", "degrees" : 25.1 }
{ "_id" : 3, "date" : ISODate("2018-06-03T00:00:00Z"), "temp" : "25.4C", "degrees" : 25.4 }
```

.. include:: /includes/note-conversion-error-use-convert.rst
