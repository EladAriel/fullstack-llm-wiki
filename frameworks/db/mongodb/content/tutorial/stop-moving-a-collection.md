---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/stop-moving-a-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================

# Stop Moving a Collection

You can stop moving an unsharded collection by using the :dbcommand:`abortMoveCollection` command.

## About this Task

To stop an in-progress :dbcommand:`moveCollection` operation, run the `abortMoveCollection` command on the `admin` database.

## Access Control

If your deployment has `access control <authorization>` enabled, the :authrole:`enableSharding` role allows you to run the `abortMoveCollection` command.

## Steps

## Learn More

- :dbcommand:`abortMoveCollection`
- :method:`sh.abortMoveCollection`
- `moveable-collections`
