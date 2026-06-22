---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/store-javascript-function-on-server.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
