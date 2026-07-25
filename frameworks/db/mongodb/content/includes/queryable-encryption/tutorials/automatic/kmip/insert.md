---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/kmip/insert.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Use your {+qe-abbr+}-enabled `MongoClient` instance to insert a {+in-use-doc+} into the `medicalRecords.patients` namespace using the following code snippet:

When you insert a document, your {+qe+}-enabled client encrypts the fields of your document such that it resembles the following:

.. include:: /includes/queryable-encryption/safe-content-warning.rst
