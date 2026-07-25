---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/search-in-community/create-admin-user-step.rst"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

To create an admin user on your `mongod`, run the following commands, replacing `<password>` with the desired password for the `myAdmin` user:

```javascript
use admin

db.createUser(
  {
    user: "myAdmin",
    pwd: "<password>",
    roles: [
       {
         role: "root",
         db: "admin"
       }
     ]
  } 
)
```
