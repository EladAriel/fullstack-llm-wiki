---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/logRotate.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================

# logRotate (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   {
     logRotate: <integer or string>,
     comment: <string>
   }
)
```

## Command Fields

The command takes the following fields:

You may also rotate the logs by sending a `SIGUSR1` signal to the :binary:`~bin.mongod` process.

For example, if a running :binary:`~bin.mongod` instance has a process ID (PID) of `2200`, the following command rotates the log file for that instance on Linux:

```bash
kill -SIGUSR1 2200
```

## Limitations

- Your :binary:`~bin.mongod` instance needs to be running with the
:option:`--logpath [file] <mongod --logpath>` option in order to use :dbcommand:`logRotate`

- `Auditing <auditing>` must be enabled to rotate the audit log.
## Behavior

The :setting:`systemLog.logRotate` setting or :option:`--logRotate <mongod --logRotate>` option specify :dbcommand:`logRotate`'s behavior.

When :setting:`systemLog.logRotate` or :option:`--logRotate <mongod --logRotate>` are set to `rename`, :dbcommand:`logRotate` renames the existing log file by appending the current timestamp to the filename. The appended timestamp has the following form:

```none
<YYYY>-<mm>-<DD>T<HH>-<MM>-<SS>
```

Then :dbcommand:`logRotate` creates a new log file with the same name as originally specified by the :setting:`systemLog.path` setting to :binary:`~bin.mongod` or :binary:`~bin.mongos`.

When :setting:`systemLog.logRotate` or :option:`--logRotate <mongod --logRotate>` are set to `reopen`, :dbcommand:`logRotate` follows the typical Linux/Unix behavior, and simply closes the log file then reopens a log file with the same name. With `reopen`, :binary:`~bin.mongod` expects that another process renames the file prior to the rotation, and that the reopen results in the creation of a new file.

## Examples

The following example rotates both the server log and the audit log:

```javascript
db.adminCommand( { logRotate: 1 } )
```

The following example rotates only the audit log, and provides a custom message to the log file at time of rotation:

```javascript
db.adminCommand( { logRotate: "audit", comment: "Rotating audit log" } )
```
