---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.removeUser.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.972087Z"
---
# db.removeUser() (mongosh method)

**meta:** :description: Use `db.dropUser()` to remove a specified username from the database, as `db.removeUser()` is deprecated.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**deprecated:** 2.6

   Use :method:`db.dropUser()` instead
   of :method:`db.removeUser()`

## Definition

**method:** db.removeUser(username)

   Removes the specified username from the database.

   The :method:`db.removeUser()` method has the following parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``username``
   
        - string
   
        - The database username.
          
## Compatibility

This method is available in deployments hosted in the following
environments:

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst