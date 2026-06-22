---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-x509-certificate-client-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in MongoDB 5.0, :binary:`mongod` and :binary:`mongos` now issue a startup warning when their certificates do not include a `Subject Alternative Name` attribute.

The following platforms do not support common name validation:

- iOS 13 and higher
- MacOS 10.15 and higher
- Go 1.15 and higher
Clients using these platforms will not `authenticate <x509-client-authentication>` to MongoDB servers that use X.509 certificates whose hostnames are `specified by CommonName attributes <KMIP-subject-alternative-name-CN>`.
