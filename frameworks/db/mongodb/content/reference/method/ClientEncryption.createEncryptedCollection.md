---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/ClientEncryption.createEncryptedCollection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================================

# ClientEncryption.createEncryptedCollection() (mongosh method)

.. versionadded:: 7.0

> **Tip:** In :binary:`mongosh`, you can use the helper
:method:`db.createEncryptedCollection()`, which runs in the context
of the current database and automatically generates data keys when
`keyId` values are not specified.

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`ClientEncryption.createEncryptedCollection` has the following syntax:

```javascript
clientEncryption = db.getMongo().getClientEncryption()

clientEncryption.createEncryptedCollection(
  dbName,
  collName,
  {
    provider: kmsProviderName,
    createCollectionOptions: encryptedFieldsMap,
    masterKey: customerMasterKeyCredentials
  }
)
```

## Command Fields

`createEncryptedCollection` takes these fields:

## Behavior

.. include:: /includes/create-an-encrypted-db-conn.rst

## Example

The following example uses a locally managed KMS for the Queryable Encryption configuration.

## Learn More

- For complete documentation on initiating MongoDB connections with
client-side field level encryption enabled, see :method:`Mongo()`.

- For a complete example of how to create and query an encrypted
collection, see `qe-quick-start`.
