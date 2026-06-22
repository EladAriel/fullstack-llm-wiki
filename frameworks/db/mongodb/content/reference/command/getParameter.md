---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getParameter.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===============================

# getParameter (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-limited-free.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     getParameter: <value>, 
     <parameter> : <value>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

## Behavior

:dbcommand:`getParameter` runs on the `admin` database only, and returns an error if run on any other database.

The possible value for `<parameter>` may vary depending on what version and storage engine in use. See `getParameter-retrieve-all-params` for an example of listing the available parameters.

## Examples

### Retrieve Single Parameter

The following operation runs :dbcommand:`getParameter` on the `admin` database using a value of `saslHostName` to retrieve the value for that parameter:

```javascript
db.adminCommand( { getParameter : 1, "saslHostName" : 1 } )
```

The command returns the following output:

.. include:: /includes/note-output-may-vary.rst

```javascript
{ "saslHostName" : "www.example.net:27018", "ok" : 1 }
```

### Retrieve All Parameters

The following operation runs :dbcommand:`getParameter` with a value of `'*'` to retrieve all parameters:

```javascript
db.adminCommand( { getParameter : '*' } )
```

> **Note:** The output may vary depending on the version of MongoDB and the
specific configuration of the running MongoDB instance.

> **Seealso:** :dbcommand:`setParameter` for more about these parameters.

### Report Details on a Single Parameter

The following example runs :dbcommand:`getParameter` with `{showDetails: true}` to report `details <showdetails-fields>` on :parameter:`saslHostName`.

```javascript
db.adminCommand( { getParameter : { showDetails: true }, "saslHostName" : 1 } )
```

Example output:

```javascript
{
  saslHostName: {
    value: '<hostname>',
    settableAtRuntime: false,
    settableAtStartup: true
  },
  ok: 1
}
```

.. include:: /includes/note-output-may-vary.rst

### Report Details for All Parameters

The following example runs :dbcommand:`getParameter` with `{showDetails: true, allParameters: true}` to report `details <showdetails-fields>` on **all** parameters.

```javascript
db.adminCommand( { getParameter : { showDetails: true, allParameters: true } } )
```

### Retrieve All Startup Parameters

.. versionadded:: 8.0

The following example runs the :dbcommand:`getParameter` command to retrieve all startup parameters:

```javascript
db.adminCommand( {
   getParameters: {
      allParameters: true,
      setAt: "startup"
   }
} )
```

### Retrieve All Runtime Parameters

.. versionadded:: 8.0

The following example runs the :dbcommand:`getParameter` command to retrieve all runtime parameters:

```javascript
db.adminCommand( {
   getParameters: {
      allParameters: true,
      setAt: "runtime"
   }
} )
```
