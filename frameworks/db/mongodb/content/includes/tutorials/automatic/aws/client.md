---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/client.rst"
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
   `Generate your {+dek-long+} <csfle-aws-create-dek>` step of this
   guide.
.. tabs-drivers::
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/InsertEncryptedDocument.java
         :start-after: start-schema
         :end-before: end-schema
         :language: java
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/node/aws/reader/insert_encrypted_document.js
         :start-after: start-schema
         :end-before: end-schema
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/python/aws/reader/insert_encrypted_document.py
         :start-after: start-schema
         :end-before: end-schema
         :language: python
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/InsertEncryptedDocument.cs
         :start-after: start-schema
         :end-before: end-schema
         :language: csharp
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/go/aws/reader/insert-encrypted-document.go
         :start-after: start-schema
         :end-before: end-schema
         :language: go
         :dedent:

#. Specify the Location of the {+shared-library+}

#. Create the MongoClient

Instantiate a MongoDB client object with the following automatic encryption settings that use the variables declared in the previous steps:
