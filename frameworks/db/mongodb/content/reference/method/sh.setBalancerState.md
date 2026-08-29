---
type: "Framework Learn Page"
framework: "MongoDB"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.setBalancerState.txt"
source_commit: "b9f2bc487a2878b65e3c1f80024bebab76954f27"
source_commit_short: "b9f2bc48"
source_commit_date: "2026-08-28T17:09:45-05:00"
generated_at: "2026-08-29T09:39:19.915412Z"
---
# sh.setBalancerState() (mongosh method)

**meta:** :description: Enable or disable the balancer using `sh.setBalancerState()` on a `mongos` instance, affecting shard balance and performance.

.. default-domain:: mongodb

**contents:** On this page
   :local:
   :backlinks: none
   :depth: 1
   :class: singlecol

## Description

**method:** sh.setBalancerState(state)

   Enables or disables the :term:`balancer`.

   .. include:: /includes/autosplit-no-operation.rst

   In MongoDB versions earlier than 6.0.3,
   :method:`sh.setBalancerState()` also enables auto-splitting if
   enabling the balancer and disables auto-splitting if disabling the
   balancer.

   Use :method:`sh.getBalancerState()` to determine if the balancer is
   currently enabled or disabled and :method:`sh.isBalancerRunning()`
   to check its current state.

   .. |dbcommand| replace:: :dbcommand:`balancerStart` and
      :dbcommand:`balancerStop` commands
   .. include:: /includes/fact-mongosh-shell-method-alt.rst


   .. important::

      You can only run :method:`sh.setBalancerState()` on a
      :binary:`~bin.mongos` instance. :method:`sh.setBalancerState()`
      errors if run on :binary:`~bin.mongod` instance.

   The :method:`sh.setBalancerState()` method has the following
   parameter:


   .. list-table::
      :header-rows: 1
      :widths: 20 20 80
   
      * - Parameter
   
        - Type
   
        - Description
   
      * - ``state``
   
        - boolean
   
        - Set this to ``true`` to enable the balancer and ``false`` to
          disable it.

          .. include:: /includes/sharding/disable-balancer-warning.rst

## Compatibility

This method is available in deployments hosted in the following environments: 

**include:** /includes/fact-environments-atlas-only.rst

**include:** /includes/fact-environments-atlas-support-no-free.rst

**include:** /includes/fact-environments-onprem-only.rst

## Learn More

- :method:`sh.enableBalancing()`
- :method:`sh.disableBalancing()`
- :method:`sh.getBalancerState()`
- :method:`sh.isBalancerRunning()`
- :method:`sh.startBalancer()`
- :method:`sh.stopBalancer()`
- :method:`sh.waitForBalancer()`
- :method:`sh.waitForBalancerOff()`