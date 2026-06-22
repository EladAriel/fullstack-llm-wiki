---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/replica-states.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Replica Set Member States

Each member of a replica set has a state.

.. include:: /includes/replica-states.rst

## States

### Core States

See `/core/replica-set-members` for more information on core states.

### Other States

### Error States

Members in any error state can't vote.

.. include:: /includes/footnote-two-primaries-edge-cases.rst
