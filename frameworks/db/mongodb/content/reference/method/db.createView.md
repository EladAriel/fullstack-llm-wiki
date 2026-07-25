---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.createView.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

================================

# db.createView() (mongosh method)

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.createView` has the following syntax:

```javascript
db.createView(<view>, <source>, <pipeline>, <collation>)
```

The method has the following parameters:

The `db.createView()` method wraps the following :dbcommand:`create` command operation:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline>, collation: <collation> } )
```

> **Important:** Operations that list collections, such as
:method:`db.getCollectionInfos()` and :method:`db.getCollectionNames()`,
include views in their outputs.
.. include:: /includes/extracts/views-public-definition.rst

## Examples

To see examples of creating a view, see the following pages:

- `manual-views-create`
- `manual-views-lookup`
- `manual-views-collation`
## Behavior

To see behavioral details of views, see `manual-views-behavior`.
