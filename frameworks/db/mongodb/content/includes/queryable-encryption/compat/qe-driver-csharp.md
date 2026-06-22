---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/compat/qe-driver-csharp.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

### Driver Compatibility

To use {+qe+} with the :driver:`.NET/C# </csharp>` driver, install driver version 2.20.0 or later.

For driver version 3.0 or later:

- Install `MongoDB.Driver.Encryption
<https://www.nuget.org/packages/MongoDB.Driver.Encryption>`__ on all operating systems.

- If your application runs on Linux, also install
`libmongocrypt <qe-reference-libmongocrypt>` version {+minimum-libmongocrypt-version+} or later.
