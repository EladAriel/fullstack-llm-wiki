---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.stopBalancer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# sh.stopBalancer() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

If a balancing round is in progress, the operation waits for balancing to complete.

## Learn More

- :method:`sh.enableBalancing()`
- :method:`sh.disableBalancing()`
- :method:`sh.getBalancerState()`
- :method:`sh.isBalancerRunning()`
- :method:`sh.setBalancerState()`
- :method:`sh.startBalancer()`
- :method:`sh.waitForBalancer()`
- :method:`sh.waitForBalancerOff()`
