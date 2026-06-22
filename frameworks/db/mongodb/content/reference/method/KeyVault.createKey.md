---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.createKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=====================================

# KeyVault.createKey() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

:method:`~KeyVault.createKey()` has the following syntax:

```javascript
keyVault = db.getMongo().getKeyVault()

keyVault.createKey(
 keyManagementService,
 customerMasterKey,
 [ "keyAltName" ]
)
```

## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example is intended for rapid evaluation of client-side field level encryption. For specific examples of using :method:`KeyVault.createKey()` with each supported :abbr:`KMS (Key Management Service)` provider, see `Create a Data Key <qe-field-level-encryption-data-key-create>`.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`keyVault <getKeyVault()>` object and use the :method:`KeyVault.createKey()` method to create a new data encryption key using the locally managed key:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.createKey("local", ["data-encryption-key"])
```

If successful, :method:`~KeyVault.createKey()` returns the `UUID` of the new data encryption key. To retrieve the new data encryption key document from the key vault, either:

- Use :method:`~KeyVault.getKey()` to retrieve the created key by
`UUID`.

-or-

- Use :method:`~KeyVault.getKeyByAltName()` to retrieve the key by its
alternate name.
