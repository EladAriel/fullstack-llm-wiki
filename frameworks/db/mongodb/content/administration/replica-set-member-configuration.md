---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/replica-set-member-configuration.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================================

# Self-Managed Member Configuration Tutorials

The following tutorials provide information on configuring replica set members to support specific operations, such as to provide dedicated backups, to support reporting, or to act as a cold standby.

> **Warning:** .. include:: /includes/warning-mixed-version-rs-config.rst

`/tutorial/adjust-replica-set-member-priority` Change the precedence given to a replica set members in an election for primary.

`/tutorial/configure-secondary-only-replica-set-member` Make a secondary member ineligible for election as primary.

`/tutorial/configure-a-hidden-replica-set-member` Configure a secondary member to be invisible to applications in order to support significantly different usage, such as a dedicated backups.

`/tutorial/configure-a-delayed-replica-set-member` Configure a secondary member to keep a delayed copy of the data set in order to provide a rolling backup.

`/tutorial/configure-a-non-voting-replica-set-member` Create a secondary member that keeps a copy of the data set but does not vote in an election.

`/tutorial/convert-secondary-into-arbiter` Convert a secondary to an arbiter.

## Contents

- Hidden Members </tutorial/configure-a-hidden-replica-set-member>
- Delayed Members </tutorial/configure-a-delayed-replica-set-member>
- Non-Voting Members </tutorial/configure-a-non-voting-replica-set-member>
- Adjust Member Priority </tutorial/adjust-replica-set-member-priority>
- Block Secondary Priority </tutorial/configure-secondary-only-replica-set-member>
- Convert Secondary to Arbiter </tutorial/convert-secondary-into-arbiter>
