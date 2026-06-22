---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-document-max-size.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The maximum BSON document size is 16 mebibytes.

The maximum document size helps ensure that a single document cannot use an excessive amount of RAM or, during transmission, an excessive amount of bandwidth. To store documents larger than the maximum size, MongoDB provides the GridFS API. For more information about GridFS, see :binary:`~bin.mongofiles` and the documentation for your :driver:`driver </>`
