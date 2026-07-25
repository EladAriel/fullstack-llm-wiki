---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-id-field.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

In MongoDB, each document stored in a standard collection requires a unique `_id` field that acts as a `primary key. If an inserted document omits the id` field, the MongoDB driver automatically generates an `objectid for the id` field.

This also applies to documents inserted through update operations with `upsert: true <upsert-parameter>`.
