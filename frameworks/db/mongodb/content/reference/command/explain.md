---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/explain.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# explain (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Required Access

.. include:: /includes/explain-required-access.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     explain: <command>,
     verbosity: <string>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

### Verbosity Modes

The behavior of :dbcommand:`explain` and the amount of information returned depend on the `verbosity` mode.

### Explain and Write Operations

For write operations, the :dbcommand:`explain` command returns information about the write operation that would be performed but does not actually modify the database.

### Stable API

The `Stable API <stable-api>` V1 supports the following verbosity modes for the `explain` command:

- `allPlansExecution <ex-allPlansExecution>`
- `executionStats <ex-executionStats>`
- `queryPlanner<ex-queryPlanner>`
> **Warning:** .. include:: /includes/fact-stable-api-explain.rst

### Restrictions

.. include:: /includes/extracts/4.2-changes-agg-out-explain.rst

## Output

.. include:: /includes/fact-explain-results-categories.rst

For details on the output, see `/reference/explain-results`.

## Examples

### `queryPlanner` Mode

The following :dbcommand:`explain` command runs in `"queryPlanner"` verbosity mode to return the query planning information for a :dbcommand:`count` command:

```javascript
db.runCommand(
   {
     explain: { count: "products", query: { quantity: { $gt: 50 } } },
     verbosity: "queryPlanner"
   }
)
```

### `executionStats` Mode

The following :dbcommand:`explain` operation runs in `"executionStats"` verbosity mode to return the query planning and execution information for a :dbcommand:`count` command:

```javascript
db.runCommand(
   {
      explain: { count: "products", query: { quantity: { $gt: 50 } } },
      verbosity: "executionStats"
   }
)
```

### `allPlansExecution` Mode

By default, :dbcommand:`explain` runs in `"allPlansExecution"` verbosity mode. The following :dbcommand:`explain` command returns the `explain.queryPlanner` and `explain.executionStats` for all considered plans for an :dbcommand:`update` command:

> **Note:** The execution of this explain will not modify data but runs the
query predicate of the update operation. For candidate plans,
MongoDB returns the execution information captured during the
`plan selection phase <query-plans-query-optimization>`.

```javascript
db.runCommand(
   {
     explain: {
        update: "products",
        updates: [
           {
               q: { quantity: 1057, category: "apparel" },
               u: { $set: { reorder: true } }
           }
        ]
     }
   }
)
```
