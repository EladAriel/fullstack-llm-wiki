---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/configuration-and-maintenance.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.762829Z"
---
.. _config-maintenance:

# Configuration and Maintenance

**meta:** :description: Manage routine operations like stopping client processes and archiving log files in MongoDB.
   :robots: noindex, nosnippet
   
.. default-domain:: mongodb

This section describes routine management operations.

:doc:`/tutorial/terminate-running-operations`
   Stop in progress MongoDB client operations using
   :method:`db.killOp()` and :method:`~cursor.maxTimeMS()`.

:doc:`/tutorial/rotate-log-files`
   Archive the current log files and start new ones.

**toctree:** :titlesonly:
   :hidden:

   Terminate Operations </tutorial/terminate-running-operations>
   Rotate Log Files </tutorial/rotate-log-files>