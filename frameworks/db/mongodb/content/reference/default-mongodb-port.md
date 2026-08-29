---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/default-mongodb-port.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.687926Z"
---
.. _default-mongodb-port:

# Default MongoDB Port

**meta:** :description: The default TCP ports used by MongoDB for various instances and configurations.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The following table lists the default TCP ports used by MongoDB:

.. list-table::
   :header-rows: 1

   * - Default Port
     - Description

   * - ``27017``

     - Default port for :binary:`~bin.mongod` and :binary:`~bin.mongos`.
       Change this port with :setting:`~net.port` or
       :option:`--port <mongod --port>`.

   * - ``27018``

     - Default port for :binary:`~bin.mongod` when using the 
       :option:`--shardsvr <mongod --shardsvr>` command-line option or
       :setting:`~sharding.clusterRole` set to ``shardsvr``
       in a configuration file.

   * - ``27019``

     - Default port for :binary:`~bin.mongod` when using the
       :option:`--configsvr <mongod --configsvr>` command-line option or
       :setting:`~sharding.clusterRole` set to ``configsvr``
       in a configuration file.

   * - ``27020``

     - Default port on which :binary:`~mongocryptd` listens for
       messages. `MongoDB Enterprise
       Server <https://www.mongodb.com/download-center/enterprise>`__
       includes ``mongocryptd``, which supports automatic encryption
       operations.