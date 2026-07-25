---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-tree-structures-with-child-references.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# Model Tree Structures with Child References

## Overview

This page describes a data model that describes a tree-like structure in MongoDB documents by storing `references <data-modeling-referencing>` in the parent-nodes to children nodes.

## Pattern

The Child References pattern stores each tree node in a document; in addition to the tree node, document stores in an array the id(s) of the node's children.

Consider the following hierarchy of categories:

.. include:: /images/data-model-tree.rst

The following example models the tree using Child References, storing the reference to the node's children in the field `children`:

```javascript
db.categories.insertMany( [
   { _id: "MongoDB", children: [] },
   { _id: "dbm", children: [] },
   { _id: "Databases", children: [ "MongoDB", "dbm" ] },
   { _id: "Languages", children: [] },
   { _id: "Programming", children: [ "Databases", "Languages" ] },
   { _id: "Books", children: [ "Programming" ] }
] )
```

- The query to retrieve the immediate children of a node is fast and
straightforward:

```javascript
  db.categories.findOne( { _id: "Databases" } ).children
```

- You can create an index on the field `children` to enable fast
search by the child nodes:

```javascript
  db.categories.createIndex( { children: 1 } )
```

- You can query for a node in the `children` field to find its parent
node as well as its siblings:

```javascript
  db.categories.find( { children: "MongoDB" } )
```

The Child References pattern provides a suitable solution to tree storage as long as no operations on subtrees are necessary. This pattern may also provide a suitable solution for storing graphs where a node may have multiple parents.
