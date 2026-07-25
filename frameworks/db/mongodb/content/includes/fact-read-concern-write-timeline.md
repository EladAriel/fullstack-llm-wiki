---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-read-concern-write-timeline.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Consider the following timeline of a write operation Write\ :sub:`0` to a three member replica set:

> **Note:** For simplification, the example assumes:
- All writes prior to Write\ :sub:`0` have been successfully
  replicated to all members.
- Write\ :sub:`prev` is the previous write before Write\ :sub:`0`.
- No other writes have occured after Write\ :sub:`0`.

.. figure:: /images/read-concern-write-timeline.svg
