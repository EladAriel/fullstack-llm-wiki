---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/operator/aggregation/currentOp.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
