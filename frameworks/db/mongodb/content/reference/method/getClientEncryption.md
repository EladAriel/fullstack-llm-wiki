---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/getClientEncryption.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

======================================

# getClientEncryption() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

`getClientEncryption()` has the following syntax:

```javascript
db.getMongo().getClientEncryption();
```

Use the `ClientEncryption` object to access the following explicit encryption methods:

- :method:`~ClientEncryption.createEncryptedCollection()`
- :method:`~ClientEncryption.encrypt()`
- :method:`~ClientEncryption.decrypt()`
## Behavior

### Enable Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

.. include:: /includes/extracts/csfle-keyvault-unique-index.rst

The following example uses a locally managed KMS for the client-side field level encryption configuration.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Use the :method:`getClientEncryption()` method to retrieve the client encryption object:

```javascript
clientEncryption = encryptedClient.getClientEncryption()
```

## Learn More

For complete documentation on initiating MongoDB connections with client-side field level encryption enabled, see :method:`Mongo()`.
