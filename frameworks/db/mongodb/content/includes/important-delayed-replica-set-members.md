---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/includes/important-delayed-replica-set-members.rst"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

> **Important:** If your replica set contains :doc:`delayed members
</core/replica-set-delayed-member>` ensure that the delayed
members are hidden and non-voting.
Hiding delayed replica set members prevents applications from seeing
and querying delayed data without a direct connection to that member.
Making delayed replica set members non-voting means they will not
count towards acknowledging write operations with write concern
:writeconcern:`"majority"`.
If you do not hide delayed members and one or more nodes
become unavailable, the replica set has to wait for the delayed
member and the commit point lags. A lagged commit point can lead to
performance issues.
For example, consider a Primary-Secondary-Delayed replica set
configuration where the delayed secondary is voting with a 10
minute delay.
With one non-delayed secondary unavailable, the degraded configuration
of Primary-Delayed must wait at least 10 minutes to acknowledge a write
operation with :writeconcern:`"majority"`. The majority commit point
will take longer to advance, leading to cache pressure similar
performance issues with a
`Primary with a Secondary and an Arbiter<rs-architecture-psa>`
(PSA) replica set.
For more information on the majority commit point, see
:doc:`Causal Consistency and Read and Write Concerns
</core/causal-consistency-read-write-concerns>`. For additional
details on resolving performance issues see the
`replica set maintenance tutorial<performance-issues-psa>`.
