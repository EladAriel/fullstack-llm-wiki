---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/community-rhel-conf.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Create a `/etc/yum.repos.d/mongodb-org-{+version+}.repo` file so that you can install MongoDB directly using `yum`:

You can also download the `.rpm` files directly from the [MongoDB repository](https://repo.mongodb.org/yum/redhat/). Downloads are organized by Red Hat / CentOS version (e.g. `9`), then MongoDB `release version <release-version-numbers>` (e.g. `{+version+}`), then architecture (e.g. `x86_64`).
