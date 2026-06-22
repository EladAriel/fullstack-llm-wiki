---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/persist-keyid/persist-keyid-node.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Tip:** This guide shows automatic {+dek-abbr-no-hover+} creation by using the
`createEncryptedCollection()` function to create the {+qe+} collection.
This call generates a `keyId` value for each encrypted field and returns
those values in a new copy of the {+enc-schema+}.
If you choose to provide an {+enc-schema+} in the automatic encryption
options of a `MongoClient` that you use to read and write encrypted
data, you need to specify the `keyId` values for each encrypted field.
Therefore, you should save the {+enc-schema+} that
`createEncryptedCollection()` returns for future use or assign
`keyAltNames` for all the encrypted fields. This allows you to
include the necessary `keyId` values in your client's
{+enc-schema+}.
To learn more about the contents of the {+enc-schema+}, see
`qe-fundamentals-enable-qe`.
To learn more about the `createEncryptedCollection()` function, see the
API documentation (TODO: add appropriate link).
