---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.find.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# db.collection.find() (mongosh method)

.. include:: /includes/wayfinding/mongosh-method-find.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.find()` has the following form:

```javascript
db.collection.find( <query>, <projection>, <options> )
```

### Parameters

`db.collection.find()` takes the following parameters:

## Behavior

### Projection

.. include:: /includes/extracts/projection-language-consistency-admonition.rst

The `projection` parameter determines which fields are returned in the matching documents. The `projection` parameter takes a document of the following form:

```javascript
{ <field1>: <value>, <field2>: <value> ... }
```

.. include:: /includes/extracts/projection-values-table.rst

### Options

.. include:: /includes/find-options-values-table.rst

Embedded Field Specification ````````````````````````````

.. include:: /includes/extracts/projection-embedded-field-format.rst

`_id` Field Projection ````````````````````````

.. include:: /includes/extracts/projection-id-field.rst

Inclusion or Exclusion ``````````````````````

.. include:: /includes/extracts/projection-inclusion-exclusion.rst

See `Projection Examples <find-projection-examples>`.

Sorting ```````

When an operation both sorts and `projects <projection>` with the same fields, MongoDB sorts on the original field values before applying the projection. For more information about operation order, see `find() Order of Operations <find-order-of-operations>`.

### Cursor Handling

Executing `find()` in :binary:`~bin.mongosh` automatically iterates the cursor to display up to the first 20 documents. Type `it` to continue iteration.

To access the returned documents with a driver, use the appropriate cursor handling mechanism for the :driver:`driver language </>`.

### Read Concern

To specify the `read concern <read-concern>`, use the :method:`cursor.readConcern()` method.

### Type Bracketing

MongoDB treats some data types as equivalent for comparison purposes. For instance, numeric types undergo conversion before comparison. For most data types, however, `comparison operators <query-selectors-comparison>` only perform comparisons on documents where the `BSON type <bson-types-comparison-order>` of the target field matches the type of the query operand. Consider the following collection:

```javascript
{ "_id": "apples", "qty": 5 }
{ "_id": "bananas", "qty": 7 }
{ "_id": "oranges", "qty": { "in stock": 8, "ordered": 12 } }
{ "_id": "avocados", "qty": "fourteen" }
```

The following query uses :query:`$gt` to return documents where the value of `qty` is greater than `4`.

```javascript
db.collection.find( { qty: { $gt: 4 } } )
```

The query returns the following documents:

```javascript
{ "_id": "apples", "qty": 5 }
{ "_id": "bananas", "qty": 7 }
```

The document with `_id` equal to `"avocados"` is not returned because its `qty` value is of type `string` while the :query:`$gt` operand is of type `integer`.

The document with `_id` equal to `"oranges"` is not returned because its `qty` value is of type `object`.

> **Note:** To enforce data types in a collection, use
`/core/schema-validation`.

### Sessions

For cursors created inside a session, you cannot call :dbcommand:`getMore` outside the session.

Similarly, for cursors created outside of a session, you cannot call :dbcommand:`getMore` inside a session.

Session Idle Timeout ````````````````````

.. include:: /includes/extracts/sessions-cursor-timeout.rst

For operations that may be idle for longer than 30 minutes, associate the operation with an explicit session using :method:`Mongo.startSession()` and periodically refresh the session using the :dbcommand:`refreshSessions` command. See :limit:`Session Idle Timeout` for more information.

### Transactions

.. include:: /includes/extracts/transactions-supported-operation.rst

.. include:: /includes/extracts/transactions-operations-getMore.rst

.. include:: /includes/extracts/transactions-usage.rst

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Query Settings

.. include:: /includes/persistent-query-settings-info-for-queries.rst

## Examples

The examples in this section use documents from the `bios collection <bios-example-collection>` where the documents generally have the form:

```javascript
{
    "_id" : <value>,
    "name" : { "first" : <string>, "last" : <string> },       // embedded document
    "birth" : <ISODate>,
    "death" : <ISODate>,
    "contribs" : [ <string>, ... ],                           // Array of Strings
    "awards" : [
        { "award" : <string>, year: <number>, by: <string> }  // Array of embedded documents
        ...
    ]
}
```

To create and populate the `bios` collection, see `bios collection <bios-example-collection>`.

### Find All Documents in a Collection

The `find()` method with no parameters returns all documents from a collection and all fields. The following example returns all documents in the `bios collection <bios-example-collection>`:

```javascript
db.bios.find()
```

Sort returned documents ``````````````````````` The following operation sorts the documents returned from the bios collection by the `name`` field in ascending order:

```javascript
db.bios.find({}, { sort: { name: 1 }})
```

Limit returned documents ```````````````````````` The following operation limits the number of returned documents from the bios collection to 5:

```javascript
db.bios.find({}, { limit: 5 })
```

Set starting point of returned documents ````````````````````````````````````````` The following operation skips the first 5 documents and returns all remaining documents from the bios collection:

```javascript
db.bios.find({}, { skip: 5 })
```

### Find Documents that Match Query Criteria

Query for Equality ``````````````````

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection> where id` equals `5`:

```javascript
  db.bios.find( { _id: 5 } )
```

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection>` where the field `last` in the `name` embedded document equals `"Hopper"`:

```javascript
  db.bios.find( { "name.last": "Hopper" } )

.. note::

  To access fields in an embedded document, use :ref:`dot notation
  <document-dot-notation-embedded-fields>` (``"<embedded
  document>.<field>"``).
```

Query Using Operators `````````````````````

To find documents that match a set of selection criteria, call `find()` with the `<criteria>` parameter.

MongoDB provides various `query operators <query-selectors>` to specify the criteria.

- The following operation uses the :query:`$in` operator to return
documents in the `bios collection </reference/bios-example-collection> where id` equals either `5` or `ObjectId("507c35dd8fada716c89d0013")`:

```javascript
  db.bios.find(
     { _id: { $in: [ 5, ObjectId("507c35dd8fada716c89d0013") ] } }
  )
```

- The following operation uses the :query:`$gt` operator returns all
the documents from the `bios` collection where `birth` is greater than `new Date('1950-01-01')`:

```javascript
  db.bios.find( { birth: { $gt: new Date('1950-01-01') } } )
```

- The following operation uses the :query:`$regex` operator to return
documents in the `bios collection </reference/bios-example-collection>` where `name.last` field starts with the letter `N` (or is `"LIKE N%"`)

```javascript
  db.bios.find(
     { "name.last": { $regex: /^N/ } }
  )
```

For a list of the query operators, see `query-selectors`.

Query for Ranges ````````````````

Combine comparison operators to specify ranges for a field. The following operation returns from the `bios collection </reference/bios-example-collection>` documents where `birth` is between `new Date('1940-01-01')` and `new Date('1960-01-01')` (exclusive):

```javascript
db.bios.find( { birth: { $gt: new Date('1940-01-01'), $lt: new Date('1960-01-01') } } )
```

Query for Multiple Conditions `````````````````````````````

The following operation returns all the documents from the `bios collection </reference/bios-example-collection>` where `birth` field is :query:`greater than <$gt>` `new Date('1950-01-01')` and `death` field does not exists:

```javascript
db.bios.find( {
   birth: { $gt: new Date('1920-01-01') },
   death: { $exists: false }
} )
```

### Compare Two Fields from A Single Document

.. include:: /includes/use-expr-in-find-query.rst

### Query Embedded Documents

The following examples query the `name` embedded field in the `bios collection <bios-example-collection>`.

Query Exact Matches on Embedded Documents `````````````````````````````````````````

The following operation returns documents in the `bios collection </reference/bios-example-collection>` where the embedded document `name` is exactly `{ first: "Yukihiro", last: "Matsumoto" }`, including the order:

```javascript
db.bios.find(
    { name: { first: "Yukihiro", last: "Matsumoto" } }
)
```

The `name` field must match the embedded document exactly. The query does **not** match documents with the following `name` fields:

```javascript
{
   first: "Yukihiro",
   aka: "Matz",
   last: "Matsumoto"
}

{
   last: "Matsumoto",
   first: "Yukihiro"
}
```

Query Fields of an Embedded Document ````````````````````````````````````

The following operation returns documents in the `bios collection </reference/bios-example-collection>` where the embedded document `name` contains a field `first` with the value `"Yukihiro"` and a field `last` with the value `"Matsumoto"`. The query uses `dot notation` to access fields in an embedded document:

```javascript
db.bios.find(
   {
     "name.first": "Yukihiro",
     "name.last": "Matsumoto"
   }
)
```

The query matches the document where the `name` field contains an embedded document with the field `first` with the value `"Yukihiro"` and a field `last` with the value `"Matsumoto"`. For instance, the query would match documents with `name` fields that held either of the following values:

```javascript
{
  first: "Yukihiro",
  aka: "Matz",
  last: "Matsumoto"
}

{
  last: "Matsumoto",
  first: "Yukihiro"
}
```

### Query Arrays

Query for an Array Element ``````````````````````````

The following examples query the `contribs` array in the `bios collection </reference/bios-example-collection>`.

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection>` where the array field `contribs` contains the element `"UNIX"`:

```javascript
  db.bios.find( { contribs: "UNIX" } )
```

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection>` where the array field `contribs` contains the element `"ALGOL"` or `"Lisp"`:

```javascript
  db.bios.find( { contribs: { $in: [ "ALGOL", "Lisp" ]} } )
```

- The following operation use the :query:`$all` query operator to
return documents in the `bios collection </reference/bios-example-collection>` where the array field `contribs` contains both the elements `"ALGOL"` and `"Lisp"`:

```javascript
  db.bios.find( { contribs: { $all: [ "ALGOL", "Lisp" ] } } )

For more examples, see :query:`$all`.  See also :query:`$elemMatch`.
```

- The following operation uses the :query:`$size` operator to return
documents in the `bios collection </reference/bios-example-collection>` where the array size of `contribs` is 4:

```javascript
  db.bios.find( { contribs: { $size: 4 } } )
```

Query an Array of Documents ```````````````````````````

The following examples query the `awards` array in the `bios collection </reference/bios-example-collection>`.

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection>` where the `awards` array contains an element with `award` field equals `"Turing Award"`:

```javascript
  db.bios.find(
     { "awards.award": "Turing Award" }
  )
```

- The following operation returns documents in the :doc:`bios
collection </reference/bios-example-collection>` where the `awards` array contains at least one element with both the `award` field equals `"Turing Award"` and the `year` field greater than 1980:

```javascript
  db.bios.find(
     { awards: { $elemMatch: { award: "Turing Award", year: { $gt: 1980 } } } }
  )

Use the :query:`$elemMatch` operator to specify multiple criteria on
an array element.
```

For more information and examples of querying an array, see:

- `/tutorial/query-arrays`
- `/tutorial/query-array-of-documents`
For a list of array specific query operators, see `operator-query-array`.

### Query for BSON Regular Expressions

To find documents that contain BSON regular expressions as values, call `find()` with the `bsonRegExp` option set to `true`. The `bsonRegExp` option allows you to return regular expressions that can't be represented as JavaScript regular expressions.

The following operation returns documents in a collection named `testbson` where the value of a field named `foo` is a `BSONRegExp` type:

### Projections

The `projection <find-projection> parameter specifies which fields to return. The parameter contains either include or exclude specifications, not both, unless the exclude is for the id` field.

> **Note:** Unless the `_id` field is explicitly excluded in the projection
document `_id: 0, the id` field is returned.

Specify the Fields to Return ````````````````````````````

The following operation finds all documents in the `bios collection </reference/bios-example-collection>` and returns only the `name` field, `contribs field and id` field:

```javascript
db.bios.find( { }, { name: 1, contribs: 1 } )
```

Explicitly Excluded Fields ``````````````````````````

The following operation queries the `bios collection </reference/bios-example-collection>` and returns all fields except the `first` field in the `name` embedded document and the `birth` field:

```javascript
db.bios.find(
   { contribs: 'OOP' },
   { 'name.first': 0, birth: 0 }
)
```

Explicitly Exclude the `_id` Field ````````````````````````````````````

> **Note:** Unless the `_id` field is explicitly excluded in the projection
document `_id: 0, the id` field is returned.

The following operation finds documents in the `bios collection </reference/bios-example-collection>` and returns only the `name` field and the `contribs` field:

```javascript
db.bios.find(
   { },
   { name: 1, contribs: 1, _id: 0 }
)
```

On Arrays and Embedded Documents ````````````````````````````````

The following operation queries the `bios collection </reference/bios-example-collection>` and returns the `last` field in the `name` embedded document and the first two elements in the `contribs` array:

```javascript
db.bios.find(
   { },
   { _id: 0, 'name.last': 1, contribs: { $slice: 2 } } )
```

You can also specify embedded fields using the nested form. For example:

```javascript
db.bios.find(
   { },
   { _id: 0, name: { last: 1 }, contribs: { $slice: 2 } }
)
```

Use Aggregation Expression ``````````````````````````

The `find()` projection can accept `aggregation expressions and syntax <aggregation-expressions>`.

With the use of aggregation expressions and syntax, you can project new fields or project existing fields with new values. For example, the following operation uses aggregation expressions to override the value of the `name` and `awards` fields as well as to include new fields `reportDate`, `reportBy`, and `reportNumber`.

```javascript
db.bios.find(
   { },
   {
     _id: 0,
     name: { 
        $concat: [ 
           { $ifNull: [ "$name.aka", "$name.first" ] },
           " ",
           "$name.last"
        ]
     },
     birth: 1,
     contribs: 1,
     awards: { $cond: { if: { $isArray: "$awards" }, then: { $size: "$awards" }, else: 0 } },
     reportDate: { $dateToString: {  date: new Date(), format: "%Y-%m-%d" } },
     reportBy: "hellouser123",
     reportNumber: { $literal: 1 }
   }
)
```

To set the `reportRun` field to the value `1` The operation returns the following documents:

```javascript
{ "birth" : ISODate("1924-12-03T05:00:00Z"), "contribs" : [ "Fortran", "ALGOL", "Backus-Naur Form", "FP" ], "name" : "John Backus", "awards" : 4, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1927-09-04T04:00:00Z"), "contribs" : [ "Lisp", "Artificial Intelligence", "ALGOL" ], "name" : "John McCarthy", "awards" : 3, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1906-12-09T05:00:00Z"), "contribs" : [ "UNIVAC", "compiler", "FLOW-MATIC", "COBOL" ], "name" : "Grace Hopper", "awards" : 4, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1926-08-27T04:00:00Z"), "contribs" : [ "OOP", "Simula" ], "name" : "Kristen Nygaard", "awards" : 3, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1931-10-12T04:00:00Z"), "contribs" : [ "OOP", "Simula" ], "name" : "Ole-Johan Dahl", "awards" : 3, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1956-01-31T05:00:00Z"), "contribs" : [ "Python" ], "name" : "Guido van Rossum", "awards" : 2, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1941-09-09T04:00:00Z"), "contribs" : [ "UNIX", "C" ], "name" : "Dennis Ritchie", "awards" : 3, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1965-04-14T04:00:00Z"), "contribs" : [ "Ruby" ], "name" : "Matz Matsumoto", "awards" : 1, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "birth" : ISODate("1955-05-19T04:00:00Z"), "contribs" : [ "Java" ], "name" : "James Gosling", "awards" : 2, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
{ "contribs" : [ "Scala" ], "name" : "Martin Odersky", "awards" : 0, "reportDate" : "2020-06-05", "reportBy" : "hellouser123", "reportNumber" : 1 }
```

### Iterate the Returned Cursor

The `find()` method returns a `cursor <cursors>` to the results.

In :binary:`~bin.mongosh`, if the returned cursor is not assigned to a variable using the `var` keyword, the cursor is automatically iterated to access up to the first 20 documents that match the query. You can update the `displayBatchSize` variable to change the number of automatically iterated documents.

The following example sets the batch size to 3. Future `find()` operations will only return 3 documents per cursor iteration.

```javascript
config.set( "displayBatchSize", 3 )
```

To manually iterate over the results, assign the returned cursor to a variable with the `var` keyword, as shown in the following sections.

With Variable Name ``````````````````

The following example uses the variable `myCursor` to iterate over the cursor and print the matching documents:

```javascript
var myCursor = db.bios.find( );

myCursor
```

With `next()` Method ``````````````````````

The following example uses the cursor method :method:`~cursor.next()` to access the documents:

```javascript
var myCursor = db.bios.find( );

var myDocument = myCursor.hasNext() ? myCursor.next() : null;

if (myDocument) {
    var myName = myDocument.name;
    print (tojson(myName));
}
```

To print, you can also use the `printjson()` method instead of `print(tojson())`:

```javascript
if (myDocument) {
   var myName = myDocument.name;
   printjson(myName);
}
```

With `forEach()` Method `````````````````````````

The following example uses the cursor method :method:`~cursor.forEach()` to iterate the cursor and access the documents:

```javascript
var myCursor = db.bios.find( );

myCursor.forEach(printjson);
```

### Modify the Cursor Behavior

:binary:`~bin.mongosh` and the :driver:`drivers </>` provide several cursor methods that call on the cursor returned by `find()` to modify its behavior.

Order Documents in the Result Set `````````````````````````````````

The :method:`~cursor.sort()` method orders the documents in the result set. The following operation returns documents in the `bios collection </reference/bios-example-collection>` sorted in ascending order by the `name` field:

```javascript
db.bios.find().sort( { name: 1 } )
```

:method:`~cursor.sort()` corresponds to the `ORDER BY` statement in SQL.

Limit the Number of Documents to Return ```````````````````````````````````````

The :method:`~cursor.limit()` method limits the number of documents in the result set. The following operation returns at most `5` documents in the `bios collection <bios-example-collection>`:

```javascript
db.bios.find().limit( 5 )
```

:method:`~cursor.limit()` corresponds to the `LIMIT` statement in SQL.

Set the Starting Point of the Result Set ````````````````````````````````````````

The :method:`~cursor.skip()` method controls the starting point of the results set. The following operation skips the first `5` documents in the `bios collection <bios-example-collection>` and returns all remaining documents:

```javascript
db.bios.find().skip( 5 )
```

Specify Collation `````````````````

.. include:: /includes/extracts/collation-description.rst

The :method:`~cursor.collation()` method specifies the `collation <collation>` for the `find()` operation.

```javascript
db.bios.find( { "name.last": "hopper" } ).collation( { locale: "en_US", strength: 1 } )
```

Combine Cursor Methods ``````````````````````

The following statements chain cursor methods :method:`~cursor.limit()` and :method:`~cursor.sort()`:

```javascript
db.bios.find().sort( { name: 1 } ).limit( 5 )
db.bios.find().limit( 5 ).sort( { name: 1 } )
```

The two statements are equivalent; i.e. the order in which you chain the :method:`~cursor.limit()` and the :method:`~cursor.sort()` methods is not significant. Both statements return the first five documents, as determined by the ascending sort order on 'name'.

Available `mongosh` Cursor Methods ````````````````````````````````````

### Use Variables in `let` Option

You can specify query options to modify query behavior and indicate how results are returned.

For example, to define variables that you can access elsewhere in the `find` method, use the `let` option. To filter results using a variable, you must access the variable within the :query:`$expr` operator.

.. include:: /includes/let-example-create-flavors.rst

The following example defines a `targetFlavor` variable in `let` and uses the variable to retrieve the chocolate cake flavor:

```javascript
db.cakeFlavors.find(
   { $expr: { $eq: [ "$flavor", "$$targetFlavor" ] } },
   { _id: 0 },
   { let : { targetFlavor: "chocolate" }
} )
```

Output:

```javascript
[ { flavor: 'chocolate' } ]
```

### Retrieve Documents for Roles Granted to the Current User

.. include:: /includes/user-roles-system-variable-introduction.rst

Perform the following steps to retrieve the documents accessible to `John`:

Perform the following steps to retrieve the documents accessible to `Jane`:

### Modify a Query with options

The following examples show how you can use the `options` field in a `find()` query. Use the following `insertMany()` to setup the `users` collection:

```javascript
db.users.insertMany( [
   { username: "david", age: 27 },
   { username: "amanda", age: 25 },
   { username: "rajiv", age: 32 },
   { username: "rajiv", age: 90 }
] )
```

limit with options ``````````````````

The following query limits the number of documents in the result set with the `limit` options parameter:

```javascript
db.users.find(
   { username : "rajiv"}, // query
   { age : 1 }, // projection
   { limit : 1 } // options
)
```

allowDiskUse with options `````````````````````````

The following query uses the `options` parameter to enable `allowDiskUse`:

```javascript
db.users.find(
   { username : "david" },
   { age : 1 },
   { allowDiskUse : true }
)
```

explain with options ````````````````````

The following query uses the `options` parameter to get the `executionStats` explain output:

```javascript
var cursor = db.users.find(
   { username: "amanda" },
   { age : 1 },
   { explain : "executionStats" }
)
cursor.next()
```

Specify Multiple options in a query ```````````````````````````````````

The following query uses multiple `options` in a single query. This query uses `limit` set to `2` to return only two documents, and `showRecordId` set to `true` to return the position of the document in the result set:

```javascript
db.users.find(
   {},
   { username: 1, age: 1 },
   {
     limit: 2, 
     showRecordId: true
   }
)
```

## Learn More

- :method:`~db.collection.findOne()`
- :method:`~db.collection.findAndModify()`
- :method:`~db.collection.findOneAndDelete()`
- :method:`~db.collection.findOneAndReplace()`
