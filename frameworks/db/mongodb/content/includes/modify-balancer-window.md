---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/modify-balancer-window.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

- Set the `activeWindow` parameter.
Using `activeWindow` sets the balancing window to be the same everyday. Set the `activeWindow` using :method:`~db.collection.updateOne()`:

- Set the `activeWindowDOW` parameter.
`activeWindowDOW` allows you to specify balancing windows for different days of the week. Set the `activeWindowDOW` using :method:`~db.collection.updateOne()`.

For example, to set the balancing window to be from 9:00am to 5:00pm from Monday to Friday, and all day on Saturday and Sunday, you would run the following:
