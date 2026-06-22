---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/let-variables-example.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

The following example:

- Matches documents from the `sample_mflix.movies` collection where the
`imdb.rating` field is greater than 8.5, limited to three results

- Defines a `minRating` variable in `let`, which is referenced in
`$gt` as `$$minRating`
