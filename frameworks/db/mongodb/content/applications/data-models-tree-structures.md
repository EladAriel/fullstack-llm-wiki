---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/data-models-tree-structures.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=====================

# Model Tree Structures

MongoDB allows various ways to use tree data structures to model large hierarchical or nested data relationships.

.. include:: /images/data-model-tree.rst

`/tutorial/model-tree-structures-with-parent-references` Presents a data model that organizes documents in a tree-like structure by storing `references <data-modeling-referencing>` to "parent" nodes in "child" nodes.

`/tutorial/model-tree-structures-with-child-references` Presents a data model that organizes documents in a tree-like structure by storing `references <data-modeling-referencing>` to "child" nodes in "parent" nodes.

`/tutorial/model-tree-structures-with-ancestors-array` Presents a data model that organizes documents in a tree-like structure by storing `references <data-modeling-referencing>` to "parent" nodes and an array that stores all ancestors.

`/tutorial/model-tree-structures-with-materialized-paths Presents a data model that organizes documents in a tree-like structure by storing full relationship paths between documents. In addition to the tree node, each document stores the id` of the nodes ancestors or path as a string.

`/tutorial/model-tree-structures-with-nested-sets` Presents a data model that organizes documents in a tree-like structure using the Nested Sets pattern. This optimizes discovering subtrees at the expense of tree mutability.

## Contents

- Parent References </tutorial/model-tree-structures-with-parent-references>
- Child References </tutorial/model-tree-structures-with-child-references>
- Array of Ancestors </tutorial/model-tree-structures-with-ancestors-array>
- Materialized Paths </tutorial/model-tree-structures-with-materialized-paths>
- Nested Sets </tutorial/model-tree-structures-with-nested-sets>
