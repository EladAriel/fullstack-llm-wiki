---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-a-delayed-replica-set-member.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===================================================

# Configure a Delayed Self-Managed Replica Set Member

To configure a delayed secondary member, set its :rsconf:`members[n].priority` value to `0`, its :rsconf:`members[n].hidden` value to `true`, and its :rsconf:`members[n].secondaryDelaySecs` value to the number of seconds to delay.

> **Important:** The length of the secondary
:rsconf:`members[n].secondaryDelaySecs` must
fit within the window of the oplog. If the oplog is shorter than
the :rsconf:`members[n].secondaryDelaySecs`
window, the delayed member cannot successfully replicate
operations.

When you configure a delayed member, the delay applies both to replication and to the member's `oplog`. For details on delayed members and their uses, see `/core/replica-set-delayed-member`.

## Example

The following example sets a 1-hour delay on a secondary member currently at the index `0` in the :rsconf:`members` array. To set the delay, issue the following sequence of operations in a :binary:`~bin.mongosh` session that is connected to the primary:

```javascript
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[0].hidden = true
cfg.members[0].secondaryDelaySecs = 3600
rs.reconfig(cfg)
```

After the replica set reconfigures, the delayed secondary member cannot become `primary` and is hidden from applications. The :rsconf:`members[n].secondaryDelaySecs` value delays both replication and the member's `oplog` by 3600 seconds (1 hour).

.. include:: /includes/fact-rs-conf-array-index.rst

.. include:: /includes/warning-rs-reconfig.rst

## Related Documents

- :rsconf:`members[n].secondaryDelaySecs`
- :ref:`Replica Set Reconfiguration
<replica-set-reconfiguration-usage>`

- `replica-set-oplog-sizing`
- `/tutorial/change-oplog-size` tutorial
- `/core/replica-set-elections`
