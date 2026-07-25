---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/sh.isBalancerRunning.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

=======================================

# sh.isBalancerRunning() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-no-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Output Document

The following is an example of a document returned by the command:

```json
{
  mode: 'full',
  inBalancerRound: false,
  numBalancerRounds: Long("1143"),
  ok: 1,
  '$clusterTime': {
     clusterTime: Timestamp({ t: 1639753724, i: 3 }),
     signature: {
        hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
        keyId: Long("0")
     }
  },
  operationTime: Timestamp({ t: 1639753724, i: 3 })
}
```

> **Seealso:** - :method:`sh.enableBalancing()`
- :method:`sh.disableBalancing()`
- :method:`sh.getBalancerState()`
- :method:`sh.setBalancerState()`
- :method:`sh.startBalancer()`
- :method:`sh.stopBalancer()`
- :method:`sh.waitForBalancer()`
- :method:`sh.waitForBalancerOff()`
