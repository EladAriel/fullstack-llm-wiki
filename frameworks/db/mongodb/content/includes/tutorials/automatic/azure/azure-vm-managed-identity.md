---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/azure/azure-vm-managed-identity.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
