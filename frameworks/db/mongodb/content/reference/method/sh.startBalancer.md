---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.startBalancer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===================================

# sh.startBalancer() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

The :binary:`~bin.mongosh` shell method :method:`sh.startBalancer()` is a wrapper around the :dbcommand:`balancerStart` command. `sh.startBalancer()` runs the `balancerStart` command in the background and returns immediately.

## Learn More

To learn how to configure the balancer for your cluster, see `<sharded-cluster-balancer>`.

To disable balancing for a specific collection, see `<disable-balancer-on-collection>`.

To re-enable balancing on a specific collection, see `<enable-balancer-on-collection>`.

- :method:`sh.getBalancerState()`
- :method:`sh.isBalancerRunning()`
- :method:`sh.setBalancerState()`
- :method:`sh.stopBalancer()`
- :method:`sh.waitForBalancer()`
- :method:`sh.waitForBalancerOff()`
