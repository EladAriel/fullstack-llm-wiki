---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/system-users-collection.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=======================================================

# `system.users` Collection in Self-Managed Deployments

The `system.users` collection in the `admin` database stores user `authentication <authentication>` and `authorization <authorization>` information. To manage data in this collection, MongoDB provides `user management commands <user-management-commands>`.

## `system.users` Schema

The documents in the `system.users` collection have the following schema:

```javascript
{
  _id: <system defined id>,
  userId : <system assigned UUID>, 
  user: "<name>",
  db: "<database>",
  credentials: { <authentication credentials> },
  roles: [
           { role: "<role name>", db: "<database>" },
           ...
         ],
  customData: <custom information>,
  authenticationRestrictions : [ <documents> ]
 }
```

Each `system.users` document has the following fields:

## Example

Consider the following document in the `system.users` collection:

```javascript
{
   "_id" : "home.Kari",
   "userId" : UUID("ec1eced7-055a-4ca8-8737-60dd02c52793"), 
   "user" : "Kari",
   "db" : "home",
   "credentials" : {
      "SCRAM-SHA-1" : {
         "iterationCount" : 10000,
         "salt" : "S/xM2yXFosynbCu4GzFDgQ==",
         "storedKey" : "Ist4cgpEd1vTbnRnQLdobgmOsBA=",
         "serverKey" : "e/0DyzS6GPboAA2YNBkGYm87+cg="
      },
      "SCRAM-SHA-256" : {
         "iterationCount" : 15000,
         "salt" : "p1G+fZadAeYAbECN8F/6TMzXGYWBaZ3DtWM0ig==",
         "storedKey" : "LEgLOqZQmkGhd0owm/+6V7VdJUYJcXBhPUvi9z+GBfk=",
         "serverKey" : "JKfnkVv9iXwxyc8JaapKVwLPy6SfnmB8gMb1Pr15T+s="
      }
   },
   "authenticationRestrictions" : [  
      { "clientSource" : [ "69.89.31.226" ], "serverAddress" : [ "172.16.254.1" ] }
   ], 
   "customData" : {
      "zipCode" : "64157"
   },
   "roles" : [
      {
         "role" : "read",
         "db" : "home"
      },
      {
         "role" : "readWrite",
         "db" : "test"
      }
   ]
}
```

The document shows that a user `Kari`'s authentication database is the `home` database. `Kari` has the :authrole:`read` role in the `home` database, the :authrole:`readWrite` role in the `test` database.
