---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.createEncryptedCollection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=================================================

# db.createEncryptedCollection() (mongosh method)

.. versionadded:: 7.0

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`db.createEncryptedCollection()` has the following syntax:

```javascript
db.createEncryptedCollection(
   collName,
   {
      provider: kmsProviderName,
      createCollectionOptions: encryptedFieldsMap,
      masterKey: customerMasterKeyCredentials
   }
)
```

## Command Fields

`db.createEncryptedCollection()` takes these fields:

## Behavior

.. include:: /includes/create-an-encrypted-db-conn.rst

### Wrapper Behavior

.. include:: /includes/fact-db-createEncryptedCollection-behavior.rst

## Example

The following example uses a locally managed KMS for the Queryable Encryption configuration.

## Learn More

- For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see :method:`Mongo()`.

- For a complete example of how to create and query an encrypted
collection, see `qe-quick-start`.
