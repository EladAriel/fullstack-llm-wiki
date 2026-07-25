---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-confirm-enterprise-binaries.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To verify that you are using MongoDB Enterprise, pass the `--version` command line option to the :binary:`~bin.mongod` or :binary:`~bin.mongos`:

```bash
mongod --version
```

In the output from this command, look for the string `modules: subscription` or `modules: enterprise` to confirm you are using the MongoDB Enterprise binaries.
