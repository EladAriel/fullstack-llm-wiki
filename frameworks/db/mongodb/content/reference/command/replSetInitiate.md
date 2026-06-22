---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/replSetInitiate.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==================================

# replSetInitiate (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-onprem-only.rst

.. include:: /includes/fact-environments-no-atlas-support.rst

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     replSetInitiate : <config_document> 
   }
)
```

The `<config_document>` is a `document` that specifies the replica set's configuration. For instance, here's a config document for creating a simple 3-member replica set:

```javascript
{
   _id : <setname>,
    members : [
        {_id : 0, host : <host0>},
        {_id : 1, host : <host1>},
        {_id : 2, host : <host2>},
    ]
}
```

.. include:: /includes/important-hostnames.rst

## IP Binding

.. include:: /includes/fact-default-bind-ip.rst

## Example

Assign a config document to a variable and then to pass the document to the :method:`rs.initiate()` helper:

```javascript
config = {
    _id : "my_replica_set",
     members : [
         {_id : 0, host : "rs1.example.net:27017"},
         {_id : 1, host : "rs2.example.net:27017"},
         {_id : 2, host : "rs3.example.net", arbiterOnly: true},
     ]
}

rs.initiate(config)
```

.. include:: /includes/important-hostnames.rst

Notice that omitting the port cause the host to use the default port of 27017. Notice also that you can specify other options in the config documents such as the `arbiterOnly` setting in this example.

> **Seealso:** - `/reference/replica-configuration`
- `/administration/replica-set-deployment`
- :ref:`Replica Set Reconfiguration
  <replica-set-reconfiguration-usage>`
