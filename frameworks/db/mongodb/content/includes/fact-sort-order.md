---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-sort-order.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

When comparing values of different `BSON types <bson-types>` in sort operations, MongoDB uses the following comparison order, from lowest to highest:

#. MinKey (internal type) #. Null #. Numbers (ints, longs, doubles, decimals) #. Symbol, String #. Object #. Array #. BinData #. ObjectId #. Boolean #. Date #. Timestamp #. Regular Expression #. JavaScript Code #. JavaScript Code with Scope #. MaxKey (internal type)
