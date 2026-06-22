---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-ftdc-windows-user-permissions.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

On Windows, to collect system data such as disk, cpu, and memory, FTDC requires Microsoft access permissions from the following groups:

- Performance Monitor Users
- Performance Log Users
If the user running :binary:`mongod <bin.mongod>` and :binary:`mongos <bin.mongos>` is not an administrator, add them to these groups to log FTDC data. For more information, see [the Microsoft documentation here](https://learn.microsoft.com/en-us/windows/win32/perfctrs/restricting-access-to-performance-extension--dlls).
