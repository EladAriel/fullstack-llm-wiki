---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/upgrade-path.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To upgrade between minor releases, you must upgrade sequentially through each minor release. You cannot skip minor releases. For example, to upgrade from 8.1 to 8.3, you must first upgrade from 8.1 to 8.2, and then upgrade from 8.2 to 8.3.

To upgrade from a minor release to the next major release, you can:

- Upgrade through each minor release to the next major.
For example, to upgrade from 8.1 to the next major release, upgrade from 8.1 to 8.2, then from 8.2 to 8.3, and then from 8.3 to the next major release.

- Downgrade to the previous major release, and then upgrade to the
next major. For example, to upgrade from 8.1 to the next major release, downgrade from 8.1 to 8.0, and then upgrade from 8.0 to the next major release.

Each upgrade or downgrade step requires both a binary upgrade and a |fcv| upgrade.
