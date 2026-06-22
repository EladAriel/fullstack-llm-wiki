---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-tcmalloc-release-rate-compatibility.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

In earlier versions, MongoDB used an older version of `tcmalloc` that:

- Set the default `tcmallocReleaseRate` to `1`.
- Accepted values for `tcmallocReleaseRate` between `0` and `10`,
inclusive.
