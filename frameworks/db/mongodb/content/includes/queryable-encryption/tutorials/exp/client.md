---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/exp/client.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Specify the {+key-vault-long-title+} Namespace

Specify `encryption.__keyVault` as the {+key-vault-long+} namespace.

#. Specify the {+cmk-long+}

Specify the KMS provider and specify your {+cmk-long+} inline:

#. Retrieve {+dek-long+}s

Retrieve the {+dek-long+}s created in the `Create a {+dek-long+} <qe-manual-encryption-tutorial-data-key-create>` step of this guide:

#. Specify the Path of the {+shared-library+}

#. Create a MongoClient Object

Instantiate a `MongoClient` object with the following automatic encryption settings:

#. Create a ClientEncryption Object

Instantiate a `ClientEncryption` object as follows:

> **Note:** To learn more about the indexed and unindexed algorithms in
{+manual-enc+}, see `<qe-fundamentals-man-enc-algorithm-choice>`.
