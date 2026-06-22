---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/quick-start/dek.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Read the {+cmk-long+} and Specify KMS Provider Settings

Retrieve the contents of the {+cmk-long+} file that you generated in the `Create a {+cmk-long+} <qe-quick-start-create-master-key>` step of this guide.

Use the {+cmk-abbr+} value in your KMS provider settings. The client uses these settings to discover the {+cmk-abbr+}. Set the provider name to `local` to indicate that you are using a Local Key Provider.

.. include:: /includes/queryable-encryption/tab-note.rst

#. Create your {+dek-long+}s

Construct a client with your MongoDB connection string and {+key-vault-long+} namespace, and create the {+dek-long+}s:

> **Note:**    .. include:: /includes/note-key-vault-permissions
.. tabs-drivers::
   .. tab::
      :tabid: shell
      .. literalinclude::  /includes/generated/in-use-encryption/queryable-encryption/mongosh/local/reader/make_data_key.js
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: javascript
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude::  /includes/generated/in-use-encryption/queryable-encryption/node/local/reader/make_data_key.js
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude::  /includes/generated/in-use-encryption/queryable-encryption/python/local/reader/make_data_key.py
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: python
         :dedent:
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/java/local/reader/src/main/java/com/mongodb/qe/MakeDataKey.java
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: java
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/go/local/reader/make-data-key.go
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: go
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/queryable-encryption/dotnet/local/reader/QueryableEncryption/MakeDataKey.cs
         :start-after: start-create-dek
         :end-before: end-create-dek
         :language: csharp
         :dedent:

#. Create Your Encrypted Collection

Use a {+qe+} enabled `MongoClient` instance to specify what fields you must encrypt and create your encrypted collection:

The output from the code in this section should resemble the following:
