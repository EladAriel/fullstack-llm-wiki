---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/logout.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.007604Z"
---
# logout (database command)

**meta:** :description: Understand the deprecated `logout` command in MongoDB, which is replaced by closing the connection.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** logout

   .. deprecated:: 5.0

   If you enabled auditing, an attempt to use the :dbcommand:`logout`
   command will create an entry in the audit log.
   
   This command will be removed in a future release.   

   .. note::

      This command was used when you could log in as multiple users on a
      single logical connection. Because this is no longer possible,
      running ``logout`` is no longer supported. Going forward, you can
      achieve the same results by closing your connection.  

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-all.rst

**include:** /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

.. code-block:: javascript

   db.runCommand(
      { 
        logout: 1 
      }
   )


## Example

.. |operation-name| replace:: :dbcommand:`logout`
**include:** /includes/note-logout-namespace.rst

**example:** .. include:: /includes/fact-change-database-context.rst

  When you have set the database context and ``db`` object, you
  can use the |operation-name| to log out of database as in the
  following operation:

  .. code-block:: javascript

     db.runCommand( { logout: 1 } )