---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/command/getLog.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# getLog (database command)

## Definition

## Compatibility

This command is available in deployments hosted in the following environments:

.. include:: /includes/fact-environments-atlas-only.rst

.. include:: /includes/fact-environments-atlas-support-all.rst

.. include:: /includes/fact-environments-onprem-only.rst

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     getLog: <value> 
   } 
)
```

## Command Fields

The possible values for :dbcommand:`getLog` are:

> **Note:** The :dbcommand:`getLog` command no longer accepts the `rs` value, as this
categorization of message type has been deprecated. Instead, log messages are
now always identified by their `component <log-message-components>` -
including REPL for replication messages. See
`log-message-parsing-example-filter-component` for log
parsing examples that filter on the component field.

## Output

If specified `*`, then the command returns a document with the names of the other acceptable values.

Otherwise, the command returns a document that includes the following fields:

- `totalLinesWritten` field that contains the number of log events
- `log` field that contains an array of log events
- A :method:`db.adminCommand()` :ref:`response document
<db-adminCommand-response>`, containing status and timestamp information.

## Behavior

### Line Truncation

:dbcommand:`getLog` truncates any event that contains more than 1024 characters.

### Character Escaping

:dbcommand:`getLog` returns log data in escaped `Relaxed Extended JSON v2.0 <mongodb-extended-json-v2>` format, using the following escape sequences to render log output as valid JSON:

.. include:: /includes/fact-json-escape-sequences.rst

## Filtering

### Within `mongosh`

:dbcommand:`getLog` output can be filtered to make results more readable or to match on specific criteria.

The following operation prints just the `log` field (which contains the array of all recent log events), and removes `character escaping <getlog-character-escaping>` from each log message:

```javascript
db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})
```

This operation presents :dbcommand:`getLog` output in the same format as the MongoDB :option:`log file <mongod --logpath>`.

> **Note:** :dbcommand:`getLog` only shows the most recent 1024 logged
events, and is not a replacement for the MongoDB
:option:`log file <mongod --logpath>`.

### Outside `mongosh` with `jq`

.. include:: /includes/fact-use-jq-with-structured-logging.rst

To use `jq` with :dbcommand:`getLog` output, you must use the :option:`--eval <mongosh --eval>` option to :binary:`~bin.mongosh`. The following operation uses `jq` to filter on the **REPL** `component <log-message-components>` to present only those log messages associated with replication:

```javascript
mongosh --quiet --eval "db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})" | jq -c '. | select(.c=="REPL")'
```

Be sure to provide any necessary connection-specific parameters to :binary:`~bin.mongosh` as needed, such as :option:`--host <mongosh --host>` or :option:`--port <mongosh --port>`.

See `log-message-parsing` for more examples of filtering log output using `jq`. The `jq` syntax presented in each linked example can be used with the above `mongo --eval` operation with minor adjustment. For example, the following syntax adapts the linked "Counting Unique Messages" example for use with :dbcommand:`getLog`:

```javascript
mongosh --quiet --eval "db.adminCommand( { getLog:'global'} ).log.forEach(x => {print(x)})" | jq -r ".msg" | sort | uniq -c | sort -rn | head -10
```

## Examples

### Retrieve Available Log Filters

The following operation, run from :binary:`~bin.mongosh`, returns the available log filters for passing to :dbcommand:`getLog`:

```javascript
db.adminCommand( { getLog: "*" } )
```

The operation returns the following document:

```javascript
{ "names" : [ "global", "startupWarnings" ], "ok" : 1 }
```

### Retrieve Recent Events from Log

The following operation, run from :binary:`~bin.mongosh`, retrieves the most recent `global` events for a :binary:`~bin.mongod` or :binary:`~bin.mongos` instance:

```javascript
db.adminCommand( { getLog : "global" } )
```

The operation returns a document similar to the following:

```javascript
{
      "totalLinesWritten" : <num>,
      "log" : [
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":4615611, \"ctx\":\"initandlisten\",\"msg\":\"MongoDB starting\",\"attr\":{\"pid\":12345,\"port\":27001,\"dbPath\":\"/var/lib/mongo\",\"architecture\":\"64-bit\",\"host\":\"server1.example.com\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":23403,   \"ctx\":\"initandlisten\",\"msg\":\"Build Info\",\"attr\":{\"buildInfo\":{\"version\":\"4.4.0\",\"gitVersion\":\"328c35e4b883540675fb4b626c53a08f74e43cf0\",\"openSSLVersion\":\"OpenSSL 1.1.1c FIPS  28 May 2019\",\"modules\":[],\"allocator\":\"tcmalloc\",\"environment\":{\"distmod\":\"rhel80\",\"distarch\":\"x86_64\",\"target_arch\":\"x86_64\"}}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":51765,   \"ctx\":\"initandlisten\",\"msg\":\"Operating System\",\"attr\":{\"os\":{\"name\":\"CentOS Linux release 8.0.1905 (Core) \",\"version\":\"Kernel 4.18.0-80.11.2.el8_0.x86_64\"}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.871+00:00\"},\"s\":\"I\",  \"c\":\"CONTROL\",  \"id\":21951,   \"ctx\":\"initandlisten\",\"msg\":\"Options set by command line\",\"attr\":{\"options\":{\"config\":\"/etc/mongod.conf\",\"net\":{\"bindIp\":\"127.0.0.1\",\"port\":27001},\"processManagement\":{\"fork\":true,\"timeZoneInfo\":\"/usr/share/zoneinfo\"},\"replication\":{\"replSetName\":\"repl-shard1\"},\"sharding\":{\"clusterRole\":\"shardsvr\"},\"storage\":{\"dbPath\":\"/var/lib/mongo\",\"journal\":{\"enabled\":true},\"wiredTiger\":{\"engineConfig\":{\"cacheSizeGB\":0.1}}},\"systemLog\":{\"destination\":\"file\",\"logAppend\":true,\"path\":\"/var/log/mongodb/mongod.log\"}}}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.873+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":22270,   \"ctx\":\"initandlisten\",\"msg\":\"Storage engine to use detected by data files\",\"attr\":{\"dbpath\":\"/var/lib/mongo\",\"storageEngine\":\"wiredTiger\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:48.873+00:00\"},\"s\":\"I\",  \"c\":\"STORAGE\",  \"id\":22315,   \"ctx\":\"initandlisten\",\"msg\":\"wiredtiger_open config\",\"attr\":{\"config\":\"create,cache_size=102M,session_max=33000,eviction=(threads_min=4,threads_max=4),config_base=false,statistics=(fast),log=(enabled=true,archive=true,path=journal,compressor=snappy),file_manager=(close_idle_time=100000,close_scan_interval=10,close_handle_minimum=250),statistics_log=(wait=0),verbose=[recovery_progress,checkpoint_progress,compact_progress],\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server1.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server2.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server3.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server4.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server5.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"CONNPOOL\", \"id\":22576,   \"ctx\":\"ReplicaSetMonitor-TaskExecutor\",\"msg\":\"Connecting\",\"attr\":{\"hostAndPort\":\"server6.example.com:27001\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23015,   \"ctx\":\"listener\",\"msg\":\"Listening on\",\"attr\":{\"address\":\"/tmp/mongodb-27001.sock\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23015,   \"ctx\":\"listener\",\"msg\":\"Listening on\",\"attr\":{\"address\":\"127.0.0.1\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:10:58.877+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":23016,   \"ctx\":\"listener\",\"msg\":\"Waiting for connections\",\"attr\":{\"port\":27001,\"ssl\":\"off\"}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:15:10.392+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":22943,   \"ctx\":\"listener\",\"msg\":\"connection accepted\",\"attr\":{\"remote\":\"127.0.0.1:35724\",\"sessionId\":67,\"connectionCount\":30}}",
              "{\"t\":{\"$date\":\"2020-05-19T19:15:10.393+00:00\"},\"s\":\"I\",  \"c\":\"NETWORK\",  \"id\":51800,   \"ctx\":\"conn67\",\"msg\":\"client metadata\",\"attr\":{\"remote\":\"127.0.0.1:35724\",\"client\":\"conn67\",\"doc\":{\"application\":{\"name\":\"MongoDB Shell\"},\"driver\":{\"name\":\"MongoDB Internal Client\",\"version\":\"4.4.0\"},\"os\":{\"type\":\"Linux\",\"name\":\"CentOS Linux release 8.0.1905 (Core) \",\"architecture\":\"x86_64\",\"version\":\"Kernel 4.18.0-80.11.2.el8_0.x86_64\"}}}}"
      ],
      "ok" : 1,
      "$gleStats" : {
              "lastOpTime" : Timestamp(<ts>),
              "electionId" : ObjectId(<id>)
      },
      "lastCommittedOpTime" : Timestamp(<ts>),
      "$configServerState" : {
              "opTime" : {
                      "ts" : Timestamp(<ts>),
                      "t" : Long(8)
               }
      },
      "$clusterTime" : {
              "clusterTime" : Timestamp(<ts>),
              "signature" : {
                      "hash" : BinData(<bin>),
                      "keyId" : Long(0)
               }
      },
      "operationTime" : Timestamp(<ts>)
}
```
