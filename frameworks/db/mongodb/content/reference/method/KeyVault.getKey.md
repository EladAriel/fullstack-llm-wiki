---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/KeyVault.getKey.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# KeyVault.getKey() (mongosh method)

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

:method:`~KeyVault.getKey()` has the following syntax:

```none
keyVault = db.getMongo().getKeyVault()

keyVault.getKey(UUID("<UUID String>"))
```

The :abbr:`UUID (Universally unique identifier)` is a BSON :bsontype:`binary data <Binary>` object with subtype `4`.

## Behavior

### Requires Configuring Client-Side Field Level Encryption on Database Connection

.. include:: /includes/extracts/csfle-requires-enabling-encryption.rst

## Example

The following example uses a `locally managed KMS <qe-fundamentals-kms-providers-local>` for the client-side field level encryption configuration.

.. include:: /includes/csfle-connection-boilerplate-example.rst

Retrieve the :method:`keyVault <getKeyVault()>` object and use the :method:`KeyVault.getKey()` to retrieve a data encryption key using its `UUID`:

```javascript
keyVault = encryptedClient.getKeyVault()
keyVault.getKey(UUID("b4b41b33-5c97-412e-a02b-743498346079"))
```

:method:`~KeyVault.getKey()` returns the data encryption key, with output similar to the following:

```json
{
  "_id" : UUID("b4b41b33-5c97-412e-a02b-743498346079"),
  "keyMaterial" : BinData(0,"E+0jZKzA4YuE1lGmSVIy2mivqH4JxFo0yFATdxYX/s0YtMFsgVXyu7Bbn4IQ2gn7F/9JAPJFOxdQc5lN3AR+oX33ewVZsd63f3DN1zzcukqdR2Y+EeO7ekRxyRjdzMaNNrBNIv9Gn5LEJgWPSYkG8VczF7cNZnc1YmnR0tuDPNYfm0J7dCZuZUNWW3FCGRcdFx6AlXiCtXKNR97hJ216pQ=="),
  "creationDate" : ISODate("2021-03-16T18:22:43.733Z"),
  "updateDate" : ISODate("2021-03-16T18:22:43.733Z"),
  "status" : 0, "version" : Long(0),
  "masterKey" : {
    "provider" : "local"
  },
  "keyAltNames" : [
     "alpha"
  ]
}
```
