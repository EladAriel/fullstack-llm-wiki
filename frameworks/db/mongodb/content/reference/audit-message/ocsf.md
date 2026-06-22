---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/audit-message/ocsf.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

==========================

# OCSF Schema Audit Messages

In the {+ocsf+} schema, recorded log messages have this syntax:

```none
{
   "activity_id" : <int>,
   "category_uid" : <int>,
   "class_uid" : <int>,
   "time" : <int>,
   "severity_id" : <int>,
   "type_uid" : <int>,
   "metadata" : <document>
   "actor" : {
      "user" : {
         "type_id" : <int>,
         "name" : <string>,
         "groups" : <array of documents>
      }
   },
   "src_endpoint" : {
      "ip": <string>,   // IP address for origin client computer
      "port": <int>,    // Port for origin client computer
      "intermediate_ips": [ {
         // IP address and port for mongos or load balancer
         "ip": <string>,
         "port": <int>
      }, {
         // IP address and port for mongos or load balancer
         "ip": <string>,
         "port": <int>
      } ]
   },
   "dst_endpoint" : {
      // IP address and port for local MongoDB server
      "ip": <string>,
      "port": <int>
   }
}
```

The following table describes the fields in the log message.

> **Note:** Log messages may contain additional fields depending on the event
that was logged.

## OCSF Category Mapping

This table describes the `category_uid` values:

## OCSF Class Mapping

For a complete list of {+ocsf+} `class_uids` and how they map to different classes, see the [OCSF Documentation](https://schema.ocsf.io/1.2.0/classes)_.

## OCSF Type Mapping

The `type_uid` field represents a combination of the audited event's class, activity, and category. The resulting UUID indicates the type of activity that occurred.

Specifically, `type_uid` is `( class_uid * 100 ) + (activity_id)`, with `category_id` being the thousands place in a `class_id`.

This table describes how audited actions map to `type_uid`:

## Examples

The following examples show {+ocsf+} schema log messages for different action types.

### Authenticate Action

```javascript
{
   "activity_id" : 1,
   "category_uid" : 3,
   "class_uid" : 3002,
   "time" : 1710715316123,
   "severity_id" : 1,
   "type_uid" : 300201,
   "metadata" : {
      "correlation_uid" : "20ec4769-984d-445c-aea7-da0429da9122",
      "product" : "MongoDB Server",
      "version" : "1.0.0"
   },
   "actor" : {
      "user" : {
         "type_id" : 1,
         "name" : "admin.admin",
         "groups" : [ { "name" : "admin.root" } ]
      }
   },
   "src_endpoint" : { "ip" : "127.0.0.1", "port" : 56692 },
   "dst_endpoint" : { "ip" : "127.0.0.1", "port" : 20040 },
   "user" : { "type_id" : 1, "name" : "admin.admin" },
   "auth_protocol" : "SCRAM-SHA-256",
   "unmapped" : { "atype" : "authenticate" }
}
```

### AuthCheck Action

```javascript
{
   "activity_id" : 0,
   "category_uid" : 6,
   "class_uid" : 6003,
   "time" : 1710715315002,
   "severity_id" : 1,
   "type_uid" : 600300,
   "metadata" : {
      "correlation_uid" : "af4510fb-0a9f-49aa-b988-06259a7a861d",
      "product" : "MongoDB Server",
      "version" : "1.0.0"
   },
   "actor" : {},
   "src_endpoint" : { "ip" : "127.0.0.1", "port" : 45836 },
   "dst_endpoint" : { "ip" : "127.0.0.1", "port" : 20040 },
   "api" : {
      "operation" : "getParameter",
      "request" : { "uid" : "admin" },
      "response" : { "code" : 13, "error" : "Unauthorized" }
   }
}
```
