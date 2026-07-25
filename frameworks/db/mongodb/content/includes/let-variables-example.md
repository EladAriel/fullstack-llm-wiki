---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/let-variables-example.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

The following example:

- Matches documents from the `sample_mflix.movies` collection where the
`imdb.rating` field is greater than 8.5, limited to three results

- Defines a `minRating` variable in `let`, which is referenced in
`$gt` as `$$minRating`
