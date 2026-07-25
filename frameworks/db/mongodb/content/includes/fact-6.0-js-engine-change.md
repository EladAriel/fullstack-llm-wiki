---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-6.0-js-engine-change.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

MongoDB 6.0 upgrades the internal JavaScript engine used for `server-side JavaScript <server-side-javascript>`, :group:`$accumulator`, :expression:`$function`, and :query:`$where` expressions and from MozJS-60 to MozJS-91. Several deprecated, non-standard array and string functions that existed in MozJS-60 are removed in MozJS-91.
