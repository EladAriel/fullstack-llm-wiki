---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/data-modeling/design-patterns/data-versioning/slowly-changing-dimensions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# Slowly Changing Dimensions

Slowly changing dimensions (SCDs) is a framework for managing and tracking changes to dimension data in a data warehouse over time. This framework refers to the dimensions as "slowly changing" because it assumes that the data SCDs cover changes with a low frequency, but without any apparent pattern in time. Use SCDs when the requirements for the data warehouse cover functionality to track and reproduce outputs based on historical states of data.

A common use case for SCDs is reporting. For example, in financial reporting systems, you need to explain the differences between the aggregated values in a report produced last month and those in the current version of the report from the data warehouse.

The different implementations of SCDs in SQL are referred to as "types." Types 0 and 1, the most basic types, only keep track of the original state of data or the current state of data, respectively. Type 2, the most commonly applied implementation, creates three new fields: `validFrom`, `validTo`, and an optional flag on the latest set of data, often called `isValid` or `isEffective`.

## SCD Types

## SCDs in MongoDB

You can apply the SCD framework to MongoDB in the same way you apply it to a relational database. The concept of slowly changing dimensions applies on a per-document basis in the chosen and optimized data model for the specific use case.

### Example

Consider a collection called `prices` that stores the prices of a set of items. You need to keep track of the changes of the price of an item over time in order to be able to process returns of an item, as the money refunded must match the price of the item at the time of purchase. Each document in the collection has an `item` and `price` field:

```javascript
db.prices.insertMany( [
   { 'item': 'shorts', 'price': 10 },
   { 'item': 't-shirt', 'price': 2 },
   { 'item': 'pants', 'price': 5 },
] )
```

Suppose the price of pants changes from `5` to `7`. To track this price change, assume the default values for the necessary data fields for SCD Type 2. The default value for `validFrom` is `01.01.1900`, `validTo` is `01.01.9999`, and `isValid` is `true`. To change the `price` field in the object with `'item': 'pants'`, insert a new document to represent the current state of the pants, and update the previously valid document to no longer be valid:

```javascript
let now = new Date(); 

db.prices.updateOne( 
   { 
      'item': 'pants', 
      "$or": [ 
         { "isValid": false }, 
         { "isValid": null } 
      ] 
   },
   { "$set": 
      {
         "validFrom": new Date("1900-01-01"), 
         "validTo": now, 
         "isValid": false
      } 
   }
);

db.prices.insertOne( 
   { 
      'item': 'pants', 
      'price': 7, 
      "validFrom": now, 
      "validTo": new Date("9999-01-01"), 
      "isValid": true
   }
);
```

To avoid breaking the chain of validity, ensure that both of the above database operation occur at the same timestamp. Depending on the requirements of the application, you can wrap the two above commands into a transaction to ensure MongoDB always applies both changes together. For more information, see `transactions`.

The following operation demonstrates how to query the latest `price` of the document containing the `pants` item:

```javascript
db.prices.find( { 'item': 'pants', 'isValid': true } );
```

To query for the `price` of the document containing the `pants` item at a specific point in time, use the following operation:

```javascript
let time = new Date("2022-11-16T13:00:00");
db.prices.find( {
   'item': 'pants', 
   'validFrom': { '$lte': time }, 
   'validTo': { '$gt': time }
} );
```

### Tracking Changes in Few Fields

If you only need to track changes over time to few fields in a document, you can use SCD type 3 by embedding the history of a field as an array in the first document.

For example, the following aggregation pipeline updates the `price` in the document representing `pants` to `7` and stores the previous value of the `price` with a timestamp of when the previous `price` became invalid in an array called `priceHistory`:

```javascript
db.prices.aggregate( [
   { $match: { 'item': 'pants' } },
   { $addFields: 
      { price: 7, priceHistory: 
         { $concatArrays: 
            [ 
               { $ifNull: [ '$priceHistory', [] ] },
               [ { price: "$price", time: now } ]
            ]
         }
      }
   },
   { $merge: 
      {
         into: "prices",
         on: "_id",
         whenMatched: "merge",
         whenNotMatched: "fail"
      }
   }
] )
```

This solution can become slow or inefficient if your array size gets too large. To avoid large arrays, you can use the `outlier <group-data-outlier-pattern>` or the `bucket <group-data-bucket-pattern>` patterns to design your schema.

## Outlook Data Federation

The above examples focus on a strict and accurate representation of document field changes. Sometimes, you might have less strict requirements on showing historical data. For example, you might have an application that only requires access to the current state of the data most of the time, but you must run some analytical queries on the full history of data.

In this case, you can store the current version of the data in one collection and the historical changes in another collection. You can then remove the historical collection from the active MongoDB cluster using the `MongoDB Atlas Federated Database <atlas-data-federation>` functionalities, and in the fully managed version using the :atlas:`Online Archive </online-archive/manage-online-archive/>`.

## Other Use Cases

While slowly changing dimensions is helpful for data warehousing, you can also use the SCD framework in event-driven applications. If you have infrequent events in different types of categories, it is expensive to find the latest event per category, as the process could require grouping or sorting your data in order to find the current state.

In the case of infrequent events, you can amend the data model by adding a field to store the time of the next event, in addition to the event time per document. The new date field ensures that if you execute a search for a specific point in time, you can easily and efficiently retrieve the respective event you are searching for.
