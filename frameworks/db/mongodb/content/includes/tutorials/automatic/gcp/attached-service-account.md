---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/tutorials/automatic/gcp/attached-service-account.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
