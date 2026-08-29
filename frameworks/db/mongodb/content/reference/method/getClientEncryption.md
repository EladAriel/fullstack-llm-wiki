---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/getClientEncryption.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.974055Z"
---
# getClientEncryption() (mongosh method)

**meta:** :description: Access the `ClientEncryption` object for manual encryption and decryption of field values using `getClientEncryption()` in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** getClientEncryption()

   Returns the ``ClientEncryption`` object for the current database
   collection. The ``ClientEncryption`` object supports explicit
   (manual) encryption and decryption of field values for
   :ref:`Client-Side field level encryption <manual-csfle-feature>`.

   :returns:

     The ``ClientEncryption`` object for current database connection.


## Compatibility

This command is available in deployments hosted in the following
environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-onprem-only.rst


## Syntax

``getClientEncryption()`` has the following syntax:

.. code-block:: javascript

   db.getMongo().getClientEncryption();

Use the ``ClientEncryption`` object to access the following 
explicit encryption methods:

- :method:`~ClientEncryption.createEncryptedCollection()` 
- :method:`~ClientEncryption.encrypt()` 
- :method:`~ClientEncryption.decrypt()`


## Behavior

### Enable Client-Side Field Level Encryption on Database Connection

**include:** /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

**include:** /includes/extracts/csfle-keyvault-unique-index.rst

The following example uses a locally managed KMS for the client-side
field level encryption configuration.

**include:** /includes/csfle-connection-boilerplate-example.rst

Use the :method:`getClientEncryption()` method to
retrieve the client encryption object:

.. code-block:: javascript

   clientEncryption = encryptedClient.getClientEncryption()

## Learn More

For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see :method:`Mongo()`.