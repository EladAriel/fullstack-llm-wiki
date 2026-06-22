---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/latest-release-reversion-restriction.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** If you choose the
:guilabel:`Latest Version With Auto Upgrades` release option
and your cluster upgrades from a major version to a minor
version, you cannot revert to a major version until the
next major version release is available.
For example, if you opt in while MongoDB 8.2 is the latest
release, your cluster stays on the latest minor version
until MongoDB 9.0 is released. You can only revert to a
major version in the window between the 9.0 release and
the first minor release (9.1). If you miss that window,
you cannot revert until MongoDB 10.0 is released.
