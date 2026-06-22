---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/code/community-amazon2023.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
