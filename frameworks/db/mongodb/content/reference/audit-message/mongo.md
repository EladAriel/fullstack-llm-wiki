---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/audit-message/mongo.txt"
source_commit: "ab9db26ed3d11618cdb61516d8180337d8e3f679"
source_commit_short: "ab9db26e"
source_commit_date: "2026-07-24T16:22:46-06:00"
generated_at: "2026-07-25T11:51:15Z"
---

===========================

# mongo Schema Audit Messages

In the `mongo` schema, recorded log messages have this syntax:

```none
{
  atype: <string>,
  ts : { $date: <timestamp> },
  uuid : { $binary: <string>, $type: <string> },
  local: { ip: <string>, port: <int> || isSystemUser: <boolean> || unix: <string> },
  remote: { ip: <string>, port: <int> || isSystemUser: <boolean> || unix: <string> },
  intermediates: [   // Added in MongoDB 8.1
     { 
        // IP address and port for mongos or load balancer
        ip: <string>,
        port: <int>
     }, {
        //  IP address and port for mongos or load balancer
        ip: <string>,
        port: <int>
     }
  ],
  users : [ { user: <string>, db: <string> }, ... ],
  roles: [ { role: <string>, db: <string> }, ... ],
  param: <document>,
  result: <int>
}
```

The following table describes the fields in the `mongo` schema.

### Audit Event Actions, Details, and Results

The following table lists for each `atype` or action type, the associated `param` details and the `result` values, if any.
