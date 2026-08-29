---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.showRecordId.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.907912Z"
---
# cursor.showRecordId() (mongosh method)

**meta:** :description: Append the `$recordId` field to documents returned by a query using `cursor.showRecordId()` in `mongosh`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** cursor.showRecordId()

   .. include:: /includes/fact-mongosh-shell-method.rst

   Appends the ``$recordId`` field to documents returned by a query.
   ``$recordId`` is the internal key that uniquely identifies a document
   in a collection. ``$recordId`` format:

   .. code-block:: javascript
      :copyable: false

      '$recordId': Long(<int>)

   :returns: A modified cursor object that contains the document fields
             and the appended ``$recordId`` field.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Example

**include:** /includes/example-showRecordId.rst