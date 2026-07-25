---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/important-selinux-customizations.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

> **Important:** In addition to the above, if SELinux is in `enforcing` mode you
will also need to further customize your SELinux policy for each of
these situations:
- You are using a **custom directory path** instead of using the
  default path for any combination of:
  - :setting:`~storage.dbPath`
  - :setting:`systemLog.path`
  - :setting:`~processManagement.pidFilePath`
- You are using a **custom port** instead of using the :doc:`default
  MongoDB port </reference/default-mongodb-port>`.
- If you have made other modifications to your MongoDB installation.
