---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.getProfilingStatus.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.994414Z"
---
# db.getProfilingStatus() (mongosh method)

**meta:** :description: Retrieve the current profiling status, including profile level, slow operation threshold, and sample rate settings.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** db.getProfilingStatus()

   :returns: The current :dbcommand:`profile` level,
             :setting:`~operationProfiling.slowOpThresholdMs` setting,
             :setting:`~operationProfiling.slowOpInProgressThresholdMs` setting,
             and :setting:`~operationProfiling.slowOpSampleRate` setting.

             You can set a ``filter`` to control which operations are logged by 
             the profiler. When set, any configured filters are also returned by
             :method:`db.getProfilingStatus()`, along with a ``note``
             explaining filter behavior.
 
             You can set the profiling filter with either:
             
             - the :method:`db.setProfilingLevel()` shell method, or

             - the :setting:`operationProfiling.filter` configuration file option.

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst