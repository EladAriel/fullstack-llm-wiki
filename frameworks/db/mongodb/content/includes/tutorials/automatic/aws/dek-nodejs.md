---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/aws/dek-nodejs.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. Add your AWS KMS Credentials

Add the service account credentials to your CSFLE-enabled client code.

#. Add Your Key Information

Update the following code to specify your {+cmk-long+}:

> **Tip:**    You recorded your {+cmk-long+}'s {+aws-arn-abbr+} and Region
   in the Create a {+cmk-long+} step of this guide.
.. literalinclude:: /includes/generated/in-use-encryption/csfle/node/aws/reader/make_data_key.js
   :end-before: end-datakeyopts
   :language: javascript
   :dedent:

#. Generate your {+dek-long+}

> **Tip:** To view a diagram showing how your client application creates your
{+dek-long+} when using an AWS KMS, see
`qe-fundamentals-kms-providers-aws-architecture`.
To learn more about the options for creating a {+dek-long+}
encrypted with a {+cmk-long+} hosted in AWS KMS, see
`qe-kms-datakeyopts-aws`.
