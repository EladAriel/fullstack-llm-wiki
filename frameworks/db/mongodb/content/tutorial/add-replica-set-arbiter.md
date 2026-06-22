---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/add-replica-set-arbiter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============================================

# Add an Arbiter to a Self-Managed Replica Set

In some circumstances (such as you have a primary and a secondary but cost constraints prohibit adding another secondary), you may choose to add a :binary:`~bin.mongod` instance to a replica set as an `arbiter <replica-set-arbiter-configuration>` to vote in elections.

Arbiters are :binary:`~bin.mongod` instances that are part of a `replica set` but do not hold data (i.e. do not provide data redundancy). They can, however, participate in `elections <replica-set-elections>`.

Arbiters have minimal resource requirements and do not require dedicated hardware. You can deploy an arbiter on an application server or a monitoring host.

> **Important:** Do not run an arbiter on systems that also host the
primary or the secondary members of the replica set.

.. include:: /includes/admonition-multiple-arbiters.rst

## Primary-Secondary-Arbiter Replica Sets

.. include:: /includes/fact-psa-performance-issues.rst

### Arbiter

An arbiter does not store data, but until the arbiter's :binary:`~bin.mongod` process is added to the replica set, the arbiter will act like any other :binary:`~bin.mongod` process and start up with a set of data files and with a full-sized `journal`.

### IP Binding

.. include:: /includes/fact-default-bind-ip.rst

.. include:: /includes/important-hostnames.rst

## Add an Arbiter

.. include:: /includes/admonition-multiple-arbiters.rst

.. include:: /includes/important-hostnames.rst

#. Create a data directory (e.g. :setting:`storage.dbPath`) for the arbiter. The :binary:`~bin.mongod` instance uses the directory for configuration data. The directory will not hold the data set. For example, create the `/var/lib/mongodb/arb` directory:

```bash
   mkdir /var/lib/mongodb/arb
```

#. Start the arbiter, specifying the data directory and the name of the replica set to join. The following starts an arbiter using the `/var/lib/mongodb/arb` as the :setting:`~storage.dbPath` and  `rs` for the replica set name:

.. include:: /includes/warning-bind-ip-security-considerations.rst

#. Connect to the primary and add the arbiter to the replica set. Use the :method:`rs.addArb()` method, as in the following example which assumes that `m1.example.net` is the hostname associated with the specified ip address for the arbiter:

```javascript
   rs.addArb("m1.example.net:27017")

This operation adds the arbiter running on port ``27017`` on the
``m1.example.net`` host.
```
