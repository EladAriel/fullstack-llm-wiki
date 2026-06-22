---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/replica-set-member-configuration.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
