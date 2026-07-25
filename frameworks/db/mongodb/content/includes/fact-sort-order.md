---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-sort-order.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

When comparing values of different `BSON types <bson-types>` in sort operations, MongoDB uses the following comparison order, from lowest to highest:

#. MinKey (internal type) #. Null #. Numbers (ints, longs, doubles, decimals) #. Symbol, String #. Object #. Array #. BinData #. ObjectId #. Boolean #. Date #. Timestamp #. Regular Expression #. JavaScript Code #. JavaScript Code with Scope #. MaxKey (internal type)
