---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/procedure-replica-set-restart-primary.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

Restart the primary member:

#. Connect to the primary using :program:`mongosh`, then use the :method:`rs.stepDown` method to step the member down as the primary:

```javascript
   rs.stepDown()    

The cluster promotes a secondary with the new certificate to serve
as the new primary.
```

#. Use the :method:`db.shutdownServer` method to shut the server down:

```javascript
   use admin
   db.shutdownServer()
```

#. Restart the server.
