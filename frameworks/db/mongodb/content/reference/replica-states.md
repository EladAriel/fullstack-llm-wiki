---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/replica-states.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
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
