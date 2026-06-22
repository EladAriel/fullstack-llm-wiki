---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/azure/cmk.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. Create your Azure Key Vault and {+cmk-long+}

To create a new {+azure-kv+} instance and {+cmk-long+}, follow Microsoft's official [Set and retrieve a key from Azure Key Vault using the Azure portal](https://docs.microsoft.com/en-us/azure/key-vault/keys/quick-create-portal)_ Quick Start.

> **Note:**    The {+cmk-long+} should have an RSA key size of 2048 or 4096
   bits.
.. important:: Record your Credentials
   Ensure you record the following credentials:
   - **Key Name**
   - **Key Identifier** (referred to as `keyVaultEndpoint` later in this guide)
   - **Key Version**
   You will need them to construct your `dataKeyOpts` object
   later in this tutorial.

#. Grant Permissions

Grant your client application `wrap` and `unwrap` permissions to the key.
