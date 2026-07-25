---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/fact-multiple-cursor-monitors.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
