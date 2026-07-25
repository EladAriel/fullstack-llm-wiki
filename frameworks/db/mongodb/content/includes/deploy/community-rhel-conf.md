---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/community-rhel-conf.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create a `/etc/yum.repos.d/mongodb-org-{+version+}.repo` file so that you can install MongoDB directly using `yum`:

You can also download the `.rpm` files directly from the [MongoDB repository](https://repo.mongodb.org/yum/redhat/). Downloads are organized by Red Hat / CentOS version (e.g. `9`), then MongoDB `release version <release-version-numbers>` (e.g. `{+version+}`), then architecture (e.g. `x86_64`).
