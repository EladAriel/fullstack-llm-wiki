---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.maxAwaitTimeMS.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

========================================

# cursor.maxAwaitTimeMS() (mongosh method)

## Definition

> **Important:** This method, :method:`~cursor.maxAwaitTimeMS()`, sets a limit on how
long a `tailable cursor <tailable-cursors-landing-page>` waits
for the next response. :method:`~cursor.maxTimeMS()` sets a limit on
total processing time.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Example

Query the `capped <manual-capped-collection>` `sales` collection to find agent Mary Kay's weekly sales totals:

```javascript
db.sales.find( 
   { agent: "Mary Kay" },
   { _id: 0, agent: 1, weeklyTotal: 1  }
).tailable( { awaitData: true } ).maxAwaitTimeMS( 1000 )
```

The highlighted line creates a `tailable cursor <tailable-cursors-landing-page>` on the `sales` collection. The :method:`~cursor.maxAwaitTimeMS()` sets a one second maximum wait time for the next cursor update.
