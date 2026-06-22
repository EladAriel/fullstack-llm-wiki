---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/administration/replica-set-deployment.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=============================================

# Self-Managed Replica Set Deployment Tutorials

The following tutorials provide information on deploying replica sets.

`server-replica-set-deploy` Configure a three-member replica set for production systems.

`server-replica-set-deploy-test` Configure a three-member replica set for either development or testing systems.

`server-replica-set-deploy-geo` Create a geographically redundant replica set to protect against location-centered availability limitations (e.g. network and power interruptions).

`server-replica-set-deploy-arbiter` Add an arbiter to give a replica set an odd number of voting members to prevent election ties.

`server-replica-set-deploy-convert` Convert an existing standalone `mongod` instance into a three-member replica set.

`server-replica-set-deploy-expand` Add a new member to an existing replica set.

`server-replica-set-remove-member` Remove a member from a replica set.

`server-replica-set-replace-member` Update the replica set configuration when the hostname of a member's corresponding `mongod` instance has changed.

## Contents

- Replica Set </tutorial/deploy-replica-set>
- Convert to Replica Set </tutorial/convert-standalone-to-replica-set>
- Add Members </tutorial/expand-replica-set>
- Add an Arbiter </tutorial/add-replica-set-arbiter>
- Remove Members </tutorial/remove-replica-set-member>
- Replace a Member </tutorial/replace-replica-set-member>
- Test & Development Replica Sets </tutorial/deploy-replica-set-for-testing>
- Geographically Redundant Replica Sets </tutorial/deploy-geographically-distributed-replica-set>
