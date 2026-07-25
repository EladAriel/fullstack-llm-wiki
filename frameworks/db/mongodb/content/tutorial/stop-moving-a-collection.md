---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/stop-moving-a-collection.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
