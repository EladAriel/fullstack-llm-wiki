---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/procedure-replica-set-restart-secondaries.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
