---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.stepDown.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

==============================

# rs.stepDown() (mongosh method)

## Description

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

### Concurrent Operations

.. include:: /includes/extracts/rs-stepdown-concurrent-ops.rst

### Availability of Eligible Secondaries

.. include:: /includes/extracts/rs-stepdown-eligible-secondaries.rst

### Client Connections

.. include:: /includes/extracts/rs-stepdown-client-connections.rst

### Writes During Stepdown

.. include:: /includes/extracts/rs-stepdown-write-fail.rst

### Election Handoff

.. include:: /includes/extracts/rs-stepdown-election-handoff.rst
