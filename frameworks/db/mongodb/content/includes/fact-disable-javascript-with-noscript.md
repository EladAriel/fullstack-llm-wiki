---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-disable-javascript-with-noscript.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

You can disable all server-side execution of JavaScript:

- For a :binary:`~bin.mongod` instance by passing the
:option:`--noscripting <mongod --noscripting>` option on the command line or setting :setting:`security.javascriptEnabled` to false in the configuration file.

- For a :binary:`~bin.mongos` instance by passing the
:option:`--noscripting <mongos --noscripting>` option on the command line or setting :setting:`security.javascriptEnabled` to false in the configuration file.
