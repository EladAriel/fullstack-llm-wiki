---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/create-view.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================

# Create and Query a View

To create a view, use one of the following methods:

- Use :method:`db.createCollection()`
- Use :method:`db.createView()`
To create a view in the {+atlas+} UI, use the `Aggregation Pipeline Builder <atlas-ui-agg-builder>`. To learn more, see `atlas-ui-views`.

> **Important:** Operations that list collections, such as
:method:`db.getCollectionInfos()` and
:method:`db.getCollectionNames()`, include views in their outputs.
.. include:: /includes/extracts/views-public-definition.rst

## `db.createCollection()` Syntax

```javascript
db.createCollection( 
  "<viewName>", 
  {
    "viewOn" : "<source>", 
    "pipeline" : [<pipeline>],
    "collation" : { <collation> }
  }
)
```

## `db.createView()` Syntax

```javascript
db.createView(
  "<viewName>",
  "<source>",
  [<pipeline>],
  {
    "collation" : { <collation> }
  }
)
```

## Restrictions

- You must create views in the same database as the source collection.
- .. include:: /includes/extracts/views-restriction-output-to-disk.rst
- You cannot rename a view once it is created.
### Unsupported Operations

Some operations are not available with views:

- :method:`db.collection.mapReduce()`.
- :query:`$text` operator, since `$text` in
aggregation is valid only for the first stage.

- Renaming a view.
For more information, see `views-supported-operations`.

## Examples

### Populate the Collection

Create a `students` collection to use for this example:

```javascript
db.students.insertMany( [
   { sID: 22001, name: "Alex", year: 1, score: 4.0 }, 
   { sID: 21001, name: "bernie", year: 2, score: 3.7 }, 
   { sID: 20010, name: "Chris", year: 3, score: 2.5 }, 
   { sID: 22021, name: "Drew", year: 1, score: 3.2 }, 
   { sID: 17301, name: "harley", year: 6, score: 3.1 }, 
   { sID: 21022, name: "Farmer", year: 1, score: 2.2 }, 
   { sID: 20020, name: "george", year: 3, score: 2.8 },
   { sID: 18020, name: "Harley", year: 5, score: 2.8 }, 
] )
```

### Use db.createView() to Create a View

```javascript
db.createView(
   "firstYears",
   "students",
   [ { $match: { year: 1 } } ]
)
```

In the example:

- `firstYears` is the name of the new view.
- `students` is the collection the view is based on.
- :pipeline:`$match` is an aggregation expression that matches first
year students in the `students` collection.

Query the View ``````````````

```javascript
db.firstYears.find({}, { _id: 0 } )
```

The `{ _id: 0 }` `projection <method-find-projection> suppresses the id` field in the output.

```javascript
[
  { sID: 22001, name: 'Alex', year: 1, score: 4 },
  { sID: 22021, name: 'Drew', year: 1, score: 3.2 },
  { sID: 21022, name: 'Farmer', year: 1, score: 2.2 }
]
```

> **Note:** .. include:: /includes/extracts/views-unsupported-projection-operators.rst

### Use db.createCollection() to Create a View

The :method:`db.createCollection()` method allows you to create a collection or a view with specific options.

The following example creates a `graduateStudents` view. The view only contains documents selected by the :pipeline:`$match` stage. The optional `collation <collation>` setting determines the sort order.

```javascript
db.createCollection(
   "graduateStudents",
   { 
      viewOn: "students",
      pipeline: [ { $match: { year: { $gt: 4 } } } ],
      collation: { locale: "en", caseFirst: "upper" }
   }
)
```

> **Note:** .. include:: /includes/extracts/views-collation-behavior.rst

Query the View ``````````````

The following example queries the view. The :pipeline:`$unset stage removes the id` field from the output for clarity.

```javascript
db.graduateStudents.aggregate(
   [
      { $sort: { name: 1 } },
      { $unset: [ "_id" ] }
   ]
)
```

When the output is sorted, the :pipeline:`$sort` stage uses the `collation <collation>` ordering to sort uppercase letters before lowercase letters.

```javascript
[
  { sID: 18020, name: 'Harley', year: 5, score: 2.8 },
  { sID: 17301, name: 'harley', year: 6, score: 3.1 }
]
```

### Retrieve Medical Information for Roles Granted to the Current User

Starting in MongoDB 7.0, you can use the new :variable:`USER_ROLES` system variable to return user `roles <roles>`.

> **Note:** .. include:: /includes/aggregation/agg-userroles-restrictions.rst

The example in this section shows users with limited access to fields in a collection containing medical information. The example uses a view that reads the current user roles from the `USER_ROLES` system variable and hides fields based on the roles.

The example creates these users:

- `James` with a `Billing` role who can access a `creditCard`
field.

- `Michelle` with a `Provider` role who can access a
`diagnosisCode` field.

Perform the following steps to create the roles, users, collection, and view:

Perform the following steps to retrieve the information accessible to `James`:

Perform the following steps to retrieve the information accessible to `Michelle`:

### Retrieve Budget Documents for Roles Granted to the Current User

.. include:: /includes/user-roles-system-variable-introduction.rst

Perform the following steps to create a view and retrieve the documents accessible to `John`:

Perform the following steps to retrieve the documents accessible to Jane:

### Roles with the Same Name in Multiple Databases

Multiple databases can have roles with the same name. If you create a view and reference a specific role in the view, you should either specify both the `db` database name field and the `role field, or specify the id` field that contains the database name and the role.

The following example returns the roles assigned to `Jane, who has roles with different names. The example returns the id`, `role`, and `db` database name:

## Behavior

### Aggregation Optimizations

When you query a view:

- Query `filter`, `projection`, `sort`, `skip`, `limit`,
and other operations for :method:`db.collection.find()` are converted to the equivalent `aggregation pipeline stages <aggregation-pipeline-operator-reference>`.

- MongoDB appends the client query to the underlying pipeline and
returns the results of that combined pipeline to the client. MongoDB may apply `aggregation pipeline optimizations <agg-pipeline-optimization>` to the combined pipeline.

- The aggregation pipeline optimizer reshapes the view aggregation
pipeline stages to improve performance without changing the query results.

### Resource Locking

.. include:: /includes/extracts/createView-resource-lock.rst
