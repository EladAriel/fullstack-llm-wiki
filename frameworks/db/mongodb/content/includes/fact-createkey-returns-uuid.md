---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-createkey-returns-uuid.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

If successful, :method:`~KeyVault.createKey()` returns the :abbr:`UUID (Universally unique identifier)` of the new data encryption key. The `UUID` is a BSON :bsontype:`Binary (BinData) <Binary>` object with subtype `4` that uniquely identifies the data encryption key. The `UUID` string is the hexadecimal representation of the underlying binary data.

If you are providing the data encryption key to an official MongoDB driver in order to configure `automatic client-side field level encryption <field-level-encryption-json-schema>`, you must use the `base64` representation of the `UUID` string.

You can run the following operation in :binary:`~bin.mongosh` to convert a `UUID` hexadecimal string to its `base64` representation:

```javascript
UUID("b4b41b33-5c97-412e-a02b-743498346079").base64()
```

Supply the `UUID` of your own data encryption key to this command, as returned from :method:`~KeyVault.createKey()` above, or as described in `field-level-encryption-data-key-retrieve`.
