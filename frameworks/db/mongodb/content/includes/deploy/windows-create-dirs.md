---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/deploy/windows-create-dirs.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

a. MongoDB needs a data directory to store your data. By default, it uses `C:\data\db`, but you may specify a different location in your config file. You can create the data directory using the Windows Command Prompt:

```bat
   mkdir c:\data\db
```

#. If you specified a log path in the configuration file, create the log directory in the same way.
