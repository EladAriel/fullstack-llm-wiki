---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/in-use-encryption/update-a-key.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To add a {+dek-abbr+} to your {+key-vault-long+}, use the `createKey` method of a `ClientEncryption` object.

To delete or update a {+dek-abbr+}, use one of the following mechanisms:

- The `rewrapManyDataKey` method
- Standard `CRUD <crud>` operations
To learn more about the `rewrapManyDataKey` method, see the documentation of the method for your client or driver:

- `MongoDB Shell <server-keyvault-rewrap-manydatakey-method>`
- [{+pymongo+}]({+pymongo-api-docs+}/pymongo/encryption.html#pymongo.encryption.ClientEncryption.rewrap_many_data_key)_
- [{+node-driver-full+}]({+node-libmongocrypt-binding-docs+}/node#RewrapManyDataKeyResult)_
- [{+csharp-driver-full+}]({+csharp-api-docs+}/MongoDB.Driver.Encryption/MongoDB.Driver.Encryption.ClientEncryption.RewrapManyDataKey.html)_
- [{+java-driver-full+}]({+java-api-docs+}/driver-sync/com/mongodb/client/vault/ClientEncryption.html#rewrapManyDataKey(org.bson.conversions.Bson))_
- [{+go-driver-full+}]({+go-api-docs+}/mongo#ClientEncryption.RewrapManyDataKey)_
> **Tip:** :binary:`~bin.mongosh` provides the following additional
methods for working with your {+key-vault-long+}:
- :method:`getKeyVault()`
- :method:`KeyVault.getKey()`
- :method:`KeyVault.getKeys()`
- :method:`KeyVault.getKeyByAltName()`
- :method:`KeyVault.createKey()`
- :method:`KeyVault.rewrapManyDataKey()`
- :method:`KeyVault.addKeyAlternateName()`
- :method:`KeyVault.removeKeyAlternateName()`
