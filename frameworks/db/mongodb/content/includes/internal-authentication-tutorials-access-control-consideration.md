---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/internal-authentication-tutorials-access-control-consideration.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

This tutorial covers creating the minimum number of administrative users on the `admin` database only. For the user authentication, the tutorial uses the default `authentication-scram` authentication mechanism. Challenge-response security mechanisms are best suited for testing or development environments. For production environments, we recommend using `X.509 certificates <security-auth-x509>` or `security-ldap` (available for MongoDB Enterprise only) or `security-kerberos` (available for MongoDB Enterprise only).

For details on creating users for specific authentication mechanism, refer to the specific authentication mechanism pages.

See `security-checklist-role-based-access-control` for best practices for user creation and management.
