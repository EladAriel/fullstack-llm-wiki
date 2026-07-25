---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-tree-structures-with-materialized-paths.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=============================================

# Model Tree Structures with Materialized Paths

## Overview

This page describes a data model that describes a tree-like structure in MongoDB documents by storing full relationship paths between documents.

## Pattern

The Materialized Paths pattern stores each tree node in a document; in addition to the tree node, document stores as a string the id(s) of the node's ancestors or path. Although the Materialized Paths pattern requires additional steps of working with strings and regular expressions, the pattern also provides more flexibility in working with the path, such as finding nodes by partial paths.

Consider the following hierarchy of categories:

.. include:: /images/data-model-tree.rst

The following example models the tree using Materialized Paths, storing the path in the field `path`; the path string uses the comma `,` as a delimiter:

```javascript
db.categories.insertMany( [
   { _id: "Books", path: null },
   { _id: "Programming", path: ",Books," },
   { _id: "Databases", path: ",Books,Programming," },
   { _id: "Languages", path: ",Books,Programming," },
   { _id: "MongoDB", path: ",Books,Programming,Databases," },
   { _id: "dbm", path: ",Books,Programming,Databases," }
] )
```

- You can query to retrieve the whole tree, sorting by the field
`path`:

```javascript
  db.categories.find().sort( { path: 1 } )
```

- You can use regular expressions on the `path` field to find the
descendants of `Programming`:

```javascript
  db.categories.find( { path: /,Programming,/ } )
```

- You can also retrieve the descendants of `Books` where the
`Books` is also at the topmost level of the hierarchy:

```javascript
  db.categories.find( { path: /^,Books,/ } )
```

- To create an index on the field `path` use the following
invocation:

```javascript
  db.categories.createIndex( { path: 1 } )

This index may improve performance depending on the query:

- For queries from the root ``Books`` sub-tree (e.g. ``/^,Books,/``
 or ``/^,Books,Programming,/``), an index on the ``path`` field
 improves the query performance significantly.

- For queries of sub-trees where the path from the root is not
 provided in the query (e.g. ``/,Databases,/``), or similar queries
 of sub-trees, where the node might be in the middle of the indexed
 string, the query must inspect the entire index.

 For these queries an index *may* provide some performance
 improvement *if* the index is significantly smaller than the
 entire collection.
```
