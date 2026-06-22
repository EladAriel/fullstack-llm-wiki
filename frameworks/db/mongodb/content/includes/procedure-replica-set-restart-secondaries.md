---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/procedure-replica-set-restart-secondaries.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Restart each secondary cluster member:

#. Use :program:`mongosh` to connect to each secondary cluster member, then use the :method:`db.shutdownServer` method to stop the server:

```javascript
   use admin
   db.shutdownServer()
```

#. Restart the server.

#. Use the :method:`rs.status` method to determine the member state:

```javascript
   rs.status().members
```

#. Wait for the `stateStr` field for this member to show a value of :replstate:`SECONDARY`, then restart the next secondary.
