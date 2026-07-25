---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/mongodb-8.0-kernel-incompatibility-warning.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Warning:** Due to an incompatibility between a new kernel release and the
currently vendored version of TCMalloc, running MongoDB 8.0 or newer
with Linux kernel version 6.19 can cause MongoDB to crash on
startup. This applies to all MongoDB packages, including those
obtained from the MongoDB website, or obtained from package managers
or Docker.
As soon as a patched version of TCMalloc is available, MongoDB will
upgrade to use it, and this compatibility issue will be resolved.
