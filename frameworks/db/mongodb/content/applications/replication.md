---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/applications/replication.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.726369Z"
---
.. _replica-set-read-write-semantics:

# Replica Set Read and Write Semantics

**meta:** :description: Explore read and write configurations for replica sets, including write concern and read preference settings.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

From the perspective of a client application, whether a MongoDB
instance is running as a single server (i.e. "standalone") or a
:term:`replica set` is transparent. However, MongoDB provides
additional read and write configurations for replica sets.

**note:** :term:`Sharded clusters <sharded cluster>` where the shards are also
   replica sets provide the same operational semantics with regards to
   write and read operations.

:doc:`/core/replica-set-write-concern`
   Write concern describes the level of acknowledgment requested
   from MongoDB for write operations.

:doc:`/core/read-preference`
   Read preference specifies where (i.e. which members of the replica
   set) the drivers should direct the read operations.

:doc:`/core/read-preference-mechanics`
   Describes the mechanics of read preference.


**toctree:** :titlesonly: 
   :hidden: 

   Write Concern </core/replica-set-write-concern>
   Read Preference </core/read-preference>
   Server Selection Algorithm </core/read-preference-mechanics>