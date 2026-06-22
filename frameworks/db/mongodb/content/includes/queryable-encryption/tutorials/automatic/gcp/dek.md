---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/gcp/dek.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Add your GCP KMS Credentials

.. include:: /includes/queryable-encryption/tab-note.rst

#. Add Your Key Information

Update the following code to specify your {+cmk-long+}:

> **Tip:**    You recorded your {+cmk-long+} details in the
   in the `Create a {+cmk-long+} <qe-gcp-create-master-key>`
   step of this guide.
.. tabs-drivers::
   .. tab::
      :tabid: shell
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/mongosh/gcp/reader/make_data_key.js
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: javascript
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/node/gcp/reader/make_data_key.js
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/python/gcp/reader/make_data_key.py
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: python
         :dedent:
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/java/gcp/reader/src/main/java/com/mongodb/qe/MakeDataKey.java
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: java
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/go/gcp/reader/make-data-key.go
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: go
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/dotnet/gcp/reader/QueryableEncryption/MakeDataKey.cs
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: csharp
         :dedent:

#. Generate your {+dek-long+}s

Construct a client with your MongoDB connection string and {+key-vault-long+} namespace, and create the {+dek-long+}s:

> **Note:**    The {+key-vault-long+} is in the `encryption.__keyVault`
   namespace. Ensure that the database user your application uses to connect
   to MongoDB has `ReadWrite <manual-reference-role-read-write>`
   permissions on this namespace.
.. tabs-drivers::
   .. tab::
      :tabid: shell
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/mongosh/gcp/reader/make_data_key.js
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: javascript
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/node/gcp/reader/make_data_key.js
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/python/gcp/reader/make_data_key.py
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: python
         :dedent:
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/java/gcp/reader/src/main/java/com/mongodb/qe/MakeDataKey.java
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: java
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/go/gcp/reader/make-data-key.go
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: go
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/dotnet/gcp/reader/QueryableEncryption/MakeDataKey.cs
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: csharp
         :dedent:

#. Create Your Encrypted Collection

Use a {+qe+} enabled `MongoClient` instance to specify what fields you must encrypt and create your encrypted collection:

The output from the code in this section should resemble the following:

> **Tip:** To view a diagram showing how your client application creates your
{+dek-long+} when using an {+gcp-kms+}, see
`qe-fundamentals-kms-providers-gcp-architecture`.
To learn more about the options for creating a {+dek-long+}
encrypted with a {+cmk-long+} hosted in {+azure-kv+}, see
`qe-kms-provider-object-gcp` and
`qe-kms-datakeyopts-gcp`.
