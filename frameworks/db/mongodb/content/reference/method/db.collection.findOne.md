---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.findOne.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# db.collection.findOne() (mongosh method)

.. include:: includes/wayfinding/mongosh-method-findOne.rst

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.collection.findOne()` has the following form:

```javascript
db.collection.findOne( <query>, <projection>, <options> )
```

`db.collection.findOne()` takes the following parameters:

## Behavior

### Client Disconnection

.. include:: /includes/extracts/4.2-changes-disconnect.rst

### Projection

> **Important:** As part of making :method:`~db.collection.find` and
:method:`~db.collection.findAndModify` projection consistent with
aggregation's :pipeline:`$project` stage:
- The :method:`~db.collection.find` and
  :method:`~db.collection.findAndModify` projection can accept
  :ref:`aggregation expressions and syntax
  <aggregation-expressions>`.
- MongoDB enforces additional restrictions with regards to
  projections. See :limit:`Projection Restrictions` for details.

The `projection` parameter determines which fields are returned in the matching documents. The `projection` parameter takes a document of the following form:

```javascript
{ field1: <value>, field2: <value> ... }
```

.. include:: /includes/extracts/projection-values-table.rst

> **Note:** .. include:: /includes/find-projection-arg-option-diff.rst

Embedded Field Specification ````````````````````````````

.. include:: /includes/extracts/projection-embedded-field-format.rst

`_id` Field Projection ````````````````````````

.. include:: /includes/extracts/projection-id-field.rst

Inclusion or Exclusion ``````````````````````

.. include:: /includes/extracts/projection-inclusion-exclusion.rst

## Examples

.. include:: /includes/sample-data-usage.rst

### With Empty Query Specification

The following operation returns a single document from the `movies` collection in the `sample_mflix` database:

### With a Query Specification

The following operation returns the first matching document from the `movies` collection where either the `title` field starts with the letter "T" **or** the `year` field is less than 1950:

### With a Projection

The `projection parameter specifies which fields to return. The parameter contains either include or exclude specifications, not both, unless the exclude is for the id` field.

Specify the Fields to Return ````````````````````````````

The following operation finds a document in the `movies` collection and returns only the `title`, `genres`, and `imdb` fields:

Return All but the Excluded Fields ``````````````````````````````````

The following operation returns a document in the `movies` collection where the `cast` array contains `"Al Pacino". The projection returns all fields except the id` field, the `votes` field in the `imdb` embedded document, and the `fullplot` field:

### With an Option

The following operation uses the `sort` option to return the first matching document from the sorted `movies` collection. In this example, the collection is sorted by `year` in ascending order.

### The `findOne` Result Document

You cannot apply cursor methods to the result of `findOne()` because a single document is returned. You have access to the document directly:

### Use Variables in `let` Option

You can specify query options to modify query behavior and indicate how results are returned.

For example, to define variables that you can access elsewhere in the `findOne` method, use the `let` option. To filter results using a variable, you must access the variable within the :query:`$expr` operator.

The following example defines a `targetTitle` variable in `let` and uses the variable to retrieve the movie titled `"The Godfather"`:
