---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/views/supported-operations.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.800739Z"
---
.. _views-supported-operations:

# Supported Operations for Views

**meta:** :description: Explore operations supported for views, including database commands and `mongosh` methods like `find`, `count`, and `aggregate`.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following operations support views:

## Database Commands

- :dbcommand:`collMod`
- :dbcommand:`count`
- :dbcommand:`create`
- :dbcommand:`distinct`
- :dbcommand:`find`


## ``mongosh`` Methods

- :method:`db.collection.aggregate()`
- :method:`db.collection.count()`
- :method:`db.collection.countDocuments()`
- :method:`db.collection.distinct()`
- :method:`db.collection.find()`
- :method:`db.collection.findOne()`
- :method:`db.createCollection()`
- :method:`db.createView()`
- :method:`db.getCollection()`
- :method:`db.getCollectionInfos()`
- :method:`db.getCollectionNames()`