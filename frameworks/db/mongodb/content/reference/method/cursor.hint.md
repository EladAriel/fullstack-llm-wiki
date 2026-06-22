---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.hint.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================

# cursor.hint() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

- When an `index filter <index-filters>` exists for the query
shape, MongoDB ignores the :method:`~cursor.hint()`.

- .. include:: /includes/fact-hint-text-query-restriction.rst
- If you use :method:`~cursor.hint()` on a :doc:`hidden index
</core/index-hidden>` or an index that doesn't exist, the operation returns an error.

- On a `time series collections <time series collection>`, you
can only specify hints using the index name, not the index key pattern.

- .. include:: /includes/hints-precedence.rst
### $natural

Use `$natural` in conjunction with `cursor.hint()` to perform a collection scan to return documents in `natural order`.

For usage, see `hint-collection-scans`.

> **Note:** .. include:: /includes/natural-sort-7.0-breaking-change.rst

## Examples

### Specify an Index

The following example returns all documents in the collection named `users` using the index on the `age` field.

```javascript
db.users.find().hint( { age: 1 } )
```

You can also specify the index using the index name:

```javascript
db.users.find().hint( "age_1" )
```

### Force Collection Scans

You can specify `{ $natural : 1 }` to force the query to perform a forwards collection scan:

```javascript
db.users.find().hint( { $natural : 1 } )
```

You can also specify `{ $natural : -1 }` to force the query to perform a reverse collection scan:

```javascript
db.users.find().hint( { $natural : -1 } )
```

> **Seealso:** - `/indexes`
- `/core/query-plans`
- `index-filters`
