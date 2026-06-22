---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/remove-replica-set-member.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# Remove Members from a Self-Managed Replica Set

To remove a member of a `replica set` use either of the following procedures.

## Remove a Member Using `rs.remove()`

1. Shut down the :binary:`~bin.mongod` instance for the member you wish to
remove. To shut down the instance, connect using :binary:`~bin.mongosh` and use the :method:`db.shutdownServer()` method.

#. Connect to the replica set's current `primary`. To determine the current primary, use :method:`db.hello()` while connected to any member of the replica set.

#. Use :method:`rs.remove()` in either of the following forms to remove the member:

```javascript
   rs.remove("mongod3.example.net:27017")
   rs.remove("mongod3.example.net")

MongoDB may disconnect the shell briefly if the replica set needs to elect a
new primary. The shell then automatically reconnects in such cases. The
shell may display a ``DBClientCursor::init call() failed`` error even
though the command succeeds.
```

## Remove a Member Using `rs.reconfig()`

You can remove a member by reconfiguring the replica set using a `replica configuration document </reference/replica-configuration>` where that member is removed from the :rsconf:`members` array.

:method:`rs.reconfig()` allows adding or removing no more than `1` :rsconf:`voting <members[n].votes>` member at a time. To remove multiple voting members from the replica set, issue a series of :method:`rs.reconfig()` operations to remove one member at a time. See `replSetReconfig-cmd-single-node` for more information.

### Procedure

1. Shut down the :binary:`~bin.mongod` instance for the member you wish to
remove. To shut down the instance, connect using :binary:`~bin.mongosh` and use the :method:`db.shutdownServer()` method.

#. Connect to the replica set's current `primary`. To determine the current primary, use :method:`db.hello()` while connected to any member of the replica set.

#. Issue the :method:`rs.conf()` method to view the current configuration document and determine the position in the `members` array of the member to remove:

#. Assign the current configuration document to the variable `cfg`:

```javascript
   cfg = rs.conf()
```

#. Modify the `cfg` object to remove the member.

#. Overwrite the replica set configuration document with the new configuration by issuing the following:

```javascript
   rs.reconfig(cfg)
```

#. To confirm the new configuration, issue :method:`rs.conf()`.

For the example above the output would be:

```javascript
   {
       "_id" : "rs",
       "version" : 8,
       "members" : [
           {
               "_id" : 0,
               "host" : "mongod_A.example.net:27017"
           },
           {
               "_id" : 1,
               "host" : "mongod_B.example.net:27017"
           }
       ]
   }
```
