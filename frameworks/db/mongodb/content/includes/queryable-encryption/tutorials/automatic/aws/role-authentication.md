---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/tutorials/automatic/aws/role-authentication.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** To use an {+aws-iam-abbr+} role instead of an {+aws-iam-abbr+} user
to authenticate your application,
specify an empty object for your credentials in your KMS provider
object. This instructs the driver to automatically retrieve the credentials
from the environment:
.. tabs-drivers::
   .. tab::
      :tabid: python
      .. code-block:: python
         kms_provider_credentials = {
           "aws": { }
         }
   .. tab::
      :tabid: java-sync
      .. code-block:: java
         kmsProviderCredentials.put("aws", new HashMap<>());
   .. tab::
      :tabid: nodejs
      .. code-block:: javascript
         kmsProviders = {
           aws: { }
         };
   .. tab::
      :tabid: shell
      .. code-block:: javascript
         kmsProviders = {
           aws: { }
         };
   .. tab::
      :tabid: csharp
      .. code-block:: csharp
         kmsProviderCredentials.Add("aws", new Dictionary<string, object>);
   .. tab::
      :tabid: go
      .. code-block:: go
         kmsProviderCredentials := map[string]map[string]interface{}{
           "aws": { },
         }
   .. tab::
      :tabid: rust
      .. code-block:: rust
         kms_providers = vec![(
             KmsProvider::aws(),
             doc! {},
             None,
         )];
   .. tab::
      :tabid: php
      .. code-block:: php
         $kmsProviders = [
            'aws' => [],
         ];
You cannot automatically retrieve credentials if you are using a named KMS provider.
