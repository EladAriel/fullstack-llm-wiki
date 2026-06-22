---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/dek-csharp.rst"
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
.. literalinclude:: /includes/generated/in-use-encryption/csfle/dotnet/aws/reader/CSFLE/MakeDataKey.cs
   :start-after: start-datakeyopts
   :end-before: end-datakeyopts
   :language: csharp
   :dedent:

#. Generate your {+dek-long+}

> **Tip:** To view a diagram showing how your client application creates your
{+dek-long+} when using an AWS KMS, see
`qe-fundamentals-kms-providers-aws-architecture`.
To learn more about the options for creating a {+dek-long+}
encrypted with a {+cmk-long+} hosted in AWS KMS, see
`qe-kms-datakeyopts-aws`.
