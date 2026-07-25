---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-explain-methods-differences.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:method:`db.collection.explain().find() <db.collection.explain()>` is similar to :method:`db.collection.find().explain() <cursor.explain()>` with the following key differences:

- The :method:`db.collection.explain().find() <db.collection.explain()>` construct allows for the
additional chaining of query modifiers. For list of query modifiers, see `db.collection.explain().find().help() <explain-method-help>`.

- The :method:`db.collection.find().explain() <db.collection.explain()>` returns
the `explain()` information on the query plan.
