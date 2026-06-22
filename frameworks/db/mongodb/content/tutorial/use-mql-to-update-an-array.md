---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/use-mql-to-update-an-array.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================================

# Update Array Elements with MQL Positional Operators

You can use positional operators with MongoDB Query Language (MQL) to `update documents <write-op-update>` that contain arrays without replacing the array or appending to it.

This tutorial presents several use cases for positional operators within MongoDB.

## Before You Begin

- Install `mongosh <mdb-shell-install>`.
- Connect to a `deployment <mdb-shell-connect>`.
- Use :binary:`~bin.mongosh` to insert documents into a new collection in the
default `test` database:

```javascript
   db.employees.insertMany( 
      [
         {
            _id: 'SF',
            engineering: [
               { name: 'Alice', email: 'missingEmail', salary: 100000 },
               { name: 'Bob', email: 'missingEmail', salary: 75000 }
            ],
            sales: [
               { name: 'Charlie', email: 'charlie@mail.com', salary: 90000, bonus: 1000 }
            ]
         },
         {
            _id: 'NYC',
            engineering: [
               { name: 'Dave', email: 'dave@mail.com', salary: 55000 },
            ],
            sales: [
               { name: 'Ed', email: 'ed@mail.com', salary: 99000, bonus: 2000 },
               { name: 'Fran', email: 'fran@mail.com', salary: 50000, bonus: 10000 }
            ]
         }
      ] 
   );
```

## Steps

The following examples show you how to:

- `positional-update-first-array-match`
- `positional-update-specific-array-match`
- `positional-update-all-array-elements`
- `positional-update-array-filter-match`
### Use the $ Operator to Update the First Match in an Array

To update only the first match within an array, use the :update:`$` operator. The :update:`$` operator acts as a placeholder to update the first element matched.

The following example uses the :method:`~db.collection.updateOne()` method with the :update:`$` and :update:`$set` operators to update the first email that has the value `missingEmail` in the `engineering` array to `alice@mail.com`.

```javascript
db.employees.updateOne(
   { "engineering.email": "missingEmail" },
   { "$set": { "engineering.$.email": "alice@mail.com" } }
);
```

Use the :method:`find() <db.collection.find()>` method to confirm the update to Alice's email.

As shown in the example above, after you filter for documents that have an array element with the `engineering.email` field set to `missingEmail`, the :update:`$` operator only updates the first occurrence that matches the filter.

### Use the $ Operator with $elemMatch to Update a Specific Element

To update a particular element, you can use the :query:`$elemMatch` operator.

The following example uses the :query:`$elemMatch` operator and the :update:`$` operator to update Bob's `email` to `"bob@mail.com"`.

```javascript
db.employees.updateOne(  
   { engineering: { $elemMatch: { name: "Bob", email: "missingEmail" } } },  
   { $set: { "engineering.$.email": "bob@mail.com" } }  
); 
```

Use the :method:`find() <db.collection.find()>` method to confirm the update to Bob's email.

### Use the $[] Operator to Update All Array Elements Within a Document

To update every element of an array with a single operation, use the :update:`$[]` operator.

Consider a case where you want to give an additional bonus of $2,000 to your sales employees in NYC. You can use the :method:`~db.collection.updateMany()` method with the :update:`$[]` operator and the :update:`$inc` operator to increase all `bonus` fields within the `sales` array in the `NYC` document by `2000`.

```javascript
db.employees.updateMany(
   { "_id": "NYC" },
   { "$inc": { "sales.$[].bonus": 2000 } }
);
```

Use the :method:`find() <db.collection.find()>` method to confirm the update to the `bonus` fields for the employees on NYC's sales team.

### Use the $[<identifier>] Operator to Update Elements that Match a Filter Condition

To update several array elements in a single operation without excessive client-side code paired with a replace operation, use the :update:`$[<identifier>]` operator. The :update:`$[<identifier>]` operator acts as a placeholder to update all elements that match an `arrayFilters <update-many-arrayFilters>` condition.

Consider a case where you want to update specific employees' salaries if they meet a number of conditions. You can use the :method:`~db.collection.updateMany()` method with the :update:`$[<identifier>]` operator to accomplish this task.

```javascript
db.employees.updateMany(
   {},
   {
      "$set": {
            "engineering.$[elemX].salary": 95000,
             "sales.$[elemY].salary": 75000
      }
   },
   {
      "arrayFilters": [
            { "elemX.name": "Bob", "elemX.salary": 75000 },
            { "elemY.name": "Ed", "elemY.salary": 50000, }
      ]
   }
);
```

In the above example, the first parameter is an empty match, to evaluate all documents in the collection.

`elemX` and `elemY` represent two different `arrayFilters <update-many-arrayFilters>`:

- To match `elemX`, an array object must have a `name` field of `Bob` and
a `salary` of `75000`.

- To match `elemY`, an array object must have a `name` field of `Ed` and a
`salary` of `50000`.

If an array item in the document matches the `elemX` filter, then `updateMany()` sets the `salary` field for the object to `95000`. If an array item matches the `elemY` filter, then `updateMany()` sets the `salary` field for the object to `75000`. If a filter doesn't match, the corresponding :update:`$set` operation doesn't trigger.

Use the :method:`find() <db.collection.find()>` method to confirm the update to Bob's salary because he meets both `elemX`'s conditions.

Use the :method:`find() <db.collection.find()>` method to confirm the update to Ed's salary did not succeed because he does not meet either `elemX` or `elemY`'s conditions.

If an array contains multiple matches for the `arrayFilters <update-many-arrayFilters>` condition, then the :update:`$[<identifier>]` operator updates all matches.

## Conclusion

This tutorial teaches you some of the positional operators within the MongoDB Query Language (MQL). These operators are useful when working with arrays because they prevent you from having to do full replaces on the array or extended client-side manipulation. To learn more about MQL, see [get started with Atlas](https://www.mongodb.com/docs/get-started/)_.

To learn more about update operators in MongoDB, see `<update-operators-ref>`.
