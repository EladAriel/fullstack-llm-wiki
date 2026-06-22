---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-validate-metadata.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Optional. A flag which allows users to perform a quick validation to detect invalid index options without scanning all of the documents and indexes.

- If `true`, a metadata validation scan is performed.
- If `false`, no metadata validation scan is not performed.
The default is `false`.

Running the validate command with `{ metadata: true }` is not supported with any other :dbcommand:`validate` options.

The `metadata` validation option:

- Provides you a faster way of identifying invalid indexes by scanning
only collections metadata.

- Provides an alternative to dropping and recreating multiple invalid
indexes when used with the :dbcommand:`collMod` command.

The `metadata` validation option only scans collection metadata to find invalid indexes more quickly.

If there is an invalid index detected, the validate command will prompt you to use the :dbcommand:`collMod` command to remove invalid indexes.

```javascript
db.runCommand( { collMod: <collectionName> } )
```

.. versionadded:: 5.0.4
