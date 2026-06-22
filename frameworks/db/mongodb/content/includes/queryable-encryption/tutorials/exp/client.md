---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/exp/client.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
