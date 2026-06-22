---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/enable-qe.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================================================

# Enabling {+qe+} when Creating Collections

## Overview

.. include:: /includes/queryable-encryption/qe-enable-qe-at-collection-creation.rst

.. include:: /includes/queryable-encryption/qe-explicitly-create-collection.rst

## Enable {+qe+} on a Collection

You can enable {+qe+} on fields in one of two ways. The following examples use Node.js to enable {+qe+}:

- Pass the {+enc-schema+}, represented by the `encryptedFieldsObject`
constant, to the client that the application uses to create the collection:

```javascript
   const client = new MongoClient(uri, {
      autoEncryption: {
         keyVaultNameSpace: "<your keyvault namespace>",
         kmsProviders: "<your kms provider>",
         extraOptions: {
            cryptSharedLibPath: "<path to {+shared-library+}>"
         },
         encryptedFieldsMap: {
            "<databaseName.collectionName>": { encryptedFieldsObject }
         }
      }

      ...

      await client.db("<database name>").createEncryptedCollection("<collection name>");
   }

For more information on ``autoEncryption`` configuration options, see the
section on :ref:`qe-reference-mongo-client`.
```

- Pass the {+enc-schema+} `encryptedFieldsObject` to
`createEncryptedCollection()`:

```javascript
   await encryptedDB.createEncryptedCollection("<collection name>", {
      encryptedFields: encryptedFieldsObject
   });

.. tip::

   Specify the ``encryptedFieldsObject`` when you create the
   collection, and also when you create a client to access the 
   collection. For more information about the security considerations of not
   defining the ``encryptedFieldsObject``, see :ref:`Security Considerations
   <qe-csfle-security-considerations>`.
```
