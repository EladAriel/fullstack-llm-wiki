---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.waitForPingChange.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.003970Z"
---
# sh.waitForPingChange() (mongosh method)

**meta:** :description: Use `sh.waitForPingChange()` to monitor changes in ping state for specified active pings with customizable timeout and interval settings.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.waitForPingChange(activePings, timeout, interval)

   :method:`sh.waitForPingChange()` waits for a change in ping state
   of one of the ``activepings``, and only returns when the specified
   ping changes state.


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``activePings``
   
        - array
   
        - An array of active pings from the :data:`~config.mongos` collection.
          
          
   
      * - ``timeout``
   
        - integer
   
        - Number of milliseconds to wait for a change in ping state.
          
          
   
      * - ``interval``
   
        - integer
   
        - Number of milliseconds to sleep in each waiting cycle.
          
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst          
   