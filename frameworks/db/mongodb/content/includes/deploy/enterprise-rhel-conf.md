---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/enterprise-rhel-conf.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Create an `/etc/yum.repos.d/mongodb-enterprise-{+version+}.repo` file so that you can install MongoDB Enterprise directly using `yum`:

> **Note:** If you have a `mongodb-enterprise.repo` file
in this directory from a previous installation of MongoDB, you
should remove it. Use the `mongodb-enterprise-{+version+}.repo`
file above to install MongoDB {+version+}.

You can also download the `.rpm` files directly from the [MongoDB repository](https://repo.mongodb.com/yum/redhat/). Downloads are organized by Red Hat / CentOS version (e.g. `9`), then MongoDB `release version <release-version-numbers>` (e.g. `{+version+}`), then architecture (e.g. `x86_64`).
