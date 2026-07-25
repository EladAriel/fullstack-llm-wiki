---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/rank-and-denseRank-behavior.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

- :group:`$rank` and :group:`$denseRank` differ in how they rank duplicate
`sortBy <setWindowFields-sortBy>` field values. For example, with `sortBy <setWindowFields-sortBy>` field values of 7, 9, 9, and 10:

- :group:`$denseRank` ranks the values as 1, 2, 2, and 3. The
duplicate 9 values have a rank of 2, and 10 has a rank of 3. There is no gap in the ranks.

- :group:`$rank` ranks the values as 1, 2, 2, and 4. The duplicate 9
values have a rank of 2, and 10 has a rank of 4. There is a gap in the ranks for 3.

- Documents with a `null` value for a :ref:`sortBy
<setWindowFields-sortBy>` field or documents missing the `sortBy <setWindowFields-sortBy>` field are assigned a rank based on the `BSON comparison order <bson-types-comparison-order>`. See the example in `rank-duplicate-null-missing-values-example`.

- .. include:: /includes/fact-8-0-rank-dense-rank-fix.rst
