---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/azure/azure-vm-managed-identity.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Tip:**       If your client runs on an Azure Virtual Machine (VM), you can allow the
      VM to use its Managed Identity to authenticate to your key vault.
      To allow the Azure VM to automatically provide your credentials,
      assign an empty map instead of one that contains your Azure
      credentials as shown in the following code:
      .. code-block:: java
          String kmsProvider = "azure";
          Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
          Map<String, Object> providerDetails = new HashMap<>();
          kmsProviders.put(kmsProvider, providerDetails);
