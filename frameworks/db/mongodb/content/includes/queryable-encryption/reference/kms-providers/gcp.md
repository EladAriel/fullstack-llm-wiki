---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/reference/kms-providers/gcp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Architecture ````````````

The following diagram describes the architecture of a {+qe+} enabled application using GCP KMS.

.. image:: /images/CSFLE_Data_Key_KMS.png

.. include:: /includes/queryable-encryption/reference/kms-providers/cmk-note.rst

kmsProviders Object ```````````````````

The following table presents the structure of a `kmsProviders` object for GCP KMS:

To use an access token instead of service account credentials, specify the `accessToken` field:

```json
{ "gcp": { "accessToken": "<access token>" } }
```

To use automatic credential fetching, specify an empty object for the `gcp` credential. The driver then retrieves credentials from the GCP metadata service:

```json
{ "gcp": {} }
```

dataKeyOpts Object ``````````````````

The following table presents the structure of a `dataKeyOpts` object for GCP KMS:
