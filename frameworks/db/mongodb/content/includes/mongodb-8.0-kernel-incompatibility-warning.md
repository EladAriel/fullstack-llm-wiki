---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/mongodb-8.0-kernel-incompatibility-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** Due to an incompatibility between a new kernel release and the
currently vendored version of TCMalloc, running MongoDB 8.0 or newer
with Linux kernel version 6.19 can cause MongoDB to crash on
startup. This applies to all MongoDB packages, including those
obtained from the MongoDB website, or obtained from package managers
or Docker.
As soon as a patched version of TCMalloc is available, MongoDB will
upgrade to use it, and this compatibility issue will be resolved.
