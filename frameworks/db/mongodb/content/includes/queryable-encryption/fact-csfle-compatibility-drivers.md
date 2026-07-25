---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/fact-csfle-compatibility-drivers.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

While {+qe+} does not support encrypting individual array elements, randomized encryption supports encrypting the entire array field rather than individual elements in the field. The example automatic encryption rules specify randomized encryption for the `medicalRecords` field to encrypt the entire array. If the automatic encryption rules specified :autoencryptkeyword:`encrypt` or :autoencryptkeyword:`encryptMetadata` within `medicalRecords.items` or `medicalRecords.additionalItems`, automatic field level encryption fails and returns an errors.

The official MongoDB drivers, :binary:`~bin.mongosh`, and the legacy `mongo` shell require specifying the automatic encryption rules as part of creating the database connection object:

- For `mongosh`, use the :method:`Mongo()`
constructor to create a database connection. Specify the automatic encryption rules to the `schemaMap` key of the `{+auto-encrypt-options+}` parameter. See `mongo-connection-automatic-client-side-encryption-enabled` for a complete example.

- For the official MongoDB drivers, use the driver-specific database connection
constructor (`MongoClient`) to create the database connection with the automatic encryption rules included as part of the {+qe+} configuration object. Defer to the `driver API reference <csfle-driver-tutorials>` for more complete documentation and tutorials.

For all clients, the `keyVault` and `kmsProviders` specified to the {+qe+} parameter must grant access to both the {+dek-long+}s specified in the automatic encryption rules and the {+cmk-long+} used to encrypt the {+dek-long+}s.
