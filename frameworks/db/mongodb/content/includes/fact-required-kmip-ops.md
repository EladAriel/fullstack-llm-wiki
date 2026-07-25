---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-required-kmip-ops.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

For an integration with a third-party key management appliance using the {+kmip-hover+}, you should allow the following KMIP operations:

- Create (`operation_create`)
- Get (`operation_get`)
- Activate (`operation_activate`)
- GetAttributes (`operation_get_attributes`)
- Encrypt (`operation_encrypt`)
- Decrypt (`operation_decrypt`)
MongoDB requires the Encrypt and Decrypt operations with the default KMIP configuration. If you set :setting:`security.kmip.useLegacyProtocol` to `true` in the MongoDB server `configuration file <configuration-options>`, MongoDB uses the KMIP 1.0/1.1 protocol, which does not require these operations.
