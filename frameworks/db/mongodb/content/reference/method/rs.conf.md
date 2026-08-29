---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.conf.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.995243Z"
---
# rs.conf() (mongosh method)

**meta:** :description: Retrieve the current replica set configuration using the `rs.conf()` method in MongoDB.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** rs.conf()

   Returns a document that contains the current :term:`replica set`
   configuration.

   .. |dbcommand| replace:: :dbcommand:`replSetGetConfig` command
   .. include:: /includes/fact-mongosh-shell-method-alt

   .. include:: /includes/extracts/4.4-replSetGetConfiguration-commitmentStatus.rst
   
.. |moreinfo| replace:: The option is only available with the :dbcommand:`replSetGetConfig`
   command.

## Compatibility

This method is available in deployments hosted in the following environments:

**include:** /includes/fact-environments-atlas-only.rst
**include:** /includes/fact-environments-atlas-support-no-free.rst
**include:** /includes/fact-environments-onprem-only.rst

## Output Example

**include:** /includes/replica-set-conf-document-output.rst

For description of the configuration settings, see
:doc:`/reference/replica-configuration`.

**method:** rs.config()

   :method:`rs.config()` is an alias of :method:`rs.conf()`.