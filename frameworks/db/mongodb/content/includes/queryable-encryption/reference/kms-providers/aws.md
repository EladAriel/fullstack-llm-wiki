---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/reference/kms-providers/aws.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Architecture ````````````

The following diagram describes the architecture of a {+qe+} enabled application using {+aws-abbr+} KMS.

.. image:: /images/CSFLE_Data_Key_KMS.png

.. include:: /includes/queryable-encryption/reference/kms-providers/cmk-note.rst

kmsProviders Object ```````````````````

The following table presents the structure of a `kmsProviders` object for AWS KMS:

To use automatic credential fetching, specify an empty object for the `aws` credential. The driver then fetches credentials using its standard AWS credential lookup flow:

```json
{ "aws": {} }
```

dataKeyOpts Object ``````````````````

The following table presents the structure of a `dataKeyOpts` object for AWS KMS:
