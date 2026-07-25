---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ftdc-windows-user-permissions.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

On Windows, to collect system data such as disk, cpu, and memory, FTDC requires Microsoft access permissions from the following groups:

- Performance Monitor Users
- Performance Log Users
If the user running :binary:`mongod <bin.mongod>` and :binary:`mongos <bin.mongos>` is not an administrator, add them to these groups to log FTDC data. For more information, see [the Microsoft documentation here](https://learn.microsoft.com/en-us/windows/win32/perfctrs/restricting-access-to-performance-extension--dlls).
