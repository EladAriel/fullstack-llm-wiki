---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/write-concern/write-lifecycle.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.866530Z"
---
.. _write-lifecycle-diagrams:

# Write Lifecycle Diagrams

**meta:** :description: Explore diagrams illustrating the lifecycle of `findAndModify` operations on primary and secondary replica set members.

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

These diagrams show the lifecycle of a :dbcommand:`findAndModify`
operation on primary and secondary replica set members. The lifecycles
of other write commands are similar, but the number of resulting oplog
entries may vary.

## Write Lifecycle on a Primary Member

**figure:** /images/write-lifecycle/write-lifecycle-primary-7-0.png
   :alt: Lifecycle of a findAndModify command on a primary member
   :figwidth: 760px

## Write Lifecycle on a Secondary Member

**figure:** /images/write-lifecycle/write-lifecycle-secondary-7-0.png
   :alt: Lifecycle of a findAndModify command on a secondary member
   :figwidth: 760px