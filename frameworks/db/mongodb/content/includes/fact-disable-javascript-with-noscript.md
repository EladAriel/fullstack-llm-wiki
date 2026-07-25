---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-disable-javascript-with-noscript.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

You can disable all server-side execution of JavaScript:

- For a :binary:`~bin.mongod` instance by passing the
:option:`--noscripting <mongod --noscripting>` option on the command line or setting :setting:`security.javascriptEnabled` to false in the configuration file.

- For a :binary:`~bin.mongos` instance by passing the
:option:`--noscripting <mongos --noscripting>` option on the command line or setting :setting:`security.javascriptEnabled` to false in the configuration file.
