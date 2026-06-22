---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/dateFromString.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# $dateFromString (expression operator)

## Definition

> **Seealso:** - :expression:`$toDate`
- :expression:`$convert`

## Behavior

## Format Specifiers

.. include:: /includes/extracts/date-format-specifiers-dateFromString.rst

## Examples

### Converting Dates

Consider a collection `logmessages` that contains the following documents with dates.

```javascript
{ _id: 1, date: "2017-02-08T12:10:40.787", timezone: "America/New_York", message:  "Step 1: Started" },
{ _id: 2, date: "2017-02-08", timezone: "-05:00", message:  "Step 1: Ended" },
{ _id: 3, message:  " Step 1: Ended " },
{ _id: 4, date: "2017-02-09", timezone: "Europe/London", message: "Step 2: Started"},
{ _id: 5, date: "2017-02-09T03:35:02.055", timezone: "+0530", message: "Step 2: In Progress"}
```

The following aggregation uses $dateFromString to convert the `date` value to a date object:

```javascript
db.logmessages.aggregate( [ {
   $project: {
      date: {
         $dateFromString: {
            dateString: '$date',
            timezone: 'America/New_York'
         }
      }
   }
} ] )
```

The above aggregation returns the following documents and converts each `date` field to the Eastern Time Zone:

```javascript
 { "_id" : 1, "date" : ISODate("2017-02-08T17:10:40.787Z") }
 { "_id" : 2, "date" : ISODate("2017-02-08T05:00:00Z") }
 { "_id" : 3, "date" : null }
 { "_id" : 4, "date" : ISODate("2017-02-09T05:00:00Z") }
 { "_id" : 5, "date" : ISODate("2017-02-09T08:35:02.055Z") }
```

The `timezone` argument can also be provided through a document field instead of a hard coded argument. For example:

```javascript
db.logmessages.aggregate( [ {
   $project: {
      date: {
         $dateFromString: {
            dateString: '$date',
            timezone: '$timezone'
         }
      }
   }
} ] )
```

The above aggregation returns the following documents and converts each `date` field to their respective UTC representations.

```javascript
 { "_id" : 1, "date" : ISODate("2017-02-08T17:10:40.787Z") }
 { "_id" : 2, "date" : ISODate("2017-02-08T05:00:00Z") }
 { "_id" : 3, "date" : null }
 { "_id" : 4, "date" : ISODate("2017-02-09T00:00:00Z") }
 { "_id" : 5, "date" : ISODate("2017-02-08T22:05:02.055Z") }
```

### `onError`

If your collection contains documents with unparsable date strings, :expression:`$dateFromString` throws an error unless you provide an `aggregation expression <aggregation-expressions>` to the optional `onError` parameter.

For example, given a collection `dates` with the following documents:

```javascript
{ "_id" : 1, "date" : "2017-02-08T12:10:40.787", timezone: "America/New_York" },
{ "_id" : 2, "date" : "20177-02-09T03:35:02.055", timezone: "America/New_York" }
```

You can use the `onError` parameter to return the invalid date in its original string form:

```javascript
db.dates.aggregate( [ {
   $project: {
      date: {
         $dateFromString: {
            dateString: '$date',
            timezone: '$timezone',
            onError: '$date'
         }
      }
   }
} ] )
```

This returns the following documents:

```javascript
{ "_id" : 1, "date" : ISODate("2017-02-08T17:10:40.787Z") }
{ "_id" : 2, "date" : "20177-02-09T03:35:02.055" }
```

### `onNull`

If your collection contains documents with `null` date strings, :expression:`$dateFromString` returns `null` unless you provide an `aggregation expression <aggregation-expressions>` to the optional `onNull` parameter.

For example, given a collection `dates` with the following documents:

```javascript
{ "_id" : 1, "date" : "2017-02-08T12:10:40.787", timezone: "America/New_York" },
{ "_id" : 2, "date" : null, timezone: "America/New_York" }
```

You can use the `onNull` parameter to have :expression:`$dateFromString` return a date representing the `unix epoch` instead of `null`:

```javascript
db.dates.aggregate( [ {
   $project: {
      date: {
         $dateFromString: {
            dateString: '$date',
            timezone: '$timezone',
            onNull: new Date(0)
         }
      }
   }
} ] )
```

This returns the following documents:

```javascript
{ "_id" : 1, "date" : ISODate("2017-02-08T17:10:40.787Z") }
{ "_id" : 2, "date" : ISODate("1970-01-01T00:00:00Z") }
```
