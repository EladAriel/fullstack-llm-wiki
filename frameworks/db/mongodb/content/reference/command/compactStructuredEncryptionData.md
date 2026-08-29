---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/compactStructuredEncryptionData.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.080471Z"
---
.. _compactStructuredEncyrptionData:

# compactStructuredEncryptionData (database command)

**meta:** :description: Use the `compactStructuredEncryptionData` command to compact documents in metadata collections and remove redundant entries.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** compactStructuredEncryptionData

   Compacts documents specified in the metadata collections and deletes 
   redundant documents.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst
   
## Syntax

The command has the following syntax:

.. code-block:: javascript

   db.runCommand(
     {
       compactStructuredEncryptionData: <collection>,
       compactionTokens: {
          encryptedFieldPath: bindata,
          ...
       },
     }
   )


## Command Fields

The command takes the following fields:

.. list-table::
   :header-rows: 1
   :widths: 20 20 80

   * - Field

     - Type

     - Description

   * - ``compactStructuredEncryptionData``

     - string

     - The name of the collection.

   * - ``compactionTokens``

     - document

     - A document that maps index fields to compaction tokens.
   
The :binary:`~bin.mongosh` provides a wrapper method
:method:`db.collection.compactStructuredEncryptionData()`.

## Required Access

The built-in roles :authrole:`readWriteAnyDatabase` and 
:authrole:`dbOwner` provide 
:authaction:`compactStructuredEncryptionData` actions on resources.

## Example

See :ref:`metadata collection compaction <qe-metadata-compaction>` for an example.