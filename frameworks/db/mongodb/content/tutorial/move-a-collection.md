---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/move-a-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================

# Move a Collection

Starting in MongoDB 8.0, you can move an unsharded collection to a different shard using the :dbcommand:`moveCollection` command.

## About this Task

.. include:: /includes/mc-considerations.rst

## Access Control

If your deployment has `access control <authorization>` enabled, the :authrole:`enableSharding` role grants you access to run the `moveCollection` command.

## Before you Begin

.. include:: /includes/mc-reqs.rst

## Steps

## Learn More

- `moveable-collections`
- :dbcommand:`moveCollection`
- :method:`sh.moveCollection`
