---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.waitForBalancer.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:20.003691Z"
---
# sh.waitForBalancer() (mongosh method)

**meta:** :description: Use `sh.waitForBalancer()` to monitor changes in the balancer's state, with options for wait, timeout, and interval settings.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.waitForBalancer(wait, timeout, interval)

   Waits for a change in the state of the balancer.
   :method:`sh.waitForBalancer()` is an internal method, which takes
   the following arguments:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``wait``
   
        - boolean
   
        - Optional. Set to ``true`` to ensure the balancer is now active. The
          default is ``false``, which waits until balancing stops
          and becomes inactive.
          
          
   
      * - ``timeout``
   
        - integer
   
        - Milliseconds to wait.
          
          
   
      * - ``interval``
   
        - integer
   
        - Milliseconds to sleep.
          
          
## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst