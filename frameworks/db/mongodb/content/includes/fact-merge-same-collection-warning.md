---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-merge-same-collection-warning.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Warning:** When :pipeline:`$merge` outputs to the same collection that is being
aggregated, documents may get updated multiple times or the operation
may result in an infinite loop. This behavior occurs when the update
performed by :pipeline:`$merge` changes the physical location of
documents stored on disk. When the physical location of a document
changes, :pipeline:`$merge` may view it as an entirely new document,
resulting in additional updates. For more information on this
behavior, see `Halloween Problem
<https://en.wikipedia.org/wiki/Halloween_Problem>`__.
