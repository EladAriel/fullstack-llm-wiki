---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/store-javascript-function-on-server.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

:orphan:

=========================================

# Store a JavaScript Function on the Server

> **Important:** Starting in MongoDB 8.0, server side JavaScript is deprecated.
`system.js` functionality may not work with all features.

There is a special system collection named `system.js` that can store JavaScript functions for reuse.

## Before you Begin

This task uses the legacy :binary:`~bin.mongo` shell to load server side functions from the `system.js` collection. This version of the shell is no longer supported. For an alternative solution in the MongoDB Shell, see `mdb-shell-write-scripts`.

## About this Task

Consider the follow recommendations when using `system.js`:

- Do not store application logic in the database.
- There are performance limitations to running JavaScript inside of
MongoDB.

- Application code is most effective when it shares version
control with the application.

## Steps

To store a function, insert the function into the `system.js` collection, as in these examples:
