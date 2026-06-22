---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/replace-replica-set-member.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================================

# Replace a Self-Managed Replica Set Member

If you need to change the hostname of a replica set member without changing the configuration of that member or the set, you can use the operation outlined in this tutorial. For example if you must re-provision systems or rename hosts, you can use this pattern to minimize the scope of that change.

## Operation

To change the hostname for a replica set member modify the :rsconf:`members[n].host` field. The value of :rsconf:`members[n]._id` field will not change when you reconfigure the set.

See `/reference/replica-configuration` and :method:`rs.reconfig()` for more information.

> **Note:** Any replica set configuration change can trigger the current
`primary` to step down, which forces an :ref:`election
<replica-set-elections>`. During the election, the current shell
session and clients connected to this replica set disconnect,
which produces an error even when the operation succeeds.

## Example

To change the hostname to `mongo2.example.net` for the replica set member configured at `members[0]`, issue the following sequence of commands:

```javascript
cfg = rs.conf()
cfg.members[0].host = "mongo2.example.net"
rs.reconfig(cfg)
```
