---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.explain.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================

# cursor.explain() (mongosh method)

## Definition

> **Note:** `cursor.explain()` defaults to `queryPlanner`, unlike
the :dbcommand:`explain` command, which defaults to
`allPlansExecution`.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/explain-required-access.rst

## Behavior

.. include:: includes/explain-ignores-cache-plan.rst

### Verbosity Modes

The behavior of :method:`cursor.explain()` and the amount of information returned depend on the `verbosity` mode.

`queryPlanner` Mode ``````````````````````

By default, :method:`cursor.explain()` runs in `queryPlanner` verbosity mode.

.. include:: /includes/fact-explain-verbosity-queryPlanner.rst

`executionStats` Mode ```````````````````````

.. include:: /includes/fact-explain-verbosity-executionStats.rst

.. include:: /includes/fact-explain-verbosity-executionStats.rst

`allPlansExecution` Mode ``````````````````````````

.. include:: /includes/fact-explain-verbosity-allPlansExecution.rst

.. include:: /includes/fact-explain-verbosity-allPlansExecution.rst

### `db.collection.explain().find()`

.. include:: /includes/fact-explain-methods-differences.rst

See :method:`db.collection.explain()` for more information.

### Sharded Clusters

.. versionadded:: 8.3

If you run `cursor.explain()` against a database that does not exist on a sharded cluster, the execution stage reaches the end-of-stream and the operation does not create the database. For more information on end-of-stream execution stats, see `explain.executionStats.executionStages.isEOF`.

## Output

.. include:: /includes/fact-explain-results-categories.rst

For details on the output, see `/reference/explain-results`.

## Example

The following example runs :method:`cursor.explain()` in `"executionStats" <explain-method-executionStats>` verbosity mode to return the query planning and execution information for the specified :method:`db.collection.find()` operation:

```javascript
db.products.find(
   { quantity: { $gt: 50 }, category: "apparel" }
).explain("executionStats")
```
