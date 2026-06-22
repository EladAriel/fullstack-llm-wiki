---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/Mongo.setWriteConcern.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
