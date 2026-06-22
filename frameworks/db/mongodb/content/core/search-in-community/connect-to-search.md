---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/search-in-community/connect-to-search.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

:noprevnext:

===================================

# Connect to MongoDB Search Community

Estimated completion time: 5 minutes

To use {+mdb-search-full+}, you must connect to your MongoDB Community deployment. Use the following methods to connect to your MongoDB Community deployment:

- :mdb-shell:`The MongoDB Shell </>`, an interactive
command line interface to MongoDB.

- :compass:`MongoDB Compass </>`, a GUI for your MongoDB data.
- :driver:`A MongoDB driver </>`. To see all available languages, refer to the
:driver:`MongoDB Driver documentation </>`.

|arrow| Use the **Select your language** drop-down menu to set the client for the procedure on this page.

## Prerequisites

Before you start, you must have the following prerequisites:

- `MongoDB Community <install-mdb-community-edition>` and
`MongoDB Search Community <community-search-deploy>`

> **Note:**   Make sure that both the `mongod` and `mongot` processes are
  running.

- Valid username and password to connect
If you haven't already created a user on your replica set, run the following commands in your terminal to create a user:

a. Connect to replica set by using `mongosh`.

```shell
     mongosh 

#. Run the following commands to create a ``mongotUser`` user in
  the ``admin`` database with the :authrole:`searchCoordinator` role. MongoDB
  uses the ``mongotUser`` user to authenticate ``mongot`` with ``mongod``. 

  .. code-block:: javascript
     :copyable: true 

     use admin
     db.createUser( {
      user: "mongotUser",
      pwd: passwordPrompt(),
         roles: [ { role: "searchCoordinator", db: "admin" } ]
     } )

  .. include:: /includes/search-in-community/grant-searchCoordinator-role.rst
```

- `Connection string to the replica set <mongodb-uri>`
The connection string for a replica set includes all member nodes. Therefore, you need the replica set name and the hostnames or IP addresses and ports of all the replica set members to connect.

## Connect to Your Replica Set

Use your replica set's `connection string <mongodb-uri>` to connect to your replica set with your preferred client. To ensure that you configured `mongot` and `mongod` correctly, you can run a command that retrieves search indexes.

## Next Steps

Now that you've connected to your replica set, proceed to :atlas:`Query with {+mdb-search-full+} </atlas-search/tutorial>`.
