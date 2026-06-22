---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/getKeyVault.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# getKeyVault() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

:method:`getKeyVault()` has the following syntax:

```javascript
keyVault = db.getMongo().getKeyVault();
```

Use the `KeyVault` object to access the following data encryption key management methods:

- :method:`~KeyVault.getKey`
- :method:`~KeyVault.getKeys`
- :method:`~KeyVault.getKeyByAltName`
- :method:`~KeyVault.createKey`
- :method:`~KeyVault.addKeyAlternateName`
- :method:`~KeyVault.removeKeyAlternateName`
- :method:`~KeyVault.deleteKey`
## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

The following example uses a `locally managed key <qe-fundamentals-kms-providers-local>` for the client-side field level encryption configuration.

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

### Unique Partial Index on Key Vault

.. include:: /includes/extracts/csfle-keyvault-unique-index.rst

## Example

The following example uses a `locally managed key <qe-fundamentals-kms-providers-local>` for the client-side field level encryption configuration.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Use the :method:`getKeyVault()` method to retrieve the key vault object:

```javascript
keyVault = encryptedClient.getKeyVault()
```

For complete documentation on initiating MongoDB connections with client-side field level encryption enabled, see :method:`Mongo()`.
