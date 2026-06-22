---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/log-messages.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

============

# Log Messages

## Overview

As part of normal operation, MongoDB maintains a running log of events, including entries such as incoming connections, commands run, and issues encountered. Generally, log messages are useful for diagnosing issues, monitoring your deployment, and tuning performance.

To get your log messages, you can use any of the following methods:

- View logs in your configured :ref:`log destination
<log-message-destinations>`.

- Run the :dbcommand:`getLog` command.
- Download logs through :atlas:`{+atlas+} </>`.
To learn more, see `log-messages-atlas`.

## Structured Logging

:binary:`~bin.mongod` / :binary:`~bin.mongos` instances output all log messages in `structured JSON format <log-message-json-output-format>`. Log entries are written as a series of key-value pairs, where each key indicates a log message field type, such as "severity", and each corresponding value records the associated logging information for that field type, such as "informational". Previously, log entries were output as plaintext.

Structured logging with key-value pairs allows for efficient parsing by automated tools or log ingestion services, and makes programmatic search and analysis of log messages easier to perform. Examples of analyzing structured log messages can be found in the `log-message-parsing` section.

> **Note:** The `mongod` quits if it's unable to write to the log file. To
ensure that `mongod` can write to the log file, verify that the log
volume has space on the disk and the logs are rotated.

### JSON Log Output Format

All log output is in JSON format including output sent to:

- Log file
- Syslog
- Stdout (standard out) :ref:`log destinations
<log-message-destinations>`

Output from the :dbcommand:`getLog` command is also in JSON format.

Each log entry is output as a self-contained JSON object which follows the `Relaxed Extended JSON v2.0 <mongodb-extended-json-v2>` specification, and has the following layout and field order:

```javascript
{
  "t": <Datetime>, // timestamp
  "s": <String>, // severity
  "c": <String>, // component
  "id": <Integer>, // unique identifier
  "ctx": <String>, // context
  "svc": <String>, // service
  "msg": <String>, // message body
  "attr": <Object>, // additional attributes (optional)
  "tags": <Array of strings>, // tags (optional)
  "truncated": <Object>, // truncation info (if truncated)
  "size": <Object> // original size of entry (if truncated)
}
```

Field descriptions:

Escaping ````````

The **message** and **attributes** fields will escape control characters as necessary according to the Relaxed Extended JSON v2.0 specification:

.. include:: /includes/fact-json-escape-sequences.rst

An example of message escaping is provided in the `examples section <log-message-json-examples>`.

Truncation ``````````

.. versionchanged:: 7.3

Any **attributes** that exceed the maximum size defined with :parameter:`maxLogSizeKB` (default: 10 KB) are truncated. Truncated attributes omit log data beyond the configured limit, but retain the JSON formatting of the entry to ensure that the entry remains parsable.

For example, the following JSON object represents a `command` attribute that contains 5000 elements in the `$in` field without truncation.

> **Note:** The example log entries are reformatted for readability.

```javascript
{ 
  "command": { 
    "find": "mycoll", 
    "filter": { 
      "value1": {
        "$in": [0, 1, 2, 3, ... 4999]
      },
      "value2": "foo"
},
"sort": { "value1": 1 },
"lsid":{"id":{"$uuid":"80a99e49-a850-467b-a26d-aeb2d8b9f42b"}},
"$db": "testdb"
}
}
```

In this example, the `$in` array is truncated at the 376th element because the size of the `command` attribute would exceed :parameter:`maxLogSizeKB` if it included the subsequent elements. The remainder of the `command` attribute is omitted. The truncated log entry resembles the following output:

```javascript
{
  "t": { "$date": "2021-03-17T20:30:07.212+01:00" },
  "s": "I",
  "c": "COMMAND",
  "id": 51803,
  "ctx": "conn9",
  "msg": "Slow query",
  "attr": {
    "command": {
      "find": "mycoll",
      "filter": {
        "value1": {
          "$in": [ 0, 1, ..., 376 ] // Values in array omitted for brevity
        }
      }
    },
    ... // Other attr fields omitted for brevity
  },
  "truncated": {
    "command": {
      "truncated": {
        "filter": {
          "truncated": {
            "value1": {
              "truncated": {
                "$in": {
                  "truncated": {
                    "377": {
                      "type": "double",
                      "size": 8
                    }
                  },
                  "omitted": 4623
                }
              }
            }
          },
          "omitted": 1
        }
      },
      "omitted": 3
    }
  },
  "size": {
    "command": 21692
  }
}
```

Log entries containing one or more truncated attributes include nested `truncated` objects, which provide the following information for each truncated attribute in the log entry:

- The attribute that was truncated
- The specific sub-object of that attribute that triggered truncation, if
applicable

- The data `type` of the truncated field
- The `size`, in bytes, of the element that triggers truncation
- The number of elements that were `omitted` under each sub-object due to
truncation

Log entries with truncated attributes may also include an additional `size` field at the end of the entry which indicates the original size of the attribute before truncation, in this case `21692` or about 22KB. This final `size` field is only shown if it is different from the `size` field in the `truncated` object, i.e. if the total object size of the attribute is different from the size of the truncated sub-object, as is the case in the example above.

Padding ```````

When output to the file or the syslog log destinations, padding is added after the **severity**, **context**, and **id** fields to increase readability when viewed with a fixed-width font.

The following MongoDB log file excerpt demonstrates this padding:

```javascript
{"t":{"$date":"2020-05-18T20:18:12.724+00:00"},"s":"I", "c":"CONTROL", "id":23285, "ctx":"main", "svc": "R", "msg":"Automatically disabling TLS 1.0, to force-enable TLS 1.0 specify --sslDisabledProtocols 'none'"}
{"t":{"$date":"2020-05-18T20:18:12.734+00:00"},"s":"W", "c":"ASIO", "id":22601, "ctx":"main", "svc": "R", "msg":"No TransportLayer configured during NetworkInterface startup"}
{"t":{"$date":"2020-05-18T20:18:12.734+00:00"},"s":"I", "c":"NETWORK", "id":4648601, "ctx":"main", "svc": "R", "msg":"Implicit TCP FastOpen unavailable. If TCP FastOpen is required, set tcpFastOpenServer, tcpFastOpenClient, and tcpFastOpenQueueSize."}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I", "c":"STORAGE", "id":4615611, "ctx":"initandlisten", "svc": "R", "msg":"MongoDB starting", "attr":{"pid":10111,"port":27001,"dbPath":"/var/lib/mongo","architecture":"64-bit","host":"centos8"}}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I", "c":"CONTROL", "id":23403, "ctx":"initandlisten", "svc": "R", "msg":"Build Info", "attr":{"buildInfo":{"version":"4.4.0","gitVersion":"328c35e4b883540675fb4b626c53a08f74e43cf0","openSSLVersion":"OpenSSL 1.1.1c FIPS  28 May 2019","modules":[],"allocator":"tcmalloc","environment":{"distmod":"rhel80","distarch":"x86_64","target_arch":"x86_64"}}}}
{"t":{"$date":"2020-05-18T20:18:12.814+00:00"},"s":"I", "c":"CONTROL", "id":51765, "ctx":"initandlisten", "svc": "R", "msg":"Operating System", "attr":{"os":{"name":"CentOS Linux release 8.0.1905 (Core) ","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}
```

Pretty Printing ```````````````

.. include:: /includes/fact-use-jq-with-structured-logging.rst

You can use `jq` to pretty-print log entries as follows:

- Pretty-print the entire log file:
```javascript
  cat mongod.log | jq
```

- Pretty-print the most recent log entry:
```javascript
  cat mongod.log | tail -1 | jq
```

More examples of working with MongoDB structured logs are available in the `log-message-parsing` section.

### Configuring Log Message Destinations

MongoDB log messages can be output to file, syslog, or stdout (standard output).

To configure the log output destination, use one of the following settings, either in the `configuration file <configuration-options>` or on the command-line:

**Configuration file:**

- The :setting:`systemLog.destination` option for file or syslog
**Command-line:**

- the :option:`--logpath <mongod --logpath>` option for
:binary:`~bin.mongod` for file

- the :option:`--syslog <mongod --syslog>` option for
:binary:`~bin.mongod` for syslog

- the :option:`--logpath <mongos --logpath>` option for
:binary:`~bin.mongos` for file

- the :option:`--syslog <mongos --syslog>` option for
:binary:`~bin.mongos` for syslog

Not specifying either file or syslog sends all logging output to stdout.

For the full list of logging settings and options see:

**Configuration file:**

- `systemLog options list <systemlog-options>`
**Command-line:**

- `Log options list <mongod-log-options-section>` for
:binary:`~bin.mongod`

- `Log options list <mongos-log-options-section>` for
:binary:`~bin.mongos`

> **Note:** Error messages sent to `stderr` (standard error), such as fatal
errors during startup when not using the file or syslog log
destinations, or messages having to do with misconfigured logging
settings, are not affected by the log output destination setting, and
are printed to `stderr` in plaintext format.

## Log Message Field Types

### Timestamp

The timestamp field type indicates the precise date and time at which the logged event occurred.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "svc": "R", 
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

When logging to file or to syslog [#syslog-ts]_, the default format for the timestamp is `iso8601-local`. To modify the timestamp format, use the :option:`--timeStampFormat <mongod --timeStampFormat>` runtime option or the :setting:`systemLog.timeStampFormat` setting.

See `log-message-parsing-example-filter-timestamp` for log parsing examples that filter on the timestamp field.

> **Note:** The `ctime` timestamp format is no longer supported.

If logging to syslog, the `syslog` daemon generates timestamps when it logs a message, not when MongoDB issues the message. This can lead to misleading timestamps for log entries, especially when the system is under heavy load.

### Severity

The severity field type indicates the severity level associated with the logged event.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "svc": "R", 
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

Severity levels range from "Fatal" (most severe) to "Debug" (least severe):

You can specify the verbosity level of various components to determine the amount of **Informational** and **Debug** messages MongoDB outputs. Severity categories above these levels are always shown. [#slow-oplogs]_ To set verbosity levels, see `log-messages-configure-verbosity`.

### Components

The component field type indicates the category a logged event is a member of, such as **NETWORK** or **COMMAND**.

```javascript
{
  "t": {
    "$date": "2020-05-01T15:16:17.180+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 12345,
  "ctx": "listener",
  "svc": "R", 
  "msg": "Listening on",
  "attr": {
    "address": "127.0.0.1"
  }
}
```

Each component is individually configurable via its own `verbosity filter <log-messages-configure-verbosity>`. The available components are as follows:

See `log-message-parsing-example-filter-component` for log parsing examples that filter on the component field.

### Client Data

:driver:`MongoDB Drivers </>` and client applications (including :binary:`~bin.mongosh`) have the ability to send identifying information at the time of connection to the server. After the connection is established, the client does not send the identifying information again unless the connection is dropped and reestablished.

This identifying information is contained in the **attributes** field of the log entry. The exact information included varies by client.

Below is a sample log message containing the client data document as transmitted from a :binary:`~bin.mongosh` connection. The client data is contained in the `doc` object in the **attributes** field:

```javascript
{"t":{"$date":"2020-05-20T16:21:31.561+00:00"},"s":"I", "c":"NETWORK", "id":51800, "ctx":"conn202", "svc": "R", "msg":"client metadata", "attr":{"remote":"127.0.0.1:37106","client":"conn202","doc":{"application":{"name":"MongoDB Shell"},"driver":{"name":"MongoDB Internal Client","version":"4.4.0"},"os":{"type":"Linux","name":"CentOS Linux release 8.0.1905 (Core) ","architecture":"x86_64","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}}
```

When secondary members of a `replica set <replica-set-members>` initiate a connection to a primary, they send similar data. A sample log message containing this initiation connection might appear as follows. The client data is contained in the `doc` object in the **attributes** field:

```javascript
{"t":{"$date":"2020-05-20T16:33:40.595+00:00"},"s":"I", "c":"NETWORK", "id":51800, "ctx":"conn214", "svc": "R", "msg":"client metadata", "attr":{"remote":"127.0.0.1:37176","client":"conn214","doc":{"driver":{"name":"NetworkInterfaceTL","version":"4.4.0"},"os":{"type":"Linux","name":"CentOS Linux release 8.0.1905 (Core) ","architecture":"x86_64","version":"Kernel 4.18.0-80.11.2.el8_0.x86_64"}}}}
```

See the `examples section <log-message-json-examples>` for a `pretty-printed <log-message-pretty-printing>` example showing client data.

For a complete description of client information and required fields, see the [MongoDB Handshake specification](https://github.com/mongodb/specifications/blob/master/source/mongodb-handshake/handshake.rst).

## Verbosity Levels

You can specify the logging verbosity level to increase or decrease the amount of log messages MongoDB outputs. Verbosity levels can be adjusted for all components together, or for specific `named components <log-message-components>` individually.

Verbosity affects log entries in the `severity <log-severity-levels>` categories **Informational** and **Debug** only. Severity categories above these levels are always shown.

You might set verbosity levels to a high value to show detailed logging for debugging or development, or to a low value to minimize writes to the log on a vetted production deployment. [#slow-oplogs]_

### View Current Log Verbosity Level

To view the current verbosity levels, use the :method:`db.getLogComponents()` method:

```javascript
db.getLogComponents()
```

Your output might resemble the following:

```javascript
{
 "verbosity" : 0,
 "accessControl" : {
    "verbosity" : -1
 },
 "command" : {
    "verbosity" : -1
 },
 ...
 "storage" : {
    "verbosity" : -1,
    "recovery" : {
       "verbosity" : -1
    },
    "journal" : {
        "verbosity" : -1
    }
 },
 ...
```

The initial `verbosity` entry is the parent verbosity level for all components, while the individual `named components <log-message-components>` that follow, such as `accessControl`, indicate the specific verbosity level for that component, overriding the global verbosity level for that particular component if set.

A value of `-1`, indicates that the component inherits the verbosity level of their parent, if they have one (as with `recovery` above, inheriting from `storage`), or the global verbosity level if they do not (as with `command`). Inheritance relationships for verbosity levels are indicated in the `components section <log-message-components>`.

### Configure Log Verbosity Levels

You can configure the verbosity level using: the :setting:`systemLog.verbosity` and `systemLog.component.<name>.verbosity` settings, the :parameter:`logComponentVerbosity` parameter, or the :method:`db.setLogLevel()` method. [#slow-oplogs]_

`systemLog` Verbosity Settings ````````````````````````````````

To configure the default log level for all `components <log-message-components>`, use the :setting:`systemLog.verbosity` setting. To configure the level of specific components, use the `systemLog.component.<name>.verbosity` settings.

For example, the following configuration sets the :setting:`systemLog.verbosity` to `1`, the :setting:`systemLog.component.query.verbosity` to `2`, the :setting:`systemLog.component.storage.verbosity` to `2`, and the :setting:`systemLog.component.storage.journal.verbosity` to `1`:

```javascript
systemLog:
   verbosity: 1
   component:
      query:
         verbosity: 2
      storage:
         verbosity: 2
         journal:
            verbosity: 1
```

You would set these values in the `configuration file <configuration-options>` or on the command line for your :binary:`~bin.mongod` or :binary:`~bin.mongos` instance.

All components not specified explicitly in the configuration have a verbosity level of `-1`, indicating that they inherit the verbosity level of their parent, if they have one, or the global verbosity level (:setting:`systemLog.verbosity`) if they do not.

`logComponentVerbosity` Parameter ```````````````````````````````````

To set the :parameter:`logComponentVerbosity` parameter, pass a document with the verbosity settings to change.

For example, the following sets the :setting:`default verbosity level <systemLog.verbosity>` to `1`, the :setting:`query <systemLog.component.query.verbosity>` to `2`, the :setting:`storage <systemLog.component.storage.verbosity>` to `2`, and the :setting:`storage.journal <systemLog.component.storage.journal.verbosity>` to `1`.

```javascript
db.adminCommand( {
   setParameter: 1,
   logComponentVerbosity: {
      verbosity: 1,
      query: {
         verbosity: 2
      },
      storage: {
         verbosity: 2,
         journal: {
            verbosity: 1
         }
      }
   }
} )
```

You would set these values from :binary:`~bin.mongosh`.

`db.setLogLevel()` ````````````````````

Use the :method:`db.setLogLevel()` method to update a single component log level. For a component, you can specify verbosity level of `0` to `5`, or you can specify `-1` to inherit the verbosity of the parent. For example, the following sets the :setting:`systemLog.component.query.verbosity` to its parent verbosity (i.e. default verbosity):

```javascript
db.setLogLevel(-1, "query")
```

You would set this value from :binary:`~bin.mongosh`.

.. include:: /includes/extracts/4.2-changes-slow-oplog-log-message-footnote.rst

### Logging Slow Operations

Client operations (such as queries) appear in the log if their duration exceeds the `slow operation threshold <slowms-threshold-option>` or when the `log verbosity level <log-message-verbosity-levels>` is 1 or higher. [#slow-oplogs]_ These log entries include the full command object associated with the operation.

.. include:: /includes/extracts/4.2-changes-log-query-shapes-plan-cache-key.rst

> **Important:** A single operation may log more than one entry. For example, if more
than one write in a `bulk write operation <bulk-write-operations>` exceeds
the slow operation threshold, each slow write is logged separately.

Version-Specific Changes ```````````````````````` The following table lists the changes to logging slow queries.

For a `pretty-printed <log-message-pretty-printing>` example of a slow operation log entry, see `log-message-json-examples`.

### Time Waiting for Shards Logged in `remoteOpWaitMillis` Field

.. versionadded:: 5.0

Starting in MongoDB 5.0, you can use the `remoteOpWaitMillis` log field to obtain the wait time (in milliseconds) for results from `shards <shard>`.

`remoteOpWaitMillis` is only logged:

- If you configure :ref:`slow operations logging
<log-message-slow-ops>`.

- On the `shard` or :binary:`~bin.mongos` that merges the results.
To determine if a merge operation or a shard issue is causing a slow query, compare the `workingMillis` and `remoteOpWaitMillis` time fields in the log. `workingMillis` is the total time the query took to complete. Specifically:

- If `workingMillis` is slightly longer than `remoteOpWaitMillis`,
then most of the time was spent waiting for a shard response. For example, `workingMillis` of 17 and `remoteOpWaitMillis` of 15.

- If `workingMillis` is significantly longer than
`remoteOpWaitMillis`, then most of the time was spent performing the merge. For example, `workingMillis` of 100 and `remoteOpWaitMillis` of 15.

## Log Redaction

### Queryable Encryption Log Redaction

When using `Queryable Encryption <qe-manual-feature-qe>`, CRUD operations against encrypted collections are omitted from the slow query log. For details, see `Queryable Encryption redaction <qe-redaction>`.

### Enterprise Log Redaction

.. include:: /includes/fact-log-redaction.rst

## Parsing Structured Log Messages

Log parsing is the act of programmatically searching through and analyzing log files, often in an automated manner. With the introduction of structured logging, log parsing is made simpler and more powerful. For example:

- Log message fields are presented as key-value pairs. Log parsers can
query by specific keys of interest to efficiently filter results.

- Log messages always contain the same message structure. Log parsers
can reliably extract information from any log message, without needing to code for cases where information is missing or formatted differently.

The following examples demonstrate common log parsing workflows when working with MongoDB JSON log output.

### Log Parsing Examples

.. include:: /includes/fact-use-jq-with-structured-logging.rst

These examples use `jq` to simplify log parsing.

Counting Unique Messages ````````````````````````

The following example shows the top 10 unique message values in a given log file, sorted by frequency:

```bash
jq -r ".msg" /var/log/mongodb/mongod.log | sort | uniq -c | sort -rn | head -10
```

Monitoring Connections `````````````````````` Remote client connections are shown in the log under the "remote" key in the attribute object. The following counts all unique connections over the course of the log file and presents them in descending order by number of occurrences:

```bash
jq -r '.attr.remote' /var/log/mongodb/mongod.log | grep -v 'null' | sort | uniq -c | sort -r
```

Note that connections from the same IP address, but connecting over different ports, are treated as different connections by this command. You could limit output to consider IP addresses only, with the following change:

```bash
jq -r '.attr.remote' /var/log/mongodb/mongod.log | grep -v 'null' | awk -F':' '{print $1}' | sort | uniq -c | sort -r
```

Analyzing Driver Connections ````````````````````````````

The following example counts all remote :driver:`MongoDB driver</>` connections, and presents each driver type and version in descending order by number of occurrences:

```bash
jq -cr '.attr.doc.driver' /var/log/mongodb/mongod.log | grep -v null | sort | uniq -c | sort -rn    
```

Analyzing Client Types ``````````````````````

The following example analyzes the reported `client data <log-messages-client-data>` of remote :driver:`MongoDB driver </>` connections and client applications, including :binary:`~bin.mongosh`, and prints a total for each unique operating system type that connected, sorted by frequency:

```bash
jq -r '.attr.doc.os.type' /var/log/mongodb/mongod.log | grep -v null | sort | uniq -c | sort -rn
```

The string "Darwin", as reported in this log field, represents a macOS client.

Analyzing Slow Queries ``````````````````````

With `slow operation logging <log-message-slow-ops>` enabled, the following returns only the slow operations that took above 2000 milliseconds:, for further analysis:

```bash
jq 'select(.attr.workingMillis>=2000)' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/) for more information on the `jq` filters shown in this example.

Filtering by Component ``````````````````````

Log components (the third field in the `JSON log output format <log-message-json-output-format>`) indicate the `general category <log-message-components>` a given log message falls under. Filtering by component is often a great starting place when parsing log messages for relevant events.

The following example prints only the log messages of `component <log-message-components>` type **REPL**:

```bash
jq 'select(.c=="REPL")' /var/log/mongodb/mongod.log
```

The following example prints all log messages except those of `component <log-message-components>` type **REPL**:

```bash
jq 'select(.c!="REPL")' /var/log/mongodb/mongod.log
```

The following example print log messages of `component <log-message-components>` type **REPL** or **STORAGE**:

```bash
jq 'select( .c as $c | ["REPL", "STORAGE"] | index($c) )' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/) for more information on the `jq` filters shown in this example.

Filtering by Known Log ID `````````````````````````

Log IDs (the fifth field in the `JSON log output format <log-message-json-output-format>`) map to specific log events, and can be relied upon to remain stable over successive MongoDB releases.

As an example, you might be interested in the following two log events, showing a client connection followed by a disconnection:

```javascript
{"t":{"$date":"2020-06-01T13:06:59.027-0500"},"s":"I", "c":"NETWORK", "id":22943, "ctx":"listener", "svc": "R", "msg":"connection accepted from {session_remote} #{session_id} ({connectionCount}{word} now open)", "attr":{"session_remote":"127.0.0.1:61298", "session_id":164,"connectionCount":11,"word":" connections"}}
{"t":{"$date":"2020-06-01T13:07:03.490-0500"},"s":"I", "c":"NETWORK", "id":22944, "ctx":"conn157", "svc": "R", "msg":"end connection {remote} ({connectionCount}{word} now open)", "attr":{"remote":"127.0.0.1:61298","connectionCount":10,"word":" connections"}}
```

The log IDs for these two entries are `22943` and `22944` respectively. You could then filter your log output to show only these log IDs, effectively showing only client connection activity, using the following `jq` syntax:

```bash
jq 'select( .id as $id | [22943, 22944] | index($id) )' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/) for more information on the `jq` filters shown in this example.

Filtering by Date Range ```````````````````````

Log output can be further refined by filtering on the timestamp field, limiting log entries returned to a specific date range. For example, the following returns all log entries that occurred on April 15th, 2020:

```bash
jq 'select(.t["$date"] >= "2020-04-15T00:00:00.000" and .t["$date"] <= "2020-04-15T23:59:59.999")' /var/log/mongodb/mongod.log
```

Note that this syntax includes the full timestamp, including milliseconds but excluding the timezone offset.

Filtering by date range can be combined with any of the examples above, creating weekly reports or yearly summaries for example. The following syntax expands the "Monitoring Connections" example from earlier to limit results to the month of May, 2020:

```bash
jq 'select(.t["$date"] >= "2020-05-01T00:00:00.000" and .t["$date"] <= "2020-05-31T23:59:59.999" and .attr.remote)' /var/log/mongodb/mongod.log
```

Consult the [jq documentation](https://stedolan.github.io/jq/manual/) for more information on the `jq` filters shown in this example.

### Log Ingestion Services

Log ingestion services are third-party products that intake and aggregate log files, usually from a distributed cluster of systems, and provide ongoing analysis of that data in a central location.

The `JSON log format <log-message-json-output-format>` allows for more flexibility when working with log ingestion and analysis services. Whereas plaintext logs generally require some manner of transformation before being eligible for use with these products, JSON files can often be consumed out of the box, depending on the service. Further, JSON-formatted logs offer more control when performing filtering for these services, as the key-value structure offers the ability to specifically import only the fields of interest, while omitting the rest.

Consult the documentation for your chosen third-party log ingestion service for more information.

## Log Message Examples

The following examples show log messages in JSON output format.

These log messages are presented in `pretty-printed format <log-message-pretty-printing>` for convenience.

### Startup Warning

This example shows a startup warning:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:17:06.188+00:00"
  },
  "s": "W",
  "c": "CONTROL",
  "id": 22120,
  "ctx": "initandlisten",
  "svc": "R", 
  "msg": "Access control is not enabled for the database. Read and write access to data and configuration is unrestricted",
  "tags": [
    "startupWarnings"
  ]
}
```

### Client Connection

This example shows a client connection that includes `client data <log-messages-client-data>`:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:18:40.604+00:00"
  },
  "s": "I",
  "c": "NETWORK",
  "id": 51800,
  "ctx": "conn281",
  "svc": "R", 
  "msg": "client metadata",
  "attr": {
    "remote": "192.168.14.15:37666",
    "client": "conn281",
    "doc": {
      "application": {
        "name": "MongoDB Shell"
      },
      "driver": {
        "name": "MongoDB Internal Client",
        "version": "4.4.0"
      },
      "os": {
        "type": "Linux",
        "name": "CentOS Linux release 8.0.1905 (Core) ",
        "architecture": "x86_64",
        "version": "Kernel 4.18.0-80.11.2.el8_0.x86_64"
      }
    }
  }
}
```

### Slow Operation

Starting in MongoDB 8.0, slow operations are logged based on the time that MongoDB spends working on that operation, rather than the total latency for the operation.

You can use the metrics in the slow operation log to identify where an operation spends time in its lifecycle, which helps identify possible performance improvements.

In the following example log message:

- The amount of time spent waiting for resources while executing the
query is shown in these metrics:

- `queues.execution.totalTimeQueuedMicros`
- `timeAcquiringMicros`
- `workingMillis`
The amount of time that MongoDB spends working on the operation.

- `durationMillis`
The operation's total latency.

- `inUseTrackedMemBytes`
.. include:: /includes/in-use-memory.rst

- `peakTrackedMemBytes`
.. include:: /includes/peak-memory.rst

```javascript
{
   "t":{
      "$date":"2024-06-01T13:24:10.034+00:00"
   },
   "s":"I",
   "c":"COMMAND",
   "id":51803,
   "ctx":"conn3",
   "msg":"Slow query",
   "attr":{
      "type":"command",
      "isFromUserConnection":true,
      "ns":"db.coll",
      "collectionType":"normal",
      "appName":"MongoDB Shell",
      "command":{
         "find":"coll",
         "filter":{
            "b":-1
         },
         "sort":{
            "splitPoint":1
         },
         "readConcern":{ },
         "$db":"db"
      },
      "planSummary":"COLLSCAN",
      "planningTimeMicros":87,
      "keysExamined":0,
      "docsExamined":20889,
      "hasSortStage":true,
      "nBatches":1,
      "cursorExhausted":true,
      "numYields":164,
      "nreturned":99,
      "inUseTrackedMemBytes":368,
      "peakTrackedMemBytes":795,
      "planCacheShapeHash":"9C05019A",
      "planCacheKey":"C41063D6",
      "queryFramework":"classic",
      "reslen":96,
      "locks":{
         "ReplicationStateTransition":{
            "acquireCount":{
               "w":3
            }
         },
         "Global":{
            "acquireCount":{
               "r":327,
               "w":1
            }
         },
         "Database":{
            "acquireCount":{
               "r":1
            },
            "acquireWaitCount":{
               "r":1
            },
            "timeAcquiringMicros":{
               "r":2814
            }
         },
         "Collection":{
            "acquireCount":{
               "w":1
            }
         }
      },
      "flowControl":{
         "acquireCount":1,
         "acquireWaitCount":1,
         "timeAcquiringMicros":8387
      },
      "readConcern":{
         "level":"local",
         "provenance":"implicitDefault"
      },
      "storage":{ },
      "cpuNanos":20987385,
      "remote":"127.0.0.1:47150",
      "protocol":"op_msg",
      "queues":{
         "ingress":{
            "admissions":7,
            "totalTimeQueuedMicros":0
         },
         "execution":{
            "admissions":328,
            "totalTimeQueuedMicros":2109
         }
      },
      "workingMillis":89,
      "durationMillis":101
   }
}
```

.. include:: /includes/plan-cache-rename.rst

### Escaping

This example demonstrates `character escaping <log-message-json-escaping>`, as shown in the `setName` field of the attribute object:

```javascript
{
  "t": {
    "$date": "2020-05-20T19:11:09.268+00:00"
  },
  "s": "I",
  "c": "REPL",
  "id": 21752,
  "ctx": "ReplCoord-0",
  "svc": "R",
  "msg": "Scheduling remote command request",
  "attr": {
    "context": "vote request",
    "request": "RemoteCommand 229 -- target:localhost:27003 db:admin cmd:{ replSetRequestVotes: 1, setName: \"my-replica-name\", dryRun: true, term: 3, candidateIndex: 0, configVersion: 2, configTerm: 3, lastAppliedOpTime: { ts: Timestamp(1589915409, 1), t: 3 } }"
  }
}
```

### View

Starting in MongoDB 5.0, `log messages for slow queries <log-message-slow-ops>` on `views <views-landing-page>` include a `resolvedViews` field that contains the view details:

```javascript
"resolvedViews": [ {
   "viewNamespace": <String>,  // namespace and view name
   "dependencyChain": <Array of strings>,  // view name and collection
   "resolvedPipeline": <Array of documents>  // aggregation pipeline for view
} ]
```

The following example uses the `test` database and creates a view named `myView` that sorts the documents in `myCollection` by the `firstName` field:

```javascript
use test
db.createView( "myView", "myCollection", [ { $sort: { "firstName" : 1 } } ] )
```

Assume a `slow query <log-message-slow-ops>` is run on `myView`. The following example log message contains a `resolvedViews` field for `myView`:

```javascript
{
   "t": {
      "$date": "2021-09-30T17:53:54.646+00:00"
   },
   "s": "I",
   "c": "COMMAND",
   "id": 51803,
   "ctx": "conn249",
   "svc": "R",
   "msg": "Slow query",
   "attr": {
      "type": "command",
      "ns": "test.myView",
      "appName": "MongoDB Shell",
      "command": {
         "find": "myView",
         "filter": {},
         "lsid": {
            "id": { "$uuid": "ad176471-60e5-4e82-b977-156a9970d30f" }
         },
         "$db": "test"
      },
      "planSummary":"COLLSCAN",
         "resolvedViews": [ {
            "viewNamespace": "test.myView",
            "dependencyChain": [ "myView", "myCollection" ],
            "resolvedPipeline": [ { "$sort": { "firstName": 1 } } ]
         } ],
         "keysExamined": 0,
         "docsExamined": 1,
         "hasSortStage": true,
         "cursorExhausted": true,
         "numYields": 0,
         "nreturned": 1,
         "planCacheShapeHash": "3344645B",
         "planCacheKey": "1D3DE690",
         "queryFramework": "classic"
         "reslen": 134,
         "locks": { "ParallelBatchWriterMode": { "acquireCount": { "r": 1 } },
         "ReplicationStateTransition": { "acquireCount": { "w": 1 } },
         "Global": { "acquireCount": { "r": 4 } },
         "Database": { "acquireCount": {"r": 1 } },
         "Collection": { "acquireCount": { "r": 1 } },
         "Mutex": { "acquireCount": { "r": 4 } } },
         "storage": {},
         "remote": "127.0.0.1:34868",
         "protocol": "op_msg",
         "workingMillis": 0,
         "durationMillis": 0
      }
   }
}
```

.. include:: /includes/plan-cache-rename.rst

### Authorization

Starting in MongoDB 5.0, `log messages for slow queries <log-message-slow-ops>` include a `system.profile.authorization` section. These metrics help determine if a request is delayed because of contention for the user authorization cache.

```javascript
"authorization": {
   "startedUserCacheAcquisitionAttempts": 1,
   "completedUserCacheAcquisitionAttempts": 1,
   "userCacheWaitTimeMicros": 508
 },
```

### Session Workflow Log Message

Starting in MongoDB 6.3, a message is added to the log if the time to send an operation response exceeds the `slowms threshold option <slowms-threshold-option>`.

The message is known as a session workflow log message and contains various times to perform an operation in a database session.

Example session workflow log message:

```javascript
{
   "t": {
     "$date": "2022-12-14T17:22:44.233+00:00"
   },
   "s": "I",
   "c": "EXECUTOR",
   "id": 6983000,
   "ctx": "conn1",
   "svc": "R",
   "msg": "Slow network response send time",
   "attr": {
      "elapsed": {
         "totalMillis": 109,
         "activeMillis": 30,
         "receiveWorkMillis": 2,
         "processWorkMillis": 10,
         "sendResponseMillis": 22,
         "yieldMillis": 15,
         "finalizeMillis": 30
      }
   }
}
```

The times are in milliseconds.

A session workflow message is added to the log if `sendResponseMillis` exceeds the `slowms threshold option <slowms-threshold-option>`.

### Connection Acquisition To Wire Log Message

Starting in MongoDB 6.3, a message is added to the log if the time that an operation waited between acquisition of a server connection and writing the bytes to send to the server over the network exceeds 1 millisecond.

By default, the message is logged at the `"I"` information level, and at most once every second to avoid too many log messages. If you must obtain every log message, change your log level to debug.

If the operation wait time exceeds 1 millisecond and the message is logged at the information level within the last second, then the next message is logged at the debug level. Otherwise, the next message is logged at the information level.

Example log message:

```javascript
{
   "t": {
      "$date":"2023-01-31T15:22:29.473+00:00"
   },
   "s": "I",
   "c": "NETWORK",
   "id": 6496702,
   "ctx": "ReplicaSetMonitor-TaskExecutor",
   "svc": "R",
   "msg": "Acquired connection for remote operation and completed writing to wire",
   "attr": {
      "durationMicros": 1683
   }
}
```

The following table describes the `durationMicros` field in `attr`.

### Cache Refresh Times

> **Note:** Cache refresh log fields are specific to sharded clusters and only
appear in logs generated by the :binary:`mongos` router. They are not
available in unsharded replica sets or standalone deployments.

Starting in MongoDB 6.1, `log messages for slow queries <log-message-slow-ops>` include the following cache refresh time fields:

Starting in MongoDB 7.0, `log messages for slow queries <log-message-slow-ops>` also include the `catalogCacheIndexLookupDurationMillis` field that indicates the time that the operation spent fetching information from the index cache. This release also renames the `shardVersionRefreshMillis` field to `placementVersionRefreshDurationMillis`.

`placementVersionRefreshDurationMillis` is the time for refreshing the cache for operations like:

- `createCollection`
- :dbcommand:`shardCollection`
- `dropCollection`
- :dbcommand:`moveChunk`
- :dbcommand:`renameCollection`
- :dbcommand:`reshardCollection`
- :dbcommand:`refineCollectionShardKey`
- :dbcommand:`mergeChunks`
- :dbcommand:`split`
The following example includes:

- `catalogCacheDatabaseLookupDurationMillis`
- `catalogCacheCollectionLookupDurationMillis`
- `catalogCacheIndexLookupDurationMillis`
```javascript
{
  "t": {
    "$date": "2023-03-17T09:47:55.929+00:00"
  },
  "s": "I",
  "c": "COMMAND",
  "id": 51803,
  "ctx": "conn14",
  "svc": "R",
  "msg": "Slow query",
  "attr": {
    "type": "command",
    "ns": "db.coll",
    "appName": "MongoDB Shell",
    "command": {
      "insert": "coll",
      "ordered": true,
      "lsid": {
        "id": {
          "$uuid": "5d50b19c-8559-420a-a122-8834e012274a"
        }
      },
      "$clusterTime": {
        "clusterTime": {
          "$timestamp": {
            "t": 1679046398,
            "i": 8
          }
        },
        "signature": {
          "hash": {  
            "$binary": {
              "base64": "AAAAAAAAAAAAAAAAAAAAAAAAAAA=",
              "subType": "0"
            }
          },
          "keyId": 0
        }
      },
      "$db": "db"
    },
    "catalogCacheDatabaseLookupDurationMillis": 19,
    "catalogCacheCollectionLookupDurationMillis": 68,
    "catalogCacheIndexLookupDurationMillis": 16026,
    "nShards": 1,
    "ninserted": 1,
    "numYields": 232,
    "reslen": 96,
    "readConcern": {
      "level": "local",
      "provenance": "implicitDefault",
    },
    "cpuNanos": 29640339,
    "remote": "127.0.0.1:48510",
    "protocol": "op_msg",
    "remoteOpWaitMillis": 4078,
    "workingMillis": 20334,
    "durationMillis": 20334
  }
}
```

## Linux Syslog Limitations

.. include:: /includes/linux-syslog-limitations.rst

## Download Your Logs

You can use {+atlas+} to download a zipped file containing the logs for a selected hostname or process in your database deployment. To learn more, see :atlas:`View and Download MongoDB Logs </mongodb-logs>`.
