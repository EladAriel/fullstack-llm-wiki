---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/tutorial/convert-secondary-into-arbiter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==============================================

# Convert a Self-Managed Secondary to an Arbiter

If you have a `secondary` in a `replica set` that no longer needs to hold data but that needs to remain in the set to ensure that the set can `elect a primary <replica-set-elections>`, you may convert the secondary to an `arbiter <replica-set-arbiters>` using either procedure in this tutorial. Both procedures are operationally equivalent:

- You may operate the arbiter on the same port as the former secondary.
In this procedure, you must shut down the secondary and remove its data before restarting and reconfiguring it as an arbiter.

For this procedure, see `replica-set-convert-secondary-to-arbiter-same-port`.

- Run the arbiter on a new port. In this procedure, you can reconfigure
the server as an arbiter before shutting down the instance running as a secondary.

For this procedure, see `replica-set-convert-secondary-to-arbiter`.

## Convert Secondary to Arbiter and Reuse the Port Number

#. If your application is connecting directly to the secondary, modify the application so that MongoDB queries don't reach the secondary.

#. Shut down the secondary.

#. Remove the `secondary` from the `replica set` by calling the :method:`rs.remove()` method. Perform this operation while connected to the current `primary` in :binary:`~bin.mongosh`:

```javascript
   rs.remove("<hostname><:port>")
```

#. Verify that the replica set no longer includes the secondary by calling the :method:`rs.conf()` method in :binary:`~bin.mongosh`:

```javascript
   rs.conf()
```

#. Move the secondary's data directory to an archive folder. For example:

```bash
   mv /data/db /data/db-old

.. note:: Optional

   You may remove the data instead.
```

#. Create a new, empty data directory to point to when restarting the :binary:`~bin.mongod` instance. You can reuse the previous name. For example:

```bash
   mkdir /data/db
```

#. Restart the :binary:`~bin.mongod` instance for the secondary, specifying the port number, the empty data directory, and the replica set. You can use the same port number you used before. Issue a command similar to the following:

.. include:: /includes/warning-bind-ip-security-considerations.rst

#. In :binary:`~bin.mongosh` convert the secondary to an arbiter using the :method:`rs.addArb()` method:

```javascript
   rs.addArb("<hostname><:port>")
```

#. Verify the arbiter belongs to the replica set by calling the :method:`rs.conf()` method in :binary:`~bin.mongosh`.

```javascript
   rs.conf()

The arbiter member should include the following:

.. code-block:: javascript

   "arbiterOnly" : true
```

## Convert Secondary to Arbiter Running on a New Port Number

#. If your application is connecting directly to the secondary or has a connection string referencing the secondary, modify the application so that MongoDB queries don't reach the secondary.

#. Create a new, empty data directory to be used with the new port number. For example:

```bash
   mkdir /data/db-temp
```

#. Start a new :binary:`~bin.mongod` instance on the new port number, specifying the new data directory and the existing replica set. Issue a command similar to the following:

.. include:: /includes/warning-bind-ip-security-considerations.rst

#. In :binary:`~bin.mongosh` connected to the current primary, convert the new :binary:`~bin.mongod` instance to an arbiter using the :method:`rs.addArb()` method:

```javascript
   rs.addArb("<hostname><:port>")
```

#. Verify the arbiter has been added to the replica set by calling the :method:`rs.conf()` method in :binary:`~bin.mongosh`.

```javascript
   rs.conf()

The arbiter member should include the following:

.. code-block:: javascript

   "arbiterOnly" : true
```

#. Shut down the secondary.

#. Remove the `secondary` from the `replica set` by calling the :method:`rs.remove()` method in :binary:`~bin.mongosh`:

```javascript
   rs.remove("<hostname><:port>")
```

#. Verify that the replica set no longer includes the old secondary by calling the :method:`rs.conf()` method in :binary:`~bin.mongosh`:

```javascript
   rs.conf()
```

#. Move the secondary's data directory to an archive folder. For example:

```bash
   mv /data/db /data/db-old

.. note:: Optional

   You may remove the data instead.
```
