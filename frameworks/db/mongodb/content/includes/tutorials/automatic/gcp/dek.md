---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/gcp/dek.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Add your GCP KMS Credentials

#. Add Your Key Information

Update the following code to specify your {+cmk-long+}:

> **Tip:**    You recorded your {+cmk-long+} details in the
   in the `Create a {+cmk-long+} <gcp-create-master-key>`
   step of this guide.
.. tabs-drivers::
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/java/gcp/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: java
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/node/gcp/reader/make_data_key.js
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/python/gcp/reader/make_data_key.py
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: python
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/dotnet/gcp/reader/CSFLE/MakeDataKey.cs
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: csharp
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/go/gcp/reader/make-data-key.go
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: go
         :dedent:

#. Generate your {+dek-long+}

Generate your {+dek-long+} using the variables declared in `step one <csfle-gcp-create-index>` of this tutorial.

> **Tip:** To view a diagram showing how your client application creates your
{+dek-long+} when using an {+gcp-kms+}, see
`qe-fundamentals-kms-providers-gcp-architecture`.
To learn more about the options for creating a {+dek-long+}
encrypted with a {+cmk-long+} hosted in {+azure-kv+}, see
`qe-kms-provider-object-gcp` and
`qe-kms-datakeyopts-gcp`.
