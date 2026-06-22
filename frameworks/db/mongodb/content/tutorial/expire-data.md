---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/expire-data.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================================

# Expire Data from Collections by Setting TTL

This document provides an introduction to MongoDB's "time to live" or `TTL` collection feature. TTL collections make it possible to store data in MongoDB and have the :binary:`~bin.mongod` automatically remove data after a specified number of seconds or at a specific clock time.

Data expiration is useful for some classes of information, including machine generated event data, logs, and session information that only need to persist for a limited period of time.

A special `TTL index property <index-feature-ttl>` supports the implementation of TTL collections. The TTL feature relies on a background thread in :binary:`~bin.mongod` that reads the date-typed values in the index and removes expired `documents <document>` from the collection.

.. include:: /includes/indexes/create-ttl-indexes.rst

> **Note:** The TTL index is a single field index. Compound indexes do not
support the TTL property. For more information on TTL indexes,
see `index-feature-ttl`.

You can modify the `expireAfterSeconds` of an existing TTL index using the :dbcommand:`collMod` command.

## Expire Documents in the {+atlas+} UI

To expire data in the `Atlas UI <atlas-ui-overview>`, follow these steps:

## Expire Documents after a Specified Number of Seconds

You can expire documents after a specified number of seconds through collection creation options or a TTL index.

### Specify Expiration at Collection Creation

To specify expiration time at collection creation, use the `expireAfterSeconds <db.createCollection.expireAfterSeconds>` option when you create your collection.

> **Note:** The `expireAfterSeconds` option is only available for :ref:`time
series collections <manual-timeseries-landing>` and :ref:`clustered
collections <clustered-collections>`.

### Specify Expiration with a TTL Index

To expire data after a specified number of seconds has passed since the indexed field, create a TTL index on a field that holds values of BSON date type or an array of BSON date-typed objects and specify a value greater than or equal to zero in the `expireAfterSeconds` field. A document expires when the number of seconds in the `expireAfterSeconds` field has passed since the time specified in its indexed field. [#field-is-array-of-dates]_

.. include:: includes/expireAfterSeconds-range.rst

For example, the following operation creates an index on the `log_events` collection's `createdAt` field and specifies the `expireAfterSeconds` value of `10` to set the expiration time to be ten seconds after the time specified by `createdAt`.

```javascript
db.log_events.createIndex( { "createdAt": 1 }, { expireAfterSeconds: 10 } )
```

When adding documents to the `log_events` collection, set the `createdAt` field to the current time:

```javascript
db.log_events.insertOne( {
   "createdAt": new Date(),
   "logEvent": 2,
   "logMessage": "Success!"
} )
```

MongoDB automatically deletes documents from the `log_events` collection when the document's `createdAt` value [#field-is-array-of-dates]_ is older than the number of seconds specified in `expireAfterSeconds`.

date-typed objects, data expires if at least one of BSON date-typed object is older than the number of seconds specified in `expireAfterSeconds`.

## Expire Documents with Filter Conditions

To expire documents with specific filter expressions, you can create an index that is both a `partial <index-type-partial>` and a `TTL <index-feature-ttl>` index.

Create a partial TTL index:

```javascript
db.foo.createIndex( 
   { F: 1 }, 
   { 
      name: "Partial-TTL-Index", 
      partialFilterExpression: { D : 1 }, 
      expireAfterSeconds: 10 
   }
)
```

Insert two documents, one of which matches the filter expression `{ D : 1 }` of the `partialFilterExpression`:

```javascript
db.foo.insertMany( [
   { "F" : ISODate("2019-03-07T20:59:18.428Z"), "D" : 3},
   { "F" : ISODate("2019-03-07T20:59:18.428Z"), "D" : 1}
] )
```

Wait for ten seconds then query the `foo` collection:

```javascript
db.foo.find({}, {_id: 0, F: 1, D: 1})
```

The document that matches the `partialFilterExpression` of `{ D : 1 }` is deleted (expired). As a result, only one document remains in the `foo` collection:

```javascript
{ "F" : ISODate("2019-03-07T20:59:18.428Z"), "D" : 3}
```

## Expire Documents at a Specific Clock Time

To expire documents at a specific clock time, create a TTL index on a field that holds values of BSON date type or an array of BSON date-typed objects, and specify an `expireAfterSeconds` value of `0`. For each document in the collection, set the indexed date field to a value corresponding to the time the document should expire. If the indexed date field contains a date in the past, MongoDB considers the document expired.

For example, the following operation creates an index on the `log_events` collection's `expireAt` field and specifies the `expireAfterSeconds` value of `0`:

```javascript
db.log_events.createIndex( { "expireAt": 1 }, { expireAfterSeconds: 0 } )
```

For each document, set the value of `expireAt` to correspond to the time the document should expire. For example, the following :method:`~db.collection.insertOne()` operation adds a document that expires at `July 22, 2013 14:00:00`.

```javascript
db.log_events.insertOne( {
   "expireAt": new Date('July 22, 2013 14:00:00'),
   "logEvent": 2,
   "logMessage": "Success!"
} )
```

MongoDB automatically deletes documents from the `log_events` collection when the documents' `expireAt` value is older than the number of seconds specified in `expireAfterSeconds`, that is, `0` seconds older in this case.

## Indexes Configured Using NaN

> **Warning:** Possible Data Loss
When a TTL index has `expireAfterSeconds` set to `NaN`, upgrade,
downgrade, and certain syncing operations can lead to unexpected
behavior and possible data loss.

Do not set `expireAfterSeconds` to `NaN` in your TTL index configuration.

Prior to MongoDB 5.0, when a TTL index has `expireAfterSeconds` set to `NaN`, MongoDB logs an error and does not remove any records.

From MongoDB 5.0.0 - 5.0.13 (and 6.0.0 - 6.0.1), `NaN` is treated as `0`. If a TTL index is configured with `expireAfterSeconds` set to `NaN`, all TTL-indexed documents expire immediately.

.. include:: /includes/indexes/expireAfterSeconds-versions.rst

However, there are still some situations which may result in unexpected behavior. Documents may expire:

- During an initial sync to an earlier version from MongoDB 5.0.0 -
5.0.13 (or 6.0.0 - 6.0.1).

- When upgrading from an earlier version to MongoDB 5.0.0 - 5.0.13.
- When restoring a collection from a pre-5.0 :binary:`~bin.mongodump`
into a MongoDB 5.0.0 - 5.0.13 (or 6.0.0 - 6.0.1) instance.

To avoid problems, either drop or correct any misconfigured TTL indexes.
