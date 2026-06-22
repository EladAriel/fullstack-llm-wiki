---
type: "Framework Learn Page"
framework: "mongodb"
source_repo: "https://github.com/mongodb/docs.git"
source_branch: "main"
source_path: "content/manual/manual/source/reference/connection-string-options.txt"
source_commit: "96788e8ed140cbdde184ff82e1066dff4996bde4"
source_commit_short: "96788e8e"
source_commit_date: "2026-06-19T21:35:03-06:00"
generated_at: "2026-06-21T07:41:52Z"
---

=========================

# Connection String Options

This page lists all connection options to connect to your database using SRV connection strings and standard connection strings.

Connection options are pairs in the following form: `name=value`.

- The option `name` is case insensitive when using a driver.
- The option `name` is case insensitive when using
:binary:`~bin.mongosh`.

- The `value` is always case sensitive.
Separate options with the ampersand (`&`) character `name1=value1&name2=value2`. In the following example, a connection includes the :urioption:`replicaSet` and :urioption:`connectTimeoutMS` options:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db1.example.net:27017,db2.example.net:2500/?replicaSet=test&connectTimeoutMS=300000
```

> **Note:** To provide backwards compatibility, drivers accept
semi-colons (`;`) as option separators.

## Replica Set Option

The following connection string connects to a replica set named `myRepl` with members running on the specified hosts. It authenticates as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`:

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com:27017,db1.example.com:27017,db2.example.com:27017/?replicaSet=myRepl
```

## Connection Options

### TLS Options

The following connection string to a replica set includes :urioption:`tls=true <tls>` option. It authenticates as user `myDatabaseUser` with the password `D1fficultP%40ssw0rd`.

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&tls=true
```

You can also use the equivalent :urioption:`ssl=true <ssl>` option:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&ssl=true
```

### Timeout Options

### Compression Options

## Connection Pool Options

Most drivers implement some kind of connection pool handling. Some drivers do not support connection pools. See your :driver:`driver </>` documentation for more information on the connection pooling implementation. These options allow applications to configure the connection pool when connecting to the MongoDB deployment.

## Write Concern Options

`Write concern <write-concern>` describes the level of acknowledgment requested from MongoDB. These options are supported by:

- MongoDB drivers
- :binary:`~bin.mongosh`
- :binary:`~bin.mongofiles`
- :binary:`~bin.mongoimport`
- :binary:`~bin.mongorestore`
You can specify write concern both in the connection string and as a parameter to methods like `insert` or `update`. If specified in both places, the method parameter overrides the connection string.

{+atlas+} deployment connection strings use :writeconcern:`"majority"` by default. If you don't specify write concern for an {+atlas+} deployment, {+atlas+} enforces :writeconcern:`"majority"`.

The following connection string to a replica set specifies :writeconcern:`"majority"` write concern and a 5 second timeout using the :urioption:`wtimeoutMS` write concern parameter:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&w=majority&wtimeoutMS=5000
```

For more information, see `write-concern`.

## readConcern Options

For the WiredTiger storage engine, MongoDB introduces the `readConcern` option for replica sets and replica set shards.

`/reference/read-concern` allows clients to choose a level of isolation for their reads from replica sets.

The following connection string to a replica set specifies :urioption:`readConcernLevel=majority <readConcernLevel>`:

```none
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&readConcernLevel=majority
```

For more information, see `/reference/read-concern`.

## Read Preference Options

`Read preferences <read-preference>` describe the behavior of read operations with regards to `replica sets <replica set>`. These parameters allow you to specify read preferences on a per-connection basis in the connection string.

For example:

- The following connection string to a replica set specifies
:readmode:`secondary` read preference mode and a :urioption:`maxStalenessSeconds` value of 120 seconds:

```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@db0.example.com,db1.example.com,db2.example.com/?replicaSet=myRepl&readPreference=secondary&maxStalenessSeconds=120
```

- The following connection string to a sharded cluster specifies
:readmode:`secondary` read preference mode and a :urioption:`maxStalenessSeconds` value of 120 seconds:

```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos1.example.com,mongos2.example.com/?readPreference=secondary&maxStalenessSeconds=120
```

- The following connection string to a sharded cluster specifies
:readmode:`secondary` read preference mode and three :urioption:`readPreferenceTags`:

```none
  mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongos1.example.com,mongos2.example.com/?readPreference=secondary&readPreferenceTags=dc:ny,rack:r1&readPreferenceTags=dc:ny&readPreferenceTags=
```

Order matters when using multiple `readPreferenceTags`. The `readPreferenceTags` are tried in order until a match is found. Once found, that specification is used to find all eligible matching members and any remaining `readPreferenceTags`  are ignored. For details, see `read-preference-tag-order-matching`.

For more information, see `Read preferences <read-preference>`.

## Authentication Options

The following connection string to a replica set specifies the :urioption:`authSource` to the `admin` database. That is, the user credentials are authenticated against the `admin` database.

```bash
mongodb://myDatabaseUser:D1fficultP%40ssw0rd@mongodb0.example.com:27017,mongodb1.example.com:27017,mongodb2.example.com:27017/?replicaSet=myRepl&authSource=admin
```

.. include:: /includes/fact-pct-encode-uri.rst

## Server Selection and Discovery Options

MongoDB provides the following options to configure how MongoDB drivers and :binary:`~bin.mongos` instances select a server to which to direct read or write operations.

## Miscellaneous Configuration
