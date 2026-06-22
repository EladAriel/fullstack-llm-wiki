---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-6.0-js-engine-change.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB 6.0 upgrades the internal JavaScript engine used for `server-side JavaScript <server-side-javascript>`, :group:`$accumulator`, :expression:`$function`, and :query:`$where` expressions and from MozJS-60 to MozJS-91. Several deprecated, non-standard array and string functions that existed in MozJS-60 are removed in MozJS-91.
