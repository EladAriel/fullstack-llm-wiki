---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/BulkWriteResult.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==================================

# BulkWriteResult() (mongosh method)

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Properties

`BulkWriteResult` has the following properties:

## writeErrors Exception

If there is a write error while processing the bulk write, `mongosh` raises an exception that contains a `writeErrors` property with the following fields:

## writeConcernError Exception

If there is a write concern error while processing the bulk write, `mongosh` raises an exception that contains a `writeConcernError` property with the following fields:
