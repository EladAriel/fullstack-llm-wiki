---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/queryable-encryption/fundamentals/enable-qe.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.821506Z"
---
**facet:** :name: genre
   :values: tutorial

**facet:** :name: programming_language
   :values: javascript/typescript

**meta:** :keywords: queryable encryption, code example, node.js

.. _qe-fundamentals-enable-qe:

# Enabling {+qe+} when Creating Collections

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 2
   :class: singlecol

## Overview

**include:** /includes/queryable-encryption/qe-enable-qe-at-collection-creation.rst

**include:** /includes/queryable-encryption/qe-explicitly-create-collection.rst

## Enable {+qe+} on a Collection

You can enable {+qe+} on fields in one of two ways. The following
examples use Node.js to enable {+qe+}:

-  Pass the {+enc-schema+}, represented by the ``encryptedFieldsObject`` 
   constant, to the client that the application uses to create the collection:

   .. code-block:: javascript
      :emphasize-lines: 8-10

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

-  Pass the {+enc-schema+} ``encryptedFieldsObject`` to 
   ``createEncryptedCollection()``:

   .. code-block:: javascript

      await encryptedDB.createEncryptedCollection("<collection name>", {
         encryptedFields: encryptedFieldsObject
      });

   .. tip::

      Specify the ``encryptedFieldsObject`` when you create the
      collection, and also when you create a client to access the 
      collection. For more information about the security considerations of not
      defining the ``encryptedFieldsObject``, see :ref:`Security Considerations
      <qe-csfle-security-considerations>`.