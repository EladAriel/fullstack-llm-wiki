---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/behavior-drop-role.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When a role is dropped on a :program:`mongod`, previously authenticated users remain logged in to the database but immediately lose the role's privileges.

When a role is dropped on a :program:`mongos`, previously authenticated users remain logged in to the database but lose the role's privileges when the cache refreshes. The cache refreshes automatically after the time specified with the :parameter:`userCacheInvalidationIntervalSecs` parameter or manually when you run the :dbcommand:`invalidateUserCache` command.
