---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/windows-create-dirs.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

a. MongoDB needs a data directory to store your data. By default, it uses `C:\data\db`, but you may specify a different location in your config file. You can create the data directory using the Windows Command Prompt:

```bat
   mkdir c:\data\db
```

#. If you specified a log path in the configuration file, create the log directory in the same way.
