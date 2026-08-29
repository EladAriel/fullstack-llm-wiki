---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/core/storage-engines.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.510692Z"
---
.. _storage-engines:

# Storage Engines for Self-Managed Deployments

**meta:** :keywords: on-prem
   :description: Explore different storage engines in MongoDB, including WiredTiger and In-Memory, to optimize data management for specific workloads.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

The :term:`storage engine` is the component of the database that is
responsible for managing how data is stored, both in memory and on disk.
MongoDB supports multiple storage engines, as different engines perform
better for specific workloads. Choosing the appropriate storage engine
for your use case can significantly impact the performance of your
applications.

|arrow| WiredTiger Storage Engine (*Default*)
   :ref:`WiredTiger <storage-wiredtiger>` is the default storage engine and is 
   recommended for new deployments. WiredTiger provides a document-level 
   concurrency model, checkpointing, and compression, among other features. 
   
   In MongoDB Enterprise, WiredTiger also supports
   :doc:`/core/security-encryption-at-rest`. See
   :ref:`encrypted-storage-engine`.

|arrow| In-Memory Storage Engine
   An :ref:`In-Memory storage engine <storage-inmemory>` is available 
   in MongoDB Enterprise. Rather than storing documents on-disk, it
   retains them in-memory for more predictable data latencies.

**toctree:** :titlesonly: 
   :hidden: 

   WiredTiger </core/self-managed-wiredtiger>
   In-Memory </core/inmemory>

.. |arrow| unicode:: U+27A4