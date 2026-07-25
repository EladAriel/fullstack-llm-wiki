---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/move-a-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
