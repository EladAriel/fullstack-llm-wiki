---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/replica-set-high-availability.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.511767Z"
---
.. _replica-set-failover-administration:
.. _replica-set-failover:
.. _failover:

# Replica Set High Availability

**meta:** :description: Understand how replica sets use elections to maintain high availability and manage rollbacks during failovers.
   :robots: noindex, nosnippet

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

Replica sets use elections to support 
:term:`high availability <high availability>`. 

:doc:`/core/replica-set-elections`
   Elections occur when the primary becomes unavailable and the
   replica set members autonomously select a new primary.

:doc:`/core/replica-set-rollbacks`
   A rollback reverts write operations on a former primary when the
   member rejoins the replica set after a failover.


**toctree:** :titlesonly: 
   :hidden: 

   Elections </core/replica-set-elections>
   Failover Rollbacks </core/replica-set-rollbacks>