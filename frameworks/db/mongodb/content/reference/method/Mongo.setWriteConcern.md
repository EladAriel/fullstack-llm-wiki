---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.setWriteConcern.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

========================================

# Mongo.setWriteConcern() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command takes the following form:

```javascript
db.getMongo().setWriteConcern( { w: <value>, j: <boolean>, wtimeout: <number> } )
```

The fields are:

## Example

In the following example:

- Two :binary:`~bin.mongod` or :binary:`~bin.mongod` instances must
acknowledge writes.

- There is a `1` second timeout to wait for write acknowledgments.
```javascript
db.getMongo().setWriteConcern( { w: 2, wtimeout: 1000 } )
```

> **Seealso:** - :method:`~Mongo.getWriteConcern()`
