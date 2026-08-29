---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/filemd5.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.051953Z"
---
# filemd5 (database command)

**meta:** :description: Retrieve the md5 hash of a file stored in GridFS using the `filemd5` command to ensure correct file storage in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**important:** Deprecated command

   This command is deprecated and its use is discouraged as MD5 is no
   longer considered cryptographically secure.

## Definition

**dbcommand:** filemd5
   
   The :dbcommand:`filemd5` command returns the :term:`md5` hash for a single
   file stored using the :term:`GridFS` specification. Client libraries
   use this command to verify that files are correctly written to MongoDB.
   The command takes the ``files_id`` of the file in question and the
   name of the GridFS root collection as arguments. 

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
        filemd5: ObjectId("4f1f10e37671b50e4ecd2776"), 
        root: "fs" 
      }
   )

.. read-lock

MongoDB computes the ``filemd5`` using all data in the GridFS file object
pulled sequentially from each chunk in the ``chunks`` collection.