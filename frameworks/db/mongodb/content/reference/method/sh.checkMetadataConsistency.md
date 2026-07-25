---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.checkMetadataConsistency.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================================

# sh.checkMetadataConsistency() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/method/checkMetadataConsistency-execute-mongos.rst

## Syntax

The :method:`sh.checkMetadataConsistency` method has the following syntax:

```javascript
sh.checkMetadataConsistency( { <options> } )
```

The `options` document can take the following fields and values:

.. include:: /includes/inconsistency-type/checkMetadataConsistency-options.rst

## Example
