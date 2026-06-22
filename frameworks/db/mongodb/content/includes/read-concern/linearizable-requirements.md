---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/read-concern/linearizable-requirements.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Linearizable read concern guarantees only apply if read operations specify a query filter that uniquely identifies a single document. Additionally if none of the following criteria are met, linearizable read concern might not read from a consistent snapshot, resulting in a document matching the filter not being returned:

- The query uses an immutable field as the search key of the query. For
example, searching on the `_id` field or using :operator:`$natural`.

- No concurrent updates mutate the search key of the query.
- The search key has a `unique index <index-type-unique>` and the
query uses that index.

If any of the preceding criteria are met, the query reads from a consistent snapshot to return the single matching document.
