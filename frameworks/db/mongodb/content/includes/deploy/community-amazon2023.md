---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/community-amazon2023.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

```cfg
[mongodb-org-{+version+}]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/amazon/2023/mongodb-org/{+version+}/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-{+pgp-version+}.asc
```

You can also download the `.rpm` files directly from the [MongoDB repository](https://repo.mongodb.org/yum/amazon/). Downloads are organized by Amazon Linux 2023 version (for example, `2023`), then MongoDB `version <release-version-numbers>` (`{+version+}`), then architecture (`x86_64`).
