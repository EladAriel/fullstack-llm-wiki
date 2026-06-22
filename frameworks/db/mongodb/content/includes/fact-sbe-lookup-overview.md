---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-sbe-lookup-overview.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Starting in version 6.0, MongoDB can use the `slot-based execution query engine <sbe-landing>` to execute :pipeline:`$lookup` stages if all preceding stages in the pipeline can also be executed by the |sbe-short| and none of the following conditions are true:

- The `$lookup` operation executes a pipeline on a foreign collection.
To see an example of this kind of operation, see `lookup-syntax-let-pipeline`.

- The `$lookup`'s `localField` or `foreignField` specify numeric
components. For example: `{ localField: "restaurant.0.review" }`.

- The `from` field of any `$lookup` in the pipeline specifies a view
or sharded collection.
