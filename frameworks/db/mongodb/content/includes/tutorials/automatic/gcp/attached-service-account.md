---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/gcp/attached-service-account.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Tip:** If you are using an `attached service account
<https://cloud.google.com/iam/docs/impersonating-service-accounts#binding-to-resources>`__,
you can allow it to automatically authenticate it to your GCP KMS.
To automatically authenticate, assign an empty map instead of one
that contains your GCP credentials, as shown in the following code:
.. code-block:: java
   String kmsProvider = "gcp";
   Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
   Map<String, Object> providerDetails = new HashMap<>();
   kmsProviders.put(kmsProvider, providerDetails);
Proceed to the next step in the guide after adding this code.
