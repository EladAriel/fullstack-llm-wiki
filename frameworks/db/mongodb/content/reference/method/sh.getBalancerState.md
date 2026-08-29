---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.getBalancerState.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.892713Z"
---
# sh.getBalancerState() (mongosh method)

**meta:** :description: Check if the balancer is enabled or disabled using `sh.getBalancerState()` in MongoDB environments.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

**method:** sh.getBalancerState()

   :returns: boolean

   :method:`sh.getBalancerState()` returns ``true`` when the
   :term:`balancer` is enabled and false if the balancer is
   disabled. This does not reflect the current state of balancing
   operations: use :method:`sh.isBalancerRunning()` to check the
   current state of the balancer.

**seealso:** - :method:`sh.enableBalancing()`
   - :method:`sh.disableBalancing()`
   - :method:`sh.isBalancerRunning()`
   - :method:`sh.setBalancerState()`
   - :method:`sh.startBalancer()`
   - :method:`sh.stopBalancer()`
   - :method:`sh.waitForBalancer()`
   - :method:`sh.waitForBalancerOff()`

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst