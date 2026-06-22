---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/important-dont-use-distro-packages.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To install MongoDB |edition| on your |distro-name| system, these instructions will use the official |package-name| package, which is maintained and supported by MongoDB Inc. The official |package-name| package always contains the latest version of MongoDB, and is available from its own dedicated repo.

> **Important:** The `mongodb` package provided by |distro-name| is **not**
maintained by MongoDB Inc. and conflicts with the official
|package-name| package. If you have already installed the `mongodb`
package on your |distro-name| system, you **must** first uninstall
the `mongodb` package before proceeding with these instructions.
