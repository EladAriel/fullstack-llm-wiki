---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/client-csharp.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Specify the {+key-vault-long-title+} Namespace

Specify `encryption.__keyVault` as the {+key-vault-long+} namespace.

#. Specify your AWS Credentials

Specify the `aws` KMS provider and your {+aws-iam-abbr+} user credentials:

#. Create an Encryption Schema For Your Collection

> **Tip:**    Make sure to update the following code to include your Base64
   {+dek-abbr+} ID. You received this value in the
   `Generate your {+dek-long+} <csfle-aws-create-dek-csharp>` step of this
   guide.
.. literalinclude:: /includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/InsertEncryptedDocument.cs
   :start-after: start-schema
   :end-before: end-schema
   :language: csharp
   :dedent:

#. Specify the Location of the {+shared-library+}

#. Create the MongoClient

Instantiate a MongoDB client object with the following automatic encryption settings that use the variables declared in the previous steps:
