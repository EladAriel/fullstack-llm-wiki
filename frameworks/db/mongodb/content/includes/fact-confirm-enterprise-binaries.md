---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-confirm-enterprise-binaries.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

To verify that you are using MongoDB Enterprise, pass the `--version` command line option to the :binary:`~bin.mongod` or :binary:`~bin.mongos`:

```bash
mongod --version
```

In the output from this command, look for the string `modules: subscription` or `modules: enterprise` to confirm you are using the MongoDB Enterprise binaries.
