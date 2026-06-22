---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/setAuditConfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=================================

# setAuditConfig (database command)

> **Important:** .. include:: /includes/deprecated-get-set-auditconfig.rst

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
     setAuditConfig: 1, 
     filter: <Filter Document>,
     auditAuthorizationSuccess: <Boolean> 
   }
)
```

## Command Fields

The command has the following fields:

## Behavior

Enable `auditing <auditing>` to use :dbcommand:`setAuditConfig` at runtime.

:parameter:`auditAuthorizationSuccess` enables auditing of authorization success for the `authCheck <audit-action-details-results>` action. The parameter value must be `true` to audit read and write operations. However, when :parameter:`auditAuthorizationSuccess` is `false` auditing has less performance impact because the audit system only logs authorization failures.

Configuration updates are distributed via the `oplog` mechanism which means updates on :binary:`~bin.mongod` nodes are distributed to secondary nodes very quickly. There is a different distribution mechanism on :binary:`~bin.mongos` nodes. :binary:`~bin.mongos` nodes have to :parameter:`poll <auditConfigPollingFrequencySecs>` the primary server at regular intervals for configuration updates. You may see stale data due to polling delay if you run :dbcommand:`setAuditConfig` on the primary server and :dbcommand:`getAuditConfig` on a `shard <sharding-introduction>` before the shard has polled the primary server for updated configuration details.

## Examples

In these examples the audit messages have been reformatted. They appear on a single line in the log file.

### Audit Collection Creation and Deletion

Enable auditing when a collection is created or deleted.

```javascript
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter:
         {
            atype:
               {
                  $in: [ "createCollection", "dropCollection" ]
               }
         },
      auditAuthorizationSuccess: false
   }
)
```

When the `inventory` collection is created in the `sales` database, the audit system will log a message like this:

```javascript
.. copyable: false

{
   "atype" : "createCollection",
   "ts" : { "$date" : "2021-08-09T13:45:05.372+00:00" },
   "uuid" : { "$binary" : "RKU/YLizS6K9se2GUU7ZVQ==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51918 },
   "users" : [],
   "roles" : [],
   "param" : { "ns" : "sales.inventory" },
   "result" : 0
}
```

When the `inventory` collection is dropped from the `sales` database, the audit system will log a message like this:

```javascript
.. copyable: false

{
   "atype" : "dropCollection",
   "ts" : { "$date" : "2021-08-09T13:45:00.661+00:00" },
   "uuid" : { "$binary" : "0gle4/pSQli+LUcz43ykag==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51928 },
   "users" : [],
   "roles" : [],
   "param" : { "ns" : "sales.inventory" },
   "result" : 0
}
```

### Audit Document Interactions

Set :parameter:`auditAuthorizationSuccess` to `true` and create a filter which includes actions of interest to audit read and write operations.

```javascript
db.admin.runCommand(
   {
      setAuditConfig: 1,
      filter:
         {
            atype: "authCheck",
            "param.command":
               {
                  $in: [ "find", "insert", "delete", "update", "findandmodify" ]
               }
         },
      auditAuthorizationSuccess: true
   }
)
```

Search the `inventory` collection in the `sales` database using the :dbcommand:`find` command to create an audit log entry like this one:

```javascript
.. copyable: false

{
   "atype" : "authCheck",
   "ts" : { "$date" : "2021-08-09T15:28:10.788+00:00" },
   "uuid" : { "$binary" : "ngwRt5CRTZqgE4TsfleoqQ==", "$type" : "04" },
   "local" : { "ip" : "127.0.0.1", "port" : 27502 },
   "remote" : { "ip" : "127.0.0.1", "port" : 51930 },
   "users" : [],
   "roles" : [],
   "param" : {
      "command" : "find",
      "ns" : "sales.inventory",
      "args" : {
         "find" : "inventory",
         "filter" : { "widget" : 1 },
         "lsid" : { "id" : { "$binary" : "FNWNxiitQ8GHKrHx8eJSbg==", "$type" : "04" } },
         "$clusterTime" : { "clusterTime" : { "$timestamp" : { "t" : 1628521381, "i" : 1 } },
         "signature" : { "hash" : { "$binary" : "AAAAAAAAAAAAAAAAAAAAAAAAAAA=", "$type" : "00" },
         "keyId" : { "$numberLong" : "0" } } },
         "$db" : "sales"
      }
   },
   "result" : 0
}
```

> **Seealso:** - :method:`db.adminCommand`
- :dbcommand:`getAuditConfig`
- `configure audit filters <audit-filter>`
