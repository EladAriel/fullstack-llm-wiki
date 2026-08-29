---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/model-tree-structures-with-nested-sets.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.643814Z"
---
# Model Tree Structures with Nested Sets

**meta:** :description: Explore how to model tree structures using the Nested Sets pattern, optimizing subtree discovery at the cost of tree mutability.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Overview

This document describes a data model that describes a tree like
structure that optimizes discovering subtrees at the expense of tree
mutability.

## Pattern

.. start-model-tree-structures-include-here

The *Nested Sets* pattern identifies each node in the tree as stops in
a round-trip traversal of the tree. The application visits each node
in the tree twice; first during the initial trip, and second during
the return trip. The *Nested Sets* pattern stores each tree node in a
document; in addition to the tree node, document stores the ID of
node's parent, the node's initial stop in the ``left`` field, and its
return stop in the ``right`` field.

Consider the following hierarchy of categories:

**include:** /images/data-model-example-nested-set.rst

The following example models the tree using *Nested Sets*:

.. code-block:: javascript

   db.categories.insertMany( [
      { _id: "Books", parent: 0, left: 1, right: 12 },
      { _id: "Programming", parent: "Books", left: 2, right: 11 },
      { _id: "Languages", parent: "Programming", left: 3, right: 4 },
      { _id: "Databases", parent: "Programming", left: 5, right: 10 },
      { _id: "MongoDB", parent: "Databases", left: 6, right: 7 },
      { _id: "dbm", parent: "Databases", left: 8, right: 9 }
   ] )

You can query to retrieve the descendants of a node:

.. code-block:: javascript

   var databaseCategory = db.categories.findOne( { _id: "Databases" } );
   db.categories.find( { left: { $gt: databaseCategory.left }, right: { $lt: databaseCategory.right } } );

The *Nested Sets* pattern provides a fast and efficient solution for
finding subtrees but is inefficient for modifying the tree structure.
As such, this pattern is best for static trees that do not change.