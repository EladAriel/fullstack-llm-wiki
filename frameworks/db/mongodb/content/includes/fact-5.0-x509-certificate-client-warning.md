---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-x509-certificate-client-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, :binary:`mongod` and :binary:`mongos` now issue a startup warning when their certificates do not include a `Subject Alternative Name` attribute.

The following platforms do not support common name validation:

- iOS 13 and higher
- MacOS 10.15 and higher
- Go 1.15 and higher
Clients using these platforms will not `authenticate <x509-client-authentication>` to MongoDB servers that use X.509 certificates whose hostnames are `specified by CommonName attributes <KMIP-subject-alternative-name-CN>`.
