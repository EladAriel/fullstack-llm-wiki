---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/currentOp.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# $currentOp (Aggregation Stage)

## Definition

> **Note:** .. include:: /includes/fact-currentOp-aggregation-stage.rst

### Syntax

```javascript
{ $currentOp: { allUsers: <boolean>, idleConnections: <boolean>, idleCursors: <boolean>, idleSessions: <boolean>, localOps: <boolean> } }
```

`$currentOp` takes an options document as its operand:

Omitting any of the above parameters will cause $currentOp to use that parameter's default value. Specify an empty document, as shown below, to use the default values of all parameters.

```javascript
{ $currentOp: { } }
```

## Constraints

### Pipeline

- `$currentOp` must be the first stage in the pipeline.
- Pipelines that start with `$currentOp` can only be run on
the `admin` database.

### Access Control

- For standalone and replica sets that enforce access control,
:authaction:`inprog` privilege is required to run `$currentOp` if `allUsers: true <currentOp-stage-allUsers>`.

- For sharded clusters that enforce access control, the :authaction:`inprog`
privilege is required to run `$currentOp`.

### Transactions

- `$currentOp` is not allowed in :ref:`transactions
<transactions>`.

### Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, `$currentOp` output redacts certain information:

- The output omits all fields after `"command"`.
- The output redacts `"command"` to include only the first element,
`$comment`, and `$db`.

## Examples

## Output Fields

Each output document may contain a subset of the following fields, as relevant for the operation:
