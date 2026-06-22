---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/limit.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# $limit (aggregation stage)

## Definition

## Compatibility

.. include:: /includes/fact-compatibility.rst

## Syntax

The :pipeline:`$limit` stage has the following prototype form:

```javascript
{ $limit: <positive 64-bit integer> }
```

:pipeline:`$limit` takes a positive integer that specifies the maximum number of documents to pass along.

> **Note:** The :pipeline:`$limit` pipeline aggregation has a 64-bit integer
limit. MongoDB returns an invalid argument error when values exceed
this limit.

## Behavior

### Using $limit with Sorted Results

If using the :pipeline:`$limit` stage with any of:

- the :pipeline:`$sort` aggregation stage,
- the :method:`~cursor.sort()` method, or
- the `sort` field to the :dbcommand:`findAndModify` command or the
:method:`~db.collection.findAndModify()` shell method,

be sure to include at least one field in your sort that contains unique values, before passing results to the :pipeline:`$limit` stage.

Sorting on fields that contain duplicate values may return an inconsistent sort order for those duplicate fields over multiple executions, especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the `_id` field in your sort query.

See the following for more information on each:

- :ref:`Consistent sorting with $sort (aggregation)
<sort-aggregation-consistent-sorting>`

- :ref:`Consistent sorting with the sort() shell method
<sort-cursor-consistent-sorting>`

- :ref:`Consistent sorting with the findAndModify command
<findandmodify-command-consistent-sorting>`

- :ref:`Consistent sorting with the findAndModify() shell method
<findandmodify-method-consistent-sorting>`

## Examples

> **Note:** .. include:: /includes/fact-agg-sort-limit.rst

## Learn More

To learn how to use :pipeline:`$limit` in a full example, see the `agg-example-filter-data` tutorial.
