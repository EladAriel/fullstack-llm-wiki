---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.shutdownServer.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

====================================

# db.shutdownServer() (mongosh method)

.. versionchanged:: 5.0

This operation provides a wrapper around the :dbcommand:`shutdown` command.

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-no-atlas-support.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

For a :binary:`~bin.mongod` started with `authentication`, you must run :method:`db.shutdownServer()` over an authenticated connection. See `method-shutdown-access-control` for more information.

For a :binary:`~bin.mongod` started without `authentication`, you must run :method:`db.shutdownServer()` from a client connected to the localhost interface. For example, run :binary:`~bin.mongosh` with the :option:`--host "127.0.0.1" <mongosh --host>` option on the same host machine as the :binary:`~bin.mongod`.

### `db.shutdownServer()` on Replica Set Members

:method:`db.shutdownServer()` fails if the :binary:`~bin.mongod` replica set member is running certain operations such as `index builds <index-operations-replicated-build>`. You can specify `force: true <shutdownServer-method-force>` to save index build progress to disk. The :binary:`~bin.mongod` recovers the index build when it restarts and continues from the saved checkpoint.

Shutting Down the Replica Set Primary, Secondary, or `mongos` ```````````````````````````````````````````````````````````````

.. include:: /includes/quiesce-period.rst

> **Warning:** Force shutdown of the primary can result in the
`rollback <replica-set-rollback>` of any writes not
yet replicated to a secondary.

## Access Control

To run :method:`db.shutdownServer()` on a :binary:`~bin.mongod` enforcing `authentication`, the authenticated user must have the :method:`db.shutdownServer()` privilege. For example, a user with the built-in role :authrole:`hostManager` has the appropriate permissions.

## Examples

### Shut down a `mongod`

```javascript
db.getSiblingDB("admin").shutdownServer()
```

### Force Shut Down a `mongod`

```javascript
db.getSiblingDB("admin").shutdownServer({ "force" : true })
```

### Shut Down a Primary `mongod` With Longer Timeout

```javascript
db.getSiblingDB("admin").shutdownServer({ "timeoutSecs": 60 })
```
