---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/cursor.limit.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# cursor.limit() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Supported Values

The behavior of :method:`~cursor.limit()` is undefined for values less than -2\ :sup:`31` and greater than 2\ :sup:`31`.

You must specify a numeric value for :method:`~cursor.limit()`.

### Zero Value

A :method:`~cursor.limit()` value of 0 (i.e. :method:`.limit(0) <cursor.limit()>`) is equivalent to setting no limit.

### Negative Values

A negative limit is similar to a positive limit but closes the cursor after returning a single `batch <cursor-batches>` of results. As such, with a negative limit, if the limited result set does not fit into a single batch, the number of documents received will be less than the specified limit. By passing a negative limit, the client indicates to the server that it will not ask for a subsequent batch via `getMore`.

### Using `limit()` with `sort()`

If using :method:`~cursor.limit()` with :method:`~cursor.sort()`, be sure to include at least one field in your sort that contains unique values, before passing results to :method:`~cursor.limit()`.

Sorting on fields that contain duplicate values may return an inconsistent sort order for those duplicate fields over multiple executions, especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the `_id` field in your sort query.

See `Consistent sorting with the sort() method <sort-cursor-consistent-sorting>` for more information.

### Using `limit()` with `skip()`

.. include:: includes/reference/skip-limit.rst
