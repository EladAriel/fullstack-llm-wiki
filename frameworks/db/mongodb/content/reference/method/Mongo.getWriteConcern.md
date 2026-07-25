---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.getWriteConcern.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# Mongo.getWriteConcern() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command takes the following form:

```javascript
db.getMongo().getWriteConcern()
```

This operation returns a document with the following values:

```javascript
{ w: <value>, wtimeout: <number>, j: <boolean> }
```

The fields are:

## Example

To return the current write concern, enter the following:

```javascript
db.getMongo().getWriteConcern()
```

When a write concern is specified using :method:`Mongo.setWriteConcern()`, the output of `Mongo.getWriteConcern()` is similar to:

```javascript
WriteConcern { w: 2, wtimeout: 1000, j: true }
```

The `Mongo.getWriteConcern()` command returns an empty line if no write concern has been specified.

> **Seealso:** - :method:`~Mongo.setWriteConcern()`
