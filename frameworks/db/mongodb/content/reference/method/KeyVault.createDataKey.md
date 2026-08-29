---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.createDataKey.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.905598Z"
---
.. _keyvault-createdatakey-method:

# KeyVault.createDataKey() (mongosh method)

**meta:** :description: Add a data encryption key to the key vault for client-side field level encryption using `KeyVault.createDataKey()`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** KeyVault.createDataKey(keyManagementService, customerMasterKey, ["keyAltName"])

   Adds a data encryption key to the key vault associated to the
   database connection. :ref:`{+csfle+}
   <csfle-guide-intro>` uses data encryption keys
   for supporting encryption and decryption of field values.

   This method is an alias for
   :method:`~KeyVault.createKey()`.


## Compatibility

This command is available in deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst


**seealso:** :method:`~KeyVault.createKey()`.