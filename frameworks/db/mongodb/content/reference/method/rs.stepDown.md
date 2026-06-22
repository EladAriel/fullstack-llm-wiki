---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/rs.stepDown.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
