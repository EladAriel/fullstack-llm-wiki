---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/reference/kms-providers/azure.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Architecture ````````````

The following diagram describes the architecture of a {+qe+} enabled application using Azure Key Vault.

.. image:: /images/CSFLE_Data_Key_KMS.png

.. include:: /includes/queryable-encryption/reference/kms-providers/cmk-note.rst

kmsProviders Object ```````````````````

The following table presents the structure of a `kmsProviders` object for Azure Key Vault:

To use an access token instead of service principal credentials, specify the `azure.accessToken` field:

```json
{ "azure": { "accessToken": "<access token>"} }
```

To use automatic credential fetching, specify an empty object for the `azure` credential. The driver then retrieves credentials from the Azure Instance Metadata Service:

```json
{ "azure": {} }
```

dataKeyOpts Object ``````````````````

The following table presents the structure of a `dataKeyOpts` object for Azure Key Vault:

.. include:: /includes/queryable-encryption/qe-csfle-warning-azure-keyversion.rst
