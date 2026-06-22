---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.addOption.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# cursor.addOption() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Flags

:binary:`~bin.mongosh` provides several additional cursor flags to modify the behavior of the cursor.

## Example

The following example adds the `DBQuery.Option.tailable` flag and the `DBQuery.Option.awaitData` flag to ensure that the query returns a `tailable cursor <tailable-cursors-landing-page>`. The sequence creates a cursor. After returning the full result set, it waits for the default interval of 1000 milliseconds so that it can capture and return additional data added during the query:

```javascript
var t = db.myCappedCollection;
var cursor = t.find().addOption(DBQuery.Option.tailable).
                      addOption(DBQuery.Option.awaitData)
```

> **Warning:** Adding incorrect wire protocol flags can cause problems and/or
extra server load.
