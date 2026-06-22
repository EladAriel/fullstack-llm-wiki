---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/upgrade-path.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To upgrade between minor releases, you must upgrade sequentially through each minor release. You cannot skip minor releases. For example, to upgrade from 8.1 to 8.3, you must first upgrade from 8.1 to 8.2, and then upgrade from 8.2 to 8.3.

To upgrade from a minor release to the next major release, you can:

- Upgrade through each minor release to the next major.
For example, to upgrade from 8.1 to the next major release, upgrade from 8.1 to 8.2, then from 8.2 to 8.3, and then from 8.3 to the next major release.

- Downgrade to the previous major release, and then upgrade to the
next major. For example, to upgrade from 8.1 to the next major release, downgrade from 8.1 to 8.0, and then upgrade from 8.0 to the next major release.

Each upgrade or downgrade step requires both a binary upgrade and a |fcv| upgrade.
