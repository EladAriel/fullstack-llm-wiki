---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/access-mongorestore-collections.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You need additional privileges if the backup data includes `system.profile <<database>.system.profile>` collection data or you run with :option:`--oplogReplay <mongorestore.--oplogReplay>`:

over the __system role. https://github.com/mongodb/docs/commit/237c44cd3b6e4b7dbe0c9077b7571c8b7ec5d7a5
