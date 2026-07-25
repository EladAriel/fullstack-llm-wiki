---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/modify-balancer-window.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- Set the `activeWindow` parameter.
Using `activeWindow` sets the balancing window to be the same everyday. Set the `activeWindow` using :method:`~db.collection.updateOne()`:

- Set the `activeWindowDOW` parameter.
`activeWindowDOW` allows you to specify balancing windows for different days of the week. Set the `activeWindowDOW` using :method:`~db.collection.updateOne()`.

For example, to set the balancing window to be from 9:00am to 5:00pm from Monday to Friday, and all day on Saturday and Sunday, you would run the following:
