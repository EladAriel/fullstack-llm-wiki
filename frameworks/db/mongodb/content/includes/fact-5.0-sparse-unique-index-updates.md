---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-5.0-sparse-unique-index-updates.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

Starting in MongoDB 5.0, `unique sparse <sparse-unique-index>` and `unique non-sparse <unique-index>` indexes with the same `key pattern<key_patterns>` can exist on a single collection.

Unique and Sparse Index Creation ````````````````````````````````

This example creates multiple indexes with the same key pattern and different `sparse` options:

Basic and Sparse Index Creation ```````````````````````````````

You can also create basic indexes with the same key pattern with and without the sparse option:
