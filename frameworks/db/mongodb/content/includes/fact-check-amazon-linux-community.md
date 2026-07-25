---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-check-amazon-linux-community.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can verify which Linux distribution you are running by running the following command on the command-line:

```none
grep ^NAME  /etc/*release
```

The result should be **Amazon Linux** or **Amazon Linux AMI**. If using a different Linux distribution, please see the `install instructions for your platform <install-mdb-community-edition-linux>`.
