---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-multiple-cursor-monitors.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

MongoDB provides multiple ways to iterate on a cursor.

The :method:`cursor.hasNext()` method blocks and waits for the next event. To monitor the `watchCursor` cursor and iterate over the events, use `hasNext()` like this:

```javascript
while (!watchCursor.isClosed()) {
   if (watchCursor.hasNext()) {
     firstChange = watchCursor.next();
     break;
   }
}
```

The :method:`cursor.tryNext()` method is non-blocking. To monitor the `watchCursor` cursor and iterate over the events, use `tryNext()` like this:

```javascript
while (!watchCursor.isClosed()) {
  let next = watchCursor.tryNext()
  while (next !== null) {
    printjson(next);
    next = watchCursor.tryNext()
  }
}
```
