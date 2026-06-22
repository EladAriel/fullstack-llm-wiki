---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/csfle/fundamentals/manage-keys.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Encryption Key Management

In this guide, you can learn how to manage your encryption keys with a {+kms-long+} ({+kms-abbr+}) in your {+csfle+} ({+csfle-abbrev+})-enabled application.

## Encryption Components

MongoDB uses the following components to perform {+csfle+}:

- {+dek-long+}s ({+dek-abbr+})s
- {+cmk-long+}s ({+cmk-abbr+})s
- {+key-vault-long+}s
- {+kms-long+} ({+kms-abbr+})
To learn more about keys and key vaults, see `qe-reference-keys-key-vaults`.

## Supported Key Management Services

{+csfle+} supports the following {+kms-long+} providers:

- {+aws-long+} KMS
- {+azure-kv+}
- {+gcp-kms-abbr+}
- Any KMIP Compliant {+kms-long+}
- Local Key Provider
.. include:: /includes/reference/fact-kmip-version.rst

To learn more about these providers, including diagrams that show how your application uses them to perform {+csfle+}, see `qe-fundamentals-kms-providers`.

## Manage a {+dek-long+}'s Alternate Name

You can assign a {+dek-long+} alternate names to make the key easier to reference. Assigning alternate names allows you to perform the following actions:

- Reference a {+dek-abbr+} by different means than the `_id` field.
- Dynamically assign DEKs at runtime.
### Create a {+dek-long+} with an Alternate Name

> **Important:** Prior to adding a new key alternate name, you must create a partial
unique index on the `keyAltNames` field. This index should have a
`partialFilterExpression` for documents where `keyAltNames` exists.
{+csfle+} depends on server-enforced uniqueness of key alternate names.
To learn how to create a partial index, refer to `index-type-partial`.

The following example creates a {+dek-long+} with an alternate name. Select the tab that corresponds to your driver language:

To learn more about `dataKeyOpts` and `kmsProviders` objects, see `qe-fundamentals-kms-providers`.

### Use Key Alternate Names in an Automatic Encryption Schema

Encryption schemas contain user-specified rules that identify which fields must be encrypted and how to encrypt those fields. In your encryption rules, you can specify alternate key names name for the {+dek-long+} which encrypts your field.

You must refer to a key alternate name with a `JSON pointer`. Use JSON pointers to reference a field in your query or update document which contains the value of your key alternate name.

> **Important:** You cannot reference a {+dek-abbr+} by it's alternate name when
encrypting a field with the :ref:`deterministic encryption algorithm
<csfle-deterministic-encryption>`. To encrypt your field
deterministically, you must specify the `_id` of the key you would
like to use to encrypt your field.

Reference Key Alternate Name in an Encryption Schema ````````````````````````````````````````````````````

Consider the following encryption schema which encrypts the `salary` field:

```json
{
  "<database>.<collection>": {
    "bsonType": "object",
    "properties": {
      "salary": {
        "encrypt": {
          "bsonType": "int",
          "keyId": "/fieldWithAltName",
          "algorithm": "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
        }
      }
    }
  }
}
```

The schema's `keyId` field contains a JSON pointer to reference the `fieldWithAltName` field within the documents being encrypted.

The following document's `fieldWithAltName` value is `my-alt-name`:

```json
{
  "name": "Jon Doe",
  "salary": 45000,
  "fieldWithAltName": "my-alt-name"
}
```

The `salary` field is encrypted by the {+dek-abbr+} that has the alternate name `my-alt-name`.

Dynamically Assign Keys at Runtime ``````````````````````````````````

You can use alternate key names to dynamically set the {+dek-long+} for a field at runtime. Use this functionality to encrypt individual documents with different DEKs using the same encryption schema.

For example, consider the following documents:

```json
{
    "name": "Jon Doe",
    "salary": 45000,
    "fieldWithAltName": "my-alt-name"
},
{
    "name": "Jane Smith",
    "salary": 70000,
    "fieldWithAltName": "my-other-alt-name"
}
```

You insert the preceding documents using a {+csfle-abbrev+}-enabled client configured with the encryption schema from the `previous example <csfle-reference-key-alt-name-in-schema>`.

In the encryption schema, the `salary.encrypt.keyId` field contains a JSON pointer to the `fieldWithAltName` field of the inserted document. As a result, the `salary` fields in the two example documents are each encrypted using a {+dek-abbr+} specific to the individual document. The keys are assigned dynamically at runtime.

## Procedure: Rotate Encryption Keys Using Mongo Shell

With version 1.5 and later of the Mongo Shell, you can rotate encryption keys using the `rewrapManyDataKey` method. The `rewrapManyDataKey` method automatically decrypts multiple data keys and re-encrypts them using a specified {+cmk-long+}. It then updates the rotated keys in the key vault collection. This method allows you to rotate encryption keys based on two optional arguments:

- A filter used to specify which keys to rotate. If no data key matches
the given filter, no keys are rotated. Omit the filter to rotate all keys in your key vault collection.

- An object that represents a new {+cmk-abbr+}. Omit this object to rotate
the data keys using their current CMKs.

The `rewrapManyDataKey` uses the following syntax:

```json
keyVault = db.getKeyVault()

keyVault.rewrapManyDataKey(
   { 
      "<Your custom filter>" 
   },
   {
      provider: "<KMS provider>",
      masterKey: {
         "<dataKeyOpts Key>" : "<dataKeyOpts Value>"
      }
   }
)
```

To learn more about the `dataKeyOpts` object for your KMS provider, see `qe-fundamentals-kms-providers-supported-kms`.

## Delete a {+dek-long+}

You can delete a {+dek-long+} from your {+key-vault-long+} using standard CRUD `delete operations <write-op-delete>`. If you delete a {+dek-abbr+}, all fields encrypted with that {+dek-abbr+} become permanently unreadable.

> **Tip:** The MongoDB shell allows you to delete a {+dek-abbr+} by `UUID` using
the `keyVault.deleteKey()` method as follows:
.. code-block:: none
   keyVault = db.getKeyVault()
   keyVault.deleteKey(UUID("<UUID String>"))

To learn more about {+key-vault-long+}s see `qe-reference-keys-key-vaults`.

## Learn More

For tutorials detailing how to set up a {+csfle-abbrev+}-enabled application with each of the supported {+kms-abbr+} providers, see the following pages:

- `csfle-tutorial-automatic-aws`
- `csfle-tutorial-automatic-azure`
- `csfle-tutorial-automatic-gcp`
- `csfle-tutorial-automatic-kmip`
To view additional examples of encryption schemas, see `csfle-reference-encryption-schemas`.
