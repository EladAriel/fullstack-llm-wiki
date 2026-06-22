---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/admonition-power-ubuntu-restriction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

For earlier MongoDB Enterprise versions that support Ubuntu 16.04 POWER/PPC64LE:

Due to a lock elision bug present in older versions of the `glibc` package on Ubuntu 16.04 for POWER, you must upgrade the `glibc` package to at least `glibc 2.23-0ubuntu5` before running MongoDB. Systems with older versions of the `glibc` package will experience database server crashes and misbehavior due to random memory corruption, and are unsuitable for production deployments of MongoDB
