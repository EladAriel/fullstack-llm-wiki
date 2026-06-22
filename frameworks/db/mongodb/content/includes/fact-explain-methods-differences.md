---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-methods-differences.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:method:`db.collection.explain().find() <db.collection.explain()>` is similar to :method:`db.collection.find().explain() <cursor.explain()>` with the following key differences:

- The :method:`db.collection.explain().find() <db.collection.explain()>` construct allows for the
additional chaining of query modifiers. For list of query modifiers, see `db.collection.explain().find().help() <explain-method-help>`.

- The :method:`db.collection.find().explain() <db.collection.explain()>` returns
the `explain()` information on the query plan.
