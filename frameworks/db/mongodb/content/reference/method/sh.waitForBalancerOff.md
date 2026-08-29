---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.waitForBalancerOff.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.989850Z"
---
# sh.waitForBalancerOff() (mongosh method)

**meta:** :description: Use `sh.waitForBalancerOff(timeout, interval)` to wait until the balancer is not running, specifying timeout and interval in milliseconds.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Definition

**method:** sh.waitForBalancerOff(timeout, interval)

   Internal method that waits until the balancer is not running.


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``timeout``
   
        - integer
   
        - Milliseconds to wait.
          
          
   
      * - ``interval``
   
        - integer
   
        - Milliseconds to sleep.

**seealso:** - :method:`sh.enableBalancing()`
   - :method:`sh.disableBalancing()`
   - :method:`sh.getBalancerState()`
   - :method:`sh.isBalancerRunning()`
   - :method:`sh.setBalancerState()`
   - :method:`sh.startBalancer()`
   - :method:`sh.stopBalancer()`
   - :method:`sh.waitForBalancer()`

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-no-atlas-support.rst

**include:** /includes/fact-environments-onprem-only.rst