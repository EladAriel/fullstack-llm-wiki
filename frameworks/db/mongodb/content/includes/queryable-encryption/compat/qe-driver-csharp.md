---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/queryable-encryption/compat/qe-driver-csharp.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

### Driver Compatibility

To use {+qe+} with the :driver:`.NET/C# </csharp>` driver, install driver version 2.20.0 or later.

For driver version 3.0 or later:

- Install `MongoDB.Driver.Encryption
<https://www.nuget.org/packages/MongoDB.Driver.Encryption>`__ on all operating systems.

- If your application runs on Linux, also install
`libmongocrypt <qe-reference-libmongocrypt>` version {+minimum-libmongocrypt-version+} or later.
