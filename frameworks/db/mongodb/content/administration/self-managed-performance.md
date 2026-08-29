---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/self-managed-performance.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.761125Z"
---
.. _self-managed-performance:

# Self-Managed Performance

.. default-domain:: mongodb

**include:** /includes/health-manager-short-names.rst

Learn how to monitor and improve performance for self-managed
deployments.

:ref:`TCMalloc Performance Optimization <tcmalloc-performance>`
   Learn how to use TCMalloc to reduce memory fragmentation and make
   your database more resilient to high-stress workloads. 

:ref:`Health Managers <health-managers-overview>`
   Learn how to use |HMS| to monitor and manage sharded cluster health
   issues.

:ref:`UNIX ulimit Settings <ulimit>`
   Learn how to configure ulimit settings to control the use of system
   resources such as threads, files, and network connections.

:ref:`Full Time Diagnostic Data Capture <self-managed-ftdc>`
   Learn how MongoDB uses diagnostic data to analyze server behavior.

**toctree:** :titlesonly:
   :hidden:

   TCMalloc Performance </administration/tcmalloc-performance>
   Health Managers </administration/health-managers>
   UNIX ulimit </reference/ulimit>
   Full Time Diagnostic Data Capture </administration/full-time-diagnostic-data-capture>