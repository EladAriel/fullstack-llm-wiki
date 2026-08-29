---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.removeKeyAltName.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.983774Z"
---
.. _keyvault-removekeyaltname-method:

# KeyVault.removeKeyAltName() (mongosh method)

**meta:** :description: Remove a specified key alternate name from a data encryption key using `KeyVault.removeKeyAltName(UUID, keyAltName)`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** KeyVault.removeKeyAltName(UUID, keyAltName)

   Removes the specified ``keyAltName`` from the data encryption key
   with the specified ``UUID``. The data encryption key must exist in
   the key vault associated with the database connection.

   This method is an alias for
   :method:`~KeyVault.removeKeyAlternateName()`.


## Compatibility

This command is available in deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst


**seealso:** :method:`~KeyVault.removeKeyAlternateName()`.