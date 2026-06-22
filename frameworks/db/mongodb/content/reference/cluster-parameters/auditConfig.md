---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/cluster-parameters/auditConfig.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

===========

# auditConfig

## Definition

## Syntax

To set `auditConfig` for your deployment, run the following command on the `admin` database:

```javascript
db.adminCommand( { setClusterParameter: { auditConfig: <value> } } )
```

To view current values for the `auditConfig` cluster parameter, run the following command on the `admin` database:

```javascript
db.adminCommand( { getClusterParameter: "auditConfig" } )
```

## Parameter Fields

## Behavior

Auditing must be enabled to use `auditConfig`.

### Retrieving Audit Configurations

If `runtime audit configuration <configure-audit-filters-at-runtime>` is enabled, the `auditAuthorizationSuccess` parameter doesn't appear in the `mongod` or `mongos` configuration file. The server will fail to start if the parameter is present.

If you run `getClusterParameter` on `auditConfig`, nodes that do not participate in a runtime audit configuration return their current configuration file settings for `auditLog.filter` and `setParameter.auditAuthorizationSuccess`.

### Setting Audit Configurations

When you set audit configurations with :dbcommand:`setClusterParameter`, changes immediately take effect on all `config servers <sharding-config-server>` and shards in a sharded cluster.

Setting too wide of an audit filter or enabling `auditConfig.auditAuthorizationSuccess` can degrade performance.

## Example

The following example uses the `setClusterParameter` command to enable auditing when a collection is created or deleted. The audit messages have been reformatted. They appear on a single line in the log file.

```javascript
db.adminCommand( 
   { 
      setClusterParameter: { 
         auditConfig: {
            filter: { 
               atype: {
                  $in: [ "createCollection", "dropCollection" ]
               }
            }, 
            auditAuthorizationSuccess: false
         }
      } 
   } 
)
```

After setting the `auditConfig` parameter, if you create an `inventory` collection in the `sales` database, the audit system logs a message that resembles the following:

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

If the `inventory` collection is dropped from the `sales` database, the audit system logs a message similar to the following:

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

## Learn More

- `auditing`
- `audit-action-details-results`
- `cluster-parameters`
- `configure-audit-filters-at-runtime`
- `audit-message`
