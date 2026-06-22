---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/isdbgrid.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========================

# isdbgrid (database command)

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
     isdbgrid: 1
   }
)
```

## Output

The returned document is similar to the following:

```javascript
{ "isdbgrid" : 1, "hostname" : "app.example.net", "ok" : 1 }
```

If you issue the :dbcommand:`isdbgrid` command when connected to a :binary:`~bin.mongod`, MongoDB returns an error document. The :dbcommand:`isdbgrid` command is not available to :binary:`~bin.mongod`. The error document, however, also includes a line that reads `"isdbgrid" : 1`, just as in the document returned for a :binary:`~bin.mongos`. The error document is similar to the following:

```javascript
{
   "errmsg" : "no such cmd: isdbgrid",
   "bad cmd" : {
         "isdbgrid" : 1
   },
   "ok" : 0
}
```

You can instead use the :dbcommand:`hello` command to determine connection to a :binary:`~bin.mongos`. When connected to a :binary:`~bin.mongos`, the :dbcommand:`hello` command returns a document that contains the string `isdbgrid` in the `msg` field.
