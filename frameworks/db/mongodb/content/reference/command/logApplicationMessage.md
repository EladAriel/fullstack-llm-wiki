---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/logApplicationMessage.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.016016Z"
---
# logApplicationMessage (database command)

**meta:** :description: Post custom messages to the audit log using the `logApplicationMessage` command, requiring `clusterAdmin` role for authorization.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**dbcommand:** logApplicationMessage

   The :dbcommand:`logApplicationMessage` command allows users to post
   a custom message to the :ref:`audit <auditing>` log. If
   running with authorization, users must have :authrole:`clusterAdmin`
   role, or roles that inherit from :authrole:`clusterAdmin`, to run
   the command.

## Compatibility

This command is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-onprem-only.rst
   
## Syntax

The command has the following syntax:

.. code-block:: javascript
   
   db.runCommand(
      {  
        logApplicationMessage: <string> 
      }
   )

## Behavior

MongoDB associates these custom messages with the :ref:`audit
operation <audit-action-details-results>` ``applicationMessage``,
and the messages are subject to any :ref:`filtering <audit-filter>`.