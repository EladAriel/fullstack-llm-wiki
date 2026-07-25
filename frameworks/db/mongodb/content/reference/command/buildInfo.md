---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/buildInfo.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

============================

# buildInfo (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     buildInfo: 1 
   }
)
```

## Usage

In :binary:`~bin.mongosh`, call :dbcommand:`buildInfo` in the following form:

```javascript
db.runCommand( { buildInfo: 1 } )
```

The output document of :dbcommand:`buildInfo` has the following form:

```javascript
{
  "version" : "<string>",
  "gitVersion" : "<string>",
  "sysInfo" : "<string>",
  "loaderFlags" : "<string>",
  "compilerFlags" : "<string>",
  "allocator" : "<string>",
  "versionArray" : [ <num>, <num>, <...> ],
  "openssl" : <document>,
  "javascriptEngine" : "<string>",
  "bits" : <num>,
  "debug" : <boolean>,
  "maxBsonObjectSize" : <num>,
  "storageEngines" : [ "<string>", "<string>", "<...>" ],
  "ok" : <num>
}
```

## Output

### Supported

These fields are stable and should provide consistent behavior.

### Unstable

These fields are for internal use only, and you should not expect their behavior or existence to remain consistent on any level.
