---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/procedure-replica-set-restart-primary.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
