---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/audit-message/mongo.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
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
