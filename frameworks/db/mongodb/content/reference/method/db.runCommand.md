---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/method/db.runCommand.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

================================

# db.runCommand() (mongosh method)

## Definition

## Compatibility

This method is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Behavior

:method:`db.runCommand()` runs the command in the context of the current database. Some commands are only applicable in the context of the `admin` database, and you must change your `db` object before running these commands or use :method:`db.adminCommand()`.

### Read Preference

Starting in mongosh 2.0, you can specify the read preference for a command with the `options <runCommand-options-readPref-arg>` argument. If you do not specify a read preference, `db.runCommand()` defaults to :readmode:`primary`.

> **Warning:** In mongosh 2.0, `db.runCommand()` ignores any other read preference
global configuration set, including using `Mongo.setReadPref()` or
by specifying `readPreference` in a connection string.
In mongosh 1.x, `db.runCommand()` does not take an `options`
argument. `db.runCommand()` uses the read preference specified either
by using `Mongo.setReadPref()` or by specifying `readPreference` in
the connection string.

## Examples

The following examples show how to use `db.runCommand()` to run database commands.

### hello Command Without Specified Read Preference

This example shows how to use `db.runCommand()` to run the :dbcommand:`hello` command.

```javascript
db.runCommand( { hello: 1 } )
```

For details on output, see `hello Output <hello-cmd-output>`.

For details on read preference behavior, see `runCommand-read-pref-behavior`.

### hello Command with readPreference: secondaryPreferred

This example shows how to use `db.runCommand()` to run the :dbcommand:`hello` command with the :readmode:`secondaryPreferred` read preference.

```javascript
db.runCommand( { hello: 1 }, { readPreference: "secondaryPreferred" } )
```

For details on output, see `hello Output <hello-cmd-output>`.

For details on read preference behavior, see `runCommand-read-pref-behavior`.

## Response

The method returns a response document that contains the following fields:

.. include:: /includes/fact-runCommand-results.rst
