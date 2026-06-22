---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/replica-set-protocol-versions.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Self-Managed Replica Set Protocol Version

MongoDB only supports replica set protocol version 1 (:rsconf:`pv1 <protocolVersion>`). `pv1` is the default for all new replica sets.

## Preservation of Writes

### `w:1` Writes

With :rsconf:`pv1 <protocolVersion>`, you can use :rsconf:`~settings.catchUpTimeoutMillis` to prioritize between faster failovers and preservation of :writeconcern:`w:1 <\<number\>>` writes.

### `w: "majority"` Writes

`pv1` guarantees the preservation of confirmed :writeconcern:`w: "majority" <"majority">` writes.

## Availability

`pv1` is available in MongoDB version 3.2 or later and is the default for all new replica sets.

## Vetoes

`pv1` does not use vetoes. Individual members can vote for or against a candidate in a particular election, but cannot individually veto (abort) an election unilaterally.

## Detection of Simultaneous Primaries

.. include:: /includes/footnote-two-primaries-edge-cases.rst

`pv1` uses the concept of `term`. This allows for a faster detection of simultaneous primaries and for multiple successful elections in a short period of time.

## Back to Back Elections

`pv1` makes a "best-effort" attempt to have the secondary with the highest :rsconf:`~members[n].priority` available call an election. This could lead to back-to-back elections as eligible members with higher priority can call an election.

However, for `pv1`:

- Priority elections have been limited to occur only if the higher
priority node is within 10 seconds of the current primary.

- Arbiters will vote no in elections if they detect a healthy primary
of equal or greater priority to the candidate.

## Double Voting

`pv1` prevents double voting in one member's call for election. This is achieved through its use of `terms <term>`.
