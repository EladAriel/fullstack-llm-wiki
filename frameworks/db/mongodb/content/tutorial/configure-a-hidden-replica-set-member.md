---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-a-hidden-replica-set-member.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================================

# Configure a Hidden Self-Managed Replica Set Member

Hidden members are part of a `replica set` but cannot become `primary` and are invisible to client applications. Hidden members may vote in `elections <replica-set-elections>`. For more information on hidden members and their uses, see `/core/replica-set-hidden-member`.

## Considerations

The most common use of hidden nodes is to support `backups <backup-restore-sharded-clusters>`.

You can also use hidden nodes to support `delayed members <replica-set-delayed-members>`. However, if you only need to prevent a member from becoming primary, configure a `priority 0 member <replica-set-secondary-only-members>`.

If the :rsconf:`settings.chainingAllowed` setting allows secondary members to sync from other secondaries, MongoDB prefers non-hidden members over hidden members as sync targets. MongoDB only chooses hidden members as a last resort. To override this behavior and sync from a specific, hidden member, use the :dbcommand:`replSetSyncFrom` database command.

> **Seealso:** `chained-replication`

## Examples

### Member Configuration Document

To configure a secondary member as hidden, set its :rsconf:`members[n].priority` value to `0` and set its :rsconf:`members[n].hidden` value to `true` in its member configuration:

```javascript
{
  "_id" : <num>
  "host" : <hostname:port>,
  "priority" : 0,
  "hidden" : true
}
```

### Configuration Procedure

The following example hides the secondary member currently at the index `0` in the :rsconf:`members` array. To configure a `hidden member`, use the following sequence of operations in a :binary:`~bin.mongosh` session that is connected to the primary, specifying the member to configure by its array index in the :rsconf:`members` array:

```javascript
cfg = rs.conf()
cfg.members[0].priority = 0
cfg.members[0].hidden = true
rs.reconfig(cfg)
```

After re-configuring the set, this secondary member has a priority of `0` so that it cannot become primary and is hidden. The other members in the set will not advertise the hidden member in the :dbcommand:`hello` command or :method:`db.hello()` method output.

.. include:: /includes/fact-rs-conf-array-index.rst

.. include:: /includes/warning-rs-reconfig.rst

## Related Documents

- `Replica Set Reconfiguration <replica-set-reconfiguration-usage>`
- `/core/replica-set-elections`
- `Read Preference <replica-set-read-preference>`
