---
type: "Framework Learn Page"
framework: "PyMongo"
source_repo: "https://github.com/mongodb/mongo-python-driver"
source_branch: "main"
source_path: "doc/api/pymongo/asynchronous/cursor.rst"
source_commit: "5cf3268f82f21e7683e10a21e0c36fa947e640fa"
source_commit_short: "5cf3268"
source_commit_date: "2026-08-28T14:23:00-04:00"
generated_at: "2026-08-29T09:39:25.624236Z"
---
# :mod:`cursor` -- Tools for iterating over MongoDB query results


**automodule:** pymongo.asynchronous.cursor
   :synopsis: Tools for iterating over MongoDB query results

   .. autoclass:: pymongo.asynchronous.cursor.AsyncCursor(collection, filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False, cursor_type=CursorType.NON_TAILABLE, sort=None, allow_partial_results=False, oplog_replay=False, batch_size=0, collation=None, hint=None, max_scan=None, max_time_ms=None, max=None, min=None, return_key=False, show_record_id=False, snapshot=False, comment=None, session=None, allow_disk_use=None)
      :members:
      :inherited-members:


      .. describe:: c[index]

         See :meth:`__getitem__` and read the warning.

      .. automethod:: __getitem__

   .. autoclass:: pymongo.asynchronous.cursor.AsyncRawBatchCursor(collection, filter=None, projection=None, skip=0, limit=0, no_cursor_timeout=False, cursor_type=CursorType.NON_TAILABLE, sort=None, allow_partial_results=False, oplog_replay=False, batch_size=0, collation=None, hint=None, max_scan=None, max_time_ms=None, max=None, min=None, return_key=False, show_record_id=False, snapshot=False, comment=None, allow_disk_use=None)