---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.collection.compactStructuredEncryptionData.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.926526Z"
---
.. _compactstructutedencdata-method:

# db.collection.compactStructuredEncryptionData() (mongosh method)

**meta:** :description: Use `db.collection.compactStructuredEncryptionData()` to compact encrypted data in MongoDB with automatic encryption enabled.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol


**include:** /includes/fact-mongosh-shell-method.rst

## Definition

**method:** db.collection.compactStructuredEncryptionData()

   This method provides a wrapper around the 
   :dbcommand:`compactStructuredEncryptionData` command. This method
   only works on connections that have 
   :ref:`automatic encryption <csfle-tutorial-automatic-encryption>`
   enabled.

   :returns: A failure or success object.

## Compatibility

.. |command| replace:: method

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst