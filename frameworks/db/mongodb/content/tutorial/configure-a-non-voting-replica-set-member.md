---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/configure-a-non-voting-replica-set-member.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

======================================================

# Configure a Non-Voting Self-Managed Replica Set Member

Non-voting members allow you to add additional members for read distribution beyond the maximum seven voting members.

To configure a member as non-voting, use the :dbcommand:`replSetReconfig` command or its :binary:`~bin.mongosh` helper method :method:`rs.reconfig()` to set its :rsconf:`members[n].votes` and :rsconf:`members[n].priority` values to `0`. Non-voting replica set members must have a :rsconf:`~members[n].priority` of `0`.

> **Note:** Replica reconfiguration can add or remove no more than one voting replica
set member at a time. To modify the votes of multiple members, issue a series
of :dbcommand:`replSetReconfig` or :method:`rs.reconfig()` operations to
modify one member at a time. See
`replSetReconfig-cmd-single-node` for more information.

## Procedure

The following procedure converts configures a single `secondary` replica set member to be non-voting. To convert the `primary` member to be non-voting, you must first successfully step the primary down using :dbcommand:`replSetStepDown` or its shell helper :method:`rs.stepDown()` before performing this procedure.

\1) Connect to the Replica Set Primary Connect :binary:`~bin.mongosh` to the replica set `primary`:

```bash
   mongosh --host "<hostname>:<port>"

Replace the ``<hostname>`` and ``<port>`` with the hostname and 
port of the replica set primary. Include any other parameters 
required for your deployment. 
```

\2) Retrieve the Replica Configuration Issue the :method:`rs.conf()` method in the shell and assign the result to a variable `cfg`:

```javascript
   cfg = rs.conf();

The returned :ref:`document <replSetGetConfig-output>` contains a 
:rsconf:`members` array, where each element in the array contains 
the configuration for a single replica set member.
```

\3) Configure the Member to be Non-Voting For the replica member to change to be non-voting, set its :rsconf:`~members[n].votes` and :rsconf:`~members[n].priority` to `0`.

```javascript
   cfg.members[n].votes = 0;
   cfg.members[n].priority = 0;

Replace ``n`` with the array index position of the member 
to modify. The :rsconf:`members` array is *zero-indexed*, 
where the first element in the array has an index position of 
``0``. 

The array index position of a member in the 
:rsconf:`members` array is *distinct* from the 
:rsconf:`members[n]._id` of a specific member. Do *not* 
use the :rsconf:`~members[n]._id` to reference the array 
index position of any any member in :rsconf:`members`.
```

\4) Reconfigure the Replica Set with the New Configuration Use :method:`rs.reconfig()` method to reconfigure the replica set with the updated replica set configuration document.

```javascript
   rs.reconfig(cfg);
```

.. include:: /includes/warning-rs-reconfig.rst

## Related Documents

- :rsconf:`members[n].votes`
- `Replica Set Reconfiguration <replica-set-reconfiguration-usage>`
- `/core/replica-set-elections`
