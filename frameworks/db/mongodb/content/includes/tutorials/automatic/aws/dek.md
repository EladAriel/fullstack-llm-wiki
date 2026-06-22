---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/dek.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Add your AWS KMS Credentials

Add the service account credentials to your CSFLE-enabled client code.

#. Add Your Key Information

Update the following code to specify your {+cmk-long+}:

> **Tip:**    You recorded your {+cmk-long+}'s {+aws-arn-abbr+} and Region
   in the Create a {+cmk-long+} step of this guide.
.. tabs-drivers::
   .. tab::
      :tabid: java-sync
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/java/aws/reader/src/main/java/com/mongodb/csfle/MakeDataKey.java
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: java
         :dedent:
   .. tab::
      :tabid: nodejs
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/node/aws/reader/make_data_key.js
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: javascript
         :dedent:
   .. tab::
      :tabid: python
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/python/aws/reader/make_data_key.py
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: python
         :dedent:
   .. tab::
      :tabid: csharp
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/MakeDataKey.cs
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: csharp
         :dedent:
   .. tab::
      :tabid: go
      .. literalinclude:: /includes/generated/in-use-encryption/csfle/go/aws/reader/make-data-key.go
         :start-after: start-datakeyopts
         :end-before: end-datakeyopts
         :language: go
         :dedent:

#. Generate your {+dek-long+}

Generate your {+dek-long+} using the variables declared in `step one <csfle-aws-create-index>` of this tutorial.

> **Tip:** To view a diagram showing how your client application creates your
{+dek-long+} when using an AWS KMS, see
`qe-fundamentals-kms-providers-aws-architecture`.
To learn more about the options for creating a {+dek-long+}
encrypted with a {+cmk-long+} hosted in AWS KMS, see
`qe-kms-datakeyopts-aws`.
